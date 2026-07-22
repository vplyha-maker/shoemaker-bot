from aiogram import Router, F, types
from keyboards import (
    get_materials_chemistry_keyboard,
    get_materials_menu_keyboard,
    get_back_to_materials_keyboard
)
from handlers.base import user_language
from texts.materials_texts import MATERIALS_INTRO_RU, MATERIALS_INTRO_UK, TEXTS_RU, TEXTS_UK

router = Router()

# 1. Открытие главного меню подраздела «Материалы»
@router.callback_query(F.data == "sub_materials")
async def process_materials_menu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    
    text = MATERIALS_INTRO_RU if lang == "ru" else MATERIALS_INTRO_UK
    keyboard = get_materials_menu_keyboard(lang)
    
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")

# 2. Отображение выбранной категории материалов с поддержкой языков
@router.callback_query(F.data.startswith("mat_cat_"))
async def process_material_category(callback: types.CallbackQuery):
    await callback.answer()
    
    lang = user_language.get(callback.from_user.id, "ru")
    category_key = callback.data 
    
    texts_dict = TEXTS_RU if lang == "ru" else TEXTS_UK
    content_text = texts_dict.get(category_key, "Контент не найден." if lang == "ru" else "Контент не знайдено.")

    await callback.message.edit_text(
        content_text,
        reply_markup=get_back_to_materials_keyboard(lang),
        parse_mode="Markdown"
    )

def register_materials_handlers(dp):
    dp.include_router(router)

