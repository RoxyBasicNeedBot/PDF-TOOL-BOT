# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
from tracer import tracer
from pyrogram import enums
from sentinel import *


async def metadataPDF(input_file: str, cDIR: str, message) -> (bool, str):
    try:
        with fitz.open(input_file) as iNPUT:
            await message.reply_chat_action(enums.ChatAction.TYPING)
            pdfMetaData = (
                "".join(
                    f"`{i} : {iNPUT.metadata[i]}`\n"
                    for i in iNPUT.metadata
                    if iNPUT.metadata[i] != ""
                )
                if iNPUT.metadata
                else ""
            )
            return (True, pdfMetaData) if pdfMetaData != "" else (False, "")

    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(e)
