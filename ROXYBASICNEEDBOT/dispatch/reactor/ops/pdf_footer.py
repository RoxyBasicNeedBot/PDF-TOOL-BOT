# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
from tracer import tracer
# from pyromod import listen  # Removed
from sentinel.dialogstream import ask as conversation_ask
from pyrogram import filters
from bs4 import BeautifulSoup
from pyrogram.types import ForceReply


async def pdfFooter(input_file: str, cDIR: str, text: str) -> (bool, str):
    """
    Adds Header to pdf files

    parameter:
        input_file : Here is the path of the file that the user entered
        text : header text

    return:
        bool        : Return True when the request is successful
        input_file : This is the path where the output file can be found.
    """
    try:
        output_path = f"{cDIR}/outPut.pdf"

        footer_html = f"<div style='text-align: center; font-size: 12px;'>{text}</div>"
        with fitz.open(input_file) as doc:
            for page_number in range(doc.page_count):
                page = doc.load_page(page_number)
                footer = BeautifulSoup(footer_html, "html.parser")
                footer_annot = fitz.Rect(0, page.rect.height - 50, page.rect.width, page.rect.height)
                page.add_annot(footer_annot, "footer", footer.prettify().encode())
            doc.save(output_path)
        return True, output_path

    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(e)
