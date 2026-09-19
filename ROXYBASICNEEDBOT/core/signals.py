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
from tracer import logger

async def trigger_startup_signals(bot):
    logger.info("Initializing system signals and state verification...")
    # Verify dynamic welcome pic is loaded
    from core.nexus import images
    if not images.WELCOME_PIC:
         logger.warning("Welcome picture not loaded. Refreshing fallback.")
         images.WELCOME_PIC = "https://i.ibb.co/Fk0k6qnz/file-29661.jpg"

async def trigger_shutdown_signals(bot):
    logger.info("De-initializing system signals... Cleaning active resources.")
    # Perform cleanups
    from sentinel.ramguard import force_cleanup
    force_cleanup()
