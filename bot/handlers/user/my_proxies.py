from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.i18n import localize
from bot.keyboards import back # أو أي لوحة مفاتيح رجوع متوفرة لديك

router = Router()

@router.message(F.text.in_(["📡 بروكسياتي", "📡 My Proxies"]))
async def my_proxies_handler(message: Message, state: FSMContext):
    """
    Show user's active proxies and details.
    """
    user_id = message.from_user.id
    
    # TODO: قم بربطه بقاعدة البيانات لاحقاً لجلب بروكسيات المستخدم الحقيقية
    # مثال على جلب البروكسيات من قاعدة البيانات:
    # proxies = await get_user_proxies(user_id)
    proxies = [] # قائمة فارغة تجريبية حالياً
    
    if not proxies:
        await message.answer(
            "📡 **البروكسيات الخاصة بك:**\n\n"
            "❌ ليس لديك أي بروكسيات نشطة حالياً.\n"
            "يمكنك شراء بروكسي جديد عبر قسم (🌍 احصل على بروكسي)."
        )
        return

    # إذا كانت لديه بروكسيات، يمكنك عرضها هنا
    text = "📡 **قائمة بروكسياتك النشطة:**\n\n"
    for proxy in proxies:
        text += f"🔹 `{proxy['ip']}:{proxy['port']}` - ينتهي في: `{proxy['expires_at']}`\n"
        
    await message.answer(text, parse_mode="Markdown")
