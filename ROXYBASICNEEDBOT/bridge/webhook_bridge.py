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

from bridge.nexus_aiogram import nexus_aiogram
from aiogram import types
from tracer import logger

async def feed_webhook_update(json_data: dict):
    # Feeds parsed webhook event directly to aiogram dispatcher instance
    if not nexus_aiogram.dp or not nexus_aiogram.bot:
        return False
    try:
        update = types.Update(**json_data)
        await nexus_aiogram.dp.feed_update(bot=nexus_aiogram.bot, update=update)
        return True
    except Exception as e:
        logger.error(f"Error feeding webhook update to aiogram: {e}")
    return False
