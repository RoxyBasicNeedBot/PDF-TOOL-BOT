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

import re
from core.nexus import settings, dm, group
from core.corestate import dataBASE, BANNED_USR_DB, BANNED_GRP_DB, GROUPS, invite_link
from core.i18n import LANG_MAP as langList
from pyrogram import Client as RoxyBot, filters, enums
from pyrogram.types import Message
from pyrogram.errors import UserNotParticipant

if dataBASE.MONGODB_URI:
    from ledger.safebox import db

async def stopBot(_, __, message: Message) -> bool:
    if (message.chat.id in dm.ADMINS) and message.text == "/stop":
        return False
    return True if settings.STOP_BOT else False

async def _stop_bot_filter(flt, client, message):
    return await stopBot(flt, client, message)

stop_bot = filters.create(_stop_bot_filter)

async def bannedUsers(_, __, message: Message) -> bool:
    if not message.from_user:
        return False
    if (
        (message.from_user.id in dm.BANNED_USERS)
        or ((dm.ADMIN_ONLY) and (message.from_user.id not in dm.ADMINS))
        or ((dataBASE.MONGODB_URI) and (message.from_user.id in BANNED_USR_DB))
    ):
        return True
    return False

async def _banned_user_filter(flt, client, message):
    return await bannedUsers(flt, client, message)

banned_user = filters.create(_banned_user_filter)

async def bannedGroups(_, __, message: Message) -> bool:
    if (
        (message.chat.id in group.BANNED_GROUP)
        or ((group.ADMIN_GROUP_ONLY) and (message.chat.id not in group.ADMIN_GROUPS))
        or ((dataBASE.MONGODB_URI) and (message.chat.id in BANNED_GRP_DB))
    ):
        return True
    return False

async def _banned_group_filter(flt, client, message):
    return await bannedGroups(flt, client, message)

banned_group = filters.create(_banned_group_filter)

async def setDb(_, bot_client: RoxyBot, message: Message):
    if (dataBASE.MONGODB_URI) and (message.chat.id not in GROUPS):
        from core.ledger import log
        await log.newUser(bot_client, message, False, False)
        GROUPS.append(message.chat.id)
    return True

async def _set_db_filter(flt, client, message):
    return await setDb(flt, client, message)

set_db = filters.create(_set_db_filter)

# Extract lang_code, refer_id, get_pdf, md5_str from /start message if exist
async def extract_data(data: str):
    lang_code = re.search(r"\-l(\w+)\-", data)
    refer_id = re.search(r"\-r(\w+)\-", data)
    get_pdf = re.search(r"\-g(\w+)\-", data)
    md5_str = re.search(r"\-m(\w+)\-", data)
    return (
        lang_code.group(1) if lang_code else None,
        refer_id.group(1) if refer_id else None,
        get_pdf.group(1) if get_pdf else None,
        md5_str.group(1) if md5_str else None,
    )

async def notSubscribed(_, bot_client: RoxyBot, message: Message):
    if not message.from_user:
        return False
        
    if message.text and message.text.startswith("/start"):
        if "-" in message.text:
            lang_code, referID, get_pdf, md5_str = await extract_data(f"{message.text}-")
            if lang_code and settings.MULTI_LANG_SUP and lang_code in langList:
                userLang[message.chat.id] = lang_code
        else:
            referID = None
        
        from sentinel import util
        lang_code = await util.getLang(message.chat.id)
        if dataBASE.MONGODB_URI:
            from core.ledger import log
            await log.newUser(bot_client, message, lang_code, referID)

    if len(invite_link) == 0:
        return False
    else:
        for ch_info in invite_link:
            try:
                userStatus = await bot_client.get_chat_member(
                    int(ch_info["channel_id"]), message.from_user.id
                )
                if userStatus.status == enums.ChatMemberStatus.BANNED:
                    return True
            except UserNotParticipant:
                return True
            except Exception as error:
                import logging
                logging.getLogger("RoxyBot").error(
                    f"Error checking forcesub member in channel {ch_info['channel_id']} for user {message.from_user.id}: {error}"
                )
                pass
        return False

async def _not_subscribed_filter(flt, client, message):
    return await notSubscribed(flt, client, message)

not_subscribed = filters.create(_not_subscribed_filter)
