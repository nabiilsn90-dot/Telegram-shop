import hashlib
import json
from decimal import Decimal, ROUND_HALF_UP

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, PreCheckoutQuery, SuccessfulPayment
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError

from bot.database.methods import get_user_referral, buy_item_transaction, process_payment_with_referral, create_pending_payment
from bot.keyboards import back, payment_menu, close, get_payment_choice
from bot.logger_mesh import logger
from bot.database.methods.audit import log_audit
from bot.database.methods.cache_utils import safe_create_task
from bot.misc import EnvKeys, ItemPurchaseRequest, validate_telegram_id, validate_money_amount, PaymentRequest
from bot.handlers.other import _any_payment_method_enabled, is_safe_item_name, caller_name
from bot.misc.metrics import get_metrics
from bot.misc.services import CryptoPayAPI, CryptoPayAPIError, send_stars_invoice, send_fiat_invoice
from bot.misc.services.payment import _minor_units_for, payload_amount
from bot.filters import ValidAmountFilter
from bot.i18n import localize, esc
from bot.states import BalanceStates

router = Router()


def _get_points_multiplier() -> Decimal:
    """Get points multiplier per 1$ from environment or default to 100."""
    try:
        return Decimal(getattr(EnvKeys, "POINTS_PER_USD", 100))
    except Exception:
        return Decimal(100)


async def _notify_referrer_bonus(bot, user_id: int, amount: Decimal | int, payer_name: str, payer_id: int):
    """Send referral bonus notification to the referrer if applicable."""
    referral_id = await get_user_referral(user_id)
    if not referral_id or not EnvKeys.REFERRAL_PERCENT:
        return
    try:
        clamped_percent = min(max(EnvKeys.REFERRAL_PERCENT, 0), 99)
        bonus = (Decimal(clamped_percent) / Decimal(100) * Decimal(amount)).quantize(Decimal("0.01"))
        if bonus > 0:
            await bot.send_message(
                referral_id,
                localize('payments.referral.bonus',
                         amount=bonus, name=esc(payer_name),
                         id=payer_id, currency=EnvKeys.PAY_CURRENCY),
                reply_markup=close()
            )
    except (TelegramBadRequest, TelegramForbiddenError) as e:
        logger.error(f"Failed to send referral notification to user {referral_id}: {e}")


@router.callback_query(F.data == "replenish_balance")
async def replenish_balance_callback_handler(call: CallbackQuery, state: FSMContext):
    """Ask user for the amount if at least one payment method is enabled."""
    if not _any_payment_method_enabled():
        await call.answer(localize("payments.not_configured"), show_alert=True)
        return

    await call.message.edit_text(
        localize("payments.replenish_prompt", currency=EnvKeys.PAY_CURRENCY),
        reply_markup=back('profile')
    )
    await state.set_state(BalanceStates.waiting_amount)


@router.message(BalanceStates.waiting_amount, ValidAmountFilter())
async def replenish_balance_amount(message: Message, state: FSMContext):
    """Store amount and show payment methods."""
    try:
        amount = validate_money_amount(
            message.text,
            min_amount=Decimal(EnvKeys.MIN_AMOUNT),
            max_amount=Decimal(EnvKeys.MAX_AMOUNT)
        )

        await state.update_data(amount=float(amount))

        await message.answer(
            localize("payments.method_choose"),
            reply_markup=get_payment_choice()
        )
        await state.set_state(BalanceStates.waiting_payment)

    except ValueError:
        await message.answer(
            localize("payments.replenish_invalid",
                     min_amount=EnvKeys.MIN_AMOUNT,
                     max_amount=EnvKeys.MAX_AMOUNT,
                     currency=EnvKeys.PAY_CURRENCY),
            reply_markup=back('replenish_balance')
        )


@router.message(BalanceStates.waiting_amount)
async def invalid_amount(message: Message, state: FSMContext):
    """Tell user the amount is invalid."""
    await message.answer(
        localize("payments.replenish_invalid",
                 min_amount=EnvKeys.MIN_AMOUNT,
                 max_amount=EnvKeys.MAX_AMOUNT,
                 currency=EnvKeys.PAY_CURRENCY),
        reply_markup=back('replenish_balance')
    )


@router.callback_query(
    BalanceStates.waiting_payment,
    F.data.in_([
        "pay_cryptopay", "pay_stars", "pay_fiat",
        "pay_binance", "pay_cryptomus", "pay_faucetpay", "pay_coinex", "pay_cwallet"
    ])
)
async def process_replenish_balance(call: CallbackQuery, state: FSMContext):
    """Create an invoice or handle payment method selection."""
    data = await state.get_data()
    amount = data.get('amount')

    if amount is None:
        await call.answer(localize("payments.session_expired"), show_alert=True)
        await call.message.edit_text(localize("menu.title"), reply_markup=back('back_to_menu'))
        await state.clear()
        return

    amount_dec = Decimal(str(amount))
    multiplier = _get_points_multiplier()
    calculated_points = (amount_dec * multiplier).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    ttl_seconds = int(getattr(EnvKeys, 'PAYMENT_TIME', 1800))

    # Handle New Custom Providers (Binance, Cryptomus, FaucetPay, Coinex, Cwallet)
    custom_providers = {
        "pay_binance": "binance",
        "pay_cryptomus": "cryptomus",
        "pay_faucetpay": "faucetpay",
        "pay_coinex": "coinex",
        "pay_cwallet": "cwallet"
    }

    if call.data in custom_providers:
        prov_name = custom_providers[call.data]
        external_id = f"{prov_name}:{call.from_user.id}:{int(hashlib.sha256(str(call.message.message_id).encode()).hexdigest()[:10], 16)}"
        
        await create_pending_payment(
            provider=prov_name,
            external_id=external_id,
            user_id=call.from_user.id,
            amount=calculated_points,
            currency=EnvKeys.PAY_CURRENCY,
        )
        await state.update_data(invoice_id=external_id, payment_type=prov_name)

        await call.message.edit_text(
            f"🌐 يرجى إتمام الدفع عبر بوابة **{prov_name.upper()}** بقيمة `{amount_dec} {EnvKeys.PAY_CURRENCY}`\n"
            f"🎁 ستتحصل على: `✨ {calculated_points} نقطة`\n\n"
            f"بعد الإتمام اضغط على زر التحقق أدناه:",
            parse_mode="Markdown",
            reply_markup=payment_menu("https://t.me") # يمكن ربطها برابط الدفع الفعلي لاحقاً
        )
        return

    # Original Providers Handler
    provider_map = {
        "pay_cryptopay": "cryptopay",
        "pay_stars": "stars",
        "pay_fiat": "fiat"
    }
    provider = provider_map.get(call.data)

    try:
        if call.data == "pay_cryptopay":
            if not EnvKeys.CRYPTO_PAY_TOKEN:
                await call.answer(localize("payments.not_configured"), show_alert=True)
                return

            try:
                crypto = CryptoPayAPI()
                invoice = await crypto.create_invoice(
                    amount=float(amount_dec),
                    expires_in=ttl_seconds,
                    currency=EnvKeys.PAY_CURRENCY,
                    accepted_assets="TON,USDT,BTC,ETH",
                    payload=str(call.from_user.id),
                )
            except CryptoPayAPIError as e:
                await log_audit("cryptopay_error", level="ERROR", user_id=call.from_user.id, resource_type="Payment", details=f"[{e.code}] {e.name}")
                await call.answer(localize("payments.crypto.api_error", error=e.name), show_alert=True)
                return
            except Exception as e:
                await log_audit("cryptopay_invoice_fail", level="ERROR", user_id=call.from_user.id, resource_type="Payment", details=str(e))
                await call.answer(localize("payments.crypto.create_fail", error=str(e)), show_alert=True)
                return

            pay_url = invoice.get("mini_app_invoice_url")
            invoice_id = invoice.get("invoice_id")

            await create_pending_payment(
                provider="cryptopay",
                external_id=str(invoice_id),
                user_id=call.from_user.id,
                amount=calculated_points,
                currency=EnvKeys.PAY_CURRENCY,
            )

            await state.update_data(invoice_id=invoice_id, payment_type="cryptopay")

            await call.message.edit_text(
                localize("payments.invoice.summary",
                         amount=calculated_points,
                         minutes=int(ttl_seconds / 60),
                         button=localize("btn.check_payment"),
                         currency=EnvKeys.PAY_CURRENCY),
                reply_markup=payment_menu(pay_url)
            )

        elif call.data == "pay_stars":
            if EnvKeys.STARS_PER_VALUE > 0:
                try:
                    await send_stars_invoice(
                        bot=call.message.bot,
                        chat_id=call.from_user.id,
                        amount=int(calculated_points),
                    )
                except Exception as e:
                    await log_audit("stars_invoice_fail", level="ERROR", user_id=call.from_user.id, resource_type="Payment", details=str(e))
                    await call.answer(localize("payments.stars.create_fail", error=str(e)), show_alert=True)
                    return
                await state.clear()
            else:
                await call.answer(localize("payments.not_configured"), show_alert=True)
                return

        elif call.data == "pay_fiat":
            if not EnvKeys.TELEGRAM_PROVIDER_TOKEN:
                await call.answer(localize("payments.not_configured"), show_alert=True)
                return

            try:
                await send_fiat_invoice(
                    bot=call.message.bot,
                    chat_id=call.from_user.id,
                    amount=int(calculated_points),
                )
            except Exception as e:
                await log_audit("fiat_invoice_fail", level="ERROR", user_id=call.from_user.id, resource_type="Payment", details=str(e))
                await call.answer(localize("payments.fiat.create_fail", error=str(e)), show_alert=True)
                return
            await state.clear()

    except Exception as e:
        logger.error(f"Payment processing error: {e}")
        await state.clear()
        await call.answer(localize("errors.something_wrong"), show_alert=True)


@router.callback_query(F.data == "check")
async def checking_payment(call: CallbackQuery, state: FSMContext):
    """Check invoice status and credit balance in points if paid."""
    user_id = call.from_user.id
    data = await state.get_data()
    payment_type = data.get("payment_type")

    if not payment_type:
        await call.answer(localize("payments.no_active_invoice"), show_alert=True)
        return

    # Handle Custom Providers Manual/API Check
    if payment_type in ["binance", "cryptomus", "faucetpay", "coinex", "cwallet"]:
        invoice_id = data.get("invoice_id")
        amount_data = data.get("amount", 0)
        multiplier = _get_points_multiplier()
        points_to_credit = (Decimal(str(amount_data)) * multiplier).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        success, error_msg = await process_payment_with_referral(
            user_id=user_id,
            amount=points_to_credit,
            provider=payment_type,
            external_id=str(invoice_id),
            referral_percent=EnvKeys.REFERRAL_PERCENT
        )

        if not success:
            if error_msg == "already_processed":
                await call.answer(localize("payments.already_processed"), show_alert=True)
            else:
                await call.answer(localize("payments.not_paid_yet"), show_alert=True)
            return

        await _notify_referrer_bonus(call.bot, user_id, points_to_credit, call.from_user.first_name, call.from_user.id)
        await call.message.edit_text(
            f"✅ تم تأكيد الدفع بنجاح عبر {payment_type.upper()}!\n✨ تمت إضافة `{points_to_credit} نقطة` إلى رصيدك.",
            reply_markup=back('profile')
        )
        await state.clear()
        return

    if payment_type == "cryptopay":
        invoice_id = data.get("invoice_id")
        if not invoice_id:
            await call.answer(localize("payments.invoice_not_found"), show_alert=True)
            await state.clear()
            return

        try:
            crypto = CryptoPayAPI()
            info = await crypto.get_invoice(invoice_id)
        except Exception as e:
            await call.answer(localize("payments.crypto.check_fail", error=str(e)), show_alert=True)
            return

        status = info.get("status")
        if status == "paid":
            raw_usd = Decimal(str(info.get("amount", "0")))
            multiplier = _get_points_multiplier()
            balance_amount = (raw_usd * multiplier).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

            if balance_amount <= 0:
                await call.answer(localize("payments.unable_determine_amount"), show_alert=True)
                return

            success, error_msg = await process_payment_with_referral(
                user_id=user_id,
                amount=balance_amount,
                provider="cryptopay",
                external_id=str(invoice_id),
                referral_percent=EnvKeys.REFERRAL_PERCENT
            )

            if not success:
                if error_msg == "already_processed":
                    await call.answer(localize("payments.already_processed"), show_alert=True)
                else:
                    await call.answer(localize("errors.general_error", e=error_msg), show_alert=True)
                return

            await _notify_referrer_bonus(call.bot, user_id, balance_amount, call.from_user.first_name, call.from_user.id)

            await call.message.edit_text(
                localize("payments.topped_simple",
                         amount=balance_amount,
                         currency="نقاط"),
                reply_markup=back('profile')
            )
            await state.clear()
        elif status == "active":
            await call.answer(localize("payments.not_paid_yet"))
        else:
            await call.answer(localize("payments.expired"), show_alert=True)


@router.pre_checkout_query()
async def pre_checkout_handler(query: PreCheckoutQuery):
    """Validate the payment before Telegram processes it."""
    try:
        payload = json.loads(query.invoice_payload or "{}")
    except Exception:
        await query.answer(ok=False, error_message="Invalid payload")
        return

    amount = payload_amount(payload)
    if amount <= 0:
        await query.answer(ok=False, error_message="Invalid amount")
        return

    if amount < int(EnvKeys.MIN_AMOUNT):
        await query.answer(ok=False, error_message="Amount below minimum")
        return

    if amount > int(EnvKeys.MAX_AMOUNT):
        await query.answer(ok=False, error_message="Amount exceeds maximum")
        return

    await query.answer(ok=True)


@router.message(F.successful_payment)
async def successful_payment_handler(message: Message):
    """Handle successful payment and convert to points."""
    sp: SuccessfulPayment = message.successful_payment
    user_id = message.from_user.id

    payload = {}
    try:
        if sp.invoice_payload:
            payload = json.loads(sp.invoice_payload)
    except Exception:
        payload = {}

    amount = payload_amount(payload)

    if amount <= 0:
        if sp.currency == "XTR":
            amount = int(
                (Decimal(int(sp.total_amount)) / Decimal(str(EnvKeys.STARS_PER_VALUE)))
                .to_integral_value(rounding=ROUND_HALF_UP)
            )
        else:
            currency = sp.currency.upper()
            multiplier_unit = _minor_units_for(currency)
            amount = int(Decimal(sp.total_amount) / Decimal(multiplier_unit))

    if amount <= 0:
        await message.answer(localize("payments.unable_determine_amount"), reply_markup=close())
        return

    multiplier = _get_points_multiplier()
    final_points = (Decimal(amount) * multiplier).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    provider = "telegram" if sp.currency != "XTR" else "stars"
    external_id = sp.telegram_payment_charge_id or sp.provider_payment_charge_id
    if not external_id:
        digest = hashlib.sha256(
            f"{provider}|{user_id}|{sp.currency}|{sp.total_amount}|{sp.invoice_payload or ''}".encode()
        ).hexdigest()
        external_id = f"{provider}:fallback:{digest[:32]}"

    success, error_msg = await process_payment_with_referral(
        user_id=user_id,
        amount=final_points,
        provider=provider,
        external_id=external_id,
        referral_percent=EnvKeys.REFERRAL_PERCENT
    )

    if not success:
        if error_msg == "already_processed":
            await message.answer(localize("payments.already_processed"), reply_markup=close())
        else:
            await message.answer(localize("payments.processing_error"), reply_markup=close())
        return

    await _notify_referrer_bonus(message.bot, user_id, final_points, message.from_user.first_name, message.from_user.id)

    await message.answer(
        f"✅ تمت عملية الشحن بنجاح!\n✨ رصيدك الجديد: `{final_points} نقطة`",
        reply_markup=back('profile')
    )


@router.callback_query(F.data == "buy_item")
async def buy_item_callback_handler(call: CallbackQuery, state: FSMContext):
    """Processing the purchase of goods with full transactional security."""
    try:
        data = await state.get_data()
        raw_item_name = data.get('csrf_item')

        if not raw_item_name:
            await call.answer(localize("middleware.security.invalid_csrf"), show_alert=True)
            return

        metrics = get_metrics()

        purchase_request = ItemPurchaseRequest(
            item_name=raw_item_name,
            user_id=call.from_user.id
        )

        if not is_safe_item_name(purchase_request.item_name):
            await call.answer(
                localize("errors.invalid_item_name"),
                show_alert=True
            )
            await log_audit("suspicious_item_name", level="WARNING", user_id=call.from_user.id, resource_type="Item", details=raw_item_name)
            return

        try:
            user_id = validate_telegram_id(call.from_user.id)
        except ValueError:
            await call.answer(localize("errors.invalid_user"), show_alert=True)
            return

        await call.answer(localize("shop.purchase.processing"))

        promo_code = data.get('applied_promo')

        success, message, purchase_data = await buy_item_transaction(
            user_id,
            purchase_request.item_name,
            promo_code=promo_code,
        )

        if not success:
            error_messages = {
                "user_not_found": "shop.purchase.fail.user_not_found",
                "item_not_found": "shop.item.not_found",
                "insufficient_funds": "shop.insufficient_funds",
                "out_of_stock": "shop.out_of_stock",
                "promo_invalid": "promo.not_found",
                "promo_expired": "promo.expired",
                "promo_max_uses": "promo.max_uses_reached",
                "promo_already_used": "promo.already_used",
                "promo_wrong_item": "promo.wrong_item",
                "promo_wrong_category": "promo.wrong_category",
            }

            error_text = localize(
                error_messages.get(message, "shop.purchase.fail.general"),
                message=message
            )

            await call.message.edit_text(
                error_text,
                reply_markup=back('back_to_item')
            )

            if message not in error_messages:
                await log_audit("purchase_error", level="ERROR", user_id=user_id, resource_type="Item", resource_id=purchase_request.item_name, details=message)
            return

        if metrics:
            metrics.track_event("purchase", call.from_user.id, {
                "item": purchase_request.item_name,
                "price": purchase_data['price']
            })
            metrics.track_conversion("purchase_funnel", "purchase", call.from_user.id)

        safe_value = esc(purchase_data['value'])
        username = esc(call.from_user.username or call.from_user.first_name)

        await state.update_data(applied_promo=None)

        from bot.keyboards.inline import simple_buttons
        buttons = [
            (f"📦 {purchase_data['item_name']}", f"bought-item:{purchase_data['bought_id']}:back_to_item"),
            (localize("btn.back"), "back_to_item"),
        ]

        await call.message.edit_text(
            localize(
                'shop.purchase.receipt',
                item_name=esc(purchase_data['item_name']),
                price=purchase_data['price'],
                unique_id=purchase_data['unique_id'],
                datetime=purchase_data['bought_datetime'],
                username=username,
                user_id=call.from_user.id,
                value=safe_value,
                currency="نقاط",
            ),
            parse_mode='HTML',
            reply_markup=simple_buttons(buttons),
        )

        safe_create_task(log_audit(
            "purchase",
            user_id=user_id,
            resource_type="Item",
            resource_id=purchase_request.item_name[:100],
            details=(
                f"name={caller_name(call)[:50]}, "
                f"price={purchase_data['price']} نقاط, "
                f"unique_id={purchase_data['unique_id']}"
            ),
        ))

    except Exception as e:
        logger.error(f"Critical error in purchase handler: {e}")
        await call.answer(
            localize("errors.something_wrong"),
            show_alert=True
        )
