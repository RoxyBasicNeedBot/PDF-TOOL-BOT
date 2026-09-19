# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

from tracer import tracer
# from pyromod import listen  # Removed
from sentinel.dialogstream import ask as conversation_ask
from pyrogram import filters
from pyrogram.types import ForceReply


async def askName(bot, callbackQuery, question):
    try:
        newName = await conversation_ask(
            bot,
            chat_id=callbackQuery.from_user.id,
            text=question,
            filters=filters.text,
            reply_to_message_id=callbackQuery.message.id,
            reply_markup=ForceReply(True, "Enter new File Name.."),
        )
        # Handle timeout case where newName is None
        if newName is None:
            return False, "Timeout: No response received"
        return (True, newName) if newName.text != "/exit" else (False, newName)
    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(e)


async def renamePDF(input_file: str):
    """
    Renaming PDF files can help you keep your files organized and easy to find.
    By giving the file a descriptive name that reflects its contents, you can
    quickly identify the file you need without having to open it.

    parameter:
        input_file : Here is the path of the file that the user entered

    return:
        bool        : Return True when the request is successful
        input_file : This is the path where the output file can be found.
    """
    return True, input_file
