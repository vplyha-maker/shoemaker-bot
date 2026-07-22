import asyncio
import logging
import os
from aiohttp import web

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.base import cmd_start, process_language
from handlers.main_menu import register_main_menu_handlers
from handlers.styles import register_styles_handlers
from handlers.constructions import register_constructions_handlers
from handlers.materials import register_materials_handlers

from utils.keepalive import handle_ping, self_ping


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    """Главная функция запуска бота"""
    
    # Регистрация обработчиков
    dp.message.register(cmd_start, lambda m: True)
    
    # Регистрация callback'ов
    dp.callback_query.register(process_language, lambda c: c.data.startswith("lang_"))
    
    # Регистрация главного меню
    register_main_menu_handlers(dp) 
    register_styles_handlers(dp)
    register_constructions_handlers(dp)
    register_materials_handlers(dp)

    logging.info("Бот успешно запущен!")

    # === Keep-Alive веб-сервер ===
    app = web.Application()
    app.router.add_get('/', handle_ping)
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    
    logging.info(f"Keep-alive сервер запущен на порту {port}")

    asyncio.create_task(self_ping())

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
