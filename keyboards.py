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
    
# Цвета и колористика(добавить к существующему коду)

def get_colors_main_menu_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if lang == "ru":
        builder.row(InlineKeyboardButton(text="🎨 Цвета", callback_data="sub_menu_colors"))
        builder.row(InlineKeyboardButton(text="🌈 Колористика", callback_data="sub_menu_coloristics"))
        builder.row(InlineKeyboardButton(text="◀️ Главное меню", callback_data="back_to_main"))
    else:
        builder.row(InlineKeyboardButton(text="🎨 Кольори", callback_data="sub_menu_colors"))
        builder.row(InlineKeyboardButton(text="🌈 Колористика", callback_data="sub_menu_coloristics"))
        builder.row(InlineKeyboardButton(text="◀️ Головне меню", callback_data="back_to_main"))
    return builder.as_markup()

def get_colors_submenu_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if lang == "ru":
        builder.row(InlineKeyboardButton(text="🧠 Психология цвета в обуви", callback_data="color_psychology"))
        builder.row(InlineKeyboardButton(text="💎 Как создать \"дорогой\" оттенок", callback_data="color_expensive"))
        builder.row(InlineKeyboardButton(text="🧪 Формулы смешивания пигментов", callback_data="color_mixing"))
        builder.row(InlineKeyboardButton(text="🔄 Таблица получения редких тонов", callback_data="color_rare_tones"))
        # 👇 ЗДЕСЬ ИСПРАВЛЕНО (для русского):
        builder.row(InlineKeyboardButton(text="◀️ Назад к разделам", callback_data="menu_colors"))
    else:
        builder.row(InlineKeyboardButton(text="🧠 Психологія кольору у взутті", callback_data="color_psychology"))
        builder.row(InlineKeyboardButton(text="💎 Як створити \"дорогий\" відтінок", callback_data="color_expensive"))
        builder.row(InlineKeyboardButton(text="🧪 Формули змішування пігментів", callback_data="color_mixing"))
        builder.row(InlineKeyboardButton(text="🔄 Таблиця отримання рідкісних тонів", callback_data="color_rare_tones"))
        # 👇 ЗДЕСЬ ИСПРАВЛЕНО (для украинского):
        builder.row(InlineKeyboardButton(text="◀️ Назад до розділів", callback_data="menu_colors"))
    return builder.as_markup()

def get_back_to_colors_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    text = "◀️ К списку тем (Цвета)" if lang == "ru" else "◀️ До списку тем (Кольори)"
    builder.row(InlineKeyboardButton(text=text, callback_data="sub_menu_colors"))
    return builder.as_markup()

# глосарий
def get_glossary_main_menu_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if lang == "ru":
        builder.row(InlineKeyboardButton(text="🧱 Материалы и детали", callback_data="glossary_materials"))
        builder.row(InlineKeyboardButton(text="🛠 Процессы и технологии", callback_data="glossary_processes"))
        builder.row(InlineKeyboardButton(text="◀️ Главное меню", callback_data="back_to_main"))
    else:
        builder.row(InlineKeyboardButton(text="🧱 Матеріали та деталі", callback_data="glossary_materials"))
        builder.row(InlineKeyboardButton(text="🛠 Процеси та технології", callback_data="glossary_processes"))
        builder.row(InlineKeyboardButton(text="◀️ Головне меню", callback_data="back_to_main"))
    return builder.as_markup()

def get_back_to_glossary_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    text = "◀️ Назад к глоссарию" if lang == "ru" else "◀️ Назад до глосарію"
    builder.row(InlineKeyboardButton(text=text, callback_data="menu_glossary"))
    return builder.as_markup()
    
    # Экспресс помошник
def get_assistant_main_menu_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if lang == "ru":
        builder.row(InlineKeyboardButton(text="🧪 Подборщик склейки", callback_data="asst_glue_start"))
        builder.row(InlineKeyboardButton(text="🚨 Исправление брака", callback_data="asst_trouble_menu"))
        builder.row(InlineKeyboardButton(text="📋 Чек-листы операций", callback_data="asst_check_menu"))
        builder.row(InlineKeyboardButton(text="◀️ Главное меню", callback_data="back_to_main"))
    else:
        builder.row(InlineKeyboardButton(text="🧪 Підбір склеювання", callback_data="asst_glue_start"))
        builder.row(InlineKeyboardButton(text="🚨 Виправлення браку", callback_data="asst_trouble_menu"))
        builder.row(InlineKeyboardButton(text="📋 Чек-листи операцій", callback_data="asst_check_menu"))
        builder.row(InlineKeyboardButton(text="◀️ Головне меню", callback_data="back_to_main"))
    return builder.as_markup()

def get_assistant_glue_soles_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if lang == "ru":
        builder.row(InlineKeyboardButton(text="🥾 ТЭП (Термоэластопласт)", callback_data="glue_res_leather_tep"))
        builder.row(InlineKeyboardButton(text="🛞 ПУ (Полиуретан)", callback_data="glue_res_leather_pu"))
        builder.row(InlineKeyboardButton(text="👟 Резина / Нитрил", callback_data="glue_res_suede_rubber"))
        builder.row(InlineKeyboardButton(text="◀️ Назад к помощнику", callback_data="menu_helper"))

    else:
        builder.row(InlineKeyboardButton(text="🥾 ТЕП", callback_data="glue_res_leather_tep"))
        builder.row(InlineKeyboardButton(text="🛞 ПУ (Поліуретан)", callback_data="glue_res_leather_pu"))
        builder.row(InlineKeyboardButton(text="👟 Гума / Нітрил", callback_data="glue_res_suede_rubber"))
        builder.row(InlineKeyboardButton(text="◀️ Назад до помічника", callback_data="menu_helper"))
    return builder.as_markup()

def get_assistant_trouble_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if lang == "ru":
        builder.row(InlineKeyboardButton(text="❌ Клей не держит / Отклеивается", callback_data="err_glue"))
        builder.row(InlineKeyboardButton(text="🔥 Кожа сжалась от фена", callback_data="err_heat"))
        builder.row(InlineKeyboardButton(text="⚪ Белый налет при покраске", callback_data="err_white"))
        builder.row(InlineKeyboardButton(text="◀️ Назад к помощнику", callback_data="menu_helper"))

    else:
        builder.row(InlineKeyboardButton(text="❌ Клей не тримає", callback_data="err_glue"))
        builder.row(InlineKeyboardButton(text="🔥 Шкіра стиснулася від фена", callback_data="err_heat"))
        builder.row(InlineKeyboardButton(text="⚪ Білий наліт при фарбуванні", callback_data="err_white"))
        builder.row(InlineKeyboardButton(text="◀️ Назад до помічника", callback_data="menu_helper"))

    return builder.as_markup()

def get_assistant_check_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if lang == "ru":
        builder.row(InlineKeyboardButton(text="📋 Перед затяжкой на колодку", callback_data="check_last"))
        builder.row(InlineKeyboardButton(text="📋 Перед финишной покраской", callback_data="check_paint"))
        builder.row(InlineKeyboardButton(text="◀️ Назад к помощнику", callback_data="menu_helper"))

    else:
        builder.row(InlineKeyboardButton(text="📋 Перед затяжкою на колодку", callback_data="check_last"))
        builder.row(InlineKeyboardButton(text="📋 Перед фінішним фарбуванням", callback_data="check_paint"))
        builder.row(InlineKeyboardButton(text="◀️ Назад до помічника", callback_data="menu_helper"))

    return builder.as_markup()

def get_back_to_assistant_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    text = "◀️ К экспресс-помощнику" if lang == "ru" else "◀️ До експрес-помічника"
    builder.row(InlineKeyboardButton(text=text, callback_data="callback_data="menu_helper"

    return builder.as_markup()



