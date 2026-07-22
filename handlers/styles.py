from aiogram import Router, F, types
from keyboards import (
    get_styles_constructions_keyboard,
    get_styles_menu_keyboard,
    get_back_to_styles_keyboard,
    get_main_menu
)
from handlers.base import user_language
from texts.styles_texts import STYLES_INTRO_RU, STYLES_INTRO_UK, TEXTS_RU, TEXTS_UK

router = Router()


# 1. Нажатие на кнопку главного меню «Фасоны и Конструкции»
@router.callback_query(F.data == "menu_styles")
async def process_styles_and_constructions(callback: types.CallbackQuery):
    await callback.answer()  # <--- Сразу гасим анимацию кнопки!
    
    lang = user_language.get(callback.from_user.id, "ru")
    text = (
        "📐 **Выберите интересующий подраздел:**" 
        if lang == "ru" else 
        "📐 **Оберіть потрібний підрозділ:**"
    )

    await callback.message.edit_text(
        text,
        reply_markup=get_styles_constructions_keyboard(lang),
        parse_mode="Markdown"
    )


# 2. Нажатие на кнопку 1: «Фасоны и Силуэты»
@router.callback_query(F.data == "sub_styles")
async def process_sub_styles(callback: types.CallbackQuery):
    await callback.answer()  # <--- Сразу гасим анимацию кнопки
    
    lang = user_language.get(callback.from_user.id, "ru")
    text = STYLES_INTRO_RU if lang == "ru" else STYLES_INTRO_UK

    await callback.message.edit_text(
        text,
        reply_markup=get_styles_menu_keyboard(lang),
        parse_mode="Markdown"
    )


# 3. Нажатие на «Конструкции сборки» (Заглушка)
@router.callback_query(F.data == "sub_constructions")
async def process_sub_constructions(callback: types.CallbackQuery):
    lang = user_language.get(callback.from_user.id, "ru")
    text = (
        "⚙️ **Раздел «Конструкции сборки» находится в разработке.**\n\nСкоро здесь появятся материалы по рантовому методу (Goodyear Welted), Клеевому, Врантовому (Blake) и др."
        if lang == "ru" else
        "⚙️ **Розділ «Конструкції збирання» перебуває в розробці.**\n\nСкоро тут з'являться матеріали про рантовий метод (Goodyear Welted), Клейовий, Блейк (Blake) тощо."
    )
    await callback.answer(text, show_alert=True)


# 4. Отображение выбранного фасона (4 подкнопки)
@router.callback_query(F.data.startswith("style_cat_"))
async def process_style_category(callback: types.CallbackQuery):
    await callback.answer()  # <--- Сразу гасим анимацию кнопки
    
    lang = user_language.get(callback.from_user.id, "ru")
    category_key = callback.data  # Берем полный ключ (например, "style_cat_toe")

    # Выбираем словарь в зависимости от языка пользователя
    texts_dict = TEXTS_RU if lang == "ru" else TEXTS_UK
    content_text = texts_dict.get(category_key, "Контент не найден." if lang == "ru" else "Контент не знайдено.")

    # Выводим сообщение с карточкой
    await callback.message.edit_text(
        content_text,
        reply_markup=get_back_to_styles_keyboard(lang),
        parse_mode="Markdown"
    )


# 5. Возврат в главное меню
@router.callback_query(F.data == "back_to_main")
async def back_to_main_menu_handler(callback: types.CallbackQuery):
    await callback.answer()  # <--- Сразу гасим анимацию кнопки
    
    lang = user_language.get(callback.from_user.id, "ru")
    title = "🏛 **Главное меню «Энциклопедии Сапожника»**" if lang == "ru" else "🏛 **Головне меню «Енциклопедії Чоботаря»**"
    
    await callback.message.edit_text(
        title,
        reply_markup=get_main_menu(lang),
        parse_mode="Markdown"
    )


def register_styles_handlers(dp):
    dp.include_router(router)


