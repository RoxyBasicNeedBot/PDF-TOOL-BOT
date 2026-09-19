# ┌─────────────────────────────────────────────────────────────┐
# │                    𝕽𝕺𝕏𝖄•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │  Created by: RoxyBasicNeedBot                               │
# │  GitHub    : https://github.com/RoxyBasicNeedBot            │
# │  Telegram  : https://t.me/roxybasicneedbot1                 │
# │  Website   : https://roxybasicneedbot.unaux.com             │
# │  YouTube   : @roxybasicneedbot                              │
# ├─────────────────────────────────────────────────────────────┤
# │      Bot Developer, Automation Architect & Python Coder      │
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import asyncio
import time
from tracer import logger
from pyrogram.errors import FloodWait

class RoxyGuardian:
    def __init__(self):
        self._sem = asyncio.Semaphore(1)
        self._last_send = 0
        self.MIN_DELAY = 10

    async def safe_call(self, coro, description="API Call"):
        async with self._sem:
            now = time.time()
            wait = self.MIN_DELAY - (now - self._last_send)
            if wait > 0:
                await asyncio.sleep(wait)
                
            for attempt in range(5):
                try:
                    result = await coro
                    self._last_send = time.time()
                    return result
                except FloodWait as e:
                    logger.warning(f"FloodWait in {description}: waiting {e.value}s (attempt {attempt+1}/5)")
                    await asyncio.sleep(e.value + 1)
            logger.error(f"FloodWait retries exhausted for {description}")
            return None

    async def safe_reply_text(self, message, text, **kwargs):
        kwargs.pop("quote", None)
        async with self._sem:
            now = time.time()
            wait = self.MIN_DELAY - (now - self._last_send)
            if wait > 0:
                await asyncio.sleep(wait)
                
            for attempt in range(5):
                try:
                    result = await message.reply_text(text, **kwargs)
                    self._last_send = time.time()
                    if result and message and getattr(message, "document", None):
                        try:
                            from sentinel.render import register_reply_cache
                            register_reply_cache(message.chat.id if message.chat else None, result.id, message)
                        except Exception as ce:
                            logger.debug(f"register_reply_cache error: {ce}")
                    return result
                except FloodWait as e:
                    logger.warning(f"FloodWait in reply: waiting {e.value}s (attempt {attempt+1}/5)")
                    await asyncio.sleep(e.value + 1)
            logger.error("FloodWait retries exhausted for reply_text")
            return None

guardian = RoxyGuardian()

async def safe_send(coro, description="API call"):
    return await guardian.safe_call(coro, description)

async def safe_reply_text(message, text, **kwargs):
    return await guardian.safe_reply_text(message, text, **kwargs)
