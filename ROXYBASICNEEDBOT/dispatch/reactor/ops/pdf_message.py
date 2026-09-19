# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
from tracer import tracer
from sentinel import *
from pyrogram.errors import FloodWait


def sanitize_text(text: str) -> str:
    """Remove invalid Unicode surrogate characters that can't be encoded to UTF-8."""
    try:
        # First try to encode with surrogatepass to handle surrogates, then decode replacing bad chars
        return text.encode('utf-8', 'surrogatepass').decode('utf-8', 'replace')
    except (UnicodeEncodeError, UnicodeDecodeError):
        # Fallback: replace any problematic characters
        return ''.join(char if ord(char) < 0xD800 or ord(char) > 0xDFFF else '\ufffd' for char in text)


async def messagePDF(
    input_file: str, cDIR: str, callbackQuery, dlMSG, text: str
) -> (bool, str):
    """
    The function takes the file path of a PDF file as input and returns the extracted text from the PDF file as output..

    parameter:
        input_file    : Here is the path of the file that the user entered
        cDIR          : This is the location of the directory that belongs to the specific user.
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

        with fitz.open(input_file) as doc:
            if doc.page_count >= 3:
                await dlMSG.pin(disable_notification=True, both_sides=True)
            for page in doc:
                pageNo = int(str(page).split(" ")[1]) + 1
                pdfText = page.get_text()
                # Sanitize text to remove invalid UTF-8 surrogate characters
                pdfText = sanitize_text(pdfText)
                if 1 <= len(pdfText) <= 1000:
                    try:
                        await callbackQuery.message.reply(
                            f"```🅿🅰🅶🅴 : {pageNo}\n\n{pdfText}```\n@roxybasicneedbot1",
                            quote=pageNo == 1,
                        )
                    except FloodWait as e:
                        await asyncio.sleep(e.value + 1)
                        await callbackQuery.message.reply(f"{pdfText}", quote=False)
                elif 1000 <= len(pdfText):
                    slice = [
                        pdfText[i : i + 1000] for i in range(0, len(pdfText), 1000)
                    ]
                    for i, j in enumerate(slice, start=1):
                        # Sanitize each slice as well
                        j = sanitize_text(j)
                        try:
                            await callbackQuery.message.reply(
                                f"```🅿🅰🅶🅴 : {pageNo}-{i}\n\n{j}```\n\n@roxybasicneedbot1",
                                quote=pageNo == 1,
                            )
                        except FloodWait as e:
                            await asyncio.sleep(e.value + 1)
                            await callbackQuery.message.reply(f"{j}", quote=False)
                if await work.work(callbackQuery, "check", False):
                    try:
                        await dlMSG.edit(
                            text["_upload"].format(pageNo, doc.page_count),
                            reply_markup=cancel,
                        )
                    except Exception:
                        pass
            await dlMSG.edit(text=text["finished"], reply_markup=completed)
        return "finished", "finished"

    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(e)
