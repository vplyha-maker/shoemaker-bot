# handlers/assistant.py

from aiogram import Router, F, types
from handlers.base import user_language
from keyboards import (
    get_assistant_main_menu_keyboard,
    get_assistant_glue_soles_keyboard,
    get_assistant_trouble_keyboard,
    get_assistant_check_keyboard,
    get_back_to_assistant_keyboard
)
from texts.assistant_texts import (
    ASSISTANT_INTRO_RU, ASSISTANT_INTRO_UK,
    GLUE_CHOICE_SOLE_RU, GLUE_CHOICE_SOLE_UK,
    GLUE_RECIPES_RU, GLUE_RECIPES_UK,
    TROUBLESHOOT_MENU_RU, TROUBLESHOOT_MENU_UK,
    TROUBLESHOOT_TEXTS_RU, TROUBLESHOOT_TEXTS_UK,
    CHECKLISTS_MENU_RU, CHECKLISTS_MENU_UK,
    CHECKLISTS_TEXTS_RU, CHECKLISTS_TEXTS_UK
)

router = Router()

# Главное меню экспресс-помощника
@router.callback_query(F.data == "menu_helper")
async def process_assistant_menu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    text = ASSISTANT_INTRO_RU if lang == "ru" else ASSISTANT_INTRO_UK
    
    await callback.message.edit_text(
        text, 
        reply_markup=get_assistant_main_menu_keyboard(lang), 
        parse_mode="Markdown"
    )

# Клик 1: Старт подборщика склейки -> переходим к выбору подошвы
@router.callback_query(F.data == "asst_glue_start")
async def process_glue_start(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    text = GLUE_CHOICE_SOLE_RU if lang == "ru" else GLUE_CHOICE_SOLE_UK
    
    await callback.message.edit_text(
        text,
        reply_markup=get_assistant_glue_soles_keyboard(lang),
        parse_mode="Markdown"
    )

# Результат подбора склейки (возврат назад к выбору подошвы)
@router.callback_query(F.data.in_(["glue_res_leather_tep", "glue_res_leather_pu", "glue_res_suede_rubber"]))
async def process_glue_result(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    recipes = GLUE_RECIPES_RU if lang == "ru" else GLUE_RECIPES_UK
    
    text = recipes.get(callback.data.replace("glue_res_", ""), "Рецепт не найден.")
    await callback.message.edit_text(
        text,
        reply_markup=get_back_to_assistant_keyboard(lang, back_callback="asst_glue_start"),
        parse_mode="Markdown"
    )

# Меню исправления брака
@router.callback_query(F.data == "asst_trouble_menu")
async def process_trouble_menu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    text = TROUBLESHOOT_MENU_RU if lang == "ru" else TROUBLESHOOT_MENU_UK
    
    await callback.message.edit_text(
        text,
        reply_markup=get_assistant_trouble_keyboard(lang),
        parse_mode="Markdown"
    )

# Шаг 2: Тексты исправления брака (возврат назад в меню брака)
@router.callback_query(F.data.in_(["err_glue", "err_heat", "err_white"]))
async def process_trouble_text(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    texts = TROUBLESHOOT_TEXTS_RU if lang == "ru" else TROUBLESHOOT_TEXTS_UK
    
    text = texts.get(callback.data, "Информация не найдена.")
    await callback.message.edit_text(
        text,
        reply_markup=get_back_to_assistant_keyboard(lang, back_callback="asst_trouble_menu"),
        parse_mode="Markdown"
    )

# Меню чек-листов
@router.callback_query(F.data == "asst_check_menu")
async def process_check_menu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    text = CHECKLISTS_MENU_RU if lang == "ru" else CHECKLISTS_MENU_UK
    
    await callback.message.edit_text(
        text,
        reply_markup=get_assistant_check_keyboard(lang),
        parse_mode="Markdown"
    )

# Шаг 2: Тексты чек-листов (возврат назад в меню чек-листов)
@router.callback_query(F.data.in_(["check_last", "check_paint"]))
async def process_check_text(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    texts = CHECKLISTS_TEXTS_RU if lang == "ru" else CHECKLISTS_TEXTS_UK
    
    text = texts.get(callback.data, "Информация не найдена.")
    await callback.message.edit_text(
        text,
        reply_markup=get_back_to_assistant_keyboard(lang, back_callback="asst_check_menu"),
        parse_mode="Markdown"
    )

def register_assistant_handlers(dp):
    dp.include_router(router)
