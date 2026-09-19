# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import os
import time
import asyncio
from PIL import Image
from pyrogram import Client as RoxyBot, filters, enums
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatMemberStatus
from core.nexus import settings, images, dm
from core.corestate import invite_link, myID, BANNED_USR_DB, DATA
from sentinel import work, getLang, translate, createBUTTON, formatThumb, thumbName, progress, _progress, gSF
from scriptorium import PDF
from tracer import logger

try:
    import fitz
    pymuSupport = True
except Exception:
    pymuSupport = False

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
                pdf.save(f"{cDIR}/outPut.pdf", garbage=4, deflate=True)
        return True
    except Exception as e:
        tTXT, tBTN = await translate(text="DOCUMENT['error']", lang_code=lang_code)
        await edit.edit(text=tTXT.format(e), reply_markup=await createBUTTON(btn={"👍": "try+", "👎": "try-"}))
        return False

async def cvApi2PDF(cDIR, edit, input_file, lang_code, API):
    try:
        import convertapi
        convertapi.api_secret = API
        fileNm, fileExt = os.path.splitext(input_file)
        convertapi.convert("pdf", {"File": f"{input_file}"}, from_format=fileExt[1:]).save_files(f"{cDIR}/outPut.pdf")
        return True
    except Exception as e:
        tTXT, tBTN = await translate(text="DOCUMENT['error']", lang_code=lang_code)
        await edit.edit(tTXT.format(e))
        return False

async def word2PDF(cDIR, edit, input_file, lang_code):
    try:
        if not wordSupport:
            raise Exception("Aspose words not installed")
        doc = word.Document(input_file)
        doc.save(f"{cDIR}/outPut.pdf")
        return True
    except Exception as e:
        tTXT, tBTN = await translate(text="DOCUMENT['error']", lang_code=lang_code)
        await edit.edit(tTXT.format(e))
        return False

async def verify_forcesub_group(bot: RoxyBot, user_id: int, lang_code: str, message: Message) -> bool:
    if len(invite_link) != 0:
        _not_joined = False
        from pyrogram.errors import UserNotParticipant
        for ch_info in invite_link:
            try:
                userStatus = await bot.get_chat_member(int(ch_info["channel_id"]), user_id)
                if userStatus.status == ChatMemberStatus.BANNED:
                    _not_joined = True
                    break
            except UserNotParticipant:
                _not_joined = True
                break
            except Exception as e:
                logger.error(f"Error checking forcesub member in group channel {ch_info['channel_id']} for user {user_id}: {e}")
                pass
        if _not_joined:
            tTXT, _ = await translate(text="BAN['Force']", asString=True, lang_code=lang_code)
            buttons = []
            for idx, ch_info in enumerate(invite_link):
                buttons.append([InlineKeyboardButton(f"🌟 JOIN CHANNEL {idx + 1} 🌟", url=ch_info["invite_link"])])
            buttons.append([InlineKeyboardButton("♻️ Refresh ♻️", callback_data="refresh")])
            await message.reply_photo(
                photo=images.WELCOME_PIC,
                quote=True,
                reply_markup=InlineKeyboardMarkup(buttons),
                caption=tTXT.format(message.from_user.first_name, message.from_user.id)
            )
            return False
    return True

@RoxyBot.on_message(filters.group & filters.incoming & filters.command(["analyse", "check", "roxybasicneedbot"]))
async def gDOC(bot: RoxyBot, message: Message) -> None:
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        lang_code = await getLang(message.chat.id)
        CHUNK, _ = await translate(text="gDOCUMENT", lang_code=lang_code)

        status = await bot.get_chat_member(message.chat.id, myID[0].id)
        if status.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            return await message.reply(CHUNK["admin"], quote=True)

        if not message.reply_to_message or not (message.reply_to_message.document or message.reply_to_message.photo):
            return await message.reply(CHUNK["notDOC"], quote=True)

        if message.from_user.id in BANNED_USR_DB:
            return

        if not await verify_forcesub_group(bot, message.from_user.id, lang_code, message):
            return

        if message.from_user.id not in dm.ADMINS:
            isAdmin = await bot.get_chat_member(message.chat.id, message.from_user.id)
            if settings.ONLY_GROUP_ADMIN and isAdmin.status != ChatMemberStatus.ADMINISTRATOR:
                return await message.reply(CHUNK["Gadmin"], quote=True)
            elif isAdmin.status != ChatMemberStatus.ADMINISTRATOR:
                if message.from_user.id != message.reply_to_message.from_user.id:
                    return await message.reply(CHUNK["adminO"])

        try:
            await message.delete()
        except Exception:
            pass

        logFile = None

        if message.reply_to_message.photo:
            imageReply = await message.reply_to_message.reply_text(CHUNK["dlImage"], quote=True)
            if not isinstance(PDF.get(message.chat.id), list):
                PDF[message.chat.id] = []
            
            loc = await message.reply_to_message.download(f"work/{message.chat.id}.jpg")
            img = Image.open(loc).convert("RGB")
            PDF[message.chat.id].append(img)
            tBTN = await createBUTTON(CHUNK["generate"])
            
            return await imageReply.edit(
                CHUNK["imageAdded"].format(len(PDF[message.chat.id]), f"{message.chat.id}") + f"\n\n👤:   {message.from_user.mention}",
                reply_markup=tBTN
            )

        fileNm, fileExt = os.path.splitext(message.reply_to_message.document.file_name)

        if (message.from_user.id not in dm.ADMINS) and MAX_FILE_SIZE and message.reply_to_message.document.file_size >= int(MAX_FILE_SIZE_IN_kiB):
            tBTN = await createBUTTON(CHUNK["bigCB"])
            return await message.reply_photo(
                photo=images.BIG_FILE,
                reply_markup=tBTN,
                caption=CHUNK["big"].format(MAX_FILE_SIZE, MAX_FILE_SIZE) + f"\n\n👤:   {message.from_user.mention}"
            )

        elif fileExt.lower() in img2pdf:
            try:
                imageDocReply = await message.reply_to_message.reply_text(CHUNK["dlImage"], quote=True)
                if not isinstance(PDF.get(message.chat.id), list):
                    PDF[message.chat.id] = []
                
                await message.reply_to_message.download(f"work/{message.chat.id}.jpg")
                img = Image.open(f"work/{message.chat.id}.jpg").convert("RGB")
                PDF[message.chat.id].append(img)
                
                tBTN = await createBUTTON(CHUNK["generate"])
                await imageDocReply.edit(
                    CHUNK["imageAdded"].format(len(PDF[message.chat.id]), f"{message.chat.id}") + f"\n\n👤:   {message.from_user.mention}",
                    reply_markup=tBTN
                )
            except Exception as e:
                return await imageDocReply.edit(CHUNK["error"].format(e))

        elif fileExt.lower() == ".pdf":
            logFile = message.reply_to_message
            pdfMsgId = await message.reply_to_message.reply_text(CHUNK["process"], quote=True)
            await asyncio.sleep(0.3)
            await pdfMsgId.edit(CHUNK["process"] + ".")
            await asyncio.sleep(0.3)
            
            tBTN = await createBUTTON(CHUNK["replyCB"])
            await pdfMsgId.edit(
                text=CHUNK["reply"].format(
                    message.reply_to_message.document.file_name,
                    await gSF(message.reply_to_message.document.file_size)
                ) + f"\n\n👤:   {message.from_user.mention}",
                reply_markup=tBTN
            )

        elif await work(message, "check", True):
            # edits refresh
            tBTN = await createBUTTON({CHUNK["refresh"].get("♻️ Refresh ♻️", "♻️ Refresh ♻️"): "refresh"})
            return await message.reply_to_message.reply_text(CHUNK["inWork"], reply_markup=tBTN, quote=True)

        elif (fileExt.lower() in pymu2PDF) or (fileExt.lower() in cnvrt_api_2PDF) or (fileExt.lower() in wordFiles):
            from ledger.safebox import db
            if (fileExt.lower() in cnvrt_api_2PDF) and (
                (not DATA.get(message.chat.id, 0) or (DATA.get(message.chat.id, 0) and not DATA.get(message.chat.id, 0)[0]))
                and settings.CONVERT_API is False
            ):
                return await message.reply_text(CHUNK["noAPI"], quote=True)

            if (fileExt.lower() in wordFiles) and not wordSupport:
                return await message.reply_text(CHUNK["useDOCKER"], quote=True)
            
            cDIR = await work(message, "create", True)
            tBTN = await createBUTTON(CHUNK["cancelCB"])
            pdfMsgId = await message.reply_to_message.reply_text(CHUNK["download"], reply_markup=tBTN, quote=True)

            # Refresh the message to get the latest file reference and access hashes
            msg = await bot.get_messages(
                chat_id=message.chat.id,
                message_ids=message.reply_to_message.id
            )
            input_file = f"{cDIR}/input_file{fileExt}"
            downloadLoc = await bot.download_media(
                message=msg,
                file_name=input_file,
                progress=progress,
                progress_args=(msg.document.file_size, pdfMsgId, time.time())
            )

            if os.path.getsize(downloadLoc) != msg.document.file_size:
                return await work(message, "delete", True)

            await pdfMsgId.edit(CHUNK["takeTime"], reply_markup=tBTN)

            isError = False
            if fileExt.lower() in pymu2PDF:
                FILE_NAME, FILE_CAPT, THUMBNAIL = await thumbName(message, f"{fileNm}.pdf")
                isError = await pymuConvert2PDF(cDIR, pdfMsgId, input_file, lang_code)

            elif fileExt.lower() in cnvrt_api_2PDF:
                FILE_NAME, FILE_CAPT, THUMBNAIL, API = await thumbName(message, f"{fileNm}.pdf", getAPI=True)
                API = API if API else settings.CONVERT_API
                isError = await cvApi2PDF(cDIR, pdfMsgId, input_file, lang_code, API)

            elif fileExt.lower() in wordFiles:
                FILE_NAME, FILE_CAPT, THUMBNAIL = await thumbName(message, f"{fileNm}.pdf")
                isError = await word2PDF(cDIR, pdfMsgId, input_file, lang_code)

            if not isError:
                return await work(message, "delete", True)

            if images.PDF_THUMBNAIL != THUMBNAIL:
                location = await bot.download_media(message=THUMBNAIL, file_name=f"{cDIR}/THUMB.jpeg")
                THUMBNAIL = await formatThumb(location)

            await pdfMsgId.edit(CHUNK["upFile"], reply_markup=tBTN)
            await message.reply_chat_action(enums.ChatAction.UPLOAD_DOCUMENT)

            logFile = await message.reply_to_message.reply_document(
                file_name=FILE_NAME,
                document=open(f"{cDIR}/outPut.pdf", "rb"),
                caption=CHUNK["fromFile"].format(fileExt, "pdf") + f"\n\n{FILE_CAPT}",
                quote=True,
                progress=_progress,
                progress_args=(pdfMsgId, time.time()),
                thumb=THUMBNAIL,
                reply_markup=await createBUTTON(btn={"👍": "try+", "👎": "try-"}) if fileExt.lower() in pymu2PDF else None
            )
            await pdfMsgId.delete()
            await work(message, "delete", True)

        else:
            return await message.reply_text(CHUNK["unsupport"], quote=True)

        if logFile:
            from core.ledger import log
            await log.newUser(bot, message, lang_code, False)
            
    except Exception as e:
        logger.error(f"Error in group document handler gDOC: {e}", exc_info=True)
        await work(message, "delete", True)

@RoxyBot.on_message(filters.group & filters.incoming & (filters.document | filters.photo))
async def gDOC_auto(bot: RoxyBot, message: Message) -> None:
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        lang_code = await getLang(message.chat.id)
        CHUNK, _ = await translate(text="gDOCUMENT", lang_code=lang_code)

        status = await bot.get_chat_member(message.chat.id, myID[0].id)
        if status.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            return

        if message.from_user.id in BANNED_USR_DB:
            return

        if not await verify_forcesub_group(bot, message.from_user.id, lang_code, message):
            return

        if message.photo:
            imageReply = await message.reply_text(CHUNK["dlImage"], quote=True)
            if not isinstance(PDF.get(message.chat.id), list):
                PDF[message.chat.id] = []
            
            loc = await message.download(f"work/{message.chat.id}.jpg")
            img = Image.open(loc).convert("RGB")
            PDF[message.chat.id].append(img)
            tBTN = await createBUTTON(CHUNK["generate"])
            
            await imageReply.edit(
                CHUNK["imageAdded"].format(len(PDF[message.chat.id]), f"{message.chat.id}") + f"\n\n👤:   {message.from_user.mention}",
                reply_markup=tBTN
            )
            return

        fileNm, fileExt = os.path.splitext(message.document.file_name)
        if fileExt.lower() in img2pdf:
            try:
                imageDocReply = await message.reply_text(CHUNK["dlImage"], quote=True)
                if not isinstance(PDF.get(message.chat.id), list):
                    PDF[message.chat.id] = []
                
                loc = await message.download(f"work/{message.chat.id}.jpg")
                img = Image.open(loc).convert("RGB")
                PDF[message.chat.id].append(img)
                tBTN = await createBUTTON(CHUNK["generate"])
                
                await imageDocReply.edit(
                    CHUNK["imageAdded"].format(len(PDF[message.chat.id]), f"{message.chat.id}") + f"\n\n👤:   {message.from_user.mention}",
                    reply_markup=tBTN
                )
            except Exception as e:
                try:
                    await imageDocReply.edit(CHUNK["error"].format(e))
                except Exception:
                    pass

    except Exception as e:
        logger.error(f"Error in automatic group document handler: {e}", exc_info=True)