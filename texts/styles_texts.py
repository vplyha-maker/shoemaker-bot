from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_styles_constructions_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    """Клавиатура разделения на Фасоны и Конструкции"""
    builder = InlineKeyboardBuilder()

    if lang == "ru":
        builder.row(InlineKeyboardButton(text="👞 Фасоны и Силуэты", callback_data="sub_styles"))
        builder.row(InlineKeyboardButton(text="⚙️ Конструкции сборки (В разработке)", callback_data="sub_constructions"))
        builder.row(InlineKeyboardButton(text="⬅️ Главное меню", callback_data="back_to_main"))
    else:  # uk
        builder.row(InlineKeyboardButton(text="👞 Фасони та Силуети", callback_data="sub_styles"))
        builder.row(InlineKeyboardButton(text="⚙️ Конструкції збирання (В розробці)", callback_data="sub_constructions"))
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
    """Кнопка возврата из карточки товара в меню фасонов"""
    builder = InlineKeyboardBuilder()
    back_text = "⬅️ Назад к фасонам" if lang == "ru" else "⬅️ Назад до фасонів"
    builder.row(InlineKeyboardButton(text=back_text, callback_data="sub_styles"))
    return builder.as_markup()

