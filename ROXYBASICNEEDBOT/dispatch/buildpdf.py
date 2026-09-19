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

import fitz
import os
import shutil
import time
from pyrogram import Client as RoxyBot, filters, enums
from pyrogram.types import CallbackQuery, Message, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton
from core.nexus import settings, images as im
from core.corestate import dataBASE, myID
from scriptorium import PDF
from dispatch.photobox import HD
from sentinel import getLang, translate, createBUTTON, formatThumb, thumbName, cbPRO, ask
from tracer import logger

if dataBASE.MONGODB_URI:
    from ledger.safebox import db

@RoxyBot.on_callback_query(filters.regex("^generate"))
async def _GEN(bot_client: RoxyBot, callbackQuery: CallbackQuery):
    logger.debug(f"🔘 Generate button clicked by user {callbackQuery.from_user.id}")
    try:
        chat_id = callbackQuery.message.chat.id
        lang_code = await getLang(chat_id)
        
        from sentinel import header
        if await header(bot_client, callbackQuery, lang_code=lang_code):
            return

        images_list = PDF.get(chat_id)
        if isinstance(PDF.get(chat_id), list):
            pgnmbr = len(PDF[chat_id])
            del PDF[chat_id]
        else:
            pgnmbr = 0

        if (not (images_list) and chat_id not in HD) or (
            chat_id in HD and len(HD[chat_id]) == 1
        ):
            tTXT, tBTN = await translate(
                text="GENERATE['noImages']", lang_code=lang_code
            )
            return await callbackQuery.answer(tTXT)
        await callbackQuery.answer()

        if callbackQuery.data[-3:] == "REN":
            tTXT, tBTN = await translate(
                text="GENERATE['getFileNm']", lang_code=lang_code
            )
            fileName = await ask(
                bot_client,
                chat_id=chat_id,
                text=tTXT,
                reply_to_message_id=callbackQuery.message.id,
                reply_markup=ForceReply(True),
            )
            if (not fileName or not fileName.text) or len(fileName.text) > 50:
                fileName = f"{chat_id}.pdf"
            else:
                if fileName.text[-4:].lower() != ".pdf":
                    fileName = fileName.text + ".pdf"
                else:
                    fileName = fileName.text
        else:
            fileName = f"{chat_id}.pdf"

        tTXT, tBTN = await translate(
            text="GENERATE['geting']",
            button="GENERATE['getingCB']",
            lang_code=lang_code,
        )
        if not images_list:
            pgnmbr = len(HD[chat_id]) - 1
            
        gen = await callbackQuery.message.reply_text(
            tTXT.format(fileName, pgnmbr), reply_markup=tBTN, quote=False
        )

        filePath = f"work/{chat_id}.pdf"
        os.makedirs("work", exist_ok=True)
        
        if chat_id not in HD:
            images_list[0].save(filePath, save_all=True, append_images=images_list[1:])
        else:
            tTXT_dl, tBTN_dl = await translate(
                text="GENERATE['currDL']",
                button="GENERATE['getingCB']",
                lang_code=lang_code,
            )
            os.makedirs(f"work/{chat_id}", exist_ok=True)
            for i, ID in enumerate(HD[chat_id]):
                if i == 0:
                    continue
                try:
                    await gen.edit(tTXT_dl.format(i, len(HD[chat_id])), reply_markup=tBTN_dl)
                except Exception:
                    pass
                await bot_client.download_media(
                    message=ID, file_name=f"work/{chat_id}/{i}.jpg"
                )

            imgList = [
                os.path.join(f"work/{chat_id}", file)
                for file in os.listdir(f"work/{chat_id}")
            ]
            imgList.sort(key=os.path.getctime)

            await gen.edit(tTXT.format(fileName, pgnmbr), reply_markup=tBTN)

            with fitz.open() as doc:
                for img in imgList:
                    try:
                        with fitz.open(img) as hdIMG:
                            rect = hdIMG[0].rect
                            pdfbytes = hdIMG.convert_to_pdf()
                            imgPDF = fitz.open("pdf", pdfbytes)
                            page = doc.new_page(width=rect.width, height=rect.height)
                            page.show_pdf_page(rect, imgPDF, 0)
                    except Exception:
                        pass
                try:
                    await bot_client.delete_messages(
                        chat_id=chat_id, message_ids=HD[chat_id][0]
                    )
                except Exception:
                    pass
                doc.save(filePath, deflate_images=True)
                del HD[chat_id]

        FILE_NAME, FILE_CAPT, THUMBNAIL = await thumbName(
            callbackQuery.message, fileName
        )
        if im.PDF_THUMBNAIL != THUMBNAIL:
            location = await bot_client.download_media(
                message=THUMBNAIL, file_name=f"{callbackQuery.message.id}.jpeg"
            )
            THUMBNAIL = await formatThumb(location)

        tTXT_up, tBTN_up = await translate(
            button="PROGRESS['upFileCB']", lang_code=lang_code
        )
        await gen.edit_reply_markup(tBTN_up)

        await callbackQuery.message.reply_chat_action(enums.ChatAction.UPLOAD_DOCUMENT)
        tTXT_up_msg, _ = await translate(
            text="GENERATE['geting']", lang_code=lang_code
        )
        logFile = await callbackQuery.message.reply_document(
            document=filePath,
            caption=f"{tTXT_up_msg.format(fileName, pgnmbr)}\n\n{FILE_CAPT}",
            file_name=FILE_NAME,
            thumb=THUMBNAIL,
            progress=cbPRO,
            progress_args=(gen, 0, "UPLOADED", True),
        )
        await gen.delete()
        
        if os.path.exists(f"work/{chat_id}"):
            shutil.rmtree(f"work/{chat_id}")
        try:
            os.remove(location)
        except Exception:
            pass
            
        from core.ledger import log
        await log.newUser(bot_client, callbackQuery.message, lang_code, False)
    except Exception as e:
        logger.error(f"Error in image-to-PDF builder: {e}", exc_info=True)
        try:
            tTXT_err, tBTN_err = await translate(
                text="DOCUMENT['error']",
                button="PDF_MESSAGE['errorCB']",
                lang_code=lang_code,
            )
            await gen.edit(tTXT_err.format(e), reply_markup=tBTN_err)
        except Exception:
            pass
        try:
            if os.path.exists(f"work/{chat_id}"):
                shutil.rmtree(f"work/{chat_id}")
            if chat_id in HD:
                del HD[chat_id]
        except Exception:
            pass
