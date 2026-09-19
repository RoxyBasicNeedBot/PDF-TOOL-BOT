# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import base64
from . import *
from modules import *
from tracer import tracer
from asyncio import sleep
from pyrogram import enums
from sentinel import *
from core.ledger import log
from core.corestate import myID
from core.nexus import dm


async def decode(bot, code, message, lang_code, cb=False):
    try:
        padding = "=" * (4 - len(code) % 4)
        base64_ = (code + padding).encode("ascii")
        string_bytes = base64.urlsafe_b64decode(base64_)
        string = string_bytes.decode("ascii")

        # Remove any non-numeric characters from the string
        string = "".join([char for char in string if char.isdigit()])

        getMSG = await bot.get_messages(
            chat_id=int(log.LOG_CHANNEL), message_ids=int(string)
        )
        if not (getMSG.empty):
            await message.reply_chat_action(enums.ChatAction.UPLOAD_DOCUMENT)
            protect = True if "🔒 PROTECTED 🔒" in getMSG.caption else False
            notify = True if "🔔 NOTIFY 🔔" in getMSG.caption else False
            await getMSG.copy(
                chat_id=message.chat.id, caption="", protect_content=protect
            )

            if notify and message.from_user.id not in dm.ADMINS:
                chat_id = int(getMSG.caption.split("•")[1])
                message_id = int(getMSG.caption.split("•")[3])

                if message.from_user.id == chat_id:
                    return
                try:
                    await bot.send_message(
                        text=f"{message.from_user.mention}",
                        chat_id=chat_id,
                        reply_to_message_id=message_id,
                    )
                except Exception:
                    pass
            return
        # if etMSG.empty is True; replies not founded error
        await message.reply_chat_action(enums.ChatAction.TYPING)
        _, __ = await util.translate(text="LINK['error']", lang_code=lang_code)
        return await message.reply(
            text=f"`{code}`\n" + _.format("`cantFINDorDELETED`"), quote=True
        )
    except Exception as e:
        logger.error("🐞 %s: %s" % (fileName, e))
        _, __ = await util.translate(text="LINK['error']", lang_code=lang_code)
        return await message.reply(text=f"`{code}`\n" + _.format(e), quote=True)


@RoxyBot.on_callback_query(filters.regex("link"))
async def _link(bot, callbackQuery):
    logger.debug(f"🔗 Link callback triggered by user {callbackQuery.from_user.id}: {callbackQuery.data}")
    try:
        lang_code = await util.getLang(callbackQuery.message.chat.id)
        if await render.header(bot, callbackQuery, lang_code=lang_code):
            return

        if not log.LOG_CHANNEL:
            _, __ = await util.translate(text="LINK['no']", lang_code=lang_code)
            return await callbackQuery.answer(_)
        await callbackQuery.answer()

        if callbackQuery.data == "link":
            logger.debug(f"📝 Initial link callback - showing public/private options")
            _, __ = await util.translate(text="LINK['gen']", lang_code=lang_code)
            dlMSG = await callbackQuery.message.reply_to_message.reply_text(
                text=_, quote=True
            )
            await sleep(1)
            _, __ = await util.translate(text="LINK['_gen']", lang_code=lang_code)
            await dlMSG.edit(text=_)
            await sleep(1)
            _, __ = await util.translate(
                text="LINK['type']", button="LINK['typeBTN']", lang_code=lang_code
            )
            logger.debug(f"✅ Showed public/private options to user")
            return await dlMSG.edit(text=_, reply_markup=__)

        if callbackQuery.data == "link-pvt":
            logger.debug(f"🔒 Private link selected - showing notify options")
            _, __ = await util.translate(
                text="LINK['notify']", button="LINK['notify_pvt']", lang_code=lang_code
            )
            return await callbackQuery.message.edit(text=_, reply_markup=__)
        elif callbackQuery.data == "link-pub":
            logger.debug(f"📢 Public link selected - showing notify options")
            _, __ = await util.translate(
                text="LINK['notify']", button="LINK['notify_pub']", lang_code=lang_code
            )
            return await callbackQuery.message.edit(text=_, reply_markup=__)

        logger.debug(f"🔄 Generating URL with data: {callbackQuery.data}")
        _, __ = await util.translate(text="LINK['_gen']", lang_code=lang_code)
        await callbackQuery.message.edit(text=_)

        _, _typ, _ntf = callbackQuery.data.split("-")
        logger.debug(f"📋 Type: {_typ}, Notify: {_ntf}")

        notify = "🔔 NOTIFY 🔔" if _ntf == "ntf" else "🔕 MUTE 🔕"
        content = "🔒 PROTECTED 🔒" if _typ == "pvt" else "📢 PUBLIC 📢"

        await sleep(1)
        file = await callbackQuery.message.reply_to_message.copy(
            int(log.LOG_CHANNEL),
            caption=f"🔗 **from:** {callbackQuery.from_user.mention}\n"
            f"    **chat:** `•{callbackQuery.from_user.id}•`\n"
            f"    **message:** `•{callbackQuery.message.id}•`"
            f"\n\n**{content}**\n**{notify}**"
            "",
        )

        string_bytes = f"{file.id}".encode("ascii")
        base64_bytes = base64.urlsafe_b64encode(string_bytes)
        base64_string = (base64_bytes.decode("ascii")).strip("=")

        link = f"https://telegram.dog/{myID[0].username}?start=-g{base64_string}"
        logger.debug(f"✅ Generated URL successfully: {link}")
        _, __ = await util.translate(text="LINK['link']", lang_code=lang_code)

        btn = await util.createBUTTON(
            {
                "📢 Share URL 📢": f"https://telegram.me/share/url?url={link}",
                "🔗 Open URL 🔗": link,
            },
            order=11,
        )
        return await callbackQuery.message.edit(
            text=_ + f"\n\n{content}", reply_markup=btn
        )

    except Exception as e:
        logger.error("🐞 %s: %s" % (fileName, Error), exc_info=True)
        _, __ = await util.translate(text="LINK['error']", lang_code=lang_code)
        await dlMSG.edit(_.format(Error))
