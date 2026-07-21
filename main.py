import os
import asyncio
import logging
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.keepalive import start_web_server, self_ping
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Не найден BOT_TOKEN в переменных окружения.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

    

# ==========================================
# 🏛 ГЛАВНОЕ МЕНЮ (12 РАЗДЕЛОВ)
# ==========================================
def get_main_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📐 Размеры, Мерки и Ортопедия", callback_data="menu_sizes"))
    builder.row(InlineKeyboardButton(text="👞 Фасоны и Конструкции", callback_data="menu_styles"))
    builder.row(InlineKeyboardButton(text="🧪 Материалы и Химия", callback_data="menu_chemistry"))
    builder.row(InlineKeyboardButton(text="🎨 Цвета и Колористика", callback_data="menu_colors"))
    builder.row(InlineKeyboardButton(text="🧮 Калькуляторы и Конвертеры", callback_data="menu_calculators"))
    builder.row(InlineKeyboardButton(text="🧼 Реставрация, Уход и Глассаж", callback_data="menu_care"))
    builder.row(InlineKeyboardButton(text="🛠 Инструменты, Заточка и ТБ", callback_data="menu_tools"))
    builder.row(InlineKeyboardButton(text="🧩 Экспресс-помощник", callback_data="menu_helper"))
    builder.row(InlineKeyboardButton(text="📋 Чек-листы и Стандарты", callback_data="menu_checklists"))
    builder.row(InlineKeyboardButton(text="📖 Глоссарий терминов", callback_data="menu_glossary"))
    builder.row(InlineKeyboardButton(text="✂️ Бесплатные лекала (PDF)", callback_data="menu_patterns"))
    builder.row(InlineKeyboardButton(text="👥 Сообщество мастеров", callback_data="menu_community"))
    return builder.as_markup()

# ==========================================
# 🛠 ПОДМЕНЮ ДЛЯ РАЗДЕЛОВ
# ==========================================

def get_sizes_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📏 Штихмассовая и Метрическая системы", callback_data="sizes_systems"))
    builder.row(InlineKeyboardButton(text="🦶 Как правильно снять мерку стопы", callback_data="sizes_measuring"))
    builder.row(InlineKeyboardButton(text="👟 Полнота стопы и ортопедия", callback_data="sizes_width"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_main"))
    return builder.as_markup()

def get_styles_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="👞 Классические фасоны (Оксфорды, Дерби...)", callback_data="styles_classic"))
    builder.row(InlineKeyboardButton(text="🪡 Методы крепления (Goodyear, Blake...)", callback_data="styles_welts"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_main"))
    return builder.as_markup()

def get_chemistry_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🧴 Клеи и Термоактивация", callback_data="chem_glues"))
    builder.row(InlineKeyboardButton(text="🥩 Виды кож и Дубление", callback_data="chem_leather"))
    builder.row(InlineKeyboardButton(text="🧪 Аппретуры, Воски и Финиши", callback_data="chem_finishes"))
    builder.row(InlineKeyboardButton(text="🧼 Растворители и Очистители", callback_data="chem_solvents"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_main"))
    return builder.as_markup()

def get_colors_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🧹 Подготовка кожи к окрашиванию", callback_data="colors_prep"))
    builder.row(InlineKeyboardButton(text="🎨 Техники патины и градиента", callback_data="colors_patina"))
    builder.row(InlineKeyboardButton(text="🧪 Смешивание красок и закрепление", callback_data="colors_mix"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_main"))
    return builder.as_markup()

def get_calculators_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📐 Перевод кв. футов в кв. дециметры (дм²)", callback_data="calc_sqft"))
    builder.row(InlineKeyboardButton(text="⚖️ Толщина кожи: Oz в миллиметры (мм)", callback_data="calc_oz"))
    builder.row(InlineKeyboardButton(text="🪡 Расчет длины нити на шов", callback_data="calc_thread"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_main"))
    return builder.as_markup()

def get_care_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="✨ Глассаж (Зеркальная полировка)", callback_data="care_glassage"))
    builder.row(InlineKeyboardButton(text="🧼 Чистка и выведение соли", callback_data="care_cleaning"))
    builder.row(InlineKeyboardButton(text="🪥 Уход за замшей и нубуком", callback_data="care_suede"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_main"))
    return builder.as_markup()

def get_tools_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🔪 Углы заточки сапожного ножа", callback_data="tools_sharpening"))
    builder.row(InlineKeyboardButton(text="🔨 Пробойники, канавкарезы и борды", callback_data="tools_punches"))
    builder.row(InlineKeyboardButton(text="🥽 Техника безопасности (ТБ)", callback_data="tools_safety"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_main"))
    return builder.as_markup()

def get_helper_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🧩 Подбор клея по материалам подошвы", callback_data="helper_glue"))
    builder.row(InlineKeyboardButton(text="🪡 Выбор нити и шага пробойника", callback_data="helper_thread"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_main"))
    return builder.as_markup()

def get_checklists_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📋 Чек-лист приемки обуви в ремонт", callback_data="check_intake"))
    builder.row(InlineKeyboardButton(text="🔎 Контроль качества затяжки", callback_data="check_quality"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_main"))
    return builder.as_markup()

# ==========================================
# 🚀 ОБРАБОТЧИКИ КОМАНД И НАВИГАЦИИ
# ==========================================

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    welcome_text = (
        f"Приветствую, **{message.from_user.first_name}**! 🤝\n\n"
        "🏛 **Добро пожаловать в «Энциклопедию Сапожника»**\n"
        "Ваш профессиональный цифровой помощник в мире конструирования, ремонта и ухода за обувью.\n\n"
        "Проект создан для объединения мастеров и свободного обмена знаниями:\n"
        "🔹 *Проверенные технологии и стандарты*\n"
        "🔹 *Справочники по химии, клеям и материалам*\n"
        "🔹 *Удобные калькуляторы и бесплатные лекала*\n\n"
        "👇 **Выберите интересующий раздел меню, чтобы начать:**"
    )
    await message.answer(welcome_text, reply_markup=get_main_menu(), parse_mode="Markdown")

@dp.callback_query(lambda c: c.data == "back_main")
async def back_main(callback: types.CallbackQuery):
    back_text = (
        "🏛 **Главное меню «Энциклопедии Сапожника»**\n\n"
        "👇 **Выберите интересующий раздел:**"
    )
    await callback.message.edit_text(back_text, reply_markup=get_main_menu(), parse_mode="Markdown")
    await callback.answer()

# === ГЛАВНЫЙ МАРШРУТИЗАТОР ===
@dp.callback_query(lambda c: c.data.startswith('menu_'))
async def process_main_menu(callback: types.CallbackQuery):
    section = callback.data.split('_')[1]

    if section == "sizes":
        await callback.message.edit_text("📐 **Раздел: Размеры, Мерки и Ортопедия**\n\nВыберите категорию:", reply_markup=get_sizes_menu(), parse_mode="Markdown")
    elif section == "styles":
        await callback.message.edit_text("👞 **Раздел: Фасоны и Конструкции**\n\nВыберите категорию:", reply_markup=get_styles_menu(), parse_mode="Markdown")
    elif section == "chemistry":
        await callback.message.edit_text("🧪 **Раздел: Материалы и Химия**\n\nВыберите категорию:", reply_markup=get_chemistry_menu(), parse_mode="Markdown")
    elif section == "colors":
        await callback.message.edit_text("🎨 **Раздел: Цвета и Колористика**\n\nВыберите категорию:", reply_markup=get_colors_menu(), parse_mode="Markdown")
    elif section == "calculators":
        await callback.message.edit_text("🧮 **Раздел: Калькуляторы и Конвертеры**\n\nВыберите нужный калькулятор:", reply_markup=get_calculators_menu(), parse_mode="Markdown")
    elif section == "care":
        await callback.message.edit_text("🧼 **Раздел: Реставрация, Уход и Глассаж**\n\nВыберите тему:", reply_markup=get_care_menu(), parse_mode="Markdown")
    elif section == "tools":
        await callback.message.edit_text("🛠 **Раздел: Инструменты, Заточка и ТБ**\n\nВыберите категорию:", reply_markup=get_tools_menu(), parse_mode="Markdown")
    elif section == "helper":
        await callback.message.edit_text("🧩 **Экспресс-помощник мастера**\n\nБыстрый выбор решений:", reply_markup=get_helper_menu(), parse_mode="Markdown")
    elif section == "checklists":
        await callback.message.edit_text("📋 **Раздел: Чек-листы и Стандарты**\n\nВыберите стандарт:", reply_markup=get_checklists_menu(), parse_mode="Markdown")
    elif section == "glossary":
        text = (
            "📖 **Глоссарий сапожных терминов (А-Я)**\n\n"
            "• **Геленок (Супинатор):** Металлическая или деревянная пластина между стелькой и подошвой для жесткости геленочной части.\n"
            "• **Рант:** Узкая полоса кожи, сшивающая верх обуви, стельку и подошву в конструкции Goodyear Welted.\n"
            "• **Штихмасс:** Сапожная измерительная лента. 1 штих = 2/3 см (6.67 мм).\n"
            "• **Союзка:** Передняя деталь верха обуви, закрывающая плюсну стопы.\n"
            "• **Шарфование (Шерфование):** Спуск (утоньшение) края кожи для аккуратного загиба и швов.\n"
            "• **Аппретура:** Финишное средство для придания коже глянца и защиты от влаги."
        )
        back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ В главное меню", callback_data="back_main")]])
        await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")
    elif section == "patterns":
        text = (
            "✂️ **Бесплатные лекала (PDF)**\n\n"
            "📂 **Доступные выкройки:**\n"
            "1. Классический Картхолдер (3 кармана)\n"
            "2. Бифолд кошелек\n"
            "3. Выкройка домашних тапочек из кожи\n\n"
            "💡 *Файлы готовятся к загрузке в облачный архив сообщества.*"
        )
        back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ В главное меню", callback_data="back_main")]])
        await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")
    elif section == "community":
        text = (
            "👥 **Сообщество мастеров-сапожников**\n\n"
            "Добро пожаловать в единое сообщество обувщиков и кожевников!\n\n"
            "🔹 Обмен опытом и разбор сложных ремонтов\n"
            "🔹 Помощь начинающим мастерам\n"
            "🔹 Проверенные поставщики кожи и химии\n\n"
            "💬 **Правила:** Уважение к коллегам, отсутствие рекламы без согласования, взаимопомощь."
        )
        back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ В главное меню", callback_data="back_main")]])
        await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")

    await callback.answer()

# ==========================================
# 📄 ОБРАБОТЧИКИ ПОДРАЗДЕЛОВ (КОНТЕНТ)
# ==========================================

# --- 📐 РАЗМЕРЫ ---
@dp.callback_query(lambda c: c.data.startswith('sizes_'))
async def process_sizes(callback: types.CallbackQuery):
    sub = callback.data.split('_')[1]
    if sub == "systems":
        text = (
            "📏 **Системы размеров обуви:**\n\n"
            "• **Штихмассовая (Европа):** 1 штих = 6.67 мм (2/3 см). Размер рассчитывается по длине стельки (длина стопы + припуск ~10 мм).\n"
            "• **Метрическая (СНГ):** Размер = длина стопы в миллиметрах (например, 275 мм = 42.5 EUR).\n"
            "• **Дюймовая (US / UK):** Основана на трети дюйма (1/3 дюйма = 8.46 мм)."
        )
    elif sub == "measuring":
        text = (
            "🦶 **Как правильно снять мерку стопы:**\n\n"
            "1. Поставьте стопу на лист бумаги с полной нагрузкой (стоя).\n"
            "2. Очертите стопу карандашом под углом 90° к бумаге.\n"
            "3. Измерьте длину от самой выступающей точки пятки до кончика большого/второго пальца.\n"
            "4. Измерьте обхват в пучках (самое широкое место стопы по косточкам).\n"
            "5. Измерьте обхват подъема (середина стопы)."
        )
    else:
        text = (
            "👟 **Полнота стопы:**\n\n"
            "Полнота обозначается цифрами (1–12 в РФ/СНГ) или буквами (C, D, E, F, G, H в Европе/США).\n"
            "• **F (6):** Средняя стандартная полнота.\n"
            "• **G (7):** Увеличенная полнота (широкая стопа).\n"
            "• **H (8):** Очень широкая стопа с высокими косточками."
        )
    back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Назад в «Размеры»", callback_data="menu_sizes")]])
    await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")
    await callback.answer()

# --- 👞 ФАСОНЫ ---
@dp.callback_query(lambda c: c.data.startswith('styles_'))
async def process_styles(callback: types.CallbackQuery):
    sub = callback.data.split('_')[1]
    if sub == "classic":
        text = (
            "👞 **Классические фасоны обуви:**\n\n"
            "• **Оксфорды:** Закрытая шнуровка (берцы пришиты под союзку).\n"
            "• **Дерби:** Открытая шнуровка (берцы нашиты сверху союзки).\n"
            "• **Лоферы:** Обувь без шнуровки с характерным полукруглым швом.\n"
            "• **Монки:** Обувь с ремешками и пряжками вместо шнурков."
        )
    else:
        text = (
            "🪡 **Методы крепления подошвы:**\n\n"
            "• **Goodyear Welted:** Рантовый метод. Прочный, долговечный, позволяет многократно менять подошву.\n"
            "• **Blake:** Шов проходит насквозь через подошву, стельку и верх. Обувь гибкая и легкая.\n"
            "• **Клеевой метод:** Самый распространенный в современной обуви. Надежен при правильном подборе клея."
        )
    back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Назад в «Фасоны»", callback_data="menu_styles")]])
    await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")
    await callback.answer()

# --- 🧪 ХИМИЯ ---
@dp.callback_query(lambda c: c.data.startswith('chem_'))
async def process_chemistry(callback: types.CallbackQuery):
    sub = callback.data.split('_')[1]
    if sub == "glues":
        text = (
            "🧴 **Справочник по Клеям:**\n\n"
            "• **Наирит:** Для кожи, затяжки, стелек. Открытое время 15–20 мин. Не подходит для ТЭП/ПУ!\n"
            "• **Десмокол:** Для подошв (ТЭП, ПУ, тунит, резина). Наносится в 2 слоя, требует термоактивации (60-70°C).\n"
            "• **САР (SAR 306):** Профессиональный полиуретановый клей повышенной термостойкости."
        )
    elif sub == "leather":
        text = (
            "🥩 **Дубление кожи:**\n\n"
            "• **Растительное («Растишка»):** Отлично форсуется, тиснится, идеальна под ручную окраску.\n"
            "• **Хромовое:** Мягкая, водостойкая кожа для верха обуви.\n"
            "• **Краст:** Кожа без финишного покрытия под самостоятельное окрашивание."
        )
    elif sub == "finishes":
        text = (
            "🧪 **Финиши и Воски:**\n\n"
            "• **Аппретура:** Защитный финишный слой для блеска и защиты.\n"
            "• **Карнаубский воск:** Твердый растительный воск для идеальной полировки урезов и носков."
        )
    else:
        text = (
            "🧼 **Растворители:**\n\n"
            "• **Этилацетат / Ацетон:** Обезжиривание перед склейкой и очистка инструментов.\n"
            "• **Очиститель полиуретана:** Бережное удаление остатков клея с ранта."
        )
    back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Назад в «Химию»", callback_data="menu_chemistry")]])
    await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")
    await callback.answer()

# --- 🎨 ЦВЕТА ---
@dp.callback_query(lambda c: c.data.startswith('colors_'))
async def process_colors(callback: types.CallbackQuery):
    sub = callback.data.split('_')[1]
    if sub == "prep":
        text = "🧹 **Подготовка к окраске:**\nТщательно обезжирьте краст этилацетатом или специальным подготовщиком (Preparador) для снятия заводского воска."
    elif sub == "patina":
        text = "🎨 **Патина и Градиент:**\nНаносите спиртовые проникающие краски круговыми движениями от светлого тона к темному на носке и пятке."
    else:
        text = "🧪 **Закрепление:**\nПосле полного высыхания краски (12 часов) обязательно зафиксируйте результат крем-финишем или закрепителем."
    back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Назад в «Колористику»", callback_data="menu_colors")]])
    await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")
    await callback.answer()

# --- 🧮 КАЛЬКУЛЯТОРЫ ---
@dp.callback_query(lambda c: c.data.startswith('calc_'))
async def process_calc(callback: types.CallbackQuery):
    sub = callback.data.split('_')[1]
    if sub == "sqft":
        text = (
            "📐 **Конвертер площади кожи:**\n\n"
            "• **1 кв. фут (sq.ft) ≈ 9.29 кв. дециметрам (дм²)**\n\n"
            "💡 *Пример:* Шкура 10 sq.ft = 92.9 дм²."
        )
    elif sub == "oz":
        text = (
            "⚖️ **Толщина кожи (Oz в мм):**\n\n"
            "• 2-3 Oz ≈ 0.8 – 1.2 мм (Подкладка)\n"
            "• 4-5 Oz ≈ 1.6 – 2.0 мм (Верх обуви, сумки)\n"
            "• 8-9 Oz ≈ 3.2 – 3.6 мм (Подошва, ремни)"
        )
    else:
        text = (
            "🪡 **Расчет длины нити:**\n\n"
            "Длина нити для седельного шва = **Длина шва × 3.5 + 20 см** (на заправку игл)."
        )
    back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Назад в «Калькуляторы»", callback_data="menu_calculators")]])
    await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")
    await callback.answer()

# --- 🧼 УХОД И ГЛАССАЖ ---
@dp.callback_query(lambda c: c.data.startswith('care_'))
async def process_care(callback: types.CallbackQuery):
    sub = callback.data.split('_')[1]
    if sub == "glassage":
        text = (
            "✨ **Техника Глассажа:**\n\n"
            "1. Нанесите базовый слой твердого воска (Pate de Luxe).\n"
            "2. Капните 1 каплю ледяной воды на носок обуви.\n"
            "3. Полируйте микрофиброй легкими круговыми движениями без нажима.\n"
            "4. Повторяйте 10–15 слоев до зеркального блеска."
        )
    elif sub == "cleaning":
        text = "🧼 **Удаление соли:** Промойте обувь раствором уксуса и воды (1:1) или специальным седельным мылом (Saddle Soap)."
    else:
        text = "🪥 **Уход за замшей:** Чистите только специальной латунной или каучуковой щеткой. Для освежения цвета используйте спрей-восстановитель."
    back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Назад в «Уход»", callback_data="menu_care")]])
    await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")
    await callback.answer()

# --- 🛠 ИНСТРУМЕНТЫ ---
@dp.callback_query(lambda c: c.data.startswith('tools_'))
async def process_tools(callback: types.CallbackQuery):
    sub = callback.data.split('_')[1]
    if sub == "sharpening":
        text = "🔪 **Углы заточки ножа:**\nСапожный нож (закройный) затачивается под углом **12°–15°**. Доводка производится на кожаном ремне с пастой ГОИ."
    elif sub == "punches":
        text = "🔨 **Пробойники:**\nДля обуви используют ромбовидные или просечные пробойники с шагом 3.38 мм, 3.85 мм или 4 мм."
    else:
        text = "🥽 **ТБ:** Работайте с клеями (Десмокол, Наирит) только в респираторе с фильтрами от органических паров (марка А1/А2)!"
    back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Назад в «Инструменты»", callback_data="menu_tools")]])
    await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")
    await callback.answer()

# --- 🧩 ПОМОЩНИК ---
@dp.callback_query(lambda c: c.data.startswith('helper_'))
async def process_helper(callback: types.CallbackQuery):
    sub = callback.data.split('_')[1]
    if sub == "glue":
        text = (
            "🧩 **Быстрый подбор клея:**\n\n"
            "• **Кожа + ТЭП/ПУ подошва** ➔ *Десмокол* (с термоактивацией)\n"
            "• **Кожа + Кожаная подошва** ➔ *Десмокол* или *САР 306*\n"
            "• **Затяжка верха на стельку** ➔ *Наирит*\n"
            "• **Приклейка подкладки** ➔ *Ecostick (водный клей)*"
        )
    else:
        text = (
            "🪡 **Подбор нити:**\n\n"
            "• **Толщина кожи 1.0–1.5 мм** ➔ Нить 0.45–0.55 мм (шаг 3.0–3.38 мм)\n"
            "• **Толщина кожи 1.5–2.5 мм** ➔ Нить 0.6–0.8 мм (шаг 3.85–4.0 мм)"
        )
    back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Назад в «Помощник»", callback_data="menu_helper")]])
    await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")
    await callback.answer()

# --- 📋 ЧЕК-ЛИСТЫ ---
@dp.callback_query(lambda c: c.data.startswith('check_'))
async def process_checklists(callback: types.CallbackQuery):
    sub = callback.data.split('_')[1]
    if sub == "intake":
        text = (
            "📋 **Чек-лист приемки обуви в ремонт:**\n\n"
            "1. Проверить износ каблуков и набоек.\n"
            "2. Осмотреть грань стельки и рант на трещины.\n"
            "3. Проверить целостность подкладки в пяточной зоне.\n"
            "4. Согласовать с клиентом цвет материалов и вид профилактики."
        )
    else:
        text = (
            "🔎 **Контроль затяжки:**\n\n"
            "• Отсутствие складок на геленке и союжке.\n"
            "• Симметричность высоты берцев слева и справа.\n"
            "• Плотно осаженная пятка без зазоров."
        )
    back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Назад в «Чек-листы»", callback_data="menu_checklists")]])
    await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")
    await callback.answer()

# ==========================================
# ==========================================
# 🌐 KEEP-ALIVE (анти-сон) + ВЕБ-СЕРВЕР
# ==========================================

async def handle_ping(request):
    return web.Response(text="Bot is running! ✅")

async def self_ping():
    """Каждые 5 минут пингует сам себя, чтобы бот не засыпал"""
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://0.0.0.0:{os.environ.get('PORT', 8080)}") as resp:
                    logging.info(f"Self-ping OK → {resp.status}")
        except Exception as e:
            logging.warning(f"Self-ping error: {e}")
        await asyncio.sleep(300)  # 5 минут


async def start_web_server():
    """Запускает веб-сервер для keep-alive"""
    app = web.Application()
    app.router.add_get('/', handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    logging.info(f"Web server started on port {port}")


async def main():
    # Запускаем веб-сервер
    await start_web_server()
    
    # Запускаем само-пинг в фоне
    asyncio.create_task(self_ping())
    
    logging.info("Бот запущен и готов к работе")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
