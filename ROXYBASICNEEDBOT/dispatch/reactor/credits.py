# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

from modules import *
from sentinel import *


@RoxyBot.on_callback_query(filters.regex("^roxybasicneedbot"))
async def __index__(bot, callbackQuery):
    try:
        parts = callbackQuery.data.split("|", 1)
        if len(parts) < 2:
            # No data after "|", answer with generic message and return
            await callbackQuery.answer("Invalid action", show_alert=False)
            return
        
        data = parts[1]
        lang_code = await util.getLang(callbackQuery.message.chat.id)

        if data.startswith("aio"):
            text, _ = await util.translate(text=f"_CLICK_RIGHT", lang_code=lang_code)
        else:
            text, _ = await util.translate(text=f"HELP['{data}']", lang_code=lang_code)

        await callbackQuery.answer(text, show_alert=True)

    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        await work.work(callbackQuery, "delete", False)
