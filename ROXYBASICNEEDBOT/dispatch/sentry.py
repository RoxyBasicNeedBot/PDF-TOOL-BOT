# ┌─────────────────────────────────────────────────────────────┐
# │                    𝕽𝕺𝕏𝖄•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝑒𝕕𝔹𝕠𝕥                     │
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
from core.nexus import settings, dm, images
from core.corestate import dataBASE, BANNED_USR_DB, BANNED_GRP_DB, invite_link, myID
from core.i18n import translate, getLang
from sentinel.gatepass import stop_bot, banned_user, banned_group, set_db, not_subscribed, extract_data
from pyrogram import Client as RoxyBot, filters, enums, StopPropagation
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from tracer import logger

if dataBASE.MONGODB_URI:
    from ledger.safebox import db

@RoxyBot.on_message(stop_bot & filters.incoming, group=-3)
async def stop_bot_handler(bot_client: RoxyBot, message: Message):
    try:
        lang_code = await getLang(message.chat.id)
        await message.reply_chat_action(enums.ChatAction.TYPING)

        if dataBASE.MONGODB_URI:
            lang_code, referID, get_pdf, md5_str = await extract_data(f"{message.text}-")
            from core.ledger import log
            await log.newUser(bot_client, message, lang_code, referID)

        trans_txt, trans_btn = await translate(
            text="_STOP", button="_STOP_CB_", lang_code=lang_code
        )

        await message.reply_photo(
            photo=images.WELCOME_PIC,
            reply_markup=trans_btn,
            caption=trans_txt.format(
                message.from_user.mention if message.from_user else "User",
                myID[0].mention if myID else "@roxybasicneedbot"
            )
        )
        raise StopPropagation
    except StopPropagation:
        raise
    except Exception as error:
        logger.error(f"Error in stop_bot_handler: {error}")

@RoxyBot.on_message(filters.private & banned_user & filters.incoming, group=-2)
async def banned_usr_handler(bot_client: RoxyBot, message: Message):
    try:
        lang_code = await getLang(message.chat.id)
        await message.reply_chat_action(enums.ChatAction.TYPING)
        
        if message.from_user.id in BANNED_USR_DB:
            ban = await db.get_key(id=message.from_user.id, key="banned")
            trans_txt, trans_btn = await translate(
                text="BAN['UCantUseDB']", button="BAN['banCB']", lang_code=lang_code
            )
            await message.reply_photo(
                photo=images.BANNED_PIC,
                reply_markup=trans_btn, quote=True,
                caption=trans_txt.format(message.from_user.mention, ban),
            )
            raise StopPropagation
        
        trans_txt, trans_btn = await translate(
            text="BAN['UCantUse']", button="BAN['banCB']", lang_code=lang_code
        )
        await message.reply_photo(
            photo=images.BANNED_PIC,
            reply_markup=trans_btn, quote=True,
            caption=trans_txt.format(message.from_user.mention),
        )
        raise StopPropagation
    except StopPropagation:
        raise
    except Exception as error:
        logger.error(f"Error in banned_usr_handler: {error}")

@RoxyBot.on_message(filters.group & set_db & banned_group & filters.incoming, group=-2)
async def banned_grp_handler(bot_client: RoxyBot, message: Message):
    try:
        lang_code = await getLang(message.chat.id)
        await message.reply_chat_action(enums.ChatAction.TYPING)
        
        if message.chat.id in BANNED_GRP_DB:
            ban = await db.get_key(id=message.chat.id, key="banned", typ="group")
            trans_txt, trans_btn = await translate(
                text="BAN['GroupCantUseDB']", button="BAN['banCB']", lang_code=lang_code
            )
            toPin = await message.reply_photo(
                photo=images.BANNED_PIC,
                reply_markup=trans_btn, quote=True,
                caption=trans_txt.format(message.chat.title, ban),
            )
        else:
            trans_txt, trans_btn = await translate(
                text="BAN['GroupCantUse']", button="BAN['banCB']", lang_code=lang_code
            )
            toPin = await message.reply_photo(
                photo=images.BANNED_PIC,
                reply_markup=trans_btn,
                caption=trans_txt.format(message.chat.title),
                quote=True,
            )

        try:
            await toPin.pin()
        except Exception:
            pass

        await bot_client.leave_chat(message.chat.id)
    except Exception as error:
        logger.error(f"Error in banned_grp_handler: {error}")

@RoxyBot.on_message(filters.private & filters.incoming & not_subscribed, group=-1)
async def non_subscriber_handler(bot_client: RoxyBot, message: Message):
    try:
        lang_code = await getLang(message.chat.id)
        await message.reply_chat_action(enums.ChatAction.TYPING)
        
        code = ""
        if message.text and message.text.startswith("/start") and ("-g" in message.text or "-m" in message.text):
            _lang, referID, get_pdf, md5_str = await extract_data(f"{message.text}-")
            if get_pdf:
                code = f"-g{get_pdf}"
            elif md5_str:
                code = f"-m{md5_str}"

        tTXT, tBTN = await translate(
            text="BAN['Force']",
            button="BAN['ForceCB']",
            asString=True,
            lang_code=lang_code,
        )

        buttons = []
        for idx, ch_info in enumerate(invite_link):
            btn_text = f"🌟 JOIN CHANNEL {idx + 1} 🌟"
            buttons.append([InlineKeyboardButton(btn_text, url=ch_info["invite_link"])])
        
        buttons.append([InlineKeyboardButton("♻️ Refresh ♻️", callback_data=f"refresh{code}")])
        
        await message.reply_photo(
            photo=images.WELCOME_PIC,
            quote=True,
            caption=tTXT.format(message.from_user.first_name if message.from_user else "User", message.from_user.id if message.from_user else message.chat.id),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        raise StopPropagation
    except StopPropagation:
        raise
    except Exception as error:
        logger.error(f"Error in non_subscriber_handler: {error}")
