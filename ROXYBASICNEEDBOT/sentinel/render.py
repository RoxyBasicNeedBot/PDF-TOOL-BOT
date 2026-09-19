# This module is part of https://github.com/RoxyBasicNeedBot
# copyright ©️ 2021 nabilanavab

import gc
import math
import time
import asyncio
import fitz
from pyrogram.enums import ChatMemberStatus, ChatType, ChatAction
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from core.nexus import dm, settings
from core.i18n import translate, getLang, createBUTTON
from sentinel.workspace import work
from tracer import logger

_REPLY_MESSAGE_CACHE = {}

def register_reply_cache(chat_id: int, reply_msg_id: int, original_msg: Message):
    if not chat_id and original_msg and original_msg.from_user:
        chat_id = original_msg.from_user.id
    if chat_id and original_msg and getattr(original_msg, "document", None):
        _REPLY_MESSAGE_CACHE[(chat_id, reply_msg_id)] = original_msg
        _REPLY_MESSAGE_CACHE[(chat_id, "latest")] = original_msg
        logger.warning(f"💾 [CACHE STORED] chat_id={chat_id}, reply_msg_id={reply_msg_id}, file={original_msg.document.file_name}")
        if len(_REPLY_MESSAGE_CACHE) > 2000:
            keys = list(_REPLY_MESSAGE_CACHE.keys())[:500]
            for k in keys:
                _REPLY_MESSAGE_CACHE.pop(k, None)
    else:
        logger.warning(f"💾 [CACHE REJECTED] chat_id={chat_id}, reply_msg_id={reply_msg_id}, has_doc={bool(getattr(original_msg, 'document', None)) if original_msg else False}")

def get_cached_reply_message(chat_id: int, reply_msg_id: int) -> Message:
    if not chat_id:
        return None
    msg = _REPLY_MESSAGE_CACHE.get((chat_id, reply_msg_id))
    if not msg:
        msg = _REPLY_MESSAGE_CACHE.get((chat_id, "latest"))
    if not msg:
        for (c_id, _), cached_m in _REPLY_MESSAGE_CACHE.items():
            if c_id == chat_id and getattr(cached_m, "document", None):
                return cached_m
    return msg

# Checks the user for a callback query and hydrates reply_to_message
async def ensure_reply_to_message(bot, callbackQuery) -> Message:
    if not callbackQuery or not callbackQuery.message:
        logger.warning("ensure_reply_to_message: callbackQuery or message is None")
        return None
        
    if callbackQuery.message.reply_to_message and getattr(callbackQuery.message.reply_to_message, "document", None):
        return callbackQuery.message.reply_to_message
        
    chat_id = callbackQuery.message.chat.id if callbackQuery.message.chat else (callbackQuery.from_user.id if callbackQuery.from_user else None)
    logger.warning(f"🔍 [CACHE LOOKUP] ensure_reply_to_message: chat_id={chat_id}, cb_msg_id={callbackQuery.message.id}, active_keys={list(_REPLY_MESSAGE_CACHE.keys())}")
    if chat_id:
        cached = get_cached_reply_message(chat_id, callbackQuery.message.id)
        if cached and getattr(cached, "document", None):
            logger.warning(f"⚡ [CACHE HIT] ensure_reply_to_message: Hydrated from memory cache for callback {callbackQuery.data}")
            callbackQuery.message.reply_to_message = cached
            return cached

    reply_id = getattr(callbackQuery.message, "reply_to_message_id", None)
    if not reply_id and getattr(callbackQuery.message, "reply_to_message", None):
        reply_id = getattr(callbackQuery.message.reply_to_message, "id", None)

    if not reply_id and hasattr(bot, "get_messages") and chat_id:
        try:
            full_msg = await bot.get_messages(chat_id, callbackQuery.message.id)
            logger.warning(f"📨 [API GET_MESSAGE] full_msg_id={full_msg.id if full_msg else None}, reply_to_msg={getattr(full_msg, 'reply_to_message', None) if full_msg else None}, reply_to_id={getattr(full_msg, 'reply_to_message_id', None) if full_msg else None}")
            if full_msg:
                if full_msg.reply_to_message and getattr(full_msg.reply_to_message, "document", None):
                    callbackQuery.message.reply_to_message = full_msg.reply_to_message
                    return full_msg.reply_to_message
                reply_id = getattr(full_msg, "reply_to_message_id", getattr(full_msg.reply_to_message, "id", None) if getattr(full_msg, "reply_to_message", None) else None)
        except Exception as e:
            logger.warning(f"ensure_reply_to_message: get_messages({callbackQuery.message.id}) error: {e}")

    if reply_id and chat_id:
        try:
            reply_msg = await bot.get_messages(chat_id, reply_id)
            if reply_msg and getattr(reply_msg, "document", None):
                callbackQuery.message.reply_to_message = reply_msg
                return reply_msg
        except Exception as e:
            logger.warning(f"ensure_reply_to_message: Failed to fetch reply_msg {reply_id}: {e}")
            
    if not callbackQuery.message.reply_to_message or not getattr(callbackQuery.message.reply_to_message, "document", None):
        logger.warning(f"❌ ensure_reply_to_message: Could not find document in reply_to_message for callback {callbackQuery.data}")
    return callbackQuery.message.reply_to_message

async def header(bot, callbackQuery, lang_code: str = settings.DEFAULT_LANG, doc: bool = True) -> bool:
    try:
        _get_main_loop()
        chat_type = callbackQuery.message.chat.type
        user_id = callbackQuery.from_user.id

        if not doc:
            if chat_type != ChatType.PRIVATE and user_id not in dm.ADMINS:
                userStat = await bot.get_chat_member(callbackQuery.message.chat.id, user_id)
                if userStat.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                    msg, _ = await translate(text="BAN['cbNotU']", lang_code=lang_code)
                    await callbackQuery.answer(msg, show_alert=True)
                    return True
            return False

        fileExist = await ensure_reply_to_message(bot, callbackQuery)
        if not fileExist:
            if chat_type != ChatType.PRIVATE:
                return True
            return False

        if chat_type != ChatType.PRIVATE and user_id != fileExist.from_user.id and user_id not in dm.ADMINS:
            userStat = await bot.get_chat_member(callbackQuery.message.chat.id, user_id)
            if userStat.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                msg, _ = await translate(text="INLINE['cbNotU']", lang_code=lang_code)
                await callbackQuery.answer(msg, show_alert=True)
                return True
        return False
    except Exception as e:
        logger.error(f"Error in header validation: {e}")
        return True

# SIZE FORMATER (TO HUMAN READABLE FORM)
async def gSF(b: int, factor: int = 2**10, suffix: str = "B") -> str:
    try:
        for unit in ["", "K", "M", "G", "T"]:
            if b < factor:
                return f"{b:.2f} {unit}{suffix}"
            b /= factor
        return f"{b:.2f} Y{suffix}"
    except Exception as e:
        logger.error(f"Error in gSF function: {e}")
        return "0 B"

# CHECKS PDF CODEC, IS ENCRYPTED OR NOT
async def checkPdf(file_path: str, callbackQuery, lang_code: str = settings.DEFAULT_LANG):
    try:
        CHUNK, _ = await translate(text="PDF_MESSAGE", lang_code=lang_code)
        replyMessage = callbackQuery.message.reply_to_message

        with fitz.open(file_path) as doc:
            pdfMetaData = (
                "".join(
                    f"`{i} : {doc.metadata[i]}`\n"
                    for i in doc.metadata
                    if doc.metadata[i] != ""
                )
                if doc.metadata
                else ""
            )

            result_status = None
            result_pages = doc.page_count

            if doc.is_encrypted:
                try:
                    await callbackQuery.edit_message_text(
                        text=CHUNK["encrypt"].format(
                            replyMessage.document.file_name,
                            await gSF(replyMessage.document.file_size),
                        )
                        + "\n\n" + CHUNK["pg"].format(doc.page_count)
                        + "\n\n" + pdfMetaData,
                        reply_markup=await createBUTTON(CHUNK["encryptCB"], order=11),
                    )
                except Exception:
                    pass

                if callbackQuery.data != "work|decrypt":
                    await work(callbackQuery, "delete", False)

                result_status = "encrypted"
            else:
                if callbackQuery.data != "#merge":
                    try:
                        await callbackQuery.edit_message_text(
                            text=CHUNK["pdf"].format(
                                replyMessage.document.file_name,
                                await gSF(replyMessage.document.file_size),
                            )
                            + "\n\n" + CHUNK["pg"].format(doc.page_count)
                            + "\n\n" + pdfMetaData,
                            reply_markup=callbackQuery.message.reply_markup,
                        )
                    except Exception as edit_error:
                        logger.debug(f"Could not edit message for valid PDF: {edit_error}")

                result_status = "pass"

        gc.collect()
        return result_status, result_pages
    except Exception as Error:
        logger.exception(f"Error in checkPdf: {Error}")
        try:
            await callbackQuery.edit_message_text(
                text=CHUNK["error"],
                reply_markup=await createBUTTON(CHUNK["errorCB"], order=11),
            )
            await work(callbackQuery, "delete", False)
        except Exception as edit_error:
            logger.debug(f"Could not edit message in error handler: {edit_error}")
        return "notPdf", "🚫"

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    
    tmp = []
    if days:
        tmp.append(f"{days}d, ")
    if hours:
        tmp.append(f"{hours}h, ")
    if minutes:
        tmp.append(f"{minutes}m, ")
    if seconds:
        tmp.append(f"{seconds}s, ")
    if milliseconds:
        tmp.append(f"{milliseconds}ms")
        
    return "".join(tmp) or "0 s"

# DOC. DOWNLOAD PROGRESS (DECOUPLED ASYNC WORKER AND SYNCHRONOUS WRAPPER)
_last_download_update = {}

async def progress(current: int, t: int, total: int, message, start: float) -> None:
    try:
        now = time.time()
        diff = now - start
        
        msg_id = message.id if hasattr(message, 'id') else id(message)
        last_update = _last_download_update.get(msg_id, 0)
        
        # Update only every 3 seconds OR when complete (prevents FloodWait)
        if (now - last_update) < 3 and current != total:
            return
        
        _last_download_update[msg_id] = now
        
        if current == total:
            _last_download_update.pop(msg_id, None)
        
        percentage = (current * 100 / total) if total > 0 else 0
        speed = (current / diff) if diff > 0 else 0
        time_to_completion = round((total - current) / speed) * 1000 if speed > 0 else 0
        
        progress_bar = "[{0}{1}] \n".format(
            "".join(["●" for _ in range(min(20, math.floor(percentage / 5)))]),
            "".join(["○" for _ in range(20 - min(20, math.floor(percentage / 5)))]),
        )

        estimated_total_time = TimeFormatter(time_to_completion)
        lang_code = await getLang(message.chat.id)
        
        tTXT, tBTN = await translate(
            text="PROGRESS['progress']",
            button="DOCUMENT['cancelCB']",
            lang_code=lang_code,
        )

        tmp = progress_bar + tTXT.format(
            await gSF(current),
            await gSF(total),
            await gSF(speed),
            estimated_total_time if estimated_total_time != "" else "0 s",
        )

        await message.edit_text(
            text="DOWNLOADING.. 📥\n{}".format(tmp)[:1000],
            reply_markup=tBTN
        )
    except Exception as e:
        pass

_main_loop = None

def _get_main_loop():
    global _main_loop
    try:
        loop = asyncio.get_running_loop()
        _main_loop = loop
        return loop
    except RuntimeError:
        if _main_loop is not None and _main_loop.is_running():
            return _main_loop
        try:
            return asyncio.get_event_loop()
        except Exception:
            return _main_loop

_last_upload_update = {}

async def _progress(current: int, total: int, message, start: float) -> None:
    try:
        now = time.time()
        diff = now - start
        
        msg_id = message.id if hasattr(message, 'id') else id(message)
        last_update = _last_upload_update.get(msg_id, 0)
        
        if (now - last_update) < 3 and current != total:
            return
        
        _last_upload_update[msg_id] = now
        
        if current == total:
            _last_upload_update.pop(msg_id, None)
        
        await message.reply_chat_action(ChatAction.UPLOAD_DOCUMENT)
        
        percentage = (current * 100 / total) if total > 0 else 0
        speed = (current / diff) if diff > 0 else 0
        time_to_completion = round((total - current) / speed) * 1000 if speed > 0 else 0
        
        progress_bar = "[{0}{1}] \n".format(
            "".join(["●" for _ in range(min(20, math.floor(percentage / 5)))]),
            "".join(["○" for _ in range(20 - min(20, math.floor(percentage / 5)))]),
        )

        estimated_total_time = TimeFormatter(time_to_completion)
        lang_code = await getLang(message.chat.id)

        tTXT, tBTN = await translate(
            text="PROGRESS['progress']",
            button="DOCUMENT['cancelCB']",
            lang_code=lang_code,
        )

        tmp = progress_bar + tTXT.format(
            await gSF(current),
            await gSF(total),
            await gSF(speed),
            estimated_total_time if estimated_total_time != "" else "0 s",
        )
        
        await message.edit_text(
            text="UPLOADING.. 📤\n{}".format(tmp), reply_markup=tBTN
        )
    except Exception as e:
        pass

async def cbPRO(current: int, t: int, message, total: int = 0, typ: str = "DOWNLOADED", cancel: bool = False):
    try:
        lang_code = await getLang(message.chat.id)
        if t != 0:
            total = t
        if total == 0:
            return
            
        if typ == "DOWNLOADED":
            tTXT, _ = await translate(text="PROGRESS['cbPRO_D']", lang_code=lang_code, asString=True)
        else:
            tTXT, _ = await translate(text="PROGRESS['cbPRO_U']", lang_code=lang_code, asString=True)
            
        percentage = (current * 100 / total) if total > 0 else 0
        btn_text = tTXT[0].format(percentage)
        cancel_btn_text = tTXT[1] if len(tTXT) > 1 else "Cancel"
        
        if cancel:
            markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(btn_text, callback_data="nabilanavab")],
                [InlineKeyboardButton(cancel_btn_text, callback_data="close|all")]
            ])
        else:
            markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(btn_text, callback_data="close|all")]
            ])
            
        await message.edit_reply_markup(reply_markup=markup)
    except Exception:
        pass
