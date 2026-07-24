from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keyboards import get_calculators_keyboard, get_main_keyboard
from texts.calculators_texts import CALCULATOR_TEXTS

router = Router()

class SizeConverterState(StatesGroup):
    category = State()
    waiting_for_length = State()

# Таблицы соответствия (Длина стопы см: EU, UK, US)
SIZE_CHARTS = {
    "men": [
        (24.5, "38.5", "5.5", "6"), (25.0, "39", "6", "6.5"), (25.5, "40", "6.5", "7.5"),
        (26.0, "40.5 - 41", "7", "8"), (26.5, "41.5 - 42", "7.5", "8.5"), (27.0, "42", "8", "9"),
        (27.5, "42.5 - 43", "8.5", "9.5"), (28.0, "43.5 - 44", "9.5", "10.5"), (28.5, "44.5", "10", "11"),
        (29.0, "45", "10.5", "11.5"), (29.5, "45.5 - 46", "11", "12"), (30.0, "46.5 - 47", "12", "13"),
        (30.5, "47.5", "12.5", "13.5"), (31.0, "48", "13", "14")
    ],
    "women": [
        (21.5, "34", "2", "4.5"), (22.0, "34.5 - 35", "2.5", "5"), (22.5, "35.5", "3", "5.5"),
        (23.0, "36", "3.5", "6"), (23.5, "36.5 - 37", "4", "6.5"), (24.0, "37.5 - 38", "4.5", "7"),
        (24.5, "38.5", "5", "7.5"), (25.0, "39", "5.5", "8"), (25.5, "39.5 - 40", "6", "8.5"),
        (26.0, "40.5", "6.5", "9"), (26.5, "41 - 41.5", "7", "9.5"), (27.0, "42", "7.5", "10")
    ],
    "kids": [
        (10.5, "17", "1.5", "2"), (11.0, "18", "2", "2.5"), (11.5, "19", "3", "3.5"),
        (12.0, "19.5", "3.5", "4"), (12.5, "20", "4", "4.5"), (13.0, "21", "4.5", "5"),
        (13.5, "22", "5.5", "6"), (14.0, "22.5", "6", "6.5"), (14.5, "23", "6.5", "7"),
        (15.0, "24", "7", "8"), (15.5, "25", "7.5", "8.5"), (16.0, "25.5", "8.5", "9"),
        (16.5, "26", "8.5", "9.5"), (17.0, "27", "9", "10"), (17.5, "28", "10", "11"),
        (18.0, "28.5", "10.5", "11.5"), (18.5, "29", "11", "12"), (19.0, "30", "11.5", "12.5"),
        (19.5, "31", "12", "13"), (20.0, "31.5", "12.5", "13.5"), (20.5, "32", "13", "1 Y"),
        (21.0, "33", "1", "1.5 Y"), (21.5, "33.5", "1.5", "2 Y")
    ]
}

async def get_user_lang(state: FSMContext, user_lang_code: str) -> str:
    """Вспомогательная функция определения языка пользователя"""
    data = await state.get_data()
    if "language" in data:
        return data["language"]
    if "lang" in data:
        return data["lang"]
    return "uk" if user_lang_code and "uk" in user_lang_code.lower() else "ru"

def get_gender_inline_keyboard(lang: str):
    t = CALCULATOR_TEXTS.get(lang, CALCULATOR_TEXTS["ru"])
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=t["gender_men"], callback_data="gender_men"),
                InlineKeyboardButton(text=t["gender_women"], callback_data="gender_women"),
            ],
            [
                InlineKeyboardButton(text=t["gender_kids"], callback_data="gender_kids")
            ]
        ]
    )

# 1. Открытие меню калькуляторов (ловит кнопки на обоих языках)
@router.message(F.text.in_(["🧮 Калькуляторы и конвертеры", "🧮 Калькулятори та конвертери"]))
async def open_calculators_menu(message: Message, state: FSMContext):
    lang = await get_user_lang(state, message.from_user.language_code)
    t = CALCULATOR_TEXTS[lang]
    await message.answer(t["menu_title"], reply_markup=get_calculators_keyboard(lang))

# 2. Кнопка Назад
@router.message(F.text.in_(["🔙 Назад в главное меню", "🔙 Назад у головне меню"]))
async def back_to_main_menu(message: Message, state: FSMContext):
    lang = await get_user_lang(state, message.from_user.language_code)
    t = CALCULATOR_TEXTS[lang]
    await state.clear()
    await message.answer(t["back_msg"], reply_markup=get_main_keyboard())

# 3. Нажатие на кнопку "Размеры обуви"
@router.message(F.text.in_(["📏 Размеры обуви", "📏 Розміри взуття"]))
async def start_size_converter(message: Message, state: FSMContext):
    lang = await get_user_lang(state, message.from_user.language_code)
    t = CALCULATOR_TEXTS[lang]
    await message.answer(t["select_gender"], reply_markup=get_gender_inline_keyboard(lang))

# 4. Выбор пола
@router.callback_query(F.data.startswith("gender_"))
async def process_gender_choice(callback: CallbackQuery, state: FSMContext):
    lang = await get_user_lang(state, callback.from_user.language_code)
    t = CALCULATOR_TEXTS[lang]
    
    category = callback.data.split("_")[1]
    cat_name = t[f"cat_{category}"]
    
    await state.update_data(category=category, lang=lang)
    await state.set_state(SizeConverterState.waiting_for_length)
    
    await callback.message.edit_text(
        t["enter_length"].format(category=cat_name),
        parse_mode="HTML"
    )
    await callback.answer()

# 5. Расчет размера
@router.message(SizeConverterState.waiting_for_length)
async def calculate_size(message: Message, state: FSMContext):
    lang = await get_user_lang(state, message.from_user.language_code)
    t = CALCULATOR_TEXTS[lang]
    
    # Если пользователь решил выйти в меню во время ввода
    if message.text in [
        "🔙 Назад в главное меню", "🔙 Назад у головне меню",
        "📏 Размеры обуви", "📏 Розміри взуття",
        "🧮 Калькуляторы и конвертеры", "🧮 Калькулятори та конвертери"
    ]:
        await state.clear()
        return

    data = await state.get_data()
    category = data.get("category", "men")
    
    try:
        length_cm = float(message.text.replace(',', '.'))
        chart = SIZE_CHARTS.get(category, SIZE_CHARTS["men"])
        
        closest_entry = min(chart, key=lambda x: abs(x[0] - length_cm))
        cm_match, eu, uk, us = closest_entry
        cat_name = t[f"cat_{category}"]
        
        text = t["result_text"].format(
            category=cat_name,
            length=length_cm,
            eu=eu,
            uk=uk,
            us=us,
            mm=int(length_cm * 10),
            match=cm_match
        )
        
        await message.answer(text, parse_mode="HTML", reply_markup=get_calculators_keyboard(lang))
        await state.clear()
        
    except ValueError:
        await message.answer(t["error_num"])
