# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
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
import os
import sys
import threading
import shutil
import warnings
import dotenv

# Suppress PyMuPDF fitz deprecation warning
warnings.filterwarnings("ignore", message=".*The `fitz` API is deprecated.*")

# Load configurations: server environment variables take precedence
for env_file in ["config.env", "../config.env", ".env", "../.env"]:
    if os.path.exists(env_file):
        dotenv.load_dotenv(env_file, override=False)

from tracer import logger
from pulse.webkeeper import WebKeeper

# Start health check Flask server
try:
    WebKeeper().start_async()
    logger.info("✅ Heartbeat WebKeeper server started successfully")
except Exception as e:
    logger.error(f"❌ Failed to start heartbeat WebKeeper server: {e}")

from scriptorium import works
from core.corestate import *
from sentinel.dialogstream import setup_conversation_handler
from sentinel.cmdvault import set_bot_commands
from core.nexus import bot, settings, images
from core.betapass import BETA
from pyrogram import Client as RoxyBot, errors
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.handlers.handler import Handler
import pyrogram.client

# ── Kurigram Plugin Loader Compatibility Patch ───────────────────
# In Kurigram >=2.2.0, _plugin_handlers treats logging.Logger.handlers
# as bot handlers, causing: TypeError: cannot unpack non-iterable StreamHandler object
_orig_plugin_handlers = getattr(pyrogram.client, "_plugin_handlers", None)
if _orig_plugin_handlers:
    def _safe_plugin_handlers(target):
        try:
            handlers = _orig_plugin_handlers(target)
            if not handlers:
                return None
            valid = []
            for item in handlers:
                if isinstance(item, (list, tuple)) and len(item) == 2 and isinstance(item[0], Handler) and isinstance(item[1], int):
                    valid.append(item)
            return valid if valid else None
        except Exception:
            return None
    pyrogram.client._plugin_handlers = _safe_plugin_handlers

# ── Kurigram Message.reply quote parameter patch ─────────────────
# In Kurigram 2.2+, Message.reply* methods removed the `quote` parameter.
# This patch intercepts calls and safely consumes `quote` (routing quote=False to send_*).
import functools
from pyrogram.types import Message

for _method_name in [
    "reply", "reply_text", "reply_photo", "reply_document", "reply_audio",
    "reply_video", "reply_animation", "reply_sticker", "reply_voice",
    "reply_media_group", "reply_location", "reply_contact"
]:
    _orig_m = getattr(Message, _method_name, None)
    if _orig_m and callable(_orig_m):
        def _make_msg_wrapper(fn, name):
            @functools.wraps(fn)
            async def _msg_wrapper(self, *args, **kwargs):
                quote = kwargs.pop("quote", None)
                if quote is False:
                    send_name = name.replace("reply_", "send_").replace("reply", "send_message")
                    send_fn = getattr(self._client, send_name, None)
                    if send_fn:
                        kwargs.pop("reply_parameters", None)
                        return await send_fn(self.chat.id, *args, **kwargs)
                return await fn(self, *args, **kwargs)
            return _msg_wrapper
        setattr(Message, _method_name, _make_msg_wrapper(_orig_m, _method_name))

if dataBASE.MONGODB_URI:
    from ledger.safebox import db

if not bot.API_TOKEN or not bot.API_HASH or not bot.API_ID:
    logger.error("API_TOKEN, API_HASH, API_ID are mandatory credentials.")
    sys.exit("Error: Missing mandatory bot credentials.")

class RoxyBotApp(RoxyBot):
    def __init__(self) -> None:
        super().__init__(
            name="RoxyPDFTool",
            api_id=bot.API_ID,
            api_hash=bot.API_HASH,
            bot_token=bot.API_TOKEN,
            plugins={"root": "dispatch"},
            workers=20,
            max_concurrent_transmissions=20
        )

    async def start(self, *args, **kwargs):
        if dataBASE.MONGODB_URI:
            b_users, b_chats = await db.get_banned()
            BANNED_USR_DB.extend(b_users)
            BANNED_GRP_DB.extend(b_chats)

            beta_users = await db.get_beta()
            BETA.extend(beta_users)

            users = await db.get_all_users()
            async for user in users:
                if user.get("thumb", False):
                    CUSTOM_THUMBNAIL_U.append(user["id"])
            
            groups = await db.get_all_chats()
            async for group in groups:
                GROUPS.append(group["id"])
                if group.get("thumb", False):
                    CUSTOM_THUMBNAIL_C.append(group["id"])

            users = await db.get_all_users()
            async for user in users:
                user_id = user.get("id")
                if user.get("api") or user.get("fname") or user.get("capt"):
                    DATA[user_id] = [0, 0, 0]
                    DATA[user_id][0] = 1 if user.get("api") else 0
                    DATA[user_id][1] = 1 if user.get("fname") else 0
                    DATA[user_id][2] = 1 if user.get("capt") else 0

        try:
            await super().start(*args, **kwargs)
        except errors.FloodWait as e:
            logger.warning(f"FloodWait {e.value} seconds... Automatically waiting...")
            await asyncio.sleep(e.value)
            await super().start(*args, **kwargs)

        try:
            # Fetch dynamic welcome image directly from channel using get_messages
            msg = await self.get_messages("roxybasicneedbot1", 169)
            if msg and msg.photo:
                images.WELCOME_PIC = msg.photo.file_id
                logger.info(f"✅ Dynamic Welcome Photo loaded from channel: {images.WELCOME_PIC}")
        except Exception as e:
            logger.warning(f"⚠️ Failed to fetch dynamic welcome photo from channel: {e}")

        logger.info("🔧 Setting up conversation message handler...")
        setup_conversation_handler(self)
        logger.info("✅ Conversation handler setup complete")
        
        # Import collective handlers to register them on the active client instance
        import collective.groupdoc
        import collective.groupwelcome

        myID.append(await self.get_me())
        await set_bot_commands(self)

        _force_channels = []
        if settings.UPDATE_CHANNEL:
            _force_channels.append(int(settings.UPDATE_CHANNEL))
        if settings.UPDATE_CHANNEL_2:
            _force_channels.append(int(settings.UPDATE_CHANNEL_2))
        settings.FORCE_SUB_CHANNELS = _force_channels

        for _ch_id in settings.FORCE_SUB_CHANNELS:
            try:
                _ch_info = await self.get_chat(_ch_id)
                if not _ch_info or not _ch_info.username:
                    _inv = await self.create_chat_invite_link(_ch_id)
                    _inv_link = _inv.invite_link
                else:
                    _inv_link = f"https://telegram.dog/{_ch_info.username}"

                invite_link.append({
                    "channel_id": _ch_id,
                    "invite_link": _inv_link
                })
            except errors.ChannelInvalid:
                logger.warning(f"Bot is not admin in channel {_ch_id}")
                settings.FORCE_SUB_CHANNELS = [c for c in settings.FORCE_SUB_CHANNELS if c != _ch_id]
            except Exception as error:
                logger.error(f"⚠️ FORCE SUBSCRIPTION ERROR for {_ch_id}: {error}", exc_info=True)

        logger.info(
            f"\n"
            f"❤ BOT ID: {myID[0].id}\n"
            f"❤ BOT NAME: {myID[0].first_name}\n"
            f"❤ BOT USERNAME: {myID[0].username}\n\n"
            f"❤ DEVELOPED BY: @roxybasicneedbot1 👑\n"
            f"❤ CHANNEL: t.me/roxybasicneedbot1\n"
        )

        if settings.SEND_RESTART:
            if len(works["u"]):
                for u in works["u"]:
                    lang_code = await getLang(int(u))
                    msg, btn = await translate(
                        text="RESTART", button="RESTART['btn']", lang_code=lang_code
                    )
                    await self.send_message(chat_id=int(u), text=msg, reply_markup=btn)

            if len(works["g"]):
                for g in works["g"]:
                    await self.send_message(chat_id=int(g[0]), text=f"restarted.. {g[1]}")

        from core.ledger import log
        if log.LOG_CHANNEL:
            try:
                if len(invite_link) > 0:
                    _ch_info_str = "\n".join(f"  • {ch['invite_link']}" for ch in invite_link)
                    caption = (
                        f"{myID[0].first_name} started successfully...✅\n\n"
                        f"FORCED CHANNELS ({len(invite_link)}):\n{_ch_info_str}\n"
                    )
                else:
                    caption = f"{myID[0].first_name} started successfully...✅"
                
                if log.LOG_FILE and log.LOG_FILE[-4:] == ".log":
                    doc = f"./{log.LOG_FILE}"
                    markUp = InlineKeyboardMarkup([
                        [InlineKeyboardButton("♻️ refresh log ♻️", callback_data="log")],
                        [InlineKeyboardButton("◍ Close ◍", callback_data="close|admin")]
                    ])
                else:
                    doc = images.THUMBNAIL_URL
                    markUp = InlineKeyboardMarkup([
                        [InlineKeyboardButton("◍ close ◍", callback_data="close|admin")]
                    ])

                await self.send_document(
                    chat_id=int(log.LOG_CHANNEL),
                    document=doc,
                    caption=caption,
                    reply_markup=markUp
                )
            except errors.ChannelInvalid:
                log.LOG_CHANNEL = False
                logger.warning("Bot is not admin in LOG_CHANNEL")
            except Exception as error:
                logger.error(f"⚠️ ERROR IN LOG CHANNEL - {error}", exc_info=True)
        
        logger.info(f"Registered handler groups: {list(self.dispatcher.groups.keys())}")
        for g, h in self.dispatcher.groups.items():
            logger.info(f"Group {g}: {len(h)} handlers registered")

    async def stop(self, *args):
        await super().stop()

if __name__ == "__main__":
    work_path = f"{os.path.abspath(os.getcwd())}/work/roxybasicneedbot"
    if os.path.exists(work_path):
        for chat in os.listdir("work/roxybasicneedbot"):
            if f"{chat}".startswith("-100"):
                works["g"].append(
                    [chat, [user for user in os.listdir(f"work/roxybasicneedbot/{chat}")]]
                )
            else:
                works["u"].append(chat)
        shutil.rmtree(f"{os.path.abspath(os.getcwd())}/work")

    os.makedirs("work/roxybasicneedbot", exist_ok=True)
    
    # Import bridge to initialize webhook relays
    import bridge
    
    app = RoxyBotApp()
    app.run()
