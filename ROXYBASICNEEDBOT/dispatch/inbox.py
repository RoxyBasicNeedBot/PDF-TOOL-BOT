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
import asyncio
import time
import fitz
import convertapi
from PIL import Image
from pyrogram import Client as RoxyBot, filters, enums
from pyrogram.types import Message
from core.nexus import settings, images
from core.corestate import dataBASE, BETA, DATA
from sentinel import work, getLang, translate, createBUTTON, formatThumb, thumbName, progress, _progress, gSF, safe_reply_text
from dispatch.photobox import HD
from scriptorium import works, PDF
from tracer import logger

try:
    import aspose.words as word
    wordSupport = True
except Exception:
    wordSupport = False

MAX_FILE_SIZE = int(settings.MAX_FILE_SIZE) if settings.MAX_FILE_SIZE else 200
MAX_FILE_SIZE_IN_kiB = MAX_FILE_SIZE * (10**6)

img2pdf = [".jpg", ".png", ".jpeg"]
pymu2PDF = [".xps", ".cbz", ".fb2", ".epub", ".oxps"]
wordFiles = [".ps", ".docx", ".doc", ".odt", ".rtf"]
cnvrt_api_2PDF = [".csv", ".log", ".mpp", ".xml", ".mpt", ".pot", ".pps", ".ppt", ".pub", ".vdx", ".vsd", ".vst", ".wpd", ".wps", ".wri", ".xlt", ".xls", ".ppsx", ".pptx", ".xlsb", ".xlsx", ".xltx", ".potx", ".vsdx", ".vstx"]

async def pymuConvert2PDF(cDIR, edit, input_file, lang_code):
    try:
        with fitz.open(input_file) as doc:
            with fitz.open("pdf", doc.convert_to_pdf()) as pdf:
                pdf.save(
                    f"{cDIR}/outPut.pdf",
                    garbage=4,
                    deflate=True,
                )
        return True
    except Exception as e:
        tTXT, tBTN = await translate(text="DOCUMENT['error']", lang_code=lang_code)
        await edit.edit(
            text=tTXT.format(e),
            reply_markup=await createBUTTON(btn={"👍": "try+", "👎": "try-"}),
        )
        return False

async def cvApi2PDF(cDIR, edit, input_file, lang_code, API):
    try:
        convertapi.api_secret = API
        fileNm, fileExt = os.path.splitext(input_file)
        convertapi.convert(
            "pdf",
            {"File": f"{input_file}"},
            from_format=fileExt[1:],
        ).save_files(f"{cDIR}/outPut.pdf")
        return True
    except Exception as e:
        tTXT, tBTN = await translate(text="DOCUMENT['error']", lang_code=lang_code)
        await edit.edit(tTXT.format(e))
        return False

async def word2PDF(cDIR, edit, input_file, lang_code):
    try:
        if not wordSupport:
            raise Exception("Aspose library is missing or unsupported on this architecture")
        doc = word.Document(input_file)
        doc.save(f"{cDIR}/outPut.pdf")
        return True
    except Exception as e:
        tTXT, tBTN = await translate(text="DOCUMENT['error']", lang_code=lang_code)
        await edit.edit(tTXT.format(e))
        return False

@RoxyBot.on_message(filters.private & filters.incoming & filters.document, group=1)
async def documents_receiver(bot_client: RoxyBot, message: Message):
    logger.debug(f"📄 Document received from user {message.from_user.id}: {message.document.file_name}")
    try:
        try:
            await message.reply_chat_action(enums.ChatAction.TYPING)
        except Exception:
            pass
            
        lang_code = await getLang(message.chat.id)
        CHUNK, _ = await translate(text="DOCUMENT", lang_code=lang_code)
        
        if await work(message, "check", True):
            tBTN = await createBUTTON(
                # edits refresh dict
                {CHUNK["refresh"].get("♻️ Refresh ♻️", "♻️ Refresh ♻️"): "refresh"}
            )
            return await message.reply_text(
                CHUNK["inWork"], reply_markup=tBTN, quote=True
            )
            
        fileNm, fileExt = os.path.splitext(message.document.file_name)
        
        if MAX_FILE_SIZE and message.document.file_size >= int(MAX_FILE_SIZE_IN_kiB):
            file_size_mb = round(message.document.file_size / (10**6), 1)
            tBTN = await createBUTTON(CHUNK["bigCB"])
            return await message.reply_photo(
                photo=images.BIG_FILE,
                caption=CHUNK["big"].format(MAX_FILE_SIZE, MAX_FILE_SIZE)
                + f"\n\n📄 Your file: **{file_size_mb} MB**"
                + f"\n⚠️ Due to server costs, we can't process files larger than **{MAX_FILE_SIZE} MB**."
                + "\n🙏 Please compress or split your file before sending.",
                reply_markup=tBTN,
            )
            
        elif fileExt.lower() == ".pdf":
            pdfMsgId = await safe_reply_text(message, CHUNK["process"], quote=True)
            if pdfMsgId is None:
                logger.error("FloodWait retries exhausted, cannot process PDF")
                return await work(message, "delete", True)
                
            await asyncio.sleep(0.3)
            await pdfMsgId.edit(CHUNK["process"] + ".")
            await asyncio.sleep(0.3)
            
            tBTN = await createBUTTON(
                CHUNK["replyCB"] if message.chat.id in BETA else CHUNK["_replyCB"]
            )
            await pdfMsgId.edit(
                text=CHUNK["reply"].format(
                    message.document.file_name,
                    await gSF(message.document.file_size),
                ),
                reply_markup=tBTN,
            )
            from sentinel.render import register_reply_cache
            register_reply_cache(message.chat.id if message.chat else None, pdfMsgId.id, message)
            logFile = message

        elif fileExt.lower() in img2pdf:
            try:
                if message.chat.id in HD:
                    if len(HD[message.chat.id]) >= 16:
                        return
                    HD[message.chat.id].append(message.document.file_id)
                    generateCB = "generate" if settings.DEFAULT_NAME else "generateRN"
                    tTXT, tBTN = await translate(
                        text="DOCUMENT['imageAdded']",
                        button=f"DOCUMENT['{generateCB}']",
                        lang_code=lang_code,
                    )
                    return await message.reply_text(
                        tTXT.format(len(HD[message.chat.id]) - 1, message.chat.id)
                        + " [HD] 🔰",
                        reply_markup=tBTN,
                        quote=True,
                    )
                imageDocReply = await message.reply_text(CHUNK["download"], quote=True)
                if not isinstance(PDF.get(message.from_user.id), list):
                    PDF[message.from_user.id] = []
                path = await message.download(
                    f"{message.from_user.id}/{message.id}.jpg"
                )
                img = Image.open(path).convert("RGB")
                PDF[message.from_user.id].append(img)
                generateCB = "generate" if settings.DEFAULT_NAME else "generateRN"
                tBTN = await createBUTTON(CHUNK[generateCB])
                await imageDocReply.edit(
                    text=CHUNK["imageAdded"].format(
                        len(PDF[message.from_user.id]), message.from_user.id
                    ),
                    reply_markup=tBTN,
                )
                os.remove(path)
                return
            except Exception as e:
                return await imageDocReply.edit(CHUNK["error"].format(e))

        elif (fileExt.lower() in pymu2PDF) or (fileExt.lower() in cnvrt_api_2PDF) or (fileExt.lower() in wordFiles):
            from ledger.safebox import db
            if (fileExt.lower() in cnvrt_api_2PDF) and (
                (
                    not DATA.get(message.chat.id, 0)
                    or (
                        DATA.get(message.chat.id, 0)
                        and not DATA.get(message.chat.id, 0)[0]
                    )
                )
                and settings.CONVERT_API is False
            ):
                return await message.reply_text(CHUNK["noAPI"], quote=True)

            if (fileExt.lower() in wordFiles) and not wordSupport:
                return await message.reply_text(CHUNK["useDOCKER"], quote=True)

            cDIR = await work(message, "create", True)
            tBTN = await createBUTTON(CHUNK["cancelCB"])
            pdfMsgId = await message.reply_text(
                CHUNK["download"], reply_markup=tBTN, quote=True
            )
            input_file = f"{cDIR}/input_file{fileExt}"
            
            logger.debug(f"⬇️ Starting conversion download to: {input_file}")
            downloadLoc = await bot_client.download_media(
                message=message.document.file_id,
                file_name=input_file,
                progress=progress,
                progress_args=(message.document.file_size, pdfMsgId, time.time()),
            )
            logger.debug(f"✅ Conversion download complete: {downloadLoc}")
            
            if os.path.getsize(downloadLoc) != message.document.file_size:
                return await work(message, "delete", True)

            await pdfMsgId.edit(CHUNK["takeTime"], reply_markup=tBTN)

            isError = False
            if fileExt.lower() in pymu2PDF:
                FILE_NAME, FILE_CAPT, THUMBNAIL = await thumbName(
                    message, f"{fileNm}.pdf"
                )
                isError = await pymuConvert2PDF(cDIR, pdfMsgId, input_file, lang_code)

            elif fileExt.lower() in cnvrt_api_2PDF:
                FILE_NAME, FILE_CAPT, THUMBNAIL, API = await thumbName(
                    message, f"{fileNm}.pdf", getAPI=True
                )
                API = API if API else settings.CONVERT_API
                isError = await cvApi2PDF(cDIR, pdfMsgId, input_file, lang_code, API)

            elif fileExt.lower() in wordFiles:
                FILE_NAME, FILE_CAPT, THUMBNAIL = await thumbName(
                    message, f"{fileNm}.pdf"
                )
                isError = await word2PDF(cDIR, pdfMsgId, input_file, lang_code)

            if not isError:
                return await work(message, "delete", True)

            if images.PDF_THUMBNAIL != THUMBNAIL:
                location = await bot_client.download_media(
                    message=THUMBNAIL, file_name=f"{cDIR}/thumb.jpeg"
                )
                THUMBNAIL = await formatThumb(location)

            await pdfMsgId.edit(CHUNK["upFile"], reply_markup=tBTN)
            await message.reply_chat_action(enums.ChatAction.UPLOAD_DOCUMENT)
            logFile = await message.reply_document(
                file_name=FILE_NAME,
                document=open(f"{cDIR}/outPut.pdf", "rb"),
                caption=CHUNK["fromFile"].format(fileExt, "pdf") + f"\n\n{FILE_CAPT}",
                quote=True,
                progress=_progress,
                progress_args=(pdfMsgId, time.time()),
                thumb=THUMBNAIL,
                reply_markup=await createBUTTON(btn={"👍": "try+", "👎": "try-"}) if fileExt.lower() in pymu2PDF else None,
            )
            await pdfMsgId.delete()
            await work(message, "delete", True)

        else:
            return await message.reply_text(CHUNK["unsupport"], quote=True)

        # Log action completed
        from core.ledger import log
        await log.newUser(bot_client, message, lang_code, False)
    except Exception as e:
        logger.error(f"Error in documents_receiver: {e}", exc_info=True)
        await work(message, "delete", True)
