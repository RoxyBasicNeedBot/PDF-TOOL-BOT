# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

media = {}

import fitz, os
from PIL import Image
from tracer import tracer, logger
from asyncio import sleep
from pyrogram import enums
from pyrogram.types import InputMediaPhoto as PyroInputMediaPhoto
from scriptorium import roxyTeleBot
from sentinel import *
from telebot.types import InputMediaPhoto


async def previewPDF(
    input_file: str, cDIR: str, editMessage, cancel, callbackQuery
) -> (bool, str):
    try:
        with fitz.open(input_file) as iNPUT:

            if iNPUT.page_count <= 10:
                preview = list(range(1, iNPUT.page_count + 1))
            else:
                preview = (
                    [1, 2, 3]
                    + list(range(iNPUT.page_count // 2 - 1, iNPUT.page_count // 2 + 2))
                    + list(range(iNPUT.page_count - 2, iNPUT.page_count + 1))
                )

            pdfMetaData = (
                "".join(
                    f"`{i} : {iNPUT.metadata[i]}`\n"
                    for i in iNPUT.metadata
                    if iNPUT.metadata[i] != ""
                )
                if iNPUT.metadata
                else ""
            )

            try:
                await editMessage.edit(
                    text=f"`𝚏𝚎𝚝𝚌𝚑𝚒𝚗𝚐 𝚙𝚊𝚐𝚎𝚜: {preview}` 🙇", reply_markup=cancel
                )
            except Exception as edit_err:
                logger.debug(f"⚠️ Could not edit message (fetching pages): {edit_err}")
            
            mat = fitz.Matrix(2, 2)
            os.makedirs(f"{cDIR}/pgs", exist_ok=True)
            for pageNo in preview:
                pix = iNPUT.load_page(int(pageNo) - 1).get_pixmap(matrix=mat)
                with open(f"{cDIR}/pgs/{pageNo}.jpg", "wb") as f:
                    pix.save(f)

            directory = f"{cDIR}/pgs"
            imag = [os.path.join(directory, file) for file in os.listdir(directory)]
            imag.sort(key=os.path.getctime)

            pyro_media = []
            for idx, file in enumerate(imag):
                if os.path.getsize(file) >= 1000000:
                    try:
                        picture = Image.open(file)
                        picture.save(file, "JPEG", optimize=True, quality=85)
                    except Exception as img_err:
                        logger.warning(f"Could not compress preview image {file}: {img_err}")
                if idx == 0:
                    pyro_media.append(PyroInputMediaPhoto(file, caption=f"`𝚙𝚊𝚐𝚎𝚜: {preview}`\n\n{pdfMetaData}"))
                else:
                    pyro_media.append(PyroInputMediaPhoto(file))

            try:
                await editMessage.edit(
                    text=f"`𝚞𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚊𝚕𝚋𝚞𝚖: {preview}` 🙇", reply_markup=cancel
                )
            except Exception as edit_err:
                logger.debug(f"⚠️ Could not edit message (uploading album): {edit_err}")
            
            if await work(callbackQuery, "check", False):
                await callbackQuery.message.reply_chat_action(
                    enums.ChatAction.UPLOAD_PHOTO
                )
                try:
                    await callbackQuery.message.reply_media_group(pyro_media, quote=True)
                    logger.debug(f"✅ Preview media group sent successfully via Pyrogram reply_media_group!")
                except Exception as send_err:
                    logger.warning(f"⚠️ reply_media_group failed, sending via send_media_group: {send_err}")
                    try:
                        await callbackQuery.message._client.send_media_group(
                            chat_id=callbackQuery.message.chat.id,
                            media=pyro_media
                        )
                        logger.debug(f"✅ Preview media group sent successfully via Pyrogram send_media_group!")
                    except Exception as e2:
                        logger.warning(f"⚠️ pyrogram send_media_group failed, trying roxyTeleBot fallback: {e2}")
                        tb_media = []
                        handles = []
                        for idx, file in enumerate(imag):
                            h = open(file, "rb")
                            handles.append(h)
                            if idx == 0:
                                tb_media.append(InputMediaPhoto(media=h, caption=f"`𝚙𝚊𝚐𝚎𝚜: {preview}`\n\n{pdfMetaData}", parse_mode="Markdown"))
                            else:
                                tb_media.append(InputMediaPhoto(media=h))
                        try:
                            await roxyTeleBot.send_media_group(callbackQuery.message.chat.id, tb_media)
                            logger.debug(f"✅ Preview media group sent successfully via roxyTeleBot fallback!")
                        finally:
                            for h in handles:
                                try:
                                    h.close()
                                except Exception:
                                    pass

        return "finished", "finished"

    except Exception as Error:
        logger.error(f"🐞 {input_file}: {Error}", exc_info=True)
        return False, str(Error)
