from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def get_language_keyboard():
    """Клавиатура выбора языка"""
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"))
    builder.row(InlineKeyboardButton(text="🇺🇦 Українська", callback_data="lang_uk"))
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
