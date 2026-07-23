# handlers/colors.py

from aiogram import Router, F, types
from handlers.base import user_language
from keyboards import (
    get_colors_main_menu_keyboard,
    get_colors_submenu_keyboard,
    get_back_to_colors_keyboard
)
from texts.colors_texts import (
    COLORS_INTRO_RU, COLORS_INTRO_UK, 
    COLOR_TEXTS_RU, COLOR_TEXTS_UK,
    ITTEN_CIRCLE_TEXT
)

router = Router()

# 1. Главное меню раздела (Выбор: Цвета или Колористика)
@router.callback_query(F.data == "menu_colors")
async def process_colors_main_menu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    
    text = (
        "🎨 **Раздел «Цвета и Колористика»**\n\nВыберите подраздел:"
        if lang == "ru" else
        "🎨 **Розділ «Кольори та Колористика»**\n\nОберіть підрозділ:"
    )
    await callback.message.edit_text(
        text, 
        reply_markup=get_colors_main_menu_keyboard(lang), 
        parse_mode="Markdown"
    )

# 2. Подраздел «Цвета»
@router.callback_query(F.data == "sub_menu_colors")
async def process_colors_submenu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    text = COLORS_INTRO_RU if lang == "ru" else COLORS_INTRO_UK
    
    await callback.message.edit_text(
        text, 
        reply_markup=get_colors_submenu_keyboard(lang), 
        parse_mode="Markdown"
    )

# 3. Обработчик всех 4-х кнопок внутри «Цвета»
@router.callback_query(F.data.in_(COLOR_TEXTS_RU.keys()))
async def process_color_topic(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    
    # Выбираем нужный словарь в зависимости от языка
    texts_dict = COLOR_TEXTS_RU if lang == "ru" else COLOR_TEXTS_UK
    content_text = texts_dict.get(callback.data, "Информация не найдена.")
    
    await callback.message.edit_text(
        content_text, 
        reply_markup=get_back_to_colors_keyboard(lang), 
        parse_mode="Markdown"
    )

# 4. Заглушка для будущей кнопки «Колористика» (чтобы не было ошибки)
@router.callback_query(F.data == "sub_menu_coloristics")
async def process_coloristics_placeholder(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    text = (
        "🚧 Раздел «Колористика» находится в разработке.\n\nСкоро здесь появятся материалы!"
        if lang == "ru" else
        "🚧 Розділ «Колористика» знаходиться в розробці.\n\nНезабаром тут з'являться матеріали!"
    )
    # 👇 ВСТАВЛЯТЬ СЮДА 👇

# 5. Обработчик для Цветового круга Иттена
@router.callback_query(F.data == "color_itten")
async def process_itten_circle(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    
    # Берем текст в зависимости от языка
    text = ITTEN_CIRCLE_TEXT_RU if lang == "ru" else ITTEN_CIRCLE_TEXT_UK
    
    # Пытаемся удалить старое сообщение с меню, чтобы было красиво
    try:
        await callback.message.delete()
    except Exception:
        pass
        
    # Ссылка на картинку
    ITTEN_IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Itten_color_wheel.svg/1024px-Itten_color_wheel.svg.png"
    
    # Отправляем фото
    try:
        await callback.message.answer_photo(photo=ITTEN_IMAGE_URL)
    except Exception as e:
        print(f"Ошибка загрузки фото: {e}")
        
    # Создаем кнопку "Назад" к главному меню цветов
    from aiogram.utils.keyboard import InlineKeyboardBuilder
    from aiogram.types import InlineKeyboardButton
    builder = InlineKeyboardBuilder()
    back_text = "◀️ Назад к цветам" if lang == "ru" else "◀️ Назад до кольорів"
    builder.row(InlineKeyboardButton(text=back_text, callback_data="menu_colors"))
    
    # Отправляем текст с правилами
    await callback.message.answer(
        text, 
        reply_markup=builder.as_markup(), 
        parse_mode="Markdown"
    )

# 👆 КОНЕЦ ВСТАВКИ 👆
    # Кнопка возврата в меню выбора (Цвета / Колористика)
    from aiogram.utils.keyboard import InlineKeyboardBuilder
    from aiogram.types import InlineKeyboardButton
    builder = InlineKeyboardBuilder()
    back_btn_text = "◀️ Назад" if lang == "ru" else "◀️ Назад"
    builder.row(InlineKeyboardButton(text=back_btn_text, callback_data="menu_colors"))
    
    await callback.message.edit_text(text, reply_markup=builder.as_markup(), parse_mode="Markdown")

def register_colors_handlers(dp):
    dp.include_router(router)

