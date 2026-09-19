# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

auth = "nabil"

import fitz
from tracer import tracer
# from pyromod import listen  # Removed
from sentinel.dialogstream import ask as conversation_ask
from pyrogram import filters
from pyrogram.types import ForceReply


async def askPassword(bot, callbackQuery, question, process: str):
    try:
        password = await conversation_ask(
            bot,
            chat_id=callbackQuery.from_user.id,
            text=question.format(process),
            filters=filters.text,
            reply_to_message_id=callbackQuery.message.id,
            reply_markup=ForceReply(True, "Enter Password.."),
        )
        # Handle timeout case where password is None
        if password is None:
            return False, "Timeout: No response received"
        return (True, password) if password.text != "/exit" else (False, password)
    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(e)


async def encryptPDF(input_file: str, password: str, cDIR: str) -> (bool, str):
    try:
        """
        PDF encryption is a security feature that allows you to protect your PDF documents by
        encrypting their content to prevent unauthorized access or modification. Encryption is
        the process of converting plain text into a secret code to protect it from unauthorized access.

        parameter:
            input_file : Here is the path of the file that the user entered
            password   : Password entered by the user for pdf encryption
            cDIR       : This is the location of the directory that belongs to the specific user.

        return:
            bool        : Return True when the request is successful
            output_path : This is the path where the output file can be found.
        """
        output_path = f"{cDIR}/outPut.pdf"
        logger.debug(f"🔒 Encrypting PDF: {input_file}")
        with fitz.open(input_file) as iNPUT:
            number_of_pages = iNPUT.page_count
            logger.debug(f"🔑 Setting encryption - owner_pw: '{auth}', user_pw: '{password}'")
            iNPUT.save(
                output_path,
                encryption=fitz.PDF_ENCRYPT_AES_256,  # strongest algorithm
                owner_pw=auth,
                user_pw=f"{password}",
                permissions=int(
                    fitz.PDF_PERM_ACCESSIBILITY
                    | fitz.PDF_PERM_PRINT
                    | fitz.PDF_PERM_COPY
                    | fitz.PDF_PERM_ANNOTATE
                ),
            )
            logger.debug(f"✅ PDF encrypted successfully, saved to: {output_path}")
        return True, output_path

    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(e)
