DEFAULT_LOCALE = "ar"

TRANSLATIONS: dict[str, dict[str, str]] = {
    "ar": {
        # === Common Buttons ===
        "btn.shop": "🏪 المتجر",
        "btn.search": "🔍 البحث في الكتالوج",
        "btn.rules": "📜 القواعد",
        "btn.profile": "👤 الملف الشخصي",
        "btn.support": "🆘 الدعم الفني",
        "btn.channel": "ℹ قناة الأخبار",
        "btn.admin_menu": "🎛 لوحة التحكم",
        "btn.back": "⬅️ رجوع",
        "btn.to_menu": "🏠 الرئيسية",
        "btn.close": "✖ إغلاق",
        "btn.buy": "🛒 شراء",
        "btn.yes": "✅ نعم",
        "btn.no": "❌ لا",
        "btn.check": "🔄 تحقق",
        "btn.check_subscription": "🔄 التحقق من الاشتراك",
        "btn.check_payment": "🔄 التحقق من الدفع",
        "btn.pay": "💳 دفع",
        "btn.pay.crypto": "💎 CryptoPay",
        "btn.pay.stars": "⭐ نجوم تيليجرام",
        "btn.pay.tg": "💸 مدفوعات تيليجرام",

        # === Admin Buttons (user management shortcuts) ===
        "btn.admin.view_profile": "👁 عرض الملف الشخصي",
        "btn.admin.promote": "⬆️ تعيين كمسؤول",
        "btn.admin.demote": "⬇️ إزالة المسؤولية",
        "btn.admin.replenish_user": "💸 شحن الرصيد",
        "btn.admin.deduct_user": "💳 خصم من الرصيد",
        "btn.admin.block": "🚫 حظر",
        "btn.admin.unblock": "✅ إلغاء الحظر",

        # === Titles / Generic Texts ===
        "menu.title": "⛩️ القائمة الرئيسية",
        "profile.caption": "👤 <b>الملف الشخصي</b> — <a href='tg://user?id={id}'>{name}</a>",
        "rules.not_set": "❌ لم يتم إضافة القواعد بعد",

        # === Subscription Flow ===
        "subscribe.prompt": "يرجى الاشتراك في قناة الأخبار أولاً",
        "subscribe.open_channel": "فتح القناة",

        # === Profile ===
        "profile.referral_id": "👤 <b>المعرف الإحالي</b> — <code>{id}</code>",
        "btn.replenish": "💳 شحن الرصيد",
        "btn.referral": "🎲 نظام الإحالة",
        "btn.purchased": "🎁 المنتجات المشتراة",

        # === Profile Info Lines ===
        "profile.id": "🆔 <b>المعرف</b> — <code>{id}</code>",
        "profile.balance": "💳 <b>الرصيد</b> — <code>{amount}</code> {currency}",
        "profile.total_topup": "💵 <b>إجمالي الشحن</b> — <code>{amount}</code> {currency}",
        "profile.purchased_count": "🎁 <b>المنتجات المشتراة</b> — {count} قطعة",
        "profile.registration_date": "🕢 <b>تاريخ التسجيل</b> — <code>{dt}</code>",

        # === Referral ===
        "referral.title": "💚 نظام الإحالة",
        "referral.link": "🔗 الرابط: https://t.me/{bot_username}?start={user_id}",
        "referral.count": "عدد الإحالات: {count}",
        "referral.description": (
            "📔 يتيح لك نظام الإحالة كسب المال دون أي استثمار. "
            "كل ما عليك فعله هو نشر رابط الإحالة الخاص بك وستحصل على "
            "{percent}% من قيمة عمليات الشحن التي يقوم بها أصدقاؤك في رصيد البوت."
        ),
        "btn.view_referrals": "👥 إحالاتي",
        "btn.view_earnings": "💰 أرباحي",
        "btn.back_to_referral": "⬅️ العودة إلى نظام الإحالة",

        "referrals.list.title": "👥 إحالاتك:",
        "referrals.list.empty": "ليس لديك أي إحالات نشطة حتى الآن",
        "referrals.item.format": "المعرف: {telegram_id} | حقق لك: {total_earned} {currency}",

        "referral.earnings.title": "💰 الأرباح من الإحالة <code>{telegram_id}</code> (<a href='tg://user?id={telegram_id}'>{name}</a>):",
        "referral.earnings.empty": "لا توجد أرباح حتى الآن من هذه الإحالة <code>{id}</code> (<a href='tg://user?id={id}'>{name}</a>)",
        "referral.earning.format": "{amount} {currency} | {date} | (من أصل {original_amount} {currency})",
        "referral.item.info": ("💰 رقم العائد: <code>{id}</code>\n"
                               "👤 الإحالة: <code>{telegram_id}</code> (<a href='tg://user?id={telegram_id}'>{name}</a>)\n"
                               "🔢 المبلغ: {amount} {currency}\n"
                               "🕘 التاريخ: <code>{date}</code>\n"
                               "💵 من شحن بقيمة {original_amount} {currency}"),

        "all.earnings.title": "💰 جميع أرباح الإحالات الخاصة بك:",
        "all.earnings.empty": "ليس لديك أي أرباح إحالة حتى الآن",
        "all.earning.format": "{amount} {currency} من المعرف:{referral_id} | {date}",

        "referrals.stats.template": (
            "📊 إحصائيات نظام الإحالة:\n\n"
            "👥 الإحالات النشطة: {active_count}\n"
            "💰 إجمالي الأرباح: {total_earned} {currency}\n"
            "📈 إجمالي شحن الإحالات: {total_original} {currency}\n"
            "🔢 عدد العمليات: {earnings_count}"
        ),

        # === Admin: Main Menu ===
        "admin.menu.main": "⛩️ لوحة تحكم المسؤول",
        "admin.menu.shop": "🛒 إدارة المتجر",
        "admin.menu.goods": "📦 إدارة الأصناف",
        "admin.menu.categories": "📂 إدارة الفئات",
        "admin.menu.users": "👥 إدارة المستخدمين",
        "admin.menu.broadcast": "📝 الإذاعة (البث)",
        "admin.menu.roles": "🛡 إدارة الأدوار",
        "admin.menu.rights": "صلاحيات غير كافية",

        # === Admin: Role Management ===
        "admin.roles.list_title": "🛡 أدوار النظام:",
        "admin.roles.create": "➕ إنشاء دور",
        "admin.roles.edit": "✏️ تعديل",
        "admin.roles.delete": "🗑 حذف",
        "admin.roles.detail": "🛡 <b>الدور</b>: {name}\n📋 الصلاحيات: {perms}\n👥 المستخدمون: {users}",
        "admin.roles.prompt_name": "أدخل اسم الدور (بحد أقصى 64 حرفاً):",
        "admin.roles.name_invalid": "⚠️ اسم غير صالح (فارغ أو أطول من 64 حرفاً).",
        "admin.roles.name_exists": "❌ يوجد دور بهذا الاسم مسبقاً",
        "admin.roles.select_perms": "اختر الصلاحيات للدور «{name}»:",
        "admin.roles.confirm": "✅ تأكيد",
        "admin.roles.created": "✅ تم إنشاء الدور «{name}»",
        "admin.roles.updated": "✅ تم تحديث الدور «{name}»",
        "admin.roles.deleted": "✅ تم حذف الدور",
        "admin.roles.delete_confirm": "هل أنت متكد من رغبتك في حذف الدور «{name}»؟",
        "admin.roles.delete_fail": "❌ فشل الحذف: {error}",
        "admin.roles.perm_denied": "⚠️ ليس لديك صلاحية للقيام بهذا الإجراء",
        "admin.roles.assign_prompt": "اختر دوراً للمستخدم {id}:",
        "admin.roles.assigned": "✅ تم تعيين الدور {role} للمستخدم {name}",
        "admin.roles.assigned_notify": "ℹ️ تم تعيين دور جديد لك: {role}",
        "admin.roles.edit_name_prompt": "أدخل اسم الدور الجديد (أو /skip للإبقاء على الحالي):",
        "btn.admin.assign_role": "🛡 تعيين دور",

        # === Admin: User Management ===
        "admin.users.prompt_enter_id": "👤 أدخل معرف (ID) المستخدم\nلعرض أو تعديل بياناته",
        "admin.users.invalid_id": "⚠️ الرجاء إدخال معرف مستخدم رقمي صحيح.",
        "admin.users.profile_unavailable": "❌ الملف الشخصي غير متوفر (هذا المستخدم لم يتواجد قط)",
        "admin.users.not_found": "❌ المستخدم غير موجود",
        "admin.users.cannot_change_owner": "لا يمكن تغيير دور المالك",
        "admin.users.referrals": "👥 <b>إحالات المستخدم</b> — {count}",
        "admin.users.btn.view_referrals": "👥 إحالات المستخدم",
        "admin.users.btn.view_earnings": "💰 أرباح المستخدم",
        "admin.users.role": "🎛 <b>الدور</b> — {role}",
        "admin.users.set_admin.success": "✅ تم منح الدور للمستخدم {name}",
        "admin.users.set_admin.notify": "✅ تم تعيينك كمسؤول (ADMIN) في البوت",
        "admin.users.remove_admin.success": "✅ تم سحب الدور من المستخدم {name}",
        "admin.users.remove_admin.notify": "❌ تم سحب صلاحيات المسؤول (ADMIN) منك",
        "admin.users.balance.topped": "✅ تمت إضافة {amount} {currency} إلى رصيد المستخدم {name}",
        "admin.users.balance.topped.notify": "✅ تم شحن رصيدك بمبلغ {amount} {currency}",
        "admin.users.balance.deducted": "✅ تم خصم {amount} {currency} من رصيد المستخدم {name}",
        "admin.users.balance.deducted.notify": "ℹ️ تم خصم {amount} {currency} من رصيدك",
        "admin.users.balance.insufficient": "❌ رصيد غير كافٍ. الرصيد الحالي: {balance} {currency}",
        "admin.users.blocked.success": "🚫 تم حظر المستخدم {name}",
        "admin.users.unblocked.success": "✅ تم إلغاء حظر المستخدم {name}",
        "admin.users.cannot_block_owner": "❌ لا يمكن حظر مالك البوت",
        "admin.users.status.blocked": "🚫 <b>الحالة</b> — محظور",

        # === Admin: Shop Management Menu ===
        "admin.shop.menu.title": "⛩️ قائمة إدارة المتجر",
        "admin.shop.menu.statistics": "📊 الإحصائيات",
        "admin.shop.menu.logs": "📁 عرض السجلات",
        "admin.shop.menu.users": "👤 المستخدمون",
        "admin.shop.menu.search_bought": "🔎 البحث عن منتج مُشترى",

        # === Admin: Categories Management ===
        "admin.categories.menu.title": "⛩️ قائمة إدارة الفئات",
        "admin.categories.add": "➕ إضافة فئة",
        "admin.categories.rename": "✏️ إعادة تسمية فئة",
        "admin.categories.delete": "🗑 حذف فئة",
        "admin.categories.prompt.add": "أدخل اسم الفئة الجديدة:",
        "admin.categories.prompt.delete": "أدخل اسم الفئة المراد حذفها:",
        "admin.categories.prompt.rename.old": "أدخل اسم الفئة الحالي المراد تغييرها:",
        "admin.categories.prompt.rename.new": "أدخل الاسم الجديد للفئة:",
        "admin.categories.add.exist": "❌ لم يتم إنشاء الفئة (موجودة مسبقاً)",
        "admin.categories.add.success": "✅ تم إنشاء الفئة بنجاح",
        "admin.categories.delete.not_found": "❌ لم يتم الحذف (الفئة غير موجودة)",
        "admin.categories.delete.success": "✅ تم حذف الفئة",
        "admin.categories.rename.not_found": "❌ لا يمكن التحديث (الفئة غير موجودة)",
        "admin.categories.rename.exist": "❌ تعذر تغيير الاسم (توجد فئة بهذا الاسم مسبقاً)",
        "admin.categories.rename.success": "✅ تم تغيير اسم الفئة \"{old}\" إلى \"{new}\"",

        # === Admin: Goods / Items Management (Add / List / Item Info) ===
        "admin.goods.add_position": "➕ إضافة صنف",
        "admin.goods.add_item": "➕ إضافة منتج للصنف",
        "admin.goods.update_position": "📝 تعديل صنف",
        "admin.goods.delete_position": "❌ حذف صنف",
        "admin.goods.show_items": "📄 عرض المنتجات داخل الصنف",
        "admin.goods.add.prompt.name": "أدخل اسم الصنف:",
        "admin.goods.add.name.exists": "❌ لا يمكن إنشاء الصنف (موجود مسبقاً)",
        "admin.goods.add.name.invalid": "⚠️ اسم غير صالح (1-100 حرف، بدون رموز تحكم).",
        "admin.goods.add.prompt.description": "أدخل وصف الصنف:",
        "admin.goods.add.prompt.price": "أدخل سعر الصنف (رقم بـ {currency}):",
        "admin.goods.add.price.invalid": "⚠️ سعر غير صالح. أدخل رقماً.",
        "admin.goods.add.prompt.category": "أدخل الفئة التي ينتمي إليها الصنف:",
        "admin.goods.add.category.not_found": "❌ تعذر إنشاء الصنف (فئة الربط مدخلة بشكل خاطئ)",
        "admin.goods.add.infinity.question": "هل سيكون لهذا الصنف منتجات غير لا نهائية؟ (سيتم إرسال نفس القيمة للجميع)",
        "admin.goods.add.values.prompt_multi": (
            "أدخل قيم المنتجات رسالة برتلو الأخرى.\n"
            "عند الانتهاء، اضغط على «إضافة المنتجات المحددة»."
        ),
        "admin.goods.add.values.added": "✅ تم إضافة القيمة «{value}» إلى القائمة ({count} قطعة).",
        "admin.goods.add.result.created": "✅ تم إنشاء الصنف.",
        "admin.goods.add.result.added": "📦 المنتجات المضافة: <b>{n}</b>",
        "admin.goods.add.result.skipped_db_dup": "↩️ تم التخطي (موجودة مسبقاً في قاعدة البيانات): <b>{n}</b>",
        "admin.goods.add.result.skipped_batch_dup": "🔁 تم التخطي (مكررة في المدخلات): <b>{n}</b>",
        "admin.goods.add.result.skipped_invalid": "🚫 تم التخطي (فارغة / غير صالحة): <b>{n}</b>",
        "admin.goods.add.single.prompt_value": "أدخل قيمة واحدة للمنتج:",
        "admin.goods.add.single.empty": "⚠️ لا يمكن أن تكون القيمة فارغة.",
        "admin.goods.add.single.created": "✅ تم إنشاء الصنف وإضافة القيمة",
        "btn.add_values_finish": "إضافة المنتجات المحددة",
        "admin.goods.position.not_found": "❌ لا توجد منتجات (هذا الصنف غير موجود)",
        "admin.goods.list_in_position.empty": "ℹ️ لا توجد منتجات في هذا الصنف حالياً.",
        "admin.goods.list_in_position.title": "المنتجات في الصنف:",
        "admin.goods.item.invalid": "بيانات غير صالحة",
        "admin.goods.item.invalid_id": "معرف المنتج غير صالح",
        "admin.goods.item.not_found": "المنتج غير موجود",
        "admin.goods.prompt.enter_item_name": "أدخل اسم الصنف",
        "admin.goods.menu.title": "⛩️ قائمة إدارة الأصناف",

        # === Admin: Time-limited sales ===
        "admin.goods.sale_manage": "🔥 إدارة التخفيضات",
        "admin.sale.prompt.name": "أدخل اسم الصنف المراد ضبط خصم له:",
        "admin.sale.not_found": "❌ لم يتم العثور على صنف بهذا الاسم.",
        "admin.sale.current.active": "ℹ️ التخفيض الحالي: <b>{percent}%</b> حتى تاريخ <b>{until}</b> (UTC).",
        "admin.sale.current.none": "ℹ️ لا يوجد خصم حالي على هذا الصنف.",
        "admin.sale.prompt.percent": "أدخل نسبة الخصم (من 1 إلى 100).\nأرسل <b>0</b> لإلغاء التخفيض.",
        "admin.sale.percent.invalid": "⚠️ نسبة غير صالحة. أدخل رقماً صحيحاً من 0 إلى 100.",
        "admin.sale.disabled": "✅ تم إيقاف التخفيض للصنف «{name}».",
        "admin.sale.prompt.days": "لمكم يوم ترغب باستمرار التخفيض؟ أدخل رقماً صحيحاً (مثل: 3).",
        "admin.sale.days.invalid": "⚠️ مدة غير صالحة. أدخل عدداً صحيحاً أكبر من 0.",
        "admin.sale.success": "✅ تم تفعيل تخفيض بنسبة <b>{percent}%</b> للصنف «{name}» حتى <b>{until}</b> (UTC).",

        # === Admin: Goods / Items Update Flow ===
        "admin.goods.update.amount.prompt.name": "أدخل اسم الصنف",
        "admin.goods.update.amount.not_exists": "❌ لا يمكن إضافة منتج (هذا الصنف غير موجود)",
        "admin.goods.update.amount.infinity_forbidden": "❌ لا يمكن إضافة منتج (هذا الصنف يحتوي على منتج لا نهائي)",
        "admin.goods.update.values.result.title": "✅ تم إضافة المنتجات",
        "admin.goods.update.position.invalid": "الصنف غير موجود.",
        "admin.goods.update.position.exists": "يوجد صنف بهذا الاسم مسبقاً.",
        "admin.goods.update.prompt.name": "أدخل اسم الصنف",
        "admin.goods.update.not_exists": "❌ لا يمكن تعديل الصنف (غير موجود)",
        "admin.goods.update.prompt.new_name": "أدخل الاسم الجديد للصنف:",
        "admin.goods.update.prompt.description": "أدخل وصف الصنف:",
        "admin.goods.update.infinity.make.question": "هل تريد جعل منتجات هذا الصنف لا نهائية؟",
        "admin.goods.update.infinity.deny.question": "هل تريد إلغاء المنتجات اللانهائية؟",
        "admin.goods.update.success": "✅ تم تحديث الصنف",

        # === Admin: Goods / Items Delete Flow ===
        "admin.goods.delete.prompt.name": "أدخل اسم الصنف",
        "admin.goods.delete.position.not_found": "❌ لم يتم حذف الصنف (غير موجود)",
        "admin.goods.delete.position.success": "✅ تم حذف الصنف",
        "admin.goods.item.delete.button": "❌ حذف المنتج",
        "admin.goods.item.already_deleted_or_missing": "المنتج محذوف مسبقاً أو غير موجود",
        "admin.goods.item.deleted": "✅ تم حذف المنتج",

        # === Admin: Item Info ===
        "admin.goods.item.info.position": "<b>الصنف</b>: <code>{name}</code>",
        "admin.goods.item.info.price": "<b>السعر</b>: <code>{price}</code> {currency}",
        "admin.goods.item.info.id": "<b>المعرف الفريد</b>: <code>{id}</code>",
        "admin.goods.item.info.value": "<b>المنتج</b>: <code>{value}</code>",

        # === Admin: Logs ===
        "admin.shop.logs.caption": "سجلات البوت (Logs)",
        "admin.shop.logs.empty": "❗️ لا توجد سجلات حتى الآن",
        "admin.shop.logs.too_large": "⚠️ السجلات أكبر من أن يتم إرسالها ({files}) — يمكنك سحبها من القرص مباشرة.",

        # === Group Notifications ===
        "shop.group.new_upload": "تعبئة جديدة",
        "shop.group.item": "المنتج",
        "shop.group.count": "الكمية",

        # === Admin: Statistics ===
        "admin.shop.stats.template": (
            "إحصائيات المتجر:\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "<b>◽المستخدمون</b>\n"
            "◾️الجدد خلال 24 ساعة: {today_users}\n"
            "◾️الإجمالي: {users}\n"
            "◾️المشترون: {buyers}\n"
            "◾️المحظورون: {blocked}\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "◽<b>الأموال</b>\n"
            "◾المبيعات خلال 24 ساعة: {today_orders} {currency} ({today_sold_count} قطعة)\n"
            "◾إجمالي المبيعات: {all_orders} {currency}\n"
            "◾متوسط السلة: {avg_order} {currency}\n"
            "◾عمليات الشحن خلال 24 ساعة: {today_topups} {currency}\n"
            "◾الأموال في النظام: {system_balance} {currency}\n"
            "◾إجمالي الشحن الكلي: {all_topups} {currency}\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "◽<b>الكتالوج</b>\n"
            "◾المتوفر: {items} قطعة\n"
            "◾الأصناف: {goods} قطعة\n"
            "◾الفئات: {categories} قطعة\n"
            "◾المباع: {sold_count} قطعة"
        ),
        "admin.shop.stats.roles_header": "\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n◽<b>الأدوار</b>",

        # === Admin: Lists & Broadcast ===
        "admin.shop.users.title": "مستخدمو البوت:",
        "admin.shop.bought.prompt_id": "أدخل المعرف الفريد للمنتج المشترى",
        "admin.shop.bought.not_found": "❌ لم يتم العثور على منتج بهذا المعرف الفريد",
        "broadcast.prompt": "أرسل الرسالة المراد بثها للمستخدمين:",
        "broadcast.creating": "📤 جاري بدء البث الإذاعي...\n👥 إجمالي المستخدمين: {ids}",
        "broadcast.progress": (
            "📤 جاري إرسال البث...\n\n"
            "📊 التقدم: {progress:.1f}%\n"
            "✅ تم الإرسال: {sent}/{total}\n"
            "❌ الأخطاء: {failed}\n"
            "⏱ الوقت المنقضي: {time} ثانية"),
        "broadcast.done": (
            "✅ اكتمل البث الإذاعي بنجاح!\n\n"
            "📊 الإحصائيات:\n"
            "👥 الإجمالي: {total}\n"
            "✅ وصل بنجاح: {sent}\n"
            "❌ فشل الوصول: {failed}\n"
            "🚫 قاموا بحظر البوت: {blocked}\n"
            "📈 نسبة النجاح: {success}%\n"
            "⏱ الوقت المستغرق: {duration} ثانية"
        ),
        "broadcast.cancel": "❌ تم إلغاء البث",
        "broadcast.warning": "لا يوجد بث نشط حالياً",
        "broadcast.already_running": "⏳ هناك بث قيد التنفيذ بالفعل. انتظر حتى اكتماله.",
        "broadcast.btn.cancel": "🛑 إيقاف البث",

        # === Payments / Top-up Flow ===
        "payments.replenish_prompt": "أدخل مبلغ الشحن بـ {currency}:",
        "payments.replenish_invalid": "❌ مبلغ غير صحيح. أدخل رقماً بين {min_amount} و {max_amount} {currency}.",
        "payments.deduct_prompt": "أدخل مبلغ الخصم بـ {currency}:",
        "payments.deduct_invalid": "❌ مبلغ غير صحيح. أدخل رقماً بين {min_amount} و {max_amount} {currency}.",
        "payments.method_choose": "اختر طريقة الدفع:",
        "payments.not_configured": "❌ خيارات الدفع والشحن غير مُعَدَّة",
        "payments.session_expired": "انتهت صلاحية جلسة الدفع. يجدر بك البدء من جديد.",
        "payments.crypto.create_fail": "❌ خطأ عند إنشاء الفاتورة: {error}",
        "payments.crypto.api_error": "❌ خطأ في واجهة برمجة تطبيقات CryptoPay: {error}",
        "payments.crypto.check_fail": "❌ فشل التحقق من الدفع: {error}",
        "payments.stars.create_fail": "❌ تعذر إصدار فاتورة بالنجوم (Stars): {error}",
        "payments.fiat.create_fail": "❌ تعذر إصدار الفاتورة: {error}",
        "payments.no_active_invoice": "❌ لم يتم العثور على فواتير نشطة. ابدأ عملية الشحن مجدداً.",
        "payments.invoice_not_found": "❌ الفاتورة غير موجودة. يرجى البدء من جديد.",
        "payments.not_paid_yet": "⌛️ لم يتم دفع الفاتورة بعد.",
        "payments.expired": "❌ انتهت صلاحية الفاتورة.",
        "payments.invoice.summary": (
            "💵 مبلغ الشحن: {amount} {currency}.\n"
            "⌛️ لديك {minutes} دقائق لإتمام الدفع.\n"
            "<b>❗️ بعد إتمام الدفع، اضغط على زر «{button}»</b>"
        ),
        "payments.unable_determine_amount": "❌ تعذر تحديد مبلغ الدفع.",
        "payments.topped_simple": "✅ تم شحن الرصيد بمبلغ {amount} {currency}",
        "payments.topped_with_suffix": "✅ تم شحن الرصيد بمبلغ {amount} {currency} ({suffix})",
        "payments.success_suffix.stars": "نجوم تيليجرام",
        "payments.success_suffix.tg": "مدفوعات تيليجرام",
        "payments.referral.bonus": "✅ لقد تلقيت {amount} {currency} من إحالتك <a href='tg://user?id={id}'>{name}</a>",
        "payments.invoice.title.topup": "شحن الرصيد",
        "payments.invoice.desc.topup.stars": "شحن بمبلغ {amount} {currency} عبر نجوم تيليجرام",
        "payments.invoice.desc.topup.fiat": "الدفع عبر مدفوعات تيليجرام (البطاقة البنكية)",
        "payments.invoice.label.fiat": "شحن بقيمة {amount} {currency}",
        "payments.invoice.label.stars": "{stars} ⭐️",
        "payments.already_processed": "تم معالجة هذه الدفعة مسبقاً ✅",
        "payments.processing_error": "حدث خطأ أثناء معالجة الدفع. حاول مرة أخرى لاحقاً.",

        # === Shop Browsing (Categories / Goods / Item Page) ===
        "shop.categories.title": "🏪 فئات المتجر",
        "shop.goods.choose": "🏪 اختر المنتج المطلوبة",
        "shop.search.prompt": "🔍 أدخل اسم المنتج أو كلمة مفتاحية:",
        "shop.search.too_short": "يجب أن يكون الاستعلام بين 2 و 64 حرفاً. حاول مرة أخرى:",
        "shop.search.results": "🔍 نتائج البحث عن «{query}» — وجدنا: {count}",
        "shop.search.empty": "🔍 لم يتم العثور على شيء يخص «{query}».",
        "shop.item.not_found": "المنتج غير موجود",
        "shop.item.title": "🏪 المنتج {name}",
        "shop.item.description": "الوصف: {description}",
        "shop.item.price": "السعر — {amount} {currency}",
        "shop.item.quantity_unlimited": "الكمية — غير محدودة",
        "shop.item.quantity_left": "الكمية المتبقية — {count} قطعة",
        "shop.insufficient_funds": "❌ رصيدك غير كافٍ",
        "shop.out_of_stock": "❌ المنتج نفد من المخزون",
        "shop.purchase.success": "✅ تم شراء المنتج. <b>رصيدك الحالي</b>: <i>{balance}</i> {currency}\n\n{value}",
        "shop.purchase.receipt": "✅ تم إتمام الطلب بنجاح!\n➖➖➖➖➖➖➖➖➖➖➖➖\n📃 المنتج: {item_name}\n💰 السعر: {price} {currency}\n📦 الكمية: 1 قطعة\n💡 الطلب: {unique_id}\n🕐 الوقت: {datetime}\n💲 الإجمالي: {price} {currency}\n👤 المشتري: @{username} ({user_id})\n➖➖➖➖➖➖➖➖➖➖➖➖\n🔑 القيمة / محتوى المنتج:\n<code>{value}</code>",
        "shop.purchase.processing": "⏳ جاري معالجة الشراء...",
        "shop.purchase.fail.user_not_found": "❌ المستخدم غير مسجل في النظام",
        "shop.purchase.fail.general": "❌ خطأ أثناء عملية الشراء: {message}",

        # === Purchases ===
        "purchases.title": "المنتجات المشتراة:",
        "purchases.pagination.invalid": "بيانات التصفح غير صالحة",
        "purchases.item.not_found": "عملية الشراء غير موجودة",
        "purchases.item.name": "<b>🧾 المنتج</b>: <code>{name}</code>",
        "purchases.item.price": "<b>💵 السعر</b>: <code>{amount}</code> {currency}",
        "purchases.item.datetime": "<b>🕒 وقت الشراء</b>: <code>{dt}</code>",
        "purchases.item.unique_id": "<b>🧾 المعرف الفريد</b>: <code>{uid}</code>",
        "purchases.item.value": "<b>🔑 القيمة</b>:\n<code>{value}</code>",
        "purchases.item.buyer": "<b>المشتري</b>: <code>{buyer}</code>",

        # === Middleware ===
        "middleware.ban": "⏳ أنت محظور مؤقتاً. انتظر {time} ثانية",
        "middleware.above_limits": "⚠️ طلبات كثيرة جداً! تم حظرك مؤقتاً.",
        "middleware.waiting": "⏳ يرجى الانتظار {time} ثانية قبل الإجراء التالي.",
        "middleware.security.session_outdated": "⚠️ انتهت صلاحية الجلسة. يرجى البدء من جديد.",
        "middleware.security.invalid_data": "❌ بيانات غير صالحة",
        "middleware.security.blocked": "❌ الوصول محظور",
        "middleware.security.not_admin": "⛔ صلاحيات غير كافية",
        "middleware.security.invalid_csrf": "⚠️ انتهت صلاحية الجلسة. يرجى المحاولة مرة أخرى.",
        "maintenance.active": "🔧 البوت خاضع للصيانة الفنية حالياً. يرجى المحاولة لاحقاً.",

        # === Admin: Maintenance ===
        "admin.menu.maintenance_on": "🔧 الصيانة: مُفَعَّلَة",
        "admin.menu.maintenance_off": "🔧 الصيانة: مُعَطَّلَة",
        "admin.maintenance.enabled": "✅ تم تفعيل وضع الصيانة",
        "admin.maintenance.disabled": "✅ تم تعطيل وضع الصيانة",

        # === Promo Codes ===
        "btn.apply_promo": "🏷 إدخال برومو كود",
        "btn.remove_promo": "❌ إزالة البرومو كود",
        "admin.menu.promo": "🏷 أكواد الخصم (Promo)",
        "admin.promo.title": "🏷 <b>إدارة اكواد الخصم</b>",
        "admin.promo.create": "➕ إنشاء كود خصم",
        "admin.promo.list_empty": "لا توجد أكواد خصم حتى الآن.",
        "admin.promo.prompt.code": "أدخل كود الخصم (حتى 50 حرفاً):",
        "admin.promo.prompt.type": "اختر نوع الخصم:",
        "admin.promo.type.percent": "📊 نسبة مئوية (%)",
        "admin.promo.type.fixed": "💰 مبلغ ثابت",
        "admin.promo.prompt.value": "أدخل قيمة الخصم ({type}):",
        "admin.promo.prompt.max_uses": "أدخل الحد الأقصى للاستخدام (0 = بدون حد):",
        "admin.promo.prompt.expires": "أدخل آخر يوم صلاحية (YYYY-MM-DD) أو 0 لجعل الكود بلا انتهاء:",
        "admin.promo.prompt.binding": "هل تريد ربطه بفئة أو منتج معين؟\n\nأرسل:\n• اسم الفئة\n• اسم المنتج\n• 0 — بدون ربط",
        "admin.promo.created": "✅ تم إنشاء كود الخصم <code>{code}</code> بنجاح!",
        "admin.promo.code_exists": "❌ كود الخصم هذا موجود مسبقاً.",
        "admin.promo.invalid_code": "❌ يمكن أن يحتوي الكود على أحرف، أرقام وشرطة فقط (حتى 50 حرفاً).",
        "admin.promo.deleted": "✅ تم حذف كود الخصم.",
        "admin.promo.toggled_on": "✅ تم تفعيل كود الخصم.",
        "admin.promo.toggled_off": "⛔ تم تعطيل كود الخصم.",
        "admin.promo.btn.activate": "✅ تفعيل",
        "admin.promo.btn.deactivate": "⛔ تعطيل",
        "admin.promo.btn.delete": "🗑 حذف",
        "admin.promo.detail": "🏷 <b>الكود</b>: <code>{code}</code>\n📊 النوع: {discount_type}\n💰 الخصم: {discount_value}\n🔗 ينطبق على: {binding}\n🔢 الاستخدامات: {current_uses}/{max_uses}\n📅 ينتهي في: {expires_at}\n✅ مفعل: {is_active}",
        "admin.promo.confirm_delete": "هل تريد حذف كود الخصم <code>{code}</code>؟",
        "admin.promo.invalid_value": "❌ قيمة غير صالحة. حاول مرة أخرى.",
        "admin.promo.invalid_date": "❌ تاريخ غير صالح. التنسيق المطلوب: YYYY-MM-DD",
        "promo.not_found": "❌ كود الخصم غير موجود.",
        "promo.inactive": "❌ كود الخصم غير مفعل.",
        "promo.expired": "❌ انتهت صلاحية كود الخصم.",
        "promo.max_uses_reached": "❌ لقد استنفد كود الخصم حد الاستخدام الأقصى.",
        "promo.already_used": "❌ لقد استخدمت هذا الكود مسبقاً.",
        "promo.wrong_item": "❌ كود الخصم غير قابل للتطبيق على هذا المنتج.",
        "promo.wrong_category": "❌ كود الخصم غير قابل للتطبيق على هذه الفئة.",
        "promo.applied": "✅ تم تطبيق كود الخصم <code>{code}</code>! قيمة الخصم: {discount}",
        "promo.enter_code": "أدخل كود الخصم:",
        "promo.removed": "تم إزالة كود الخصم.",
        "promo.not_balance_type": "❌ هذا الكود ليس مخصصاً لشحن الرصيد.",
        "promo.enter_redeem_code": "أدخل كود التفعيل لتعبئة رصيدك:",
        "promo.balance_redeemed": "✅ تم تفعيل كود <code>{code}</code>! تمت إضافة {amount} {currency} إلى رصيدك.",
        "shop.item.price_discounted": "💰 <b>السعر</b>: <s>{original}</s> <b>{discounted}</b> {currency} (برومو {code})",
        "shop.item.price_sale": "🔥 <b>السعر</b>: <s>{original}</s> <b>{sale}</b> {currency} (خصم {percent}%)",
        "admin.promo.type.balance": "💰 شحن الرصيد",
        "admin.promo.prompt.binding_type": "ربط كود الخصم بفئة أم منتج؟",
        "admin.promo.binding.category": "فئة",
        "admin.promo.binding.item": "منتج",
        "admin.promo.binding.none": "بدون ربط",
        "admin.promo.binding.on_category": "الفئة «{name}»",
        "admin.promo.binding.on_item": "المنتج «{name}»",
        "admin.promo.binding.dangling": "⚠️ تم حذف الربط — الكود لا يُطبق على أي شيء حالياً",
        "admin.promo.prompt.category_name": "أدخل اسم الفئة:",
        "admin.promo.prompt.item_name": "أدخل اسم المنتج:",
        "admin.promo.category_not_found": "❌ الفئة غير موجودة.",
        "admin.promo.item_not_found": "❌ المنتج غير موجود.",
        "btn.redeem_promo": "🏷 تفعيل برومو شحن",
        "review.disabled": "التقييمات معطلة.",

        # === Cart ===
        "btn.cart": "🛒 السلة ({count})",
        "btn.cart_empty": "🛒 السلة",
        "btn.add_to_cart": "🛒 إضافة إلى السلة",
        "btn.cart_checkout": "💳 إتمام الشراء",
        "btn.cart_clear": "🗑 إفراغ السلة",
        "btn.cart_remove_item": "❌ {name}",
        "btn.cart_remove_promo": "🏷 إزالة الكود {code}",
        "btn.cart_receipt_all": "📋 كافة المشتريات",
        "cart.title": "🛒 <b>سلة المشتريات</b>",
        "cart.empty": "سلة المشتريات فارغة.",
        "cart.item": "• {name} ×{qty} — {price} {currency}",
        "cart.item_sale": "🔥 <b>{name}</b> ×{qty} — <s>{original}</s> {price} {currency}",
        "cart.item_promo": "🏷 <b>{name}</b> ×{qty} — <s>{original}</s> {price} {currency} ({code})",
        "cart.item_promo_invalid": "⚠️ <b>{name}</b> ×{qty} — {price} {currency}\n    كود الخصم {code} لا يسري على هذا المنتج",
        "cart.item_promo_elsewhere": "• {name} ×{qty} — {price} {currency}\n    تم احتساب كود الخصم {code} في منتج آخر",
        "cart.total": "\n💰 <b>الإجمالي</b>: {total} {currency}",
        "cart.added": "✅ تمت إضافة {name} إلى السلة.",
        "cart.full": "❌ السلة ممتلئة (الحد الأقصى 10 منتجات).",
        "cart.qty_max": "❌ الحد الأقصى هو {max} قطعة لنفس المنتج.",
        "cart.out_of_stock": "المخزون غير كافٍ للكمية المطلوبة. قلل الكمية وحاول مجدداً.",
        "cart.price_changed": "تغير السعر في السلة. افتح السلة وقم بتأكيد المبلغ الجديد.",
        "cart.item_not_found": "❌ المنتج غير موجود.",
        "cart.removed": "✅ تمت إزالة المنتج من السلة.",
        "cart.cleared": "✅ تم إفراغ السلة.",
        "cart.checkout_confirm": "إتمام الشراء لعدد {count} منتج(منتجات) بقيمة إجمالية {total} {currency}؟",
        "cart.checkout_success": "✅ تم إتمام الطلب! تم شراء {count} منتج(منتجات).\n\n💰 المتبقي في الرصيد: {balance} {currency}",
        "cart.checkout_receipt": "✅ تم إتمام الطلب بنجاح!\n➖➖➖➖➖➖➖➖➖➖➖➖\n📦 الكمية: {count} قطعة\n💲 الإجمالي: {total} {currency}\n👤 المشتري: @{username} ({user_id})\n🕐 الوقت: {datetime}\n➖➖➖➖➖➖➖➖➖➖➖➖\nاضغط على المنتج لعرض التفاصيل:",
        "cart.checkout_fail": "❌ فشل إتمام الطلب: {reason}",
        "cart.items_unavailable": "بعض المنتجات لم تعد متوفرة وتمت إزالتها من السلة.",


        # === Stock Subscriptions ===
        "btn.notify_stock": "🔔 إعلامي عند توفره",
        "btn.notify_stock_off": "🔕 إلغاء التنبيه",
        "stock.subscribed": "🔔 سنقوم بإعلامك فور توفر المنتج.",
        "stock.unsubscribed": "🔕 تم إلغاء تنبيه توفر المنتج.",
        "stock.back_in_stock": "🔔 المنتج <b>{name}</b> متوفر مجدداً في المخزون!",


        # === Operation History ===
        "btn.operation_history": "📋 سجل العمليات",
        "history.title": "📋 <b>سجل العمليات</b>",
        "history.empty": "سجل العمليات فارغ.",
        "history.topup": "💰 شحن رصيد: +{amount} {currency}",
        "history.purchase": "🛒 عملية شراء: {amount} {currency}",
        "history.referral": "🎲 مكافأة إحالة: +{amount} {currency}",
        "history.date": "📅 {date}",

        # === Reviews ===
        "btn.leave_review": "⭐ اترك تقييماً",
        "btn.view_reviews": "📝 التقييمات ({count})",
        "btn.skip_review_text": "⏭ تخطي النص",
        "review.prompt_rating": "قيم المنتج <b>{name}</b> من 1 إلى 5:",
        "review.prompt_text": "اكتب نص التقييم (حتى 500 حرف) أو اضغط «تخطي»:",
        "review.created": "✅ شكراً لتقييمك!",
        "review.already_exists": "لقد قمت بتقييم هذا المنتج مسبقاً.",
        "review.not_purchased": "لم تقوم بشراء هذا المنتج لتتمكن من تقييمه.",
        "review.avg_rating": "⭐ التقييم: {rating}/5 (من {count} تقييم)",
        "review.item": "⭐ {rating}/5 — {text}",
        "review.item_no_text": "⭐ {rating}/5",
        "review.list_title": "📝 <b>تقييمات المنتج {name}</b>",
        "review.list_empty": "لا توجد تقييمات حتى الآن.",

        # === Errors ===
        "errors.not_subscribed": "أنت غير مشترك في القناة",
        "errors.something_wrong": "❌ حدث خطأ ما. يرجى المحاولة مرة أخرى.",
        "errors.pagination_invalid": "بيانات التصفح غير صالحة",
        "errors.invalid_data": "❌ بيانات غير صحيحة",
        "errors.id_should_be_number": "❌ يجب أن يكون المعرف (ID) رقماً.",
        "errors.channel.telegram_not_found": "لا يمكنني الكتابة في القناة. قم بإضافتي كمسؤول في القناة المخصصة للرفع @{channel} مع منح صلاحية نشر الرسائل.",
        "errors.channel.telegram_forbidden_error": "لم يتم العثور على القناة. تحقق من معرف القناة المخصص للرفع @{channel}.",
        "errors.channel.telegram_bad_request": "فشل الإرسال إلى قناة النشر: {e}",
        "errors.general_error": "❌ خطأ: {e}",
        "errors.invalid_item_name": "❌ اسم المنتج غير صالح",
        "errors.invalid_user": "❌ مستخدم غير صالح",
    },

    "en": {
        # === Common Buttons ===
        "btn.shop": "🏪 Shop",
        "btn.search": "🔍 Search catalog",
        "btn.rules": "📜 Rules",
        "btn.profile": "👤 Profile",
        "btn.support": "🆘 Support",
        "btn.channel": "ℹ News channel",
        "btn.admin_menu": "🎛 Admin panel",
        "btn.back": "⬅️ Back",
        "btn.to_menu": "🏠 Menu",
        "btn.close": "✖ Close",
        "btn.buy": "🛒 Buy",
        "btn.yes": "✅ Yes",
        "btn.no": "❌ No",
        "btn.check": "🔄 Check",
        "btn.check_subscription": "🔄 Check subscription",
        "btn.check_payment": "🔄 Check payment",
        "btn.pay": "💳 Pay",
        "btn.pay.crypto": "💎 CryptoPay",
        "btn.pay.stars": "⭐ Telegram Stars",
        "btn.pay.tg": "💸 Telegram Payments",

        # === Admin Buttons (user management shortcuts) ===
        "btn.admin.view_profile": "👁 View profile",
        "btn.admin.promote": "⬆️ Make admin",
        "btn.admin.demote": "⬇️ Remove admin",
        "btn.admin.replenish_user": "💸 Top up balance",
        "btn.admin.deduct_user": "💳 Deduct from balance",
        "btn.admin.block": "🚫 Block",
        "btn.admin.unblock": "✅ Unblock",

        # === Titles / Generic Texts ===
        "menu.title": "⛩️ Main menu",
        "profile.caption": "👤 <b>Profile</b> — <a href='tg://user?id={id}'>{name}</a>",
        "rules.not_set": "❌ Rules have not been added",

        # === Profile ===
        "btn.replenish": "💳 Top up your balance",
        "btn.referral": "🎲 Referral system",
        "btn.purchased": "🎁 Purchased goods",
        "profile.referral_id": "👤 <b>Referral</b> — <code>{id}</code>",

        # === Subscription Flow ===
        "subscribe.prompt": "First, subscribe to the news channel",
        "subscribe.open_channel": "Open channel",

        # === Profile Info Lines ===
        "profile.id": "🆔 <b>ID</b> — <code>{id}</code>",
        "profile.balance": "💳 <b>Balance</b> — <code>{amount}</code> {currency}",
        "profile.total_topup": "💵 <b>Total topped up</b> — <code>{amount}</code> {currency}",
        "profile.purchased_count": "🎁 <b>Purchased items</b> — {count} pcs",
        "profile.registration_date": "🕢 <b>Registered at</b> — <code>{dt}</code>",

        # === Referral ===
        "referral.title": "💚 Referral system",
        "referral.link": "🔗 Link: https://t.me/{bot_username}?start={user_id}",
        "referral.count": "Referrals count: {count}",
        "referral.description": (
            "📔 The referral system lets you earn without any investment. "
            "Share your personal link and you will receive {percent}% of your referrals’ "
            "top-ups to your bot balance."
        ),
        "btn.view_referrals": "👥 My referrals",
        "btn.view_earnings": "💰 My earnings",
        "btn.back_to_referral": "⬅️ Back to referral system",

        "referrals.list.title": "👥 Your referrals:",
        "referrals.list.empty": "You don't have any active referrals yet",
        "referrals.item.format": "ID: {telegram_id} | Earned: {total_earned} {currency}",

        "referral.earnings.title": "💰 Earnings from referral <code>{telegram_id}</code> (<a href='tg://user?id={telegram_id}'>{name}</a>):",
        "referral.earnings.empty": "No earnings from this referral <code>{id}</code> (<a href='tg://user?id={id}'>{name}</a>) yet",
        "referral.earning.format": "{amount} {currency} | {date} | (from {original_amount} {currency})",
        "referral.item.info": ("💰 Earning number: <code>{id}</code>\n"
                               "👤 Referral: <code>{telegram_id}</code> (<a href='tg://user?id={telegram_id}'>{name}</a>)\n"
                               "🔢 Amount: {amount} {currency}\n"
                               "🕘 Date: <code>{date}</code>\n"
                               "💵 From a deposit to {original_amount} {currency}"),

        "all.earnings.title": "💰 All your referral earnings:",
        "all.earnings.empty": "You have no referral earnings yet",
        "all.earning.format": "{amount} {currency} from ID:{referral_id} | {date}",

        "referrals.stats.template": (
            "📊 Referral system statistics:\n\n"
            "👥 Active referrals: {active_count}\n"
            "💰 Total earned: {total_earned} {currency}\n"
            "📈 Total referrals top-ups: {total_original} {currency}\n"
            "🔢 Number of earnings: {earnings_count}"
        ),

        # === Admin: Main Menu ===
        "admin.menu.main": "⛩️ Admin Menu",
        "admin.menu.shop": "🛒 Shop management",
        "admin.menu.goods": "📦 Items management",
        "admin.menu.categories": "📂 Categories management",
        "admin.menu.users": "👥 Users management",
        "admin.menu.broadcast": "📝 Broadcast",
        "admin.menu.roles": "🛡 Role management",
        "admin.menu.rights": "Insufficient permissions",

        # === Admin: Role Management ===
        "admin.roles.list_title": "🛡 System roles:",
        "admin.roles.create": "➕ Create role",
        "admin.roles.edit": "✏️ Edit",
        "admin.roles.delete": "🗑 Delete",
        "admin.roles.detail": "🛡 <b>Role</b>: {name}\n📋 Permissions: {perms}\n👥 Users: {users}",
        "admin.roles.prompt_name": "Enter the role name (max 64 characters):",
        "admin.roles.name_invalid": "⚠️ Invalid name (empty or exceeds 64 characters).",
        "admin.roles.name_exists": "❌ A role with this name already exists",
        "admin.roles.select_perms": "Select permissions for role \"{name}\":",
        "admin.roles.confirm": "✅ Confirm",
        "admin.roles.created": "✅ Role \"{name}\" created",
        "admin.roles.updated": "✅ Role \"{name}\" updated",
        "admin.roles.deleted": "✅ Role deleted",
        "admin.roles.delete_confirm": "Are you sure you want to delete the role \"{name}\"?",
        "admin.roles.delete_fail": "❌ Failed to delete: {error}",
        "admin.roles.perm_denied": "⚠️ Insufficient permissions for this action",
        "admin.roles.assign_prompt": "Select a role for user {id}:",
        "admin.roles.assigned": "✅ Role {role} assigned to {name}",
        "admin.roles.assigned_notify": "ℹ️ Your role has been set to: {role}",
        "admin.roles.edit_name_prompt": "Enter the new role name (or /skip to keep current):",
        "btn.admin.assign_role": "🛡 Assign role",

        # === Admin: User Management ===
        "admin.users.prompt_enter_id": "👤 Enter the user ID to view / edit data",
        "admin.users.invalid_id": "⚠️ Please enter a valid numeric user ID.",
        "admin.users.profile_unavailable": "❌ Profile unavailable (such user never existed)",
        "admin.users.not_found": "❌ User not found",
        "admin.users.cannot_change_owner": "You cannot change the owner’s role",
        "admin.users.referrals": "👥 <b>User referrals</b> — {count}",
        "admin.users.btn.view_referrals": "👥 User's referrals",
        "admin.users.btn.view_earnings": "💰 User's earnings",
        "admin.users.role": "🎛 <b>Role</b> — {role}",
        "admin.users.set_admin.success": "✅ Role assigned to {name}",
        "admin.users.set_admin.notify": "✅ You have been granted the ADMIN role",
        "admin.users.remove_admin.success": "✅ Admin role revoked from {name}",
        "admin.users.remove_admin.notify": "❌ Your ADMIN role has been revoked",
        "admin.users.balance.topped": "✅ {name}'s balance has been topped up by {amount} {currency}",
        "admin.users.balance.topped.notify": "✅ Your balance has been topped up by {amount} {currency}",
        "admin.users.balance.deducted": "✅ Deducted {amount} {currency} from {name}'s balance",
        "admin.users.balance.deducted.notify": "ℹ️ {amount} {currency} has been deducted from your balance",
        "admin.users.balance.insufficient": "❌ Insufficient funds. Current balance: {balance} {currency}",
        "admin.users.blocked.success": "🚫 User {name} has been blocked",
        "admin.users.unblocked.success": "✅ User {name} has been unblocked",
        "admin.users.cannot_block_owner": "❌ Cannot block the owner",
        "admin.users.status.blocked": "🚫 <b>Status</b> — Blocked",

        # === Admin: Shop Management Menu ===
        "admin.shop.menu.title": "⛩️ Shop management",
        "admin.shop.menu.statistics": "📊 Statistics",
        "admin.shop.menu.logs": "📁 Show logs",
        "admin.shop.menu.users": "👤 Users",
        "admin.shop.menu.search_bought": "🔎 Search purchased item",

        # === Admin: Categories Management ===
        "admin.categories.menu.title": "⛩️ Categories management",
        "admin.categories.add": "➕ Add category",
        "admin.categories.rename": "✏️ Rename category",
        "admin.categories.delete": "🗑 Delete category",
        "admin.categories.prompt.add": "Enter a new category name:",
        "admin.categories.prompt.delete": "Enter the category name to delete:",
        "admin.categories.prompt.rename.old": "Enter the current category name to rename:",
        "admin.categories.prompt.rename.new": "Enter the new category name:",
        "admin.categories.add.exist": "❌ Category not created (already exists)",
        "admin.categories.add.success": "✅ Category created",
        "admin.categories.delete.not_found": "❌ Category not deleted (does not exist)",
        "admin.categories.delete.success": "✅ Category deleted",
        "admin.categories.rename.not_found": "❌ Category cannot be updated (does not exist)",
        "admin.categories.rename.exist": "❌ Cannot rename (a category with this name already exists)",
        "admin.categories.rename.success": "✅ Category \"{old}\" renamed to \"{new}\"",

        # === Admin: Goods / Items Management (Add / List / Item Info) ===
        "admin.goods.add_position": "➕ add item",
        "admin.goods.add_item": "➕ Add product to item",
        "admin.goods.update_position": "📝 change item",
        "admin.goods.delete_position": "❌ delete item",
        "admin.goods.show_items": "📄 show goods in item",
        "admin.goods.add.prompt.name": "Enter the item name",
        "admin.goods.add.name.exists": "❌ Item cannot be created (it already exists)",
        "admin.goods.add.name.invalid": "⚠️ Invalid name (1–100 characters, no control characters).",
        "admin.goods.add.prompt.description": "Enter item description:",
        "admin.goods.add.prompt.price": "Enter item price (number in {currency}):",
        "admin.goods.add.price.invalid": "⚠️ Invalid price. Please enter a number.",
        "admin.goods.add.prompt.category": "Enter the category the item belongs to:",
        "admin.goods.add.category.not_found": "❌ Item cannot be created (invalid category provided)",
        "admin.goods.add.infinity.question": "Should this item have infinite values? (everyone will receive the same value copy)",
        "admin.goods.add.values.prompt_multi": (
            "Send product values one per message.\n"
            "When finished, press “Add the listed goods”."
        ),
        "admin.goods.add.values.added": "✅ Value “{value}” added to the list ({count} pcs).",
        "admin.goods.add.result.created": "✅ Item has been created.",
        "admin.goods.add.result.added": "📦 Added values: <b>{n}</b>",
        "admin.goods.add.result.skipped_db_dup": "↩️ Skipped (already in DB): <b>{n}</b>",
        "admin.goods.add.result.skipped_batch_dup": "🔁 Skipped (duplicate in input): <b>{n}</b>",
        "admin.goods.add.result.skipped_invalid": "🚫 Skipped (empty/invalid): <b>{n}</b>",
        "admin.goods.add.single.prompt_value": "Enter a single value for the item:",
        "admin.goods.add.single.empty": "⚠️ Value cannot be empty.",
        "admin.goods.add.single.created": "✅ Item created, value added",
        "btn.add_values_finish": "Add the listed goods",
        "admin.goods.position.not_found": "❌ No goods (this item doesn't exist)",
        "admin.goods.list_in_position.empty": "ℹ️ There are no goods in this item yet.",
        "admin.goods.list_in_position.title": "Goods in item:",
        "admin.goods.item.invalid": "Invalid data",
        "admin.goods.item.invalid_id": "Invalid item ID",
        "admin.goods.item.not_found": "Item not found",
        "admin.goods.prompt.enter_item_name": "Enter the item name",
        "admin.goods.menu.title": "⛩️ Items management menu",

        # === Admin: Time-limited sales ===
        "admin.goods.sale_manage": "🔥 Manage discount",
        "admin.sale.prompt.name": "Enter the item name you want to set a discount for:",
        "admin.sale.not_found": "❌ No item with that name was found.",
        "admin.sale.current.active": "ℹ️ Current discount: <b>{percent}%</b> until <b>{until}</b> (UTC).",
        "admin.sale.current.none": "ℹ️ This item currently has no discount.",
        "admin.sale.prompt.percent": "Enter the discount percent (1–100).\nSend <b>0</b> to remove the discount.",
        "admin.sale.percent.invalid": "⚠️ Invalid percent. Enter an integer from 0 to 100.",
        "admin.sale.disabled": "✅ Discount for «{name}» has been removed.",
        "admin.sale.prompt.days": "For how many days should the discount last? Enter an integer (e.g. 3).",
        "admin.sale.days.invalid": "⚠️ Invalid duration. Enter an integer number of days greater than 0.",
        "admin.sale.success": "✅ Discount <b>{percent}%</b> set for «{name}» until <b>{until}</b> (UTC).",

        # === Admin: Goods / Items Update Flow ===
        "admin.goods.update.amount.prompt.name": "Enter the item name",
        "admin.goods.update.amount.not_exists": "❌ Unable to add values (item does not exist)",
        "admin.goods.update.amount.infinity_forbidden": "❌ Unable to add values (this item is infinite)",
        "admin.goods.update.values.result.title": "✅ Values added",
        "admin.goods.update.position.invalid": "Item not found.",
        "admin.goods.update.position.exists": "An item with this name already exists.",
        "admin.goods.update.prompt.name": "Enter the item name",
        "admin.goods.update.not_exists": "❌ Item cannot be updated (does not exist)",
        "admin.goods.update.prompt.new_name": "Enter a new item name:",
        "admin.goods.update.prompt.description": "Enter item description:",
        "admin.goods.update.infinity.make.question": "Do you want to make the item infinite?",
        "admin.goods.update.infinity.deny.question": "Do you want to disable infinity?",
        "admin.goods.update.success": "✅ Item updated",

        # === Admin: Goods / Items Delete Flow ===
        "admin.goods.delete.prompt.name": "Enter the item name",
        "admin.goods.delete.position.not_found": "❌ item not deleted (this item doesn't exist)",
        "admin.goods.delete.position.success": "✅ item deleted",
        "admin.goods.item.delete.button": "❌ Delete item",
        "admin.goods.item.already_deleted_or_missing": "Item already deleted or not found",
        "admin.goods.item.deleted": "✅ Item deleted",

        # === Admin: Item Info ===
        "admin.goods.item.info.position": "<b>Item</b>: <code>{name}</code>",
        "admin.goods.item.info.price": "<b>Price</b>: <code>{price}</code> {currency}",
        "admin.goods.item.info.id": "<b>Unique ID</b>: <code>{id}</code>",
        "admin.goods.item.info.value": "<b>Product</b>: <code>{value}</code>",

        # === Admin: Logs ===
        "admin.shop.logs.caption": "Bot logs",
        "admin.shop.logs.empty": "❗️ No logs yet",
        "admin.shop.logs.too_large": "⚠️ Logs are too large to send ({files}) — grab them from disk.",

        # === Group Notifications ===
        "shop.group.new_upload": "New stock",
        "shop.group.item": "Item",
        "shop.group.count": "Quantity",

        # === Admin: Statistics ===
        "admin.shop.stats.template": (
            "Shop statistics:\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "<b>◽USERS</b>\n"
            "◾️New in last 24h: {today_users}\n"
            "◾️Total: {users}\n"
            "◾️Buyers: {buyers}\n"
            "◾️Blocked: {blocked}\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "◽<b>FUNDS</b>\n"
            "◾Sales in last 24h: {today_orders} {currency} ({today_sold_count} pcs)\n"
            "◾Total sold: {all_orders} {currency}\n"
            "◾Avg order: {avg_order} {currency}\n"
            "◾Top-ups in last 24h: {today_topups} {currency}\n"
            "◾Funds in system: {system_balance} {currency}\n"
            "◾Total top-ups: {all_topups} {currency}\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
            "◽<b>CATALOG</b>\n"
            "◾In stock: {items} pcs\n"
            "◾Positions: {goods} pcs\n"
            "◾Categories: {categories} pcs\n"
            "◾Sold: {sold_count} pcs"
        ),
        "admin.shop.stats.roles_header": "\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n◽<b>ROLES</b>",

        # === Admin: Lists & Broadcast ===
        "admin.shop.users.title": "Bot users:",
        "admin.shop.bought.prompt_id": "Enter purchased item unique ID",
        "admin.shop.bought.not_found": "❌ Item with given unique ID not found",
        "broadcast.prompt": "Send a message to broadcast:",
        "broadcast.creating": "📤 Starting the newsletter...\n👥 Total users: {ids}",
        "broadcast.progress": (
            "📤 Broadcasting in progress...\n\n"
            "📊 Progress: {progress:.1f}%\n"
            "✅ Sent: {sent}/{total}\n"
            "❌ Errors: {failed}\n"
            "⏱ Time elapsed: {time} sec"),
        "broadcast.done": (
            "✅ Broadcasting is complete! \n\n"
            "📊 Statistics:📊\n"
            "👥 Total: {total}\n"
            "✅ Delivered: {sent}\n"
            "❌ Undelivered: {failed}\n"
            "🚫 Blocked bot: {blocked}\n"
            "📈 Success rate: {success}%\n"
            "⏱ Time: {duration} sec"
        ),
        "broadcast.cancel": "❌ The broadcast has been canceled.",
        "broadcast.warning": "No active broadcast",
        "broadcast.already_running": "⏳ A broadcast is already running. Wait for it to finish.",
        "broadcast.btn.cancel": "🛑 Cancel broadcast",

        # === Payments / Top-up Flow ===
        "payments.replenish_prompt": "Enter top-up amount in {currency}:",
        "payments.replenish_invalid": "❌ Invalid amount. Enter a number from {min_amount} to {max_amount} {currency}.",
        "payments.deduct_prompt": "Enter deduction amount in {currency}:",
        "payments.deduct_invalid": "❌ Invalid amount. Enter a number from {min_amount} to {max_amount} {currency}.",
        "payments.method_choose": "Choose a payment method:",
        "payments.not_configured": "❌ Top-ups are not configured",
        "payments.session_expired": "Payment session has expired. Please start again.",
        "payments.crypto.create_fail": "❌ Failed to create invoice: {error}",
        "payments.crypto.api_error": "❌ CryptoPay API error: {error}",
        "payments.crypto.check_fail": "❌ Payment check failed: {error}",
        "payments.stars.create_fail": "❌ Failed to issue Stars invoice: {error}",
        "payments.fiat.create_fail": "❌ Failed to issue invoice: {error}",
        "payments.no_active_invoice": "❌ No active invoices found. Start top-up again.",
        "payments.invoice_not_found": "❌ Invoice not found. Please start again.",
        "payments.not_paid_yet": "⌛️ Payment is not completed yet.",
        "payments.expired": "❌ Invoice has expired.",
        "payments.invoice.summary": (
            "💵 Top-up amount: {amount} {currency}.\n"
            "⌛️ You have {minutes} minutes to pay.\n"
            "<b>❗️ After paying, press «{button}»</b>"
        ),
        "payments.unable_determine_amount": "❌ Failed to determine the paid amount.",
        "payments.topped_simple": "✅ Balance topped up by {amount} {currency}",
        "payments.topped_with_suffix": "✅ Balance topped up by {amount} {currency} ({suffix})",
        "payments.success_suffix.stars": "Telegram Stars",
        "payments.success_suffix.tg": "Telegram Payments",
        "payments.referral.bonus": "✅ You received {amount} {currency} from your referral <a href='tg://user?id={id}'>{name}</a>",
        "payments.invoice.title.topup": "Balance top-up",
        "payments.invoice.desc.topup.stars": "Top-up {amount} {currency} via Telegram Stars",
        "payments.invoice.desc.topup.fiat": "Pay via Telegram Payments (card)",
        "payments.invoice.label.fiat": "Top-up {amount} {currency}",
        "payments.invoice.label.stars": "{stars} ⭐️",
        "payments.already_processed": "This payment has already been processed ✅",
        "payments.processing_error": "Payment processing error. Please try again later.",

        # === Shop Browsing (Categories / Goods / Item Page) ===
        "shop.categories.title": "🏪 Shop categories",
        "shop.search.prompt": "🔍 Enter a product name or keyword:",
        "shop.search.too_short": "The query must be 2 to 64 characters. Try again:",
        "shop.search.results": "🔍 Results for “{query}” — found: {count}",
        "shop.search.empty": "🔍 Nothing found for “{query}”.",
        "shop.goods.choose": "🏪 Choose a product",
        "shop.item.not_found": "Item not found",
        "shop.item.title": "🏪 Item {name}",
        "shop.item.description": "Description: {description}",
        "shop.item.price": "Price — {amount} {currency}",
        "shop.item.quantity_unlimited": "Quantity — unlimited",
        "shop.item.quantity_left": "Quantity — {count} pcs",
        "shop.insufficient_funds": "❌ Insufficient funds",
        "shop.out_of_stock": "❌ Item is out of stock",
        "shop.purchase.success": "✅ Item purchased. <b>Balance</b>: <i>{balance}</i> {currency}\n\n{value}",
        "shop.purchase.receipt": "✅ Order placed successfully!\n➖➖➖➖➖➖➖➖➖➖➖➖\n📃 Item: {item_name}\n💰 Price: {price} {currency}\n📦 Qty: 1\n💡 Order: {unique_id}\n🕐 Time: {datetime}\n💲 Total: {price} {currency}\n👤 Buyer: @{username} ({user_id})\n➖➖➖➖➖➖➖➖➖➖➖➖\n🔑 Value:\n<code>{value}</code>",
        "shop.purchase.processing": "⏳ Processing the purchase...",
        "shop.purchase.fail.user_not_found": "❌ User not found in the system",
        "shop.purchase.fail.general": "❌ Purchase error: {message}",

        # === Purchases ===
        "purchases.title": "Purchased items:",
        "purchases.pagination.invalid": "Invalid pagination data",
        "purchases.item.not_found": "Purchase not found",
        "purchases.item.name": "<b>🧾 Item</b>: <code>{name}</code>",
        "purchases.item.price": "<b>💵 Price</b>: <code>{amount}</code> {currency}",
        "purchases.item.datetime": "<b>🕒 Purchased at</b>: <code>{dt}</code>",
        "purchases.item.unique_id": "<b>🧾 Unique ID</b>: <code>{uid}</code>",
        "purchases.item.value": "<b>🔑 Value</b>:\n<code>{value}</code>",
        "purchases.item.buyer": "<b>Buyer</b>: <code>{buyer}</code>",

        # === Middleware ===
        "middleware.ban": "⏳ You are temporarily blocked. Wait {time} seconds.",
        "middleware.above_limits": "⚠️ Too many requests! You are temporarily blocked.",
        "middleware.waiting": "⏳ Wait {time} seconds for the next action.",
        "middleware.security.session_outdated": "⚠️ Session is outdated. Please start again.",
        "middleware.security.invalid_data": "❌ Invalid data",
        "middleware.security.blocked": "❌ Access blocked",
        "middleware.security.not_admin": "⛔ Insufficient permissions",
        "middleware.security.invalid_csrf": "⚠️ Session expired. Please try again.",
        "maintenance.active": "🔧 The bot is under maintenance. Please try again later.",

        # === Admin: Maintenance ===
        "admin.menu.maintenance_on": "🔧 Maintenance: ON",
        "admin.menu.maintenance_off": "🔧 Maintenance: OFF",
        "admin.maintenance.enabled": "✅ Maintenance mode enabled",
        "admin.maintenance.disabled": "✅ Maintenance mode disabled",

        # === Promo Codes ===
        "btn.apply_promo": "🏷 Apply promo code",
        "btn.remove_promo": "❌ Remove promo code",
        "admin.menu.promo": "🏷 Promo Codes",
        "admin.promo.title": "🏷 <b>Promo Code Management</b>",
        "admin.promo.create": "➕ Create promo code",
        "admin.promo.list_empty": "No promo codes yet.",
        "admin.promo.prompt.code": "Enter promo code (up to 50 characters):",
        "admin.promo.prompt.type": "Choose discount type:",
        "admin.promo.type.percent": "📊 Percent (%)",
        "admin.promo.type.fixed": "💰 Fixed amount",
        "admin.promo.prompt.value": "Enter discount value ({type}):",
        "admin.promo.prompt.max_uses": "Enter max uses (0 = unlimited):",
        "admin.promo.prompt.expires": "Enter the last valid day (YYYY-MM-DD) — the code works through the end of that day, or 0 for no expiry:",
        "admin.promo.prompt.binding": "Bind to category/item?\n\nSend:\n• Category name\n• Item name\n• 0 — no binding",
        "admin.promo.created": "✅ Promo code <code>{code}</code> created!",
        "admin.promo.code_exists": "❌ Promo code already exists.",
        "admin.promo.invalid_code": "❌ A code may contain only letters, digits and hyphens (up to 50 characters).",
        "admin.promo.deleted": "✅ Promo code deleted.",
        "admin.promo.toggled_on": "✅ Promo code activated.",
        "admin.promo.toggled_off": "⛔ Promo code deactivated.",
        "admin.promo.btn.activate": "✅ Activate",
        "admin.promo.btn.deactivate": "⛔ Deactivate",
        "admin.promo.btn.delete": "🗑 Delete",
        "admin.promo.detail": "🏷 <b>Promo Code</b>: <code>{code}</code>\n📊 Type: {discount_type}\n💰 Discount: {discount_value}\n🔗 Applies to: {binding}\n🔢 Uses: {current_uses}/{max_uses}\n📅 Expires: {expires_at}\n✅ Active: {is_active}",
        "admin.promo.confirm_delete": "Delete promo code <code>{code}</code>?",
        "admin.promo.invalid_value": "❌ Invalid value. Try again.",
        "admin.promo.invalid_date": "❌ Invalid date. Format: YYYY-MM-DD",
        "promo.not_found": "❌ Promo code not found.",
        "promo.inactive": "❌ Promo code is inactive.",
        "promo.expired": "❌ Promo code has expired.",
        "promo.max_uses_reached": "❌ Promo code uses exhausted.",
        "promo.already_used": "❌ You already used this promo code.",
        "promo.wrong_item": "❌ Promo code is not applicable to this item.",
        "promo.wrong_category": "❌ Promo code is not applicable to this category.",
        "promo.applied": "✅ Promo code <code>{code}</code> applied! Discount: {discount}",
        "promo.enter_code": "Enter promo code:",
        "promo.removed": "Promo code removed.",
        "promo.not_balance_type": "❌ This promo code is not a balance top-up code.",
        "promo.enter_redeem_code": "Enter promo code to redeem:",
        "promo.balance_redeemed": "✅ Promo code <code>{code}</code> redeemed! {amount} {currency} added to your balance.",
        "shop.item.price_discounted": "💰 <b>Price</b>: <s>{original}</s> <b>{discounted}</b> {currency} (promo {code})",
        "shop.item.price_sale": "🔥 <b>Price</b>: <s>{original}</s> <b>{sale}</b> {currency} ({percent}% off)",
        "admin.promo.type.balance": "💰 Balance top-up",
        "admin.promo.prompt.binding_type": "Bind promo code to category or item?",
        "admin.promo.binding.category": "Category",
        "admin.promo.binding.item": "Item",
        "admin.promo.binding.none": "No binding",
        "admin.promo.binding.on_category": "category “{name}”",
        "admin.promo.binding.on_item": "item “{name}”",
        "admin.promo.binding.dangling": "⚠️ binding deleted — this promo applies to nothing",
        "admin.promo.prompt.category_name": "Enter category name:",
        "admin.promo.prompt.item_name": "Enter item name:",
        "admin.promo.category_not_found": "❌ Category not found.",
        "admin.promo.item_not_found": "❌ Item not found.",
        "btn.redeem_promo": "🏷 Redeem promo code",
        "review.disabled": "Reviews are disabled.",

        # === Cart ===
        "btn.cart": "🛒 Cart ({count})",
        "btn.cart_empty": "🛒 Cart",
        "btn.add_to_cart": "🛒 Add to cart",
        "btn.cart_checkout": "💳 Checkout",
        "btn.cart_clear": "🗑 Clear cart",
        "btn.cart_remove_item": "❌ {name}",
        "btn.cart_remove_promo": "🏷 Remove promo {code}",
        "btn.cart_receipt_all": "📋 All purchases",
        "cart.title": "🛒 <b>Cart</b>",
        "cart.empty": "Cart is empty.",
        "cart.item": "• {name} ×{qty} — {price} {currency}",
        "cart.item_sale": "🔥 <b>{name}</b> ×{qty} — <s>{original}</s> {price} {currency}",
        "cart.item_promo": "🏷 <b>{name}</b> ×{qty} — <s>{original}</s> {price} {currency} ({code})",
        "cart.item_promo_invalid": "⚠️ <b>{name}</b> ×{qty} — {price} {currency}\n    promo {code} does not apply to this item",
        "cart.item_promo_elsewhere": "• {name} ×{qty} — {price} {currency}\n    promo {code} was applied to another line",
        "cart.total": "\n💰 <b>Total</b>: {total} {currency}",
        "cart.added": "✅ {name} added to cart.",
        "cart.full": "❌ Cart is full (max 10 items).",
        "cart.qty_max": "❌ Maximum {max} units of one item.",
        "cart.out_of_stock": "Not enough stock for the requested quantity. Reduce it and try again.",
        "cart.price_changed": "The cart total changed. Open the cart and confirm the new amount.",
        "cart.item_not_found": "❌ Item not found.",
        "cart.removed": "✅ Item removed from cart.",
        "cart.cleared": "✅ Cart cleared.",
        "cart.checkout_confirm": "Checkout {count} item(s) for {total} {currency}?",
        "cart.checkout_success": "✅ Order placed! Bought {count} item(s).\n\n💰 Balance: {balance} {currency}",
        "cart.checkout_receipt": "✅ Order placed!\n➖➖➖➖➖➖➖➖➖➖➖➖\n📦 Qty: {count}\n💲 Total: {total} {currency}\n👤 Buyer: @{username} ({user_id})\n🕐 Time: {datetime}\n➖➖➖➖➖➖➖➖➖➖➖➖\nTap an item to view details:",
        "cart.checkout_fail": "❌ Checkout failed: {reason}",
        "cart.items_unavailable": "Some items are no longer available and were removed from cart.",


        # === Stock Subscriptions ===
        "btn.notify_stock": "🔔 Notify me when in stock",
        "btn.notify_stock_off": "🔕 Cancel notification",
        "stock.subscribed": "🔔 We'll let you know when it's back.",
        "stock.unsubscribed": "🔕 Notification cancelled.",
        "stock.back_in_stock": "🔔 <b>{name}</b> is back in stock!",


        # === Operation History ===
        "btn.operation_history": "📋 Operation History",
        "history.title": "📋 <b>Operation History</b>",
        "history.empty": "Operation history is empty.",
        "history.topup": "💰 Top-up: +{amount} {currency}",
        "history.purchase": "🛒 Purchase: {amount} {currency}",
        "history.referral": "🎲 Referral bonus: +{amount} {currency}",
        "history.date": "📅 {date}",

        # === Reviews ===
        "btn.leave_review": "⭐ Leave a review",
        "btn.view_reviews": "📝 Reviews ({count})",
        "btn.skip_review_text": "⏭ Skip text",
        "review.prompt_rating": "Rate <b>{name}</b> from 1 to 5:",
        "review.prompt_text": "Write a review (up to 500 chars) or click Skip:",
        "review.created": "✅ Thank you for your review!",
        "review.already_exists": "You already reviewed this item.",
        "review.not_purchased": "You haven't purchased this item.",
        "review.avg_rating": "⭐ Rating: {rating}/5 ({count} reviews)",
        "review.item": "⭐ {rating}/5 — {text}",
        "review.item_no_text": "⭐ {rating}/5",
        "review.list_title": "📝 <b>Reviews for {name}</b>",
        "review.list_empty": "No reviews yet.",

        # === Errors ===
        "errors.not_subscribed": "You are not subscribed",
        "errors.something_wrong": "❌ Something went wrong. Please try again.",
        "errors.pagination_invalid": "Invalid pagination data",
        "errors.invalid_data": "❌ Invalid data",
        "errors.id_should_be_number": "❌ ID must be a number.",
        "errors.channel.telegram_not_found": "I can't write to the channel. Add me as a channel admin for uploads @{channel} with the right to publish messages.",
        "errors.channel.telegram_forbidden_error": "Channel not found. Check the channel username for uploads @{channel}.",
        "errors.channel.telegram_bad_request": "Failed to send to the channel for uploads: {e}",
        "errors.general_error": "❌ Error: {e}",
        "errors.invalid_item_name": "❌ Invalid item name",
        "errors.invalid_user": "❌ Invalid user",
    },
}
