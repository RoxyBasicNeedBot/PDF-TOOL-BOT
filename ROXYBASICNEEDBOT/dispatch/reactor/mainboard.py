# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

# ┌─────────────────────────────────────────────────────────────┐
# │                    𝕽𝕺𝕏𝖄•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │  Created by: RoxyBasicNeedBot                               │
# │  GitHub    : https://github.com/RoxyBasicNeedBot            │
# │  Telegram  : https://t.me/roxybasicneedbot1                 │
# │  Website   : https://roxybasicneedbot.unaux.com             │
# │  YouTube   : @roxybasicneedbot                              │
# ├─────────────────────────────────────────────────────────────┘

import os
import shutil
import time
import asyncio
from pyrogram import Client as RoxyBot, filters, enums
from pyrogram.types import CallbackQuery, Message, InputMediaPhoto, ForceReply
from core.nexus import settings, images
from core.corestate import myID
from sentinel import work, getLang, translate, createBUTTON, formatThumb, thumbName, checkPdf, progress, _progress, cbPRO, header, check_memory_for_file, force_cleanup, caption, ensure_reply_to_message
from tracer import logger

# Import all operations
import dispatch.reactor.ops.pdf_compress as compressPDF
import dispatch.reactor.ops.pdf_encrypt as encryptPDF
import dispatch.reactor.ops.pdf_decrypt as decryptPDF
import dispatch.reactor.ops.pdf_merge as mergePDF
import dispatch.reactor.ops.pdf_split as splitPDF
import dispatch.reactor.ops.pdf_rotate as rotatePDF
import dispatch.reactor.ops.pdf_watermark as watermarkPDF
import dispatch.reactor.ops.pdf_ocr as ocrPDF
import dispatch.reactor.ops.pdf_to_images as pdfToImages
import dispatch.reactor.ops.pdf_to_word as pdfToWord
import dispatch.reactor.ops.pdf_to_excel as pdfToExcel
import dispatch.reactor.ops.pdf_to_ppt as pdfToPPT
import dispatch.reactor.ops.pdf_rename as renamePDF
import dispatch.reactor.ops.pdf_header as pdfHeader
import dispatch.reactor.ops.pdf_footer as pdfFooter
import dispatch.reactor.ops.pdf_stamp as stampPDF
import dispatch.reactor.ops.pdf_bw as blackAndWhitePdf
import dispatch.reactor.ops.pdf_invert as invertPDF
import dispatch.reactor.ops.pdf_zoom as zoomPDF
import dispatch.reactor.ops.pdf_saturate as saturatePDF
import dispatch.reactor.ops.pdf_format as formatPDF
import dispatch.reactor.ops.pdf_2in1 as twoPagesToOne
import dispatch.reactor.ops.pdf_2in1h as twoPagesToOneH
import dispatch.reactor.ops.pdf_3in1 as threePagesToOne
import dispatch.reactor.ops.pdf_3in1h as threePagesToOneH
import dispatch.reactor.ops.pdf_combine as combinePages
import dispatch.reactor.ops.pdf_preview as previewPDF
import dispatch.reactor.ops.pdf_extract as extractPDF
import dispatch.reactor.ops.pdf_archive as zipTarPDF
import dispatch.reactor.ops.pdf_message as messagePDF
import dispatch.reactor.ops.pdf_deeplink as deeplinkPDF
import dispatch.reactor.ops.pdf_striplinks as urlRemover
import dispatch.reactor.ops.pdf_draw as drawPDF
import dispatch.reactor.ops.pdf_deletepage as deletePDFPg
import dispatch.reactor.ops.pdf_metadata as metadataPDF
import dispatch.reactor.ops.pdf_text as textPDF
import dispatch.reactor.ops.pdf_extract as partPDF

# Import new operations
import dispatch.reactor.ops.pdf_sign as signPDF
import dispatch.reactor.ops.pdf_qr as qrPDF
import dispatch.reactor.ops.pdf_redact as redactPDF
import dispatch.reactor.ops.pdf_flatten as flattenPDF
import dispatch.reactor.ops.pdf_bookmarks as bookmarksPDF
import dispatch.reactor.ops.pdf_pagenum as pagenumPDF

@RoxyBot.on_callback_query(filters.regex("^#"))
async def main_callback_router(bot_client: RoxyBot, callbackQuery: CallbackQuery):
    logger.debug(f"🔘 main_callback_router: {callbackQuery.data}")
    try:
        chat_id = callbackQuery.message.chat.id
        lang_code = await getLang(chat_id)
        
        reply_msg = await ensure_reply_to_message(bot_client, callbackQuery)
        logger.debug(f"🔍 ensure_reply_to_message returned: {reply_msg.id if reply_msg else None} (document={reply_msg.document.file_name if reply_msg and getattr(reply_msg, 'document', None) else None})")

        # Check ownership and permissions
        if await header(bot_client, callbackQuery, lang_code=lang_code):
            logger.warning(f"🛑 header check blocked execution for callback {callbackQuery.data} (user={callbackQuery.from_user.id})")
            return

        data = callbackQuery.data[1:] # strip '#' prefix
        CHUNK, _ = await translate(text="INDEX", lang_code=lang_code)

        # File size limits and memory guard pre-checks
        if reply_msg and getattr(reply_msg, "document", None):
            file_size = reply_msg.document.file_size
            max_size_mb = int(settings.MAX_FILE_SIZE) if settings.MAX_FILE_SIZE else 200
            max_size_bytes = max_size_mb * (10**6)
            
            if file_size >= max_size_bytes:
                size_mb = round(file_size / (10**6), 1)
                logger.warning(f"🛑 File too large: {size_mb}MB exceeds {max_size_mb}MB limit")
                await callbackQuery.answer(f"⚠️ File too large ({size_mb}MB). Max: {max_size_mb}MB", show_alert=True)
                return
                
            if not check_memory_for_file(file_size):
                logger.warning(f"🛑 Memory check failed for file size {file_size}")
                await callbackQuery.answer("⚠️ Server busy, please try again in a few minutes.", show_alert=True)
                return

        # Create work directory
        cDIR = await work(callbackQuery, "create", False)
        logger.debug(f"📁 Work directory created/retrieved: {cDIR}")
        if not cDIR:
            logger.warning(f"⚠️ Work directory already exists for {chat_id}, returning inWork")
            return await callbackQuery.answer(CHUNK["inWork"])
        await callbackQuery.answer(CHUNK["process"])

        # Interactive prompts
        password = None
        newName = None
        hfData = None
        mergeId = None
        imageList = None
        watermark = None
        splitData = None
        custom_text = None

        if data in ["decrypt", "encrypt"]:
            notExit, password = await encryptPDF.askPassword(
                bot_client, callbackQuery, question=CHUNK["pyromodASK_1"],
                process="Decryption 🔓" if data == "decrypt" else "Encryption 🔐"
            )
            if not notExit:
                await work(callbackQuery, "delete", False)
                return await callbackQuery.message.reply_text(CHUNK["exit"], quote=True)
                
        elif data == "rename":
            notExit, newName = await renamePDF.askName(bot_client, callbackQuery, question=CHUNK["pyromodASK_2"])
            if not notExit:
                await work(callbackQuery, "delete", False)
                return await callbackQuery.message.reply_text(CHUNK["exit"], quote=True)
                
        elif data in ["header", "footer"]:
            notExit, hfData = await pdfHeader.askText(bot_client, callbackQuery, question=CHUNK["pyromodASK_2"])
            if not notExit:
                await work(callbackQuery, "delete", False)
                return await callbackQuery.message.reply_text(CHUNK["exit"], quote=True)
                
        elif data == "merge":
            notExit, mergeId = await mergePDF.askPDF(bot_client, callbackQuery, question=CHUNK["pyromodASK_3"], size=CHUNK["sizeLoad"])
            if not notExit:
                await work(callbackQuery, "delete", False)
                return await callbackQuery.message.reply_text(CHUNK["exit"], quote=True)
                
        elif (data.startswith("p2img") and not data.endswith("A")) or data.startswith(("split", "deletePg")):
            limit_val = int(callbackQuery.message.text.split("•")[1]) if "•" in callbackQuery.message.text else 1000
            notExit, imageList = await pdfToImages.askimageList(bot_client, callbackQuery, question=CHUNK["pyromodASK_4"], limit=limit_val)
            if not notExit:
                await work(callbackQuery, "delete", False)
                return await callbackQuery.message.reply_text(CHUNK["pdfToImgError"].format(limit_val, imageList), quote=True)
                
        elif data.startswith("wa"):
            question = CHUNK["watermark_txt"] if "txt" in data else (CHUNK["watermark_img"] if "img" in data else CHUNK["watermark_pdf"])
            notExit, watermark = await watermarkPDF.askWatermark(bot_client, callbackQuery, question=question, data=data)
            if not notExit:
                await work(callbackQuery, "delete", False)
                return await callbackQuery.message.reply_text(CHUNK["exit"], quote=True)
                
        elif data == "partPDF":
            limit_val = int(callbackQuery.message.text.split("•")[1]) if "•" in callbackQuery.message.text else None
            notExit, splitData = await partPDF.askPartPdf(bot_client, callbackQuery, question=CHUNK["askImage"], limit=limit_val)
            if not notExit:
                await work(callbackQuery, "delete", False)
                return await callbackQuery.message.reply_text(CHUNK["pdfSplitError"].format(limit_val or "_"), quote=True)

        # ✨ NEW OPERATION INTERACTIVES ↓
        elif data == "sign":
            getName = await ask(bot_client, chat_id=chat_id, text="📝 **Send me your signature text/date:**\n\nExample: `Roxy Bot 13/07/2026`")
            if not getName or not getName.text or getName.text == "/cancel":
                await work(callbackQuery, "delete", False)
                return await callbackQuery.message.reply_text("❌ Action cancelled.", quote=True)
            custom_text = getName.text
            await getName.delete()
            
        elif data == "qr":
            getName = await ask(bot_client, chat_id=chat_id, text="🔗 **Send me the URL to generate and embed QR code:**")
            if not getName or not getName.text or getName.text == "/cancel":
                await work(callbackQuery, "delete", False)
                return await callbackQuery.message.reply_text("❌ Action cancelled.", quote=True)
            custom_text = getName.text
            await getName.delete()
            
        elif data == "redact":
            getName = await ask(bot_client, chat_id=chat_id, text="⬛ **Send me the exact text you want to redact/blackout:**")
            if not getName or not getName.text or getName.text == "/cancel":
                await work(callbackQuery, "delete", False)
                return await callbackQuery.message.reply_text("❌ Action cancelled.", quote=True)
            custom_text = getName.text
            await getName.delete()

        if not reply_msg:
            logger.warning(f"🛑 reply_msg is None right before download for callback {callbackQuery.data}! Deleting work and returning.")
            await work(callbackQuery, "delete", False)
            return await callbackQuery.answer("❌ Original file not found. Please send the document again.", show_alert=True)

        # Download input PDF
        logger.debug(f"💬 Sending download status message to Telegram...")
        dlMSG = await callbackQuery.message.reply_text(CHUNK["download"], quote=True)
        if not dlMSG:
            logger.warning("🛑 dlMSG (reply_text) returned None right before download!")
        logger.debug(f"⬇️ Starting download to: {cDIR}/inPut.pdf (file_id={getattr(reply_msg.document, 'file_id', None)})")
        input_file = await bot_client.download_media(
            message=reply_msg.document.file_id,
            file_name=f"{cDIR}/inPut.pdf",
            progress=progress,
            progress_args=(reply_msg.document.file_size, dlMSG, time.time())
        )
        logger.debug(f"✅ Download complete. File saved as: {input_file}")
        await dlMSG.edit(text=CHUNK["completed"])

        if not os.path.exists(input_file) or os.path.getsize(input_file) != reply_msg.document.file_size:
            return await work(callbackQuery, "delete", False)

        # Check page count
        if "•" not in callbackQuery.message.text:
            checked, number_of_pages = await checkPdf(input_file, callbackQuery, lang_code)
            if data == "decrypt" and checked != "encrypted":
                await work(callbackQuery, "delete", False)
                return await dlMSG.edit(CHUNK["notEncrypt"])
        else:
            number_of_pages = int(callbackQuery.message.text.split("•")[1])

        # Metadata early return removed to be handled by router board
        isSuccess = False
        output_file = None

        # Main operations router board
        if data == "metadata" and "•" in callbackQuery.message.text:
            await work(callbackQuery, "delete", False)
            return await callbackQuery.answer("Metadata is already shown above!", show_alert=True)
            
        if data == "metadata":
            await work(callbackQuery, "delete", False)
            return await dlMSG.delete()
            
        elif data == "rename":
            isSuccess, output_file = await renamePDF.renamePDF(input_file=input_file)
        elif data == "partPDF":
            isSuccess, output_file = await partPDF.partPDF(input_file=input_file, cDIR=cDIR, part=splitData.text)
        elif data == "header":
            isSuccess, output_file = await pdfHeader.pdfHeader(input_file=input_file, cDIR=cDIR, text=hfData.text)
        elif data == "footer":
            isSuccess, output_file = await pdfFooter.pdfFooter(input_file=input_file, cDIR=cDIR, text=hfData.text)
        elif data == "ocr":
            isSuccess, output_file = await ocrPDF.ocrPDF(input_file=input_file, cDIR=cDIR)
        elif data == "baw":
            isSuccess, output_file = await blackAndWhitePdf.blackAndWhitePdf(cDIR=cDIR, input_file=input_file)
        elif data == "urlRemover":
            isSuccess, output_file = await urlRemover.urlRemover(cDIR=cDIR, input_file=input_file)
        elif data == "sat":
            isSuccess, output_file = await saturatePDF.saturatePDF(cDIR=cDIR, input_file=input_file)
        elif data == "1-format":
            isSuccess, output_file = await formatPDF.formatPDF(cDIR=cDIR, input_file=input_file)
        elif data == "2-format-V":
            isSuccess, output_file = await twoPagesToOne.twoPagesToOne(cDIR=cDIR, input_file=input_file)
        elif data == "2-format-H":
            isSuccess, output_file = await twoPagesToOneH.twoPagesToOneH(cDIR=cDIR, input_file=input_file)
        elif data == "3-format-V":
            isSuccess, output_file = await threePagesToOne.threePagesToOne(cDIR=cDIR, input_file=input_file)
        elif data == "3-format-H":
            isSuccess, output_file = await threePagesToOneH.threePagesToOneH(cDIR=cDIR, input_file=input_file)
        elif data == "4-format":
            isSuccess, output_file = await combinePages.combinePages(cDIR=cDIR, input_file=input_file)
        elif data == "draw":
            isSuccess, output_file = await drawPDF.drawPDF(cDIR=cDIR, input_file=input_file)
        elif data == "zoom":
            isSuccess, output_file = await zoomPDF.zoomPDF(cDIR=cDIR, input_file=input_file)
        elif data == "encrypt":
            isSuccess, output_file = await encryptPDF.encryptPDF(cDIR=cDIR, input_file=input_file, password=password.text)
        elif data == "decrypt":
            isSuccess, output_file = await decryptPDF.decryptPDF(cDIR=cDIR, input_file=input_file, password=password.text)
        elif data.startswith("compress"):
            level = data.split("|")[1] if "|" in data else "medium"
            isSuccess, output_file = await compressPDF.compressPDF(cDIR=cDIR, input_file=input_file, returnRatio=True, compression_level=level)
        elif data == "preview":
            isSuccess, output_file = await previewPDF.previewPDF(cDIR=cDIR, input_file=input_file, cancel=_, editMessage=dlMSG, callbackQuery=callbackQuery)
        elif data == "split":
            isSuccess, output_file = await splitPDF.splitPDF(cDIR=cDIR, input_file=input_file, imageList=imageList)
        elif data == "deletePg":
            isSuccess, output_file = await deletePDFPg.deletePDFPg(cDIR=cDIR, input_file=input_file, imageList=imageList)
        elif data == "merge":
            isSuccess, output_file = await mergePDF.mergePDF(cDIR=cDIR, input_file=input_file, text=CHUNK, mergeId=mergeId, bot=bot_client, dlMSG=dlMSG, callbackQuery=callbackQuery)
        elif data == "textM":
            isSuccess, output_file = await messagePDF.messagePDF(cDIR=cDIR, input_file=input_file, text=CHUNK, callbackQuery=callbackQuery, dlMSG=dlMSG)
        elif data == "inv":
            isSuccess, output_file = await invertPDF.invertPDF(cDIR=cDIR, input_file=input_file)
        elif data.startswith("rot"):
            isSuccess, output_file = await rotatePDF.rotatePDF(cDIR=cDIR, input_file=input_file, angle=data)
        elif data.startswith("text") and data != "textM":
            isSuccess, output_file = await textPDF.textPDF(cDIR=cDIR, input_file=input_file, data=data)
        elif data.startswith(("p2img|I", "p2img|D")):
            isSuccess, output_file = await pdfToImages.pdfToImages(cDIR=cDIR, input_file=input_file, text=CHUNK, callbackQuery=callbackQuery, dlMSG=dlMSG, imageList=imageList if not data.endswith("A") else "all")
        elif data.startswith(("p2img|zip", "p2img|tar")):
            isSuccess, output_file = await zipTarPDF.zipTarPDF(cDIR=cDIR, input_file=input_file, text=CHUNK, callbackQuery=callbackQuery, dlMSG=dlMSG, imageList=imageList if not data.endswith("A") else "all")
        elif data.startswith("wa"):
            isSuccess, output_file = await watermarkPDF.watermarkPDF(cDIR=cDIR, input_file=input_file, callbackQuery=callbackQuery, watermark=watermark, text=CHUNK["adding_wa"])
        elif data.startswith("spP"):
            isSuccess, output_file = await stampPDF.stampPDF(cDIR=cDIR, input_file=input_file, data=data)
            
        # ✨ NEW OPERATIONS EXECUTION ↓
        elif data == "sign":
            isSuccess, output_file = await signPDF.pdf_sign(input_file=input_file, cDIR=cDIR, sign_text=custom_text)
        elif data == "qr":
            isSuccess, output_file = await qrPDF.pdf_qr(input_file=input_file, cDIR=cDIR, url=custom_text)
        elif data == "redact":
            isSuccess, output_file = await redactPDF.pdf_redact(input_file=input_file, cDIR=cDIR, redact_text=custom_text)
        elif data == "flatten":
            isSuccess, output_file = await flattenPDF.pdf_flatten(input_file=input_file, cDIR=cDIR)
        elif data == "bookmarks":
            isSuccess, output_file = await bookmarksPDF.pdf_bookmarks(input_file=input_file, cDIR=cDIR)
        elif data == "pagenum":
            isSuccess, output_file = await pagenumPDF.pdf_pagenum(input_file=input_file, cDIR=cDIR)

        # Handle operation output flows
        if isSuccess == "finished":
            await work(callbackQuery, "delete", False)
            return await dlMSG.delete() if not data.startswith(("p2img", "textM")) else ""
            
        elif not isSuccess:
            await work(callbackQuery, "delete", False)
            if data == "decrypt":
                return await dlMSG.edit(text=CHUNK["decrypt_error"].format(output_file))
            elif data.startswith("compress"):
                return await dlMSG.edit(text=CHUNK["cantCompress"])
            return await dlMSG.edit(text=CHUNK["error"].format(output_file))

        # Output properties definitions
        file_name_ref = reply_msg.document.file_name if (reply_msg and getattr(reply_msg, "document", None)) else "output.pdf"
        FILE_NAME, FILE_CAPT, THUMBNAIL = await thumbName(
            callbackQuery.message,
            file_name_ref if data != "rename" else newName.text
        )
        if images.PDF_THUMBNAIL != THUMBNAIL:
            location = await bot_client.download_media(message=THUMBNAIL, file_name=f"{cDIR}/temp.jpeg")
            THUMBNAIL = await formatThumb(location)

        # Generate custom captions
        arg = None
        if data == "encrypt":
            arg = [number_of_pages, password.text]
        elif data == "rename":
            arg = [file_name_ref, newName.text]
        elif data.startswith("compress"):
            arg = isSuccess
            
        _caption = await caption(data=data.split("|")[0] if "|" in data else data, lang_code=lang_code, args=arg)

        try:
            await dlMSG.edit(CHUNK["upload"])
        except Exception:
            pass

        # Update extensions if non-PDF formats
        if data.startswith(("text", "p2img")):
            if data.startswith("p2img"):
                data = data[:-1]
            ext = {"textT": ".txt", "textH": ".html", "textJ": ".json", "p2img|zip": ".zip", "p2img|tar": ".tar"}
            FILE_NAME = FILE_NAME[:-4] + ext.get(data, "")
        # Bookmark output extension mapping
        elif data == "bookmarks":
            FILE_NAME = FILE_NAME[:-4] + ".txt"

        await callbackQuery.message.reply_chat_action(enums.ChatAction.UPLOAD_DOCUMENT)
        _COFFEE, COFFEE = await translate(button="feedbackMsg['button']", lang_code=lang_code)

        if data == "partPDF":
            docs = [os.path.join(cDIR, file) for file in os.listdir(cDIR) if file != "inPut.pdf"]
            docs.sort(key=os.path.getctime)
            for _index, _file in enumerate(docs):
                await callbackQuery.message.reply_document(
                    file_name=FILE_NAME if os.path.splitext(FILE_NAME)[1] else f"{FILE_NAME}_{_index}.pdf",
                    document=_file,
                    thumb=THUMBNAIL,
                    caption=f"`part: {_index+1}`\n\n{FILE_CAPT}",
                    reply_markup=COFFEE if settings.COFFEE else None,
                    progress=_progress,
                    progress_args=(dlMSG, time.time())
                )
            await dlMSG.edit("👇")
            await callbackQuery.message.reply_text("👆", quote=True)
        else:
            await callbackQuery.message.reply_document(
                file_name=FILE_NAME if os.path.splitext(FILE_NAME)[1] else f"{FILE_NAME}.pdf",
                quote=True,
                reply_markup=COFFEE,
                document=output_file,
                thumb=THUMBNAIL,
                caption=f"{_caption}\n\n{FILE_CAPT}",
                progress=_progress,
                progress_args=(dlMSG, time.time())
            )
            await dlMSG.delete()

        await work(callbackQuery, "delete", False)
        force_cleanup()
    except Exception as Error:
        logger.error(f"Error in main_callback_router: {Error}", exc_info=True)
        await work(callbackQuery, "delete", False)
        force_cleanup()
