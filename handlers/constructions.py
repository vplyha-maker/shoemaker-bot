from aiogram import Router, F, types
from keyboards import (
    get_constructions_menu_keyboard,
    get_back_to_constructions_keyboard,
    get_main_menu
)
from handlers.base import user_language
from texts.constructions_texts import CONSTRUCTIONS_INTRO_RU, CONSTRUCTIONS_INTRO_UK, TEXTS_RU, TEXTS_UK

router = Router()

# 1. Открытие главного меню раздела «Конструкции»
@router.callback_query(F.data == "sub_constructions")
async def process_constructions_menu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    
    text = CONSTRUCTIONS_INTRO_RU if lang == "ru" else CONSTRUCTIONS_INTRO_UK
    keyboard = get_constructions_menu_keyboard(lang)
    
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")

# 2. Отображение выбранного конструктивного узла
@router.callback_query(F.data.startswith("const_cat_"))
async def process_construction_category(callback: types.CallbackQuery):
    await callback.answer()
    
    lang = user_language.get(callback.from_user.id, "ru")
    category_key = callback.data  # Например: "const_cat_fastening"
    
    texts_dict = TEXTS_RU if lang == "ru" else TEXTS_UK
    content_text = texts_dict.get(category_key, "Контент не найден." if lang == "ru" else "Контент не знайдено.")

    await callback.message.edit_text(
        content_text,
        reply_markup=get_back_to_constructions_keyboard(lang),
        parse_mode="Markdown"
    )

def register_constructions_handlers(dp):
    dp.include_router(router)

