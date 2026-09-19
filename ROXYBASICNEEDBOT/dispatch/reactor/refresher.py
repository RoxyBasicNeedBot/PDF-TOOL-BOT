# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

from modules import *
from ..photobox import images_handler as images
from sentinel import *
from core.corestate import myID
from ..inbox import documents_receiver as documents
from core.corestate import invite_link
from core.nexus import settings
from .ops.pdf_deeplink import decode
from collective.groupdoc import gDOC
from ..inline.openinbot import openInBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@RoxyBot.on_callback_query(filters.regex("^refresh"))
async def _refresh(bot, callbackQuery):
    try:
        lang_code = await util.getLang(callbackQuery.message.chat.id)
        if await render.header(bot, callbackQuery, lang_code=lang_code):
            return

        if invite_link:
            try:
                for ch_info in invite_link:
                    userStatus = await bot.get_chat_member(
                        str(ch_info["channel_id"]), callbackQuery.from_user.id
                    )
                    if userStatus.status == "kicked":
                        return await callbackQuery.answer("🤧")
            except Exception:
                tTXT, _ = await util.translate(text="BAN['Fool']", lang_code=lang_code)
                return await callbackQuery.answer(tTXT, show_alert=True)

        if callbackQuery.data.startswith("refresh-g"):  # this means "refresh-g{code}
            await decode(
                bot, callbackQuery.data[9:], callbackQuery.message, lang_code, cb=True
            )
            return await callbackQuery.message.delete()

        elif callbackQuery.data.startswith("refresh-m"):  # this means "refresh-g{code}
            await openInBot(bot, callbackQuery.message, callbackQuery.data.split("-m"))
            return await callbackQuery.message.delete()

        reply_msg = await ensure_reply_to_message(bot, callbackQuery)

        if await work.work(callbackQuery, "check", False):
            tTXT, _ = await util.translate(
                text="PROGRESS['workInP']", lang_code=lang_code
            )
            return await callbackQuery.answer(tTXT)

        if not reply_msg:
            return await callbackQuery.answer("❌ Original message not found.", show_alert=True)

        elif reply_msg.document:
            await callbackQuery.message.delete()
            return await documents(bot, reply_msg)

        elif reply_msg.photo:
            await callbackQuery.message.delete()
            return await images(bot, reply_msg)

        elif reply_msg.text and reply_msg.text.startswith("/start"):
            tTXT, tBTN = await util.translate(
                text="HOME['HomeA']",
                button="HOME['HomeACB']",
                lang_code=lang_code,
                order=2121,
            )
            await callbackQuery.edit_message_caption(
                caption=tTXT.format(callbackQuery.from_user.mention, myID[0].mention),
                reply_markup=tBTN,
            )
            tTXT, tBTN = await util.translate(
                text="HOME['search']", lang_code=lang_code
            )
            await callbackQuery.message.reply_sticker(
                sticker="CAACAgUAAxkBAAIDK2k6tE1vTHhIs_tYD3bIuTC5rpLzAAKdFwACZzqZVsIlT2pK1QJuHgQ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text=tTXT[0], switch_inline_query_current_chat=""
                            )
                        ],
                        [InlineKeyboardButton(text=tTXT[1], callback_data="beta")],
                    ]
                ),
            )
            return await reply_msg.delete()

        elif reply_msg.text and reply_msg.text.startswith("/"):
            await callbackQuery.message.delete()
            return await gDOC(bot, reply_msg)

        elif reply_msg.text:
            await callbackQuery.message.delete()
            return await _url(bot, reply_msg)

    except Exception as Error:
        logger.debug(f"Error in refresher: {Error}")
