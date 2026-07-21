import os
import asyncio
import logging
import aiohttp
from aiohttp import web

async def handle_ping(request):
    """Простой пинг для keep-alive"""
    return web.Response(text="Bot is running! ✅")


async def self_ping():
    """Само-пинг каждые 5 минут"""
    while True:
        try:
            port = int(os.environ.get("PORT", 8080))
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://0.0.0.0:{port}") as resp:
                    logging.info(f"Self-ping OK: {resp.status}")
        except Exception as e:
            logging.warning(f"Self-ping error: {e}")
        await asyncio.sleep(300)
