# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

from pyrogram import Client as RoxyBot, filters, enums
from pyrogram.types import Message
from core.nexus import images
from sentinel import getLang, translate
from tracer import logger

@RoxyBot.on_message(filters.group & filters.incoming & filters.command("start"))
async def start_group_welcome_handler(bot_client: RoxyBot, message: Message):
    """
    Handle the /start command when sent inside a Telegram Group.
    """
    try:
        try:
            await message.reply_chat_action(enums.ChatAction.TYPING)
        except Exception:
            pass
            
        lang_code = await getLang(message.chat.id)

        # Retrieve group welcome localized string structures
        tTXT, tBTN = await translate(
            text="HomeG['HomeA']",
            lang_code=lang_code,
            button="HomeG['HomeACB']"
        )

        await message.reply_photo(
            photo=images.WELCOME_PIC,
            caption=tTXT.format(message.chat.title, "𝐈 ❤️ 𝐏𝐃𝐅"),
            reply_markup=tBTN,
            quote=False
        )

        # Clear trigger message
        try:
            await message.delete()
        except Exception:
            pass
    except Exception as e:
        logger.error(f"Error in start_group_welcome_handler: {e}", exc_info=True)