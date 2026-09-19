# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

from modules import *
from sentinel import *


@RoxyBot.on_message(filters.private & filters.command(["txt2pdf"]) & filters.incoming, group=0)
async def text2PDF(bot, message):
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        lang_code = await util.getLang(message.chat.id)
        tTXT, tBTN = await util.translate(
            text="pdf2TXT['TEXT']",
            button="pdf2TXT['size_btn']",
            order=121,
            lang_code=lang_code,
        )
        await message.reply_photo(
            photo="https://graph.org/file/3218aa8e08eb10e216552.jpg",
            caption=tTXT,
            reply_markup=tBTN,
        )
        await message.delete()
    except Exception as e:
        logger.error("🐞 %s: %s" % (file_name, Error), exc_info=True)
