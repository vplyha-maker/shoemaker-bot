from aiogram import Router, F, types
from keyboards import (
    get_materials_chemistry_keyboard,
    get_materials_menu_keyboard,
    get_back_to_materials_keyboard
)
from handlers.base import user_language
from texts.materials_texts import MATERIALS_INTRO_RU, MATERIALS_INTRO_UK, TEXTS_RU, TEXTS_UK

router = Router()

# 1. При нажатии «Материалы и химия» в Главном меню -> Открываем выбор (Материалы / Химия)
@router.callback_query(F.data == "menu_chemistry")
async def process_materials_chemistry_menu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    
    text = (
        "🧪 **Раздел «Материалы и Химия».**\n\nВыберите подраздел для изучения:"
        if lang == "ru" else
        "🧪 **Розділ «Матеріали та Хімія».**\n\nОберіть підрозділ для вивчення:"
    )
    keyboard = get_materials_chemistry_keyboard(lang)
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")

# 2. Нажатие на «Химия» (Всплывающее окно-заглушка)
@router.callback_query(F.data == "sub_chemistry")
async def process_sub_chemistry_stub(callback: types.CallbackQuery):
    lang = user_language.get(callback.from_user.id, "ru")
    text = (
        "🧪 **Раздел «Химия и Клеи» находится в разработке.**\n\nСкоро здесь появятся материалы по полиуретановым клеям, праймерам, аппретурам и финишам."
        if lang == "ru" else
        "🧪 **Розділ «Хімія та Клеї» перебуває в розробці.**\n\nСкоро тут з'являться матеріали щодо поліуретанових клеїв, праймерів та аппретур."
    )
    await callback.answer(text, show_alert=True)

# 3. Нажатие на «Материалы» -> Переход к 4 категориям
@router.callback_query(F.data == "sub_materials")
async def process_materials_menu(callback: types.CallbackQuery):
    await callback.answer()
    lang = user_language.get(callback.from_user.id, "ru")
    
    text = MATERIALS_INTRO_RU if lang == "ru" else MATERIALS_INTRO_UK
    keyboard = get_materials_menu_keyboard(lang)
    
    await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="Markdown")

# 4. Просмотр конкретной категории материалов (Кожа, Подошвы, Подкладка, Экзотика)
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


