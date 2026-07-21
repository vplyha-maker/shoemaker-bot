import os
import asyncio
import logging
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Не найден BOT_TOKEN в переменных окружения.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def get_main_menu():
    builder = InlineKeyboardBuilder()
    # Размещаем по одной кнопке в ряд, чтобы длинный текст не обрезался на экранах телефонов
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

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    welcome = (
        f"Привет, {message.from_user.first_name}! 👞\n\n"
        "Добро пожаловать в **Энциклопедию Сапожника**.\n"
        "Выбери нужный раздел:"
    )
    # Используем parse_mode="Markdown" для красивого форматирования текста
    await message.answer(welcome, reply_markup=get_main_menu(), parse_mode="Markdown")

@dp.callback_query(lambda c: c.data.startswith('menu_'))
async def process_menu(callback: types.CallbackQuery):
    # Словарь с заготовками текстов для каждого раздела
    sections_info = {
        "sizes": "📐 **Размеры, Мерки и Ортопедия**\n\nЗдесь будут: Размерные сетки, полнота стопы, инструкции, особенности.",
        "styles": "👞 **Фасоны и Конструкции**\n\nЗдесь будут: Классификация обуви, методы крепления подошвы, колодки.",
        "chemistry": "🧪 **Материалы и Химия**\n\nЗдесь будут: Виды кож, клеи, аппретуры, пропитки, воски.",
        "colors": "🎨 **Цвета и Колористика**\n\nЗдесь будут: Сочетания, рецепты смешивания красок, патина, градиенты.",
        "calculators": "🧮 **Калькуляторы и Конвертеры**\n\nЗдесь будут: дм² / футы, толщина в Oz, расход нити.",
        "care": "🧼 **Реставрация, Уход и Глассаж**\n\nЗдесь будут: Глубокая чистка, удаление соли, полировка воском.",
        "tools": "🛠 **Инструменты, Заточка и ТБ**\n\nЗдесь будут: Углы заточки, обслуживание оборудования, защита органов.",
        "helper": "🧩 **Экспресс-помощник**\n\nЗдесь будет: Быстрый подбор клея, нитей и пробойников за 3 клика.",
        "checklists": "📋 **Чек-листы и Стандарты**\n\nЗдесь будут: Контроль качества, приемка в работу, ГОСТы.",
        "glossary": "📖 **Глоссарий терминов**\n\nЗдесь будет: Полный справочник терминов от А до Я.",
        "patterns": "✂️ **Бесплатные лекала (PDF)**\n\nЗдесь будет: Библиотека скачиваемых выкроек.",
        "community": "👥 **Сообщество мастеров**\n\nЗдесь будет: Чат для взаимопомощи и разбора сложных случаев."
    }
    
    section = callback.data.split('_')[1]
    text = sections_info.get(section, "🚧 Раздел в разработке.")

    # Кнопка возврата в главное меню
    back_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_main")]
    ])
    
    await callback.message.edit_text(text, reply_markup=back_kb, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(lambda c: c.data == "back_main")
async def back_main(callback: types.CallbackQuery):
    await callback.message.edit_text("Выбери нужный раздел:", reply_markup=get_main_menu(), parse_mode="Markdown")
    await callback.answer()

# Веб-сервер заглушка для Render (чтобы хостинг работал бесплатно и не отключался)
async def handle_ping(request):
    return web.Response(text="Bot is running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

async def main():
    await start_web_server()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
