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
import os
import asyncio
import requests
from pyrogram import Client as RoxyBot, filters, enums
from pyrogram.types import Message, CallbackQuery, InputMediaPhoto
from core.nexus import settings, images
from core.corestate import dataBASE, DATA
from sentinel import util, work, render, getLang, translate, createBUTTON, formatThumb, thumbName, cbPRO
from tracer import logger

try:
    import pdfkit
    pattern = re.compile(r"(https?://|www\.)?(www\.)?([a-z0-9-]+)(\..+)?")
    urlSupport = True
except Exception:
    urlSupport = False

MAX_FILE_SIZE = int(settings.MAX_FILE_SIZE) if settings.MAX_FILE_SIZE else 200
MAX_FILE_SIZE_IN_kiB = MAX_FILE_SIZE * (10**6)

links = ["https://telegram.dog/", "https://t.me/", "https://telegram.me/"]

async def urlsFromText(text: str) -> list:
    try:
        urls = re.findall(r"(https?://\S+)", text)
        return urls if urls else None
    except Exception:
        return None

async def gDriveID(gDriveLink: str) -> str:
    try:
        if not gDriveLink.startswith("https://drive.google.com"):
            return None
        if "export=download" in gDriveLink:
            return gDriveLink
        elif gDriveLink.startswith("https://drive.google.com/file/d/"):
            FILE_ID = gDriveLink.split("d/")[1].split("/")[0]
            return f"https://drive.google.com/uc?export=download&id={FILE_ID}"
        else:
            return None
    except Exception:
        return None

@RoxyBot.on_message(filters.private & filters.incoming & filters.text, group=1)
async def _url(bot_client: RoxyBot, message: Message):
    try:
        urls = await urlsFromText(message.text)
        if urls is None:
            return
        lang_code = await getLang(message.chat.id)

        for url in urls:
            try:
                await message.reply_chat_action(enums.ChatAction.TYPING)
            except Exception:
                pass

            _, __ = await translate(
                text="DOCUMENT['process']", button="URL['close']", lang_code=lang_code
            )
            data = await message.reply(text=_, quote=True, reply_markup=__)
            await asyncio.sleep(0.3)
            await data.edit(text=_ + ".", reply_markup=__)

            if url.startswith(tuple(links)):
                if "?start=" in url or "?startgroup=" in url:
                    await data.delete()
                    continue
                    
                part = url.split("/")
                try:
                    message_ids = int(part[-1])
                except ValueError:
                    await data.delete()
                    continue
                    
                try:
                    chat_id = int(part[-2])
                    chat_id = int("-100" + f"{chat_id}")
                except Exception:
                    chat_id = part[-2]
                try:
                    file = await bot_client.get_messages(
                        chat_id=chat_id, message_ids=message_ids
                    )
                except Exception as e:
                    tTXT, _ = await translate(
                        text="URL['error']", lang_code=lang_code
                    )
                    return await data.edit(text=tTXT.format(e), reply_markup=__)
                
                await asyncio.sleep(0.3)
                if not file or not file.document:
                    tTXT, _ = await translate(
                        text="URL['notPDF']", lang_code=lang_code
                    )
                    return await data.edit(tTXT)
                    
                isProtect = (
                    "🔒 Protected 🔒"
                    if (
                        (file.sender_chat and file.sender_chat.has_protected_content)
                        or (file.chat and file.chat.has_protected_content)
                    )
                    else "👀 Public 👀"
                )
                tTXT, tBTN = await translate(
                    text="URL['_get']", button="URL['get']", lang_code=lang_code
                )
                await data.edit(
                    text=tTXT.format(
                        url,
                        file.chat.type,
                        file.chat.title,
                        file.chat.username,
                        file.sender_chat.id if file.chat.type == enums.ChatType.CHANNEL else file.chat.id,
                        file.date,
                        file.media,
                        file.document.file_name,
                        await render.gSF(file.document.file_size),
                        isProtect,
                    ),
                    reply_markup=tBTN if file.document.file_name[-4:] == ".pdf" else None,
                    disable_web_page_preview=True,
                )

            elif await gDriveID(url) or url.endswith(".pdf") or bool(urlSupport):
                try:
                    cDIR = await work(message, "create", True)
                    if not cDIR:
                        tTXT_work, tBTN_work = await translate(
                            text='DOCUMENT["refresh"]', lang_code=lang_code
                        )
                        tBTN_work = await createBUTTON(
                            # edit dict refresh values
                            {tTXT_work.get("♻️ Refresh ♻️", "♻️ Refresh ♻️"): "refresh"}
                        )
                        tTXT_inwork, _ = await translate(
                            text='DOCUMENT["inWork"]', lang_code=lang_code
                        )
                        return await data.edit(tTXT_inwork, reply_markup=tBTN_work)

                    if await gDriveID(url):
                        url = await gDriveID(url)
                        
                    response = requests.get(url, stream=True)
                    directDlLink = (
                        True
                        if "Content-Type" in response.headers
                        and (
                            response.headers["Content-Type"] == "application/pdf"
                            or "drive.google" in url
                        )
                        else False
                    )

                    if not (directDlLink or urlSupport):
                        await data.delete()
                        continue

                    if directDlLink:
                        match = re.match(r".*/([^/]+)/?$", url)
                        if "drive.google" in url:
                            content_disposition = response.headers.get("Content-Disposition")
                            if content_disposition:
                                match = re.search(r'filename="(.+)"', content_disposition)
                                if match:
                                    outputName = match.group(1)
                                else:
                                    outputName = (
                                        response.headers.get("Content-Disposition")
                                        .split(";")[-1]
                                        .strip()
                                        .split("=")[-1]
                                        .replace('"', "")
                                    )
                            else:
                                outputName = response.headers.get("Content-Type").split("/")[-1]
                        else:
                            outputName = (
                                match.group(1)
                                if match.group(1).endswith(".pdf")
                                else f"{match.group(1)}.pdf"
                            )

                        response = requests.get(url)

                        if "drive.google" in url:
                            try:
                                headers = {"Range": "bytes=0-1"}
                                res = requests.get(url, headers=headers)
                                total_size = int(
                                    res.headers["Content-Range"].split("/")[-1]
                                )
                            except Exception:
                                tTXT_view, tBTN_view = await translate(
                                    text="URL['view']",
                                    button="URL['close']",
                                    lang_code=lang_code,
                                )
                                return await data.edit(text=tTXT_view, reply_markup=tBTN_view)
                        else:
                            total_size = int(response.headers.get("Content-Length", 0))
                            
                        telegramCan = True if total_size < 20000000 else False
                        if not telegramCan:
                            with open(f"{cDIR}/{message.id}.pdf", "wb") as f:
                                f.write(response.content)

                    elif not directDlLink:
                        outputName = pattern.sub(r"\3", url)
                        pdfkit.from_url(url, f"{cDIR}/{message.id}.pdf")

                    tTXT_done, tBTN_done = await translate(
                        text="URL['done']", button="URL['close']", lang_code=lang_code
                    )
                    try:
                        await data.edit(text=tTXT_done, reply_markup=tBTN_done)
                    except Exception:
                        pass

                    FILE_NAME, FILE_CAPT, THUMBNAIL = await thumbName(
                        message, f"{outputName}.pdf"
                    )
                    if images.PDF_THUMBNAIL != THUMBNAIL:
                        location = await bot_client.download_media(
                            message=THUMBNAIL, file_name=f"{cDIR}/thumb.jpeg"
                        )
                        THUMBNAIL = await formatThumb(location)

                    await message.reply_chat_action(enums.ChatAction.UPLOAD_DOCUMENT)
                    tTXT_open, _ = await translate(
                        text="URL['openCB']", lang_code=lang_code
                    )
                    logFile = await message.reply_document(
                        document=url if directDlLink and telegramCan else f"{cDIR}/{message.id}.pdf",
                        file_name=FILE_NAME.replace("+", " "),
                        caption=f"Url: `{url}`\n\n{FILE_CAPT}",
                        reply_markup=await createBUTTON(
                            # edit dynamic link
                            {tTXT_open.get("🔗 Open In Browser 🔗", "🔗 Open In Browser 🔗"): url}
                        ),
                        thumb=THUMBNAIL,
                        progress=cbPRO,
                        progress_args=(data, 0, "UPLOADED", True),
                        quote=True,
                    )
                    await data.delete()
                    from core.ledger import log
                    await log.newUser(bot_client, message, lang_code, False)
                except Exception as e:
                    logger.error(f"Error converting URL to PDF: {e}", exc_info=True)
                    tTXT_err, tBTN_err = await translate(
                        text="URL['_error']", button="URL['close']", lang_code=lang_code
                    )
                    await data.edit(tTXT_err.format(e), reply_markup=tBTN_err)
            await work(message, "delete", True)

    except Exception as e:
        logger.error(f"Error in URL webpage snapper: {e}", exc_info=True)
        await work(message, "delete", True)
        tTXT_err, tBTN_err = await translate(
            text="URL['error']", button="URL['close']", lang_code=lang_code
        )
        try:
            await data.edit(text=tTXT_err.format(e), reply_markup=tBTN_err)
        except Exception:
            pass

@RoxyBot.on_callback_query(filters.regex("getFile"))
async def _getFile(bot_client: RoxyBot, callbackQuery: CallbackQuery):
    try:
        lang_code = await getLang(callbackQuery.message.chat.id)
        url = callbackQuery.message.reply_to_message.text
        part = url.split("/")
        message_ids = int(part[-1])
        try:
            chat_id = int(part[-2])
            chat_id = int("-100" + f"{chat_id}")
        except Exception:
            chat_id = part[-2]
            
        file = await bot_client.get_messages(chat_id=chat_id, message_ids=message_ids)
        if MAX_FILE_SIZE and file.document.file_size >= int(MAX_FILE_SIZE_IN_kiB):
            tTXT_big, _ = await translate(text="getFILE['big']", lang_code=lang_code)
            return await callbackQuery.answer(tTXT_big.format(MAX_FILE_SIZE))

        from sentinel import header
        if await header(bot_client, callbackQuery, lang_code=lang_code):
            return

        cDIR = await work(callbackQuery, "create", False)
        if not cDIR:
            _, __ = await translate(text="getFILE['inWork']", lang_code=lang_code)
            return await callbackQuery.answer(_)

        _, __ = await translate(text="getFILE['wait']", lang_code=lang_code)
        await callbackQuery.answer(_)
        
        if not (
            (file.sender_chat and file.sender_chat.has_protected_content)
            or (file.chat and file.chat.has_protected_content)
        ):
            await work(callbackQuery, "delete", False)
            return await file.copy(
                chat_id=callbackQuery.message.chat.id, caption=file.caption
            )

        _, __ = await translate(button="getFILE['dl']", lang_code=lang_code)
        await callbackQuery.edit_message_reply_markup(__)
        
        location = await bot_client.download_media(
            message=file.document.file_id,
            file_name=f"{cDIR}/{file.document.file_name}",
            progress=cbPRO,
            progress_args=(callbackQuery.message, file.document.file_size, "DOWNLOADED", True),
        )
        
        _, __ = await translate(button="getFILE['up']", lang_code=lang_code)
        await callbackQuery.edit_message_reply_markup(__)
        
        logFile = await callbackQuery.message.reply_document(
            document=location,
            caption=file.caption,
            progress=cbPRO,
            progress_args=(callbackQuery.message, 0, "UPLOADED", True),
        )
        
        _, __ = await translate(button="getFILE['complete']", lang_code=lang_code)
        await callbackQuery.edit_message_reply_markup(__)
        await work(callbackQuery, "delete", False)
        from core.ledger import log
        await log.newUser(bot_client, callbackQuery.message, lang_code, False)
    except Exception as e:
        logger.error(f"Error in B2B Snatcher getFile: {e}", exc_info=True)
        await work(callbackQuery, "delete", False)
