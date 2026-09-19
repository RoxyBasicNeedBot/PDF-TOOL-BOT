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

import aiohttp
import json
import time
from tracer import logger
from bridge.protocols import BridgeMessage

async def send_relay_to_partner(target_url: str, sender_id: int, file_id: str, file_name: str, caption: str = ""):
    # Packages a file relay request and sends it to the partner bot's bridge endpoint
    msg = BridgeMessage(
        type="file_relay",
        sender_id=sender_id,
        recipient_id=0, # resolved by receiver
        payload={
            "file_id": file_id,
            "file_name": file_name,
            "caption": caption
        },
        timestamp=time.time()
    )
    
    headers = {"Content-Type": "application/json"}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(target_url, data=msg.to_json(), headers=headers, timeout=15) as resp:
                if resp.status == 200:
                    logger.info(f"Relayed file {file_name} to {target_url} successfully")
                    return True
                else:
                    logger.warning(f"Failed to relay file, status={resp.status}")
    except Exception as e:
        logger.error(f"Error in send_relay_to_partner: {e}")
    return False
