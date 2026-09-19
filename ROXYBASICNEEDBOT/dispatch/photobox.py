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

import os
from PIL import Image
from pyrogram import Client as RoxyBot, filters, enums
from pyrogram.types import Message
from core.nexus import settings
from sentinel import getLang, translate, createBUTTON
from scriptorium import PDF
from tracer import logger

HD = {}

@RoxyBot.on_message((filters.private | filters.group) & filters.command("hd") & filters.incoming, group=0)
async def _hd(bot_client: RoxyBot, message: Message):
    try:
        if isinstance(PDF.get(message.chat.id), list):
            del PDF[message.chat.id]
        if message.chat.id in HD:
            return await message.delete()
        await message.reply_chat_action(enums.ChatAction.TYPING)
        lang_code = await getLang(message.chat.id)
        tTXT, tBTN = await translate(
            text="DOCUMENT['setHdImg']",
            button="DOCUMENT['setDefault']",
            lang_code=lang_code,
        )
        imageReply = await message.reply_text(text=tTXT, reply_markup=tBTN, quote=True)
        HD[message.chat.id] = [imageReply.id]
        return await message.delete()
    except Exception as Error:
        logger.error(f"Error in hd command handler: {Error}", exc_info=True)

@RoxyBot.on_message(filters.photo & filters.private & filters.incoming, group=1)
async def images_handler(bot_client: RoxyBot, message: Message):
    try:
        if message.via_bot and message.via_bot.is_self:
            return
        await message.reply_chat_action(enums.ChatAction.TYPING)
        lang_code = await getLang(message.chat.id)
        
        if message.chat.id in HD:
            if len(HD[message.chat.id]) >= 26:
                return
            HD[message.chat.id].append(message.photo.file_id)
            generateCB = "DOCUMENT['generate']" if settings.DEFAULT_NAME else "DOCUMENT['generateRN']"
            tTXT, tBTN = await translate(
                text="DOCUMENT['imageAdded']", button=generateCB, lang_code=lang_code
            )
            return await message.reply_text(
                tTXT.format(len(HD[message.chat.id]) - 1, message.chat.id) + " [HD] 🔰",
                reply_markup=tBTN,
                quote=True,
            )

        tTXT, tBTN = await translate(
            text="DOCUMENT['dlImage']", lang_code=lang_code
        )
        imageReply = await message.reply_text(tTXT, quote=True)
        if not isinstance(PDF.get(message.chat.id), list):
            PDF[message.chat.id] = []
            
        work_dir = f"work/{message.chat.id}"
        os.makedirs(work_dir, exist_ok=True)
        path = await message.download(f"{work_dir}/{message.id}.jpg")
        img = Image.open(path).convert("RGB")
        PDF[message.chat.id].append(img)
        
        generateCB = "DOCUMENT['generate']" if settings.DEFAULT_NAME else "DOCUMENT['generateRN']"
        tTXT, tBTN = await translate(
            text="DOCUMENT['imageAdded']", button=generateCB, lang_code=lang_code
        )
        await imageReply.edit(
            tTXT.format(len(PDF[message.chat.id]), message.chat.id), reply_markup=tBTN
        )
        os.remove(path)
    except Exception as Error:
        logger.error(f"Error in images_handler: {Error}", exc_info=True)
