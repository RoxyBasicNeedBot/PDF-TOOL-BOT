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

import shutil
import os
from pyrogram import Client as RoxyBot, filters, enums
from pyrogram.types import Message
from core.nexus import dm, settings
from core.corestate import BETA, dataBASE, myID
from sentinel import work, getLang, translate, createBUTTON
from scriptorium import PDF
from tracer import logger

if dataBASE.MONGODB_URI:
    from ledger.safebox import db

@RoxyBot.on_message((filters.private | filters.group) & filters.command(["cancel", "refresh", "clear", "reset"]) & filters.incoming, group=0)
async def cancelP2I(bot_client: RoxyBot, message: Message):
    logger.debug(f"❌ /cancel or /refresh command received from user {message.from_user.id}")
    try:
        await work(message, "delete", True)
        try:
            await message.reply_text("✅ Workspace cleared! You can now send a new file.", quote=True)
        except Exception:
            pass
        return
    except Exception:
        pass

@RoxyBot.on_message((filters.private | filters.group) & filters.command(["delete"]) & filters.incoming, group=0)
async def _cancelI2P(bot_client: RoxyBot, message: Message):
    logger.debug(f"🗑️ /delete command received from user {message.from_user.id}")
    try:
        lang_code = await getLang(message.chat.id)
        await message.reply_chat_action(enums.ChatAction.TYPING)
        
        if message.chat.id in PDF:
            del PDF[message.chat.id]
            
        trans_txt, trans_btn = await translate(
            text="GENERATE['deleteQueue']", lang_code=lang_code
        )
        await message.reply_text(trans_txt, quote=True)
        shutil.rmtree(f"work/{message.chat.id}", ignore_errors=True)
    except Exception:
        trans_txt, trans_btn = await translate(
            text="GENERATE['noQueue']", lang_code=lang_code
        )
        await message.reply_text(trans_txt, quote=True)

@RoxyBot.on_message(filters.private & filters.command(["beta"]) & filters.incoming, group=0)
async def _betaMode(bot_client: RoxyBot, message: Message):
    logger.debug(f"🔰 /beta command received from user {message.from_user.id}")
    try:
        lang_code = await getLang(message.from_user.id)
        CHUNK, _ = await translate(text="BETA", lang_code=lang_code)

        if message.chat.id in dm.ADMINS:
            logger.debug(f"Beta Users: {list(BETA)}")

        if not dataBASE.MONGODB_URI:
            return await message.reply_text(CHUNK["cant"], quote=True)

        if (message.chat.id not in dm.ADMINS) and settings.REFER_BETA:
            refer_ids = await db.get_key(id=message.chat.id, key="refer")
            if (not refer_ids) or not (len(refer_ids.split("|")) >= 5):
                return await message.reply_text(
                    CHUNK["refer"].format(
                        "0" if not refer_ids else f"`{refer_ids.replace('|', '`, `')}`",
                        f"https://t.me/{myID[0].username}?start=-r{message.from_user.id}",
                    ),
                    quote=True,
                )

        if message.chat.id in dm.ADMINS and len(message.text.split(" ")) == 2:
            target_user = int(message.text.split(" ")[1])
            await db.set_key(id=target_user, key="beta", value=True)
            BETA.append(target_user)
            return await message.reply_text("Now He is a beta user", quote=True)

        if message.chat.id not in BETA:
            await db.set_key(id=message.chat.id, key="beta", value=True)
            BETA.append(message.chat.id)
            return await message.reply_text(CHUNK["nowbeta"], quote=True)
        else:
            await db.dlt_key(id=message.chat.id, key="beta")
            BETA.remove(message.chat.id)
            return await message.reply_text(CHUNK["nownotbeta"], quote=True)
    except Exception as Error:
        logger.error(f"Error in beta command handler: {Error}", exc_info=True)
