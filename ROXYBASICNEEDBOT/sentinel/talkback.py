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

from core.i18n import translate
from core.nexus import settings
from tracer import logger

class TalkBack:
    @staticmethod
    async def caption(data: str, args: list = None, lang_code: str = settings.DEFAULT_LANG) -> str:
        try:
            watermark = "\n\n🤖 **Powered by @roxybasicneedbot1**"
            
            if data == "encrypt":
                msg, _ = await translate(text="INDEX['encrypt_caption']", lang_code=lang_code)
                return (msg.format(*args) if args else msg) + watermark
            elif data == "rename":
                msg, _ = await translate(text="INDEX['rename_caption']", lang_code=lang_code)
                return (msg.format(*args) if args else msg) + watermark
            elif data == "compress":
                msg, _ = await translate(text="INDEX['compress_caption']", lang_code=lang_code)
                return (msg.format(*args) if args else msg) + watermark
            
            # Default text caption
            msg, _ = await translate(text=f"INDEX['{data}_caption']", lang_code=lang_code)
            if msg:
                return (msg.format(*args) if args else msg) + watermark
        except Exception as e:
            if "not found in" not in str(e):
                logger.error(f"Error in TalkBack.caption: {e}")
        return watermark.strip()

async def caption(data: str, args: list = None, lang_code: str = settings.DEFAULT_LANG) -> str:
    return await TalkBack.caption(data, args, lang_code)
