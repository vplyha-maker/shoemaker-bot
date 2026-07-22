# handlers/glossary.py

from aiogram import Router, F, types
from handlers.base import user_language
from keyboards import (
    get_glossary_main_menu_keyboard,
    get_back_to_glossary_keyboard
)
from texts.glossary_texts import (
    GLOSSARY_INTRO_RU, GLOSSARY_INTRO_UK,
    GLOSSARY_MATERIALS_RU, GLOSSARY_MATERIALS_UK,
    GLOSSARY_PROCESSES_RU, GLOSSARY_PROCESSES_UK
)

router = Router()

# Главное меню глоссария (выбор категории)
@router.callback_query(F.data == "menu_glossary")
async def process_glossary_menu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    text = GLOSSARY_INTRO_RU if lang == "ru" else GLOSSARY_INTRO_UK
    
    await callback.message.edit_text(
        text, 
        reply_markup=get_glossary_main_menu_keyboard(lang), 
        parse_mode="Markdown"
    )

# Подраздел: Материалы и детали
@router.callback_query(F.data == "glossary_materials")
async def process_glossary_materials(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    text = GLOSSARY_MATERIALS_RU if lang == "ru" else GLOSSARY_MATERIALS_UK
    
    await callback.message.edit_text(
        text, 
        reply_markup=get_back_to_glossary_keyboard(lang), 
        parse_mode="Markdown"
    )

# Подраздел: Процессы и технологии
@router.callback_query(F.data == "glossary_processes")
async def process_glossary_processes(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    text = GLOSSARY_PROCESSES_RU if lang == "ru" else GLOSSARY_PROCESSES_UK
    
    await callback.message.edit_text(
        text, 
        reply_markup=get_back_to_glossary_keyboard(lang), 
        parse_mode="Markdown"
    )

def register_glossary_handlers(dp):
    dp.include_router(router)

