from aiogram import Router, F, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

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

# Вспомогательная функция для безопасного обновления меню (работает и для текста, и для фото)
async def safe_edit_or_send(callback: types.CallbackQuery, text: str, reply_markup=None):
    try:
        await callback.message.edit_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    except TelegramBadRequest:
        # Если текущее сообщение — это фото, edit_text выдаст ошибку.
        # В таком случае удаляем фото и отправляем чистое текстовое меню.
        await callback.message.delete()
        await callback.message.answer(text, reply_markup=reply_markup, parse_mode="Markdown")


# 1. Главное меню раздела (Выбор: Цвета или Колористика)
@router.callback_query(F.data == "menu_colors")
async def process_colors_main_menu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    
    text = (
        "🎨 *Раздел* «Цвета и Колористика»**\n\nВыберите подраздел:"
        if lang == "ru" else
        "🎨 *Розділ* «Кольори та Колористика»**\n\nОберіть підрозділ:"
    )
    await safe_edit_or_send(callback, text, get_colors_main_menu_keyboard(lang))


# 2. Подраздел «Цвета»
@router.callback_query(F.data == "sub_menu_colors")
async def process_colors_submenu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    text = COLORS_INTRO_RU if lang == "ru" else COLORS_INTRO_UK
    
    await safe_edit_or_send(callback, text, get_colors_submenu_keyboard(lang))


# 3. Обработчик всех 4-х кнопок внутри «Цвета»
@router.callback_query(F.data.in_(COLOR_TEXTS_RU.keys()))
async def process_color_topic(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    
    texts_dict = COLOR_TEXTS_RU if lang == "ru" else COLOR_TEXTS_UK
    content_text = texts_dict.get(callback.data, "Информация не найдена.")
    
    await safe_edit_or_send(callback, content_text, get_back_to_colors_keyboard(lang))


# 4. Заглушка для будущей кнопки «Колористика»
@router.callback_query(F.data == "sub_menu_coloristics")
async def process_coloristics_placeholder(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    text = (
        "🚧 Раздел «Колористика» находится в разработке.\n\nСкоро здесь появятся материалы!"
        if lang == "ru" else
        "🚧 Розділ «Колористика» знаходиться в розробці.\n\nНезабаром тут з'являться матеріали!"
    )
    
    builder = InlineKeyboardBuilder()
    back_btn_text = "◀️ Назад"
    builder.row(InlineKeyboardButton(text=back_btn_text, callback_data="menu_colors"))
    
    await safe_edit_or_send(callback, text, builder.as_markup())


# 5. Обработчик для Цветового круга Иттена
@router.callback_query(F.data == "color_itten")
async def process_itten_circle(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    text = ITTEN_CIRCLE_TEXT.get(lang, ITTEN_CIRCLE_TEXT["ru"])
    
    builder = InlineKeyboardBuilder()
    back_text = "◀️ Назад к разделам" if lang == "ru" else "◀️ Назад до розділів"
    # Возвращаем в подраздел "Цвета"
    builder.row(InlineKeyboardButton(text=back_text, callback_data="sub_menu_colors"))
    
    try:
        photo = types.FSInputFile("images/itten.jpg") 
        # Удаляем предыдущее текстовое меню, чтобы сообщения не дублировались
        await callback.message.delete()
        
        # Отправляем ФОТО С ПОДПИСЬЮ
        await callback.message.answer_photo(
            photo=photo,
            caption=text,
            reply_markup=builder.as_markup(),
            parse_mode="Markdown"
        )
    except Exception as e:
        print(f"Ошибка загрузки фото (отправляем текстом): {e}")
        # Если фото не найдено, просто редактируем текст
        await safe_edit_or_send(callback, text, builder.as_markup())


def register_colors_handlers(dp):
    dp.include_router(router)
