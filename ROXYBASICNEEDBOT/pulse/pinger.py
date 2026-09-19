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
import aiohttp
import os
from tracer import logger

async def start_pinger():
    # If the bot is deployed on Render, self-ping to prevent it from going to sleep
    render_url = os.environ.get("RENDER_URL")
    if not render_url:
        logger.info("RENDER_URL not set. Self-pinger inactive.")
        return
        
    if not render_url.startswith("http"):
        render_url = f"https://{render_url}"
        
    ping_endpoint = f"{render_url.rstrip('/')}/ping"
    logger.info(f"Self-pinger started targeting endpoint: {ping_endpoint}")
    
    while True:
        try:
            # Sleep 14 minutes (Render free tier sleeps after 15 min inactivity)
            await asyncio.sleep(14 * 60)
            async with aiohttp.ClientSession() as session:
                async with session.get(ping_endpoint) as response:
                    text = await response.text()
                    logger.debug(f"Self-ping response: status={response.status}, text={text}")
        except asyncio.CancelledError:
            logger.info("Self-pinger cancelled.")
            break
        except Exception as e:
            logger.warning(f"Self-pinger encountered error: {e}")
