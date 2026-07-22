from aiogram import Router, F, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.base import user_language
from texts.colors_texts import (
    COLORS_INTRO_RU, COLORS_INTRO_UK,
    COLOR_TEXTS_RU, COLOR_TEXTS_UK
)

router = Router()

# 1. Главный выбор раздела: Цвета или Колористика
@router.callback_query(F.data == "menu_colors_coloristics")
async def process_colors_main_menu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    
    builder = InlineKeyboardBuilder()
    if lang == "ru":
        builder.row(types.InlineKeyboardButton(text="🎨 Цвета в обуви", callback_data="sub_menu_colors"))
        builder.row(types.InlineKeyboardButton(text="🌈 Колористика (в разработке)", callback_data="sub_menu_coloristics_dev"))
        builder.row(types.InlineKeyboardButton(text="◀️ Главное меню", callback_data="back_to_main"))
        text = "🎨 **Эстетика, цвета и колористика**\n\nВыберите подраздел для изучения:"
    else:
        builder.row(types.InlineKeyboardButton(text="🎨 Кольори у взутті", callback_data="sub_menu_colors"))
        builder.row(types.InlineKeyboardButton(text="🌈 Колористика (в розробці)", callback_data="sub_menu_coloristics_dev"))
        builder.row(types.InlineKeyboardButton(text="◀️ Головне меню", callback_data="back_to_main"))
        text = "🎨 **Естетика, кольори та колористика**\n\nОберіть підрозділ для вивчення:"
    
    await callback.message.edit_text(text, reply_markup=builder.as_markup(), parse_mode="Markdown")

# Заглушка для пока не заполненного подраздела «Колористика»
@router.callback_query(F.data == "sub_menu_coloristics_dev")
async def process_coloristics_dev(callback: types.CallbackQuery):
    lang = user_language.get(callback.from_user.id, "ru")
    alert_text = "Этот подраздел находится в разработке 🚧" if lang == "ru" else "Цей підрозділ знаходиться в розробці 🚧"
    await callback.answer(alert_text, show_alert=True)

# 2. Открытие подменю «Цвета» (с четырьмя кнопками тем)
@router.callback_query(F.data == "sub_menu_colors")
async def process_colors_submenu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    
    builder = InlineKeyboardBuilder()
    if lang == "ru":
        builder.row(types.InlineKeyboardButton(text="🧠 Психология цвета в обуви", callback_data="color_psychology"))
        builder.row(types.InlineKeyboardButton(text="💎 Как создать \"дорогой\" оттенок", callback_data="color_expensive"))
        builder.row(types.InlineKeyboardButton(text="🧪 Формулы смешивания пигментов", callback_data="color_mixing"))
        builder.row(types.InlineKeyboardButton(text="🔄 Таблица получения редких тонов", callback_data="color_rare_tones"))
        builder.row(types.InlineKeyboardButton(text="◀️ Назад к подразделам", callback_data="menu_colors_coloristics"))
        text = COLORS_INTRO_RU
    else:
        builder.row(types.InlineKeyboardButton(text="🧠 Психологія кольору у взутті", callback_data="color_psychology"))
        builder.row(types.InlineKeyboardButton(text="💎 Як створити \"дорогий\" відтінок", callback_data="color_expensive"))
        builder.row(types.InlineKeyboardButton(text="🧪 Формули змішування пігментів", callback_data="color_mixing"))
        builder.row(types.InlineKeyboardButton(text="🔄 Таблиця отримання рідкісних тонів", callback_data="color_rare_tones"))
        builder.row(types.InlineKeyboardButton(text="◀️ Назад до підрозділів", callback_data="menu_colors_coloristics"))
        text = COLORS_INTRO_UK
    
    await callback.message.edit_text(text, reply_markup=builder.as_markup(), parse_mode="Markdown")

# 3. Обработка нажатий на конкретные темы раздела «Цвета»
@router.callback_query(F.data.in_(COLOR_TEXTS_RU.keys()))
async def process_color_topic(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    topic_key = callback.data
    
    texts_dict = COLOR_TEXTS_RU if lang == "ru" else COLOR_TEXTS_UK
    content_text = texts_dict.get(topic_key, "Информация не найдена." if lang == "ru" else "Інформацію не знайдено.")
    
    builder = InlineKeyboardBuilder()
    back_btn_text = "◀️ К списку тем (Цвета)" if lang == "ru" else "◀️ До списку тем (Кольори)"
    builder.row(types.InlineKeyboardButton(text=back_btn_text, callback_data="sub_menu_colors"))
    
    await callback.message.edit_text(content_text, reply_markup=builder.as_markup(), parse_mode="Markdown")

def register_colors_handlers(dp):
    dp.include_router(router)

