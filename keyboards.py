from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_language_keyboard():
    """Клавиатура выбора языка"""
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text=" Русский", callback_data="lang_ru"))
    builder.row(InlineKeyboardButton(text=" Українська", callback_data="lang_uk"))
    return builder.as_markup()


def get_main_menu(lang: str = "ru"):
    """Главное меню"""
    builder = InlineKeyboardBuilder()

    if lang == "ru":
        builder.row(InlineKeyboardButton(text="📐 Размеры, Мерки и Ортопедия", callback_data="menu_sizes"))
        builder.row(InlineKeyboardButton(text="👞 Фасоны и Конструкции", callback_data="menu_styles"))
        builder.row(InlineKeyboardButton(text="🧪 Материалы и Химия", callback_data="menu_chemistry"))
        builder.row(InlineKeyboardButton(text="🎨 Цвета и Колористика", callback_data="menu_colors"))
        builder.row(InlineKeyboardButton(text="🧮 Калькуляторы и Конвертеры", callback_data="menu_calculators"))
        builder.row(InlineKeyboardButton(text="🧼 Реставрация, Уход и Глассаж", callback_data="menu_care"))
        builder.row(InlineKeyboardButton(text="🛠 Инструменты, Заточка и ТБ", callback_data="menu_tools"))
        builder.row(InlineKeyboardButton(text="🧩 Экспресс-помощник", callback_data="menu_helper"))
        builder.row(InlineKeyboardButton(text="📋 Чек-листы и Стандарты", callback_data="menu_checklists"))
        builder.row(InlineKeyboardButton(text="📖 Глоссарий терминов", callback_data="menu_glossary"))
        builder.row(InlineKeyboardButton(text="✂️ Бесплатные лекала (PDF)", callback_data="menu_patterns"))
        builder.row(InlineKeyboardButton(text="👥 Сообщество мастеров", callback_data="menu_community"))
    else:  # uk
        builder.row(InlineKeyboardButton(text="📐 Розміри, Мірки та Ортопедія", callback_data="menu_sizes"))
        builder.row(InlineKeyboardButton(text="👞 Фасони та Конструкції", callback_data="menu_styles"))
        builder.row(InlineKeyboardButton(text="🧪 Матеріали та Хімія", callback_data="menu_chemistry"))
        builder.row(InlineKeyboardButton(text="🎨 Кольори та Колористика", callback_data="menu_colors"))
        builder.row(InlineKeyboardButton(text="🧮 Калькулятори та Конвертери", callback_data="menu_calculators"))
        builder.row(InlineKeyboardButton(text="🧼 Реставрація, Догляд та Глассаж", callback_data="menu_care"))
        builder.row(InlineKeyboardButton(text="🛠 Інструменти, Заточка та ТБ", callback_data="menu_tools"))
        builder.row(InlineKeyboardButton(text="🧩 Експрес-помічник", callback_data="menu_helper"))
        builder.row(InlineKeyboardButton(text="📋 Чек-листи та Стандарти", callback_data="menu_checklists"))
        builder.row(InlineKeyboardButton(text="📖 Глосарій термінів", callback_data="menu_glossary"))
        builder.row(InlineKeyboardButton(text="✂️ Безкоштовні лекала (PDF)", callback_data="menu_patterns"))
        builder.row(InlineKeyboardButton(text="👥 Спільнота майстрів", callback_data="menu_community"))

    return builder.as_markup()


def get_styles_constructions_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    """Клавиатура разделения на Фасоны и Конструкции"""
    builder = InlineKeyboardBuilder()

    if lang == "ru":
        builder.row(InlineKeyboardButton(text="👞 Фасоны и Силуэты", callback_data="sub_styles"))
        builder.row(InlineKeyboardButton(text="⚙️ Конструкции и Методы крепления", callback_data="sub_constructions"))
        builder.row(InlineKeyboardButton(text="⬅️ Главное меню", callback_data="back_to_main"))
    else:  # uk
        builder.row(InlineKeyboardButton(text="👞 Фасони та Силуети", callback_data="sub_styles"))
        builder.row(InlineKeyboardButton(text="⚙️ Конструкції та Методи кріплення", callback_data="sub_constructions"))
        builder.row(InlineKeyboardButton(text="⬅️ Головне меню", callback_data="back_to_main"))

    return builder.as_markup()


def get_styles_menu_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    """Клавиатура с 4 категориями фасонов"""
    builder = InlineKeyboardBuilder()

    if lang == "ru":
        builder.row(InlineKeyboardButton(text="📐 Формы носочной части (Колодки)", callback_data="style_cat_toe"))
        builder.row(InlineKeyboardButton(text="👞 Классические фасоны (Мужские/Унисекс)", callback_data="style_cat_classic"))
        builder.row(InlineKeyboardButton(text="👠 Женские силуэты и каблуки", callback_data="style_cat_women"))
        builder.row(InlineKeyboardButton(text="👟 Спортивные и уличные конструкции", callback_data="style_cat_street"))
        builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="menu_styles"))
    else:  # uk
        builder.row(InlineKeyboardButton(text="📐 Форми носочної частини (Колодки)", callback_data="style_cat_toe"))
        builder.row(InlineKeyboardButton(text="👞 Класичні фасони (Чоловічі/Унісекс)", callback_data="style_cat_classic"))
        builder.row(InlineKeyboardButton(text="👠 Жіночі силуети та підбори", callback_data="style_cat_women"))
        builder.row(InlineKeyboardButton(text="👟 Спортивні та вуличні конструкції", callback_data="style_cat_street"))
        builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="menu_styles"))

    return builder.as_markup()


def get_back_to_styles_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    """Кнопка возврата из карточки фасона в меню фасонов"""
    builder = InlineKeyboardBuilder()
    back_text = "⬅️ Назад к фасонам" if lang == "ru" else "⬅️ Назад до фасонів"
    builder.row(InlineKeyboardButton(text=back_text, callback_data="sub_styles"))
    return builder.as_markup()


# 👇 НОВЫЕ КЛАВИАТУРЫ ДЛЯ РАЗДЕЛА КОНСТРУКЦИЙ:

def get_constructions_menu_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    """Клавиатура с 4 категориями конструкций"""
    builder = InlineKeyboardBuilder()

    if lang == "ru":
        builder.row(InlineKeyboardButton(text="🪡 Методы крепления подошвы", callback_data="const_cat_fastening"))
        builder.row(InlineKeyboardButton(text="🦴 Внутренний силовой каркас", callback_data="const_cat_frame"))
        builder.row(InlineKeyboardButton(text="👟 Конструкции верха (Крой)", callback_data="const_cat_upper"))
        builder.row(InlineKeyboardButton(text="💧 Гидроизоляция и мембраны", callback_data="const_cat_water"))
        builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="menu_styles"))
    else:  # uk
        builder.row(InlineKeyboardButton(text="🪡 Методи кріплення підошви", callback_data="const_cat_fastening"))
        builder.row(InlineKeyboardButton(text="🦴 Внутрішній силовий каркас", callback_data="const_cat_frame"))
        builder.row(InlineKeyboardButton(text="👟 Конструкції верху (Крій)", callback_data="const_cat_upper"))
        builder.row(InlineKeyboardButton(text="💧 Гідроізоляція та мембрани", callback_data="const_cat_water"))
        builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="menu_styles"))

    return builder.as_markup()


def get_back_to_constructions_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    """Кнопка возврата из карточки конструкции в меню конструкций"""
    builder = InlineKeyboardBuilder()
    back_text = "⬅️ Назад к конструкциям" if lang == "ru" else "⬅️ Назад до конструкцій"
    builder.row(InlineKeyboardButton(text=back_text, callback_data="sub_constructions"))
    return builder.as_markup()
    
#  Кнопки Материалы и химия

def get_materials_chemistry_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if lang == "ru":
        builder.row(InlineKeyboardButton(text="🪵 Материалы", callback_data="sub_materials"),
                    InlineKeyboardButton(text="🧪 Химия", callback_data="sub_chemistry"))
        builder.row(InlineKeyboardButton(text="⬅️ Главное меню", callback_data="back_to_main"))
    else:
        builder.row(InlineKeyboardButton(text="🪵 Матеріали", callback_data="sub_materials"),
                    InlineKeyboardButton(text="🧪 Хімія", callback_data="sub_chemistry"))
        builder.row(InlineKeyboardButton(text="⬅️ Головне меню", callback_data="back_to_main"))
    return builder.as_markup()

def get_materials_menu_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if lang == "ru":
        builder.row(InlineKeyboardButton(text="🐄 Натуральная кожа и замша", callback_data="mat_cat_leather"))
        builder.row(InlineKeyboardButton(text="🧪 Полимеры и материалы подошв", callback_data="mat_cat_soles"))
        builder.row(InlineKeyboardButton(text="🕸️ Подкладка и дублирование", callback_data="mat_cat_lining"))
        builder.row(InlineKeyboardButton(text="🐍 Экзотика и технологичные материалы", callback_data="mat_cat_exotic"))
        builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="menu_chemistry"))
    else:
        builder.row(InlineKeyboardButton(text="🐄 Натуральна шкіра та замша", callback_data="mat_cat_leather"))
        builder.row(InlineKeyboardButton(text="🧪 Полімери та матеріали підошов", callback_data="mat_cat_soles"))
        builder.row(InlineKeyboardButton(text="🕸️ Підкладка та дублювання", callback_data="mat_cat_lining"))
        builder.row(InlineKeyboardButton(text="🐍 Екзотика та технологічні матеріали", callback_data="mat_cat_exotic"))
        builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="menu_chemistry"))
    return builder.as_markup()

def get_back_to_materials_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    back_text = "⬅️ Назад к материалам" if lang == "ru" else "⬅️ Назад до матеріалів"
    builder.row(InlineKeyboardButton(text=back_text, callback_data="sub_materials"))
    return builder.as_markup()

def get_chemistry_menu_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if lang == "ru":
        builder.row(InlineKeyboardButton(text="🍯 Клеи и отвердители", callback_data="chem_cat_adhesives"))
        builder.row(InlineKeyboardButton(text="🧪 Очистители и праймеры", callback_data="chem_cat_primers"))
        builder.row(InlineKeyboardButton(text="✨ Аппретуры и воски", callback_data="chem_cat_finishes"))
        builder.row(InlineKeyboardButton(text="🛡️ Защита и спецхимия", callback_data="chem_cat_protection"))
        builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="menu_chemistry"))
    else:
        builder.row(InlineKeyboardButton(text="🍯 Клеї та затверджувачі", callback_data="chem_cat_adhesives"))
        builder.row(InlineKeyboardButton(text="🧪 Очисники та праймери", callback_data="chem_cat_primers"))
        builder.row(InlineKeyboardButton(text="✨ Апретури та воски", callback_data="chem_cat_finishes"))
        builder.row(InlineKeyboardButton(text="🛡️ Захист та спецхімія", callback_data="chem_cat_protection"))
        builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="menu_chemistry"))
    return builder.as_markup()

def get_back_to_chemistry_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    back_text = "⬅️ Назад к химии" if lang == "ru" else "⬅️ Назад до хімії"
    builder.row(InlineKeyboardButton(text=back_text, callback_data="sub_chemistry"))
    return builder.as_markup()


