# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

from modules import *
from sentinel import *
from .ops import *
from core.nexus import images


@RoxyBot.on_callback_query(filters.regex("processAIO"))
async def __index__(bot, callbackQuery):
    try:
        data = callbackQuery.data[1:]
        lang_code = await util.getLang(callbackQuery.message.chat.id)
        reply_msg = await ensure_reply_to_message(bot, callbackQuery)

        if await render.header(bot, callbackQuery, lang_code=lang_code):
            return

        CHUNK, _ = await util.translate(
            text="INDEX", button="INDEX['button']", lang_code=lang_code
        )

        if not reply_msg or not reply_msg.document:
            await work.work(callbackQuery, "delete", False)
            return await callbackQuery.message.reply_text(
                "#old_queue 💔\n\n`try by sending new file`", reply_markup=_, quote=True
            )

        inPassword, outName, watermark, outPassword = callbackQuery.message.text.split(
            "•"
        )[1::2]
        buttons = callbackQuery.message.reply_markup.inline_keyboard
        callback = [
            element.callback_data
            for button in buttons
            for index, element in enumerate(button, start=1)
            if index % 2 == 0
        ]
        all_data = [
            "{F}" if element.endswith("{F}") else element.split("|")[-1]
            for element in callback
        ][:-1]

        WORKS = {
            "metadata": True if all_data[0] == "{T}" else False,
            "preview": True if all_data[1] == "{T}" else False,
            "text": all_data[3] if all_data[3] != "{F}" else False,
            "rotate": all_data[4] if all_data[4] != "{F}" else False,
            "format": all_data[5] if all_data[5] != "{F}" else False,
            "watermark": watermark
            if all_data[7] != "{F}" and watermark != "None"
            else False,
            "compress": True if all_data[2] == "{T}" else False,
            "encrypt": outPassword
            if all_data[6] != "{F}" and outPassword != "None"
            else False,
            "rename": outName if all_data[8] != "{F}" and outName != "None" else False,
        }
        DEFAULT_WORK = {
            "metadata": False,
            "preview": False,
            "compress": False,
            "text": False,
            "rotate": False,
            "format": False,
            "encrypt": False,
            "watermark": False,
            "rename": False,
        }

        if DEFAULT_WORK == WORKS:
            return await callbackQuery.answer("atleast add one work.. 💔")

        # create a brand new directory to store all of your important user data
        cDIR = await work.work(callbackQuery, "create", False)
        if not cDIR:
            return await callbackQuery.answer(CHUNK["inWork"])
        await callbackQuery.answer(CHUNK["process"])

        dlMSG = await callbackQuery.message.reply_text(
            CHUNK["download"], reply_markup=_, quote=True
        )

        logger.debug(f"⬇️ Starting AIO download to: {cDIR}/inPut.pdf")
        input_file = await bot.download_media(
            message=reply_msg.document.file_id,
            file_name=f"{cDIR}/inPut.pdf",
            progress=render.progress,
            progress_args=(
                reply_msg.document.file_size,
                dlMSG,
                time.time(),
            ),
        )
        logger.debug(f"✅ AIO Download complete. File saved as: {input_file}")

        await dlMSG.edit(text=CHUNK["completed"], reply_markup=_)

        # The program checks the size of the file and the file
        # on the server to avoid errors when canceling the download
        if (
            os.path.getsize(input_file)
            != reply_msg.document.file_size
        ):
            return await work.work(callbackQuery, "delete", False)

        if inPassword != "None":
            isSuccess, output_file = await decryptPDF.decryptPDF(
                input_file=input_file, cDIR=cDIR, password=inPassword
            )
            if isSuccess:
                os.remove(input_file)
                os.rename(output_file, input_file)
            else:
                return await dlMSG.edit(
                    text=CHUNK["decrypt_error"].format(output_file), reply_markup=_
                )

        for job, work_info in WORKS.items():
            await dlMSG.edit(text=CHUNK["aio"].format(job.upper()), reply_markup=_)

            work_in_this_loop = False

            if job == "metadata" and work_info:
                isSuccess, output_file = await metadataPDF.metadataPDF(
                    input_file=input_file, cDIR=cDIR, message=dlMSG
                )
                await callbackQuery.message.reply_text(output_file, quote=True)

            elif job == "preview" and work_info:
                isSuccess, output_file = await previewPDF.previewPDF(
                    input_file=input_file,
                    cDIR=cDIR,
                    editMessage=dlMSG,
                    cancel=_,
                    callbackQuery=callbackQuery,
                )
            elif job == "text" and work_info:
                isSuccess, output_file = await textPDF.textPDF(
                    input_file=input_file,
                    cDIR=cDIR,
                    data=f"text{WORKS['text'][0].upper()}",
                )
                await callbackQuery.message.reply_document(
                    file_name=output_file.split("/")[-1],
                    quote=True,
                    document=output_file,
                    progress=render._progress,
                    progress_args=(dlMSG, time.time()),
                )

            elif job == "rotate" and work_info:
                isSuccess, output_file = await rotatePDF.rotatePDF(
                    input_file=input_file, angle=all_data[4].lower(), cDIR=cDIR
                )
                work_in_this_loop = True

            elif job == "format" and work_info:

                if work_info == "format1":
                    isSuccess, output_file = await formatPDF.formatPDF(
                        input_file=input_file, cDIR=cDIR
                    )
                    work_in_this_loop = True

                elif work_info == "format2v":
                    isSuccess, output_file = await twoPagesToOne.twoPagesToOne(
                        input_file=input_file, cDIR=cDIR
                    )
                    work_in_this_loop = True

                elif work_info == "format2h":
                    isSuccess, output_file = await twoPagesToOneH.twoPagesToOneH(
                        input_file=input_file, cDIR=cDIR
                    )
                    work_in_this_loop = True

                elif work_info == "format3v":
                    isSuccess, output_file = await threePagesToOne.threePagesToOne(
                        input_file=input_file, cDIR=cDIR
                    )
                    work_in_this_loop = True

                elif work_info == "format3h":
                    isSuccess, output_file = await threePagesToOneH.threePagesToOneH(
                        input_file=input_file, cDIR=cDIR
                    )
                    work_in_this_loop = True

                elif work_info == "format4":
                    isSuccess, output_file = await combinePages.combinePages(
                        input_file=input_file, cDIR=cDIR
                    )
                    work_in_this_loop = True

            elif job == "encrypt" and work_info:
                isSuccess, output_file = await encryptPDF.encryptPDF(
                    input_file=input_file, password=outPassword, cDIR=cDIR
                )
                work_in_this_loop = True

            elif job == "watermark" and work_info:
                isSuccess, output_file = await watermark45.watermarkPDF(
                    input_file=input_file, cDIR=cDIR, watermark=watermark
                )
                work_in_this_loop = True

            if work_in_this_loop:
                os.remove(input_file)
                os.rename(output_file, input_file)

        if WORKS["compress"]:
            output_file = output_file if work_in_this_loop else input_file
            isSuccess, output_file = await compressPDF.compressPDF(
                input_file=output_file, cDIR=cDIR
            )
            work_in_this_loop = True

        if inPassword == "None":
            for _upload in all_data[2:]:
                if _upload != "{F}":
                    break
            else:
                await dlMSG.delete()
                completed = await util.createBUTTON(btn=CHUNK["_completed"])
                await callbackQuery.message.reply_text(
                    text=CHUNK["finished"], reply_markup=completed, quote=True
                )
                return await work.work(callbackQuery, "delete", False)

        # getting thumbnail
        file_name_ref = msg.document.file_name if (msg and msg.document) else (reply_msg.document.file_name if reply_msg and reply_msg.document else "output.pdf")
        FILE_NAME, FILE_CAPT, THUMBNAIL = await fncta.thumbName(
            callbackQuery.message,
            file_name_ref
            if all_data[8] == "{F}"
            else f"{outName}.pdf",
        )
        if images.PDF_THUMBNAIL != THUMBNAIL:
            location = await bot.download_media(
                message=THUMBNAIL, file_name=f"{cDIR}/temp.jpeg"
            )
            THUMBNAIL = await formatThumb(location)

        await callbackQuery.message.reply_chat_action(enums.ChatAction.UPLOAD_DOCUMENT)
        await callbackQuery.message.reply_document(
            file_name=FILE_NAME,
            quote=True,
            document=output_file if work_in_this_loop else input_file,
            thumb=THUMBNAIL,
            progress=render._progress,
            progress_args=(dlMSG, time.time()),
        )

        await dlMSG.delete()
        completed = await util.createBUTTON(btn=CHUNK["_completed"])
        await callbackQuery.message.reply_text(
            text=CHUNK["finished"], reply_markup=completed, quote=True
        )
        await work.work(callbackQuery, "delete", False)

    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        await work.work(callbackQuery, "delete", False)
