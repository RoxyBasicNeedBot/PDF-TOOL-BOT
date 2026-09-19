# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz, os
from PIL import Image
import shutil, asyncio
from tracer import tracer, logger
# from pyromod import listen  # Removed
from sentinel.dialogstream import ask as conversation_ask
from sentinel import *
from scriptorium import roxyTeleBot
from pyrogram import filters, enums
from pyrogram.errors import FloodWait
from pyrogram.types import ForceReply
from telebot.types import InputMediaPhoto, InputMediaDocument

media = {}


async def askimageList(bot, callbackQuery, question, limit: int = 1000) -> (bool, list):
    """
    return a list with a specific range of numbers and some specific values from the input

    eg:
        '18:20,4,5,1:3'
        [1, 2, 3, 4, 5, 18, 19, 20]    <---return
    """
    try:
        input_str = await conversation_ask(
            bot,
            chat_id=callbackQuery.from_user.id,
            text=question,
            filters=filters.text,
            reply_to_message_id=callbackQuery.message.id,
            reply_markup=ForceReply(True, "Eg: 7:13 [start:end], 2, 3, 21:27.."),
        )
        if not input_str or not input_str.text:
            return False, "Cancelled or Timeout"
            
        my_list = []
        for elem in input_str.text.split(","):
            try:
                if ":" in elem:
                    start, end = map(int, elem.split(":"))
                    my_list.extend(range(start, end + 1, 1))
                else:
                    my_list.append(int(elem))
            except ValueError:
                pass
        my_list = sorted(set([x for x in my_list if isinstance(x, int) and x <= limit]))
        return (True, my_list) if len(my_list) != 0 else (False, input_str)
    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(e)


async def pdfToImages(
    input_file: str, cDIR: str, callbackQuery, dlMSG, imageList: list, text: str
) -> (bool, str):
    """
     function that allows you to fetch pages from a PDF file. Essentially, this means that you can extract specific pages
     from a large PDF document without having to download the entire file. For example, if you only need a few pages from a
     200-page PDF, you can use this function to extract just those pages and save yourself a lot of time and data usage.
     This feature is especially helpful for users who frequently work with large PDF documents and need to extract specific
     information quickly and efficiently.

    parameter:
        input_file    : Here is the path of the file that the user entered
        cDIR          : This is the location of the directory that belongs to the specific user.
        imageList     : List of page numbers that the user requires
        dlMSG         : Edit Message progress bar
        text          : Edit Message Content [progress]
        callbackQuery : CallbackQuery

    return:
        "finished"    : Return finished when the request is successful
        "finished"    : Return finished when the request is successful
    """
    try:
        cancel = await util.createBUTTON(btn=text["_cancelCB"])
        canceled = await util.createBUTTON(btn=text["_canceledCB"])
        completed = await util.createBUTTON(btn=text["_completed"])

        imageType = "Img" if callbackQuery.data.startswith("#p2img|I") else "Doc"
        
        # Check if input file exists (with retry for potential race conditions)
        for attempt in range(3):
            if os.path.exists(input_file):
                break
            await asyncio.sleep(0.5)  # Wait a bit and retry
        
        if not os.path.exists(input_file):
            logger.error(f"Input file not found after retries: {input_file}")
            return False, "Input file not found. Please try again."
        
        logger.debug(f"📂 Opening PDF: {input_file}, Size: {os.path.getsize(input_file)}")
        with fitz.open(input_file) as doc:
            number_of_pages = doc.page_count
            if callbackQuery.data.endswith("A"):
                imageList = list(range(1, number_of_pages + 1))
            mat = fitz.Matrix(2, 2)
            if len(imageList) >= 11:
                await dlMSG.pin(disable_notification=True, both_sides=True)
            await dlMSG.edit(
                text=text["_total"].format(len(imageList)), reply_markup=cancel
            )

            convertedPages = 0
            for i in range(0, len(imageList), 10):
                pgList = imageList[i : i + 10]
                os.makedirs(f"{cDIR}/pgs", exist_ok=True)

                for pageNo in pgList:
                    if int(pageNo) <= int(number_of_pages):
                        page = doc.load_page(int(pageNo) - 1)
                        pix = page.get_pixmap(matrix=mat)
                    else:
                        continue
                    convertedPages += 1
                    if convertedPages % 5 == 0:
                        if not await work.work(callbackQuery, "check", False):
                            return await dlMSG.edit(
                                text=text["_canceledAT"].format(
                                    convertedPages, len(imageList)
                                ),
                                reply_markup=canceled,
                            )
                    pix.save(f"{cDIR}/pgs/{pageNo}.jpg", jpg_quality=85)

                directory = f"{cDIR}/pgs"
                imag = [os.path.join(directory, file) for file in os.listdir(directory)]
                imag.sort(key=os.path.getctime)

                media[callbackQuery.message.chat.id] = []
                for file in imag:
                    if imageType == "Img" and os.path.getsize(file) >= 1000000:
                        try:
                            picture = Image.open(file)
                            if picture.mode in ("RGBA", "P"):
                                picture = picture.convert("RGB")
                            picture.save(file, "JPEG", optimize=True, quality=75)
                        except Exception as e:
                            logger.error(f"Image compression failed: {e}")
                    
                    if imageType == "Img":
                        media[callbackQuery.message.chat.id].append(
                            InputMediaPhoto(open(file, "rb"))
                        )
                    elif imageType == "Doc":
                        media[callbackQuery.message.chat.id].append(
                            InputMediaDocument(open(file, "rb"))
                        )
                try:
                    await dlMSG.edit(
                        text=text["_upload"].format(convertedPages, len(imageList)),
                        reply_markup=cancel,
                    )
                except Exception:
                    pass

                if imageType == "Img":
                    await callbackQuery.message.reply_chat_action(
                        enums.ChatAction.UPLOAD_PHOTO
                    )
                elif imageType == "Doc":
                    await callbackQuery.message.reply_chat_action(
                        enums.ChatAction.UPLOAD_DOCUMENT
                    )

                # Retry logic for FloodWait errors
                max_retries = 3
                for retry in range(max_retries):
                    try:
                        await roxyTeleBot.send_media_group(
                            callbackQuery.message.chat.id,
                            media[callbackQuery.message.chat.id],
                        )
                        break  # Success, exit retry loop
                    except FloodWait as e:
                        logger.warning(f"FloodWait: waiting {e.value} seconds (retry {retry + 1}/{max_retries})")
                        await asyncio.sleep(e.value + 1)  # Wait required time + 1 buffer
                        # Rebuild media list since file handles may be closed
                        media[callbackQuery.message.chat.id] = []
                        for file in imag:
                            if imageType == "Img":
                                media[callbackQuery.message.chat.id].append(
                                    InputMediaPhoto(open(file, "rb"))
                                )
                            else:
                                media[callbackQuery.message.chat.id].append(
                                    InputMediaDocument(open(file, "rb"))
                                )
                    except Exception as e:
                        # Try to parse FloodWait from string for telebot errors
                        try:
                            wait = int(str(e).rsplit(" ", 1)[1])
                            logger.warning(f"FloodWait (parsed): waiting {wait} seconds")
                            await asyncio.sleep(wait + 1)
                            media[callbackQuery.message.chat.id] = []
                            for file in imag:
                                if imageType == "Img":
                                    media[callbackQuery.message.chat.id].append(
                                        InputMediaPhoto(open(file, "rb"))
                                    )
                                else:
                                    media[callbackQuery.message.chat.id].append(
                                        InputMediaDocument(open(file, "rb"))
                                    )
                        except:
                            logger.error(f"Error sending media group: {e}")
                            raise e
                
                if os.path.exists(f"{cDIR}/pgs"):
                    shutil.rmtree(f"{cDIR}/pgs")
                
                # Add delay between batches to prevent FloodWait
                await asyncio.sleep(10)
            await dlMSG.edit(text=text["finished"], reply_markup=completed)
            return "finished", "finished"
    except Exception as Error:
        try:
            if os.path.exists(f"{cDIR}/pgs"):
                shutil.rmtree(f"{cDIR}/pgs")
        except Exception as cleanup_error:
            logger.debug(f"Could not clean up directory: {cleanup_error}")
        logger.error(f"🐞 {input_file}: {Error}", exc_info=True)
        return False, str(Error)
