from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(F.text.in_(["🎮 العب واكسب", "🎮 Play & Earn"]))
async def play_and_earn_handler(message: Message, state: FSMContext):
    """
    عرض تفاصيل لعبة المربعات والربح اليومي مع زر بدء اللعبة.
    """
    user_id = message.from_user.id
    
    # TODO: تحقق هنا من قاعدة البيانات إذا كان المستخدم قد لعب اليوم أم لا
    has_played_today = False  # افتراضياً لم يلعب اليوم
    
    if has_played_today:
        await message.answer(
            "🎮 **لعبة المربعات والربح اليومي:**\n\n"
            "⏳ لقد لعبت بالفعل اليوم! يمكنك المحاولة مرة أخرى غداً."
        )
        return

    # إنشاء لوحة أزرار تفاعلية للعبة (مثلاً شبكة مربعات 3x3)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📦 مربع 1", callback_data="play_box_1"),
            InlineKeyboardButton(text="📦 مربع 2", callback_data="play_box_2"),
            InlineKeyboardButton(text="📦 مربع 3", callback_data="play_box_3"),
        ],
        [
            InlineKeyboardButton(text="📦 مربع 4", callback_data="play_box_4"),
            InlineKeyboardButton(text="📦 مربع 5", callback_data="play_box_5"),
            InlineKeyboardButton(text="📦 مربع 6", callback_data="play_box_6"),
        ],
        [
            InlineKeyboardButton(text="📦 مربع 7", callback_data="play_box_7"),
            InlineKeyboardButton(text="📦 مربع 8", callback_data="play_box_8"),
            InlineKeyboardButton(text="📦 مربع 9", callback_data="play_box_9"),
        ]
    ])

    await message.answer(
        "🎮 **اكتشف واربح:**\n\n"
        "أفتح لعبة واختر المربعات واربح نقاط مجانية.\n"
        "⚠️ **هناك قنبلة واحدة مخفية!**\n\n"
        "يمكنك اللعب مرة واحدة فقط يومياً. اختر مربعاً للبدء:",
        reply_markup=keyboard
    )


# معالج الضغط على مربعات اللعبة
@router.callback_query(F.data.startswith("play_box_"))
async def process_game_box(call: CallbackQuery, state: FSMContext):
    box_number = call.data.split("_")[-1]
    
    # يمكنك هنا تخصيص منطق الربح أو خسارة النقطة (القنبلة)
    # كمثال بسيط: نجاح واكتساب نقاط
    await call.message.edit_text(
        f"🎮 **اكتشف واربح**\n\n"
        f"✅ تم اختيار المربع رقم `{box_number}` وإضافة نقاط إلى رصيدك بنجاح!\n"
        f"رصيدك الآن محدث."
    )
    await call.answer("مبروك لقد ربحت نقاطاً جديدة!", show_alert=True)
