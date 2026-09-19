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
import os
import shutil
import time
import psutil
from core.nexus import settings, dm, images
from core.corestate import dataBASE, myID, invite_link, works, ping_list, CUSTOM_THUMBNAIL_U, CUSTOM_THUMBNAIL_C, GROUPS, DATA
from sentinel import util, work, render, getLang, translate, createBUTTON
from pyrogram import Client as RoxyBot, filters, enums
from pyrogram.types import Message, CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from dispatch.sentry import extract_data
from dispatch.prefs import _settings
from tracer import logger

if dataBASE.MONGODB_URI:
    from ledger.safebox import db

@RoxyBot.on_message(filters.private & filters.incoming & filters.command(["start"]), group=0)
async def start_cmd(bot_client: RoxyBot, message: Message):
    logger.debug(f"📩 /start command received from user {message.from_user.id}")
    try:
        await work(message, "delete", True)
        lang_code = await getLang(message.chat.id)
        await message.reply_chat_action(enums.ChatAction.TYPING)
        
        get_pdf = None
        md5_str = None
        
        if "-" in message.text:
            lang_code, refer_id, get_pdf, md5_str = await extract_data(f"{message.text}-")

        if (
            settings.MULTI_LANG_SUP
            and message.from_user.language_code
            and message.from_user.language_code != "en"
            and lang_code == "eng"
        ):
            change, _ = await translate(text="SETTINGS['chgLang']", lang_code=lang_code)
            from core.i18n import LANG_MAP as langList
            _lang = {
                langList[lang][1]: f"set|lang|{lang}"
                for lang in langList
                if lang != lang_code
            }
            change.update(_lang)
            back, _ = await translate(text="SETTINGS['back'][1]", lang_code=lang_code)
            change.update(back)
            tBTN = await createBUTTON(
                btn=change,
                order=int(f"1{((len(change)-2)//3)*'3'}{(len(change)-2)%3}1"),
            )
            tTXT, _ = await translate(text="SETTINGS['lang']", lang_code=lang_code)
        elif "-" in message.text and md5_str:
            from dispatch.reactor.ops.pdf_deeplink import openInBot
            return await openInBot(bot_client, message, md5_str)
        else:
            tTXT, tBTN = await translate(
                text="HOME['HomeA']",
                lang_code=lang_code,
                order=2121 if message.chat.id not in dm.ADMINS else 21221,
                button="HOME['HomeACB']" if message.chat.id not in dm.ADMINS else "HOME['HomeAdminCB']",
            )

        for retry in range(3):
            try:
                await message.reply_photo(
                    photo=images.WELCOME_PIC,
                    reply_markup=tBTN,
                    caption=tTXT.format(message.from_user.mention, myID[0].mention),
                )
                break
            except FloodWait as e:
                logger.warning(f"FloodWait in /start: waiting {e.value} seconds")
                await asyncio.sleep(e.value + 1)
        
        tTXT, tBTN = await translate(text="HOME['search']", lang_code=lang_code)
        
        for retry in range(3):
            try:
                await message.reply_sticker(
                    sticker="CAACAgUAAxkBAAIDK2k6tE1vTHhIs_tYD3bIuTC5rpLzAAKdFwACZzqZVsIlT2pK1QJuHgQ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="📩 Contact Admin 📩", url="https://t.me/roxycontactbot"
                                )
                            ],
                        ]
                    ),
                )
                break
            except FloodWait as e:
                logger.warning(f"FloodWait in /start sticker: waiting {e.value} seconds")
                await asyncio.sleep(e.value + 1)
        
        if "-" in message.text and get_pdf:
            from dispatch.reactor.ops.pdf_deeplink import decode
            await decode(bot_client, get_pdf, message, lang_code)
        return await message.delete()
    except Exception as e:
        logger.error(f"Error in start_cmd: {e}", exc_info=True)

@RoxyBot.on_callback_query(filters.regex("^Home"))
async def home_callback(bot_client: RoxyBot, callbackQuery: CallbackQuery):
    try:
        lang_code = await getLang(callbackQuery.message.chat.id)
        if await render.header(bot_client, callbackQuery, lang_code, doc=False):
            return

        await callbackQuery.answer()
        data = callbackQuery.data
        home, page = callbackQuery.data.split("|")

        if page in ["A", "B2A"]:
            args = [callbackQuery.from_user.mention, myID[0].mention]
            if callbackQuery.message.chat.type == enums.ChatType.PRIVATE:
                if page == "B2A":
                    await callbackQuery.edit_message_media(
                        InputMediaPhoto(images.WELCOME_PIC)
                    )
                tTXT, tBTN = await translate(
                    text="HOME['HomeA']",
                    order=2121,
                    button="HOME['HomeACB']" if callbackQuery.message.chat.id not in dm.ADMINS else "HOME['HomeAdminCB']",
                    lang_code=lang_code,
                )
            else:
                tTXT, tBTN = await translate(
                    text="HomeG['HomeA']",
                    button="HomeG['HomeACB']" if callbackQuery.message.chat.id not in dm.ADMINS else "HOME['HomeAdminCB']",
                    lang_code=lang_code,
                )
            return await callbackQuery.edit_message_caption(
                caption=tTXT.format(*args), reply_markup=tBTN
            )

        elif page in ["B", "B2S"]:
            return await _settings(bot_client, callbackQuery)

        elif page == "C":
            tTXT, tBTN = await translate(
                text="HOME['HomeC']", button="HOME['HomeCCB']", lang_code=lang_code
            )
            return await callbackQuery.edit_message_caption(
                caption=tTXT, reply_markup=tBTN
            )

        elif page == "D":
            tTXT, tBTN = await translate(
                text="HOME['HomeD']", button="HOME['HomeDCB']", lang_code=lang_code
            )
            return await callbackQuery.edit_message_caption(
                caption=tTXT, reply_markup=tBTN
            )
    except Exception as e:
        logger.error(f"Error in home_callback: {e}", exc_info=True)

@RoxyBot.on_callback_query(filters.regex("^status"))
async def status_callback(bot_client: RoxyBot, callbackQuery: CallbackQuery):
    try:
        lang_code = await getLang(callbackQuery.message.chat.id)
        _, __ = callbackQuery.data.split("|")

        if await render.header(bot_client, callbackQuery, lang_code, doc=False):
            return

        if __ in ["db", "users"] and not dataBASE.MONGODB_URI:
            tTXT, tBTN = await translate(
                text="STATUS_MSG['NO_DB']", lang_code=lang_code
            )
            return await callbackQuery.answer(tTXT)
        await callbackQuery.answer()

        if __ in "db":
            total_users = await db.total_users_count()
            total_chats = await db.total_chat_count()
            tTXT, tBTN = await translate(
                text="STATUS_MSG['DB']",
                button="STATUS_MSG['BACK']",
                lang_code=lang_code,
            )
            return await callbackQuery.edit_message_caption(
                caption=tTXT.format(total_users, total_chats), reply_markup=tBTN
            )

        elif __ == "server":
            total, used, free = shutil.disk_usage(".")
            total_str = await render.gSF(total)
            used_str = await render.gSF(used)
            free_str = await render.gSF(free)
            cpu_usage = psutil.cpu_percent()
            ram_usage = psutil.virtual_memory().percent
            disk_usage = psutil.disk_usage("/").percent
            tTXT, tBTN = await translate(
                text="STATUS_MSG['SERVER']",
                button="STATUS_MSG['BACK']",
                lang_code=lang_code,
            )
            return await callbackQuery.edit_message_caption(
                caption=tTXT.format(
                    total_str,
                    used_str,
                    disk_usage,
                    free_str,
                    cpu_usage,
                    ram_usage,
                    len("a"),
                    callbackQuery.message.id,
                ),
                reply_markup=tBTN,
            )

        elif __ == "admin":
            msg, tBTN = await translate(
                text="STATUS_MSG['ADMIN']",
                button="STATUS_MSG['BACK']",
                lang_code=lang_code,
            )
            for admin in dm.ADMINS:
                try:
                    userINFO = await bot_client.get_users(int(admin))
                    msg += f"\n {userINFO.mention}"
                except Exception:
                    pass
            return await callbackQuery.message.edit(
                text=msg.format(len(dm.ADMINS)), reply_markup=tBTN
            )

        elif __ == "users":
            users = await db.get_all_users()
            tTXT, tBTN = await translate(
                text="STATUS_MSG['USERS']",
                button="STATUS_MSG['BACK']",
                lang_code=lang_code,
            )
            await callbackQuery.message.edit(text=tTXT, reply_markup=tBTN)
            rollnumber = 0
            text = ""
            async for user in users:
                rollnumber += 1
                if rollnumber % 500 == 0 and rollnumber % 1000 != 0:
                    await asyncio.sleep(0.5)
                    try:
                        await callbackQuery.message.edit(
                            text=f"{tTXT}.", reply_markup=tBTN
                        )
                    except Exception:
                        pass
                elif rollnumber % 500 == 0 and rollnumber % 1000 == 0:
                    try:
                        await callbackQuery.message.edit(text=tTXT, reply_markup=tBTN)
                    except Exception:
                        pass
                try:
                    text += f"[{user['name']}](tg://user?id={user['id']})"
                except Exception:
                    logger.debug(f"••• error user: {user}")
                if user.get("banned", False):
                    text += " `Banned ⚠️`"
                text += "\n"
                if rollnumber % 100 == 0:
                    with open(f"{myID[0].username}.txt", "w+") as outfile:
                        outfile.write(text)
                    text = ""
            with open(f"{myID[0].username}.txt", "w+") as outfile:
                outfile.write(text)
            await callbackQuery.message.reply_document(f"{myID[0].username}.txt")
            os.remove(f"{myID[0].username}.txt")

        elif __ == "home":
            tTXT, tBTN = await translate(
                text="STATUS_MSG['HOME']",
                button="STATUS_MSG['_HOME']",
                order=12121,
                lang_code=lang_code,
            )
            return await callbackQuery.message.edit(text=tTXT, reply_markup=tBTN)
    except Exception as e:
        logger.error(f"Error in status_callback: {e}", exc_info=True)

@RoxyBot.on_callback_query(filters.regex("^close"))
async def close_callback(bot_client: RoxyBot, callbackQuery: CallbackQuery):
    try:
        _, data = callbackQuery.data.split("|")
        if data == "admin":
            if callbackQuery.from_user.id in dm.ADMINS:
                return await callbackQuery.message.delete()
            else:
                return await callbackQuery.answer("🫡")

        if await render.header(bot_client, callbackQuery, doc=False):
            return

        # Always clean up workspace when user closes/cancels an operation
        if data in ["me", "all", "P2I", "mee"]:
            await work(callbackQuery, "delete", False)

        if data == "me":
            await callbackQuery.message.delete()
            return
        elif data == "hd":
            await callbackQuery.message.delete()
            from dispatch.photobox import HD
            if callbackQuery.message.chat.id in HD:
                del HD[callbackQuery.message.chat.id]
            return
        elif data == "mee":
            return await callbackQuery.message.delete()
        elif data == "all":
            if callbackQuery.message.chat.type == enums.ChatType.PRIVATE:
                try:
                    await callbackQuery.message.delete()
                except Exception:
                    pass
                try:
                    if callbackQuery.message.reply_to_message:
                        await callbackQuery.message.reply_to_message.delete()
                except Exception:
                    pass
                return
            await callbackQuery.message.delete()
            return
        elif data == "P2I":
            lang_code = await util.getLang(callbackQuery.from_user.id)
            _, canceled = await translate(
                text="INDEX['cancelCB']",
                button="INDEX['_canceledCB']",
                lang_code=lang_code,
            )
            await callbackQuery.answer(_.replace("`", ""))
            return await callbackQuery.edit_message_reply_markup(canceled)
        elif data == "dev":
            lang_code = await util.getLang(callbackQuery.from_user.id)
            _, __ = await translate(text="cbAns", lang_code=lang_code)
            return await callbackQuery.answer(_[0])
    except Exception as e:
        logger.error(f"Error in close_callback: {e}", exc_info=True)
