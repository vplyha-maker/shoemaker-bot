import asyncio
import logging
import os
from aiohttp import web

from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from config import BOT_TOKEN
from handlers.base import cmd_start, process_language
from handlers.main_menu import register_main_menu_handlers
from handlers.styles import register_styles_handlers
from handlers.constructions import register_constructions_handlers
from handlers.materials import register_materials_handlers
from handlers.colors import register_colors_handlers
from handlers.glossary import register_glossary_handlers
from handlers.assistant import register_assistant_handlers






from utils.keepalive import handle_ping, self_ping

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://shoemaker-bot.onrender.com")


async def on_startup(app: web.Application):
    webhook_url = f"{WEBHOOK_URL}{WEBHOOK_PATH}"
    await bot.set_webhook(webhook_url)
    logging.info(f"✅ Webhook установлен: {webhook_url}")
    asyncio.create_task(self_ping())


async def on_shutdown(app: web.Application):
    await bot.delete_webhook()
    await bot.session.close()
    logging.info("Бот остановлен")


async def main():
    # Регистрация всех обработчиков (роутеров)
    register_main_menu_handlers(dp)
    register_styles_handlers(dp)
    register_constructions_handlers(dp)
    register_materials_handlers(dp)
    register_colors_handlers(dp)
    register_glossary_handlers(dp)
    register_assistant_handlers(dp)
    
    
    dp.message.register(cmd_start, lambda m: True)
    dp.callback_query.register(process_language, lambda c: c.data.startswith("lang_"))

    app = web.Application()
    
    # Для UptimeRobot
    app.router.add_get('/', handle_ping)
    
    # Webhook для Telegram
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)

    setup_application(app, dp, bot=bot)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

    logging.info(f"🚀 Сервер запущен на порту {port}")
    logging.info("Бот работает через Webhook")

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
