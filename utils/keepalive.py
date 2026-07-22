import os
import asyncio
import logging
import aiohttp
from aiohttp import web

async def handle_ping(request):
    """Простой пинг для UptimeRobot"""
    return web.Response(text="Bot is running! ✅")


async def self_ping():
    """Само-пинг каждые 4–5 минут"""
    while True:
        try:
            port = int(os.environ.get("PORT", 8080))
            # ← Вот здесь исправление
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://127.0.0.1:{port}") as resp:
                    if resp.status == 200:
                        logging.info(f"Self-ping OK (status {resp.status})")
                    else:
                        logging.warning(f"Self-ping bad status: {resp.status}")
        except Exception as e:
            logging.warning(f"Self-ping error: {e}")
        await asyncio.sleep(240)  # 4 минуты — лучше, чем 5
