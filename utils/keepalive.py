import os
import asyncio
import logging
import aiohttp
from aiohttp import web

async def handle_ping(request):
    """Простой пинг для UptimeRobot"""
    return web.Response(text="Bot is running! ✅")


async def self_ping():
    """Само-пинг с задержкой"""
    await asyncio.sleep(15)   # ← Это главное исправление
    
    while True:
        try:
            port = int(os.environ.get("PORT", 10000))
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
                async with session.get(f"http://127.0.0.1:{port}") as resp:
                    if resp.status == 200:
                        logging.info(f"Self-ping OK (status {resp.status})")
                    else:
                        logging.warning(f"Self-ping bad status: {resp.status}")
        except Exception as e:
            logging.warning(f"Self-ping error: {e}")
        
        await asyncio.sleep(240)
