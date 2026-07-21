import asyncio
import logging
import os
from aiohttp import web

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.base import cmd_start, process_language
from handlers.main_menu import register_main_menu_handlers
# from handlers.sizes import register_sizes_handlers
# from handlers.calculators import register_calculators_handlers
# ... добавляй по мере создания

from utils.keepalive import handle_ping, self_ping


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    """Основная функция запуска бота"""
    
    # === Регистрация всех обработчиков ===
    dp.message.register(cmd_start, lambda message: True)   # /start
    
    # register_main_menu_handlers(dp)
    # register_sizes_handlers(dp)
    # register_calculators_handlers(dp)
    # ... другие обработчики

    logging.info("Бот запущен. Ожидание команд...")

    # === Запуск Keep-Alive сервера ===
    app = web.Application()
    app.router.add_get('/', handle_ping)
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    
    logging.info(f"Web-сервер запущен на порту {port}")

    # Запуск само-пинга в фоне
    asyncio.create_task(self_ping())

    # Запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
