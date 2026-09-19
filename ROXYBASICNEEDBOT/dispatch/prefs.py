# ┌─────────────────────────────────────────────────────────────┐
# │                    𝕽𝕺𝕏𝖄•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │  Created by: RoxyBasicNeedBot                               │
# │  GitHub    : https://github.com/RoxyBasicNeedBot            │
# │  Telegram  : https://t.me/roxybasicneedbot1                 │
# │  Website   : https://roxybasicneedbot.unaux.com             │
# │  YouTube   : @roxybasicneedbot                              │
# ├─────────────────────────────────────────────────────────────┤
# │      Bot Developer, Automation Architect & Python Coder      │
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import asyncio
from pyrogram import Client as RoxyBot, filters, enums
from pyrogram.types import Message, CallbackQuery, InputMediaPhoto
from pyrogram.enums import ChatType, ChatMemberStatus
from core.nexus import settings, dm, images
from core.corestate import CUSTOM_THUMBNAIL_U, CUSTOM_THUMBNAIL_C, DATA, dataBASE, myID
from sentinel import util, getLang, translate, createBUTTON, ask
from core.i18n import disLang
from tracer import logger

if dataBASE.MONGODB_URI:
    from ledger.safebox import db

@RoxyBot.on_callback_query(filters.regex("^set"))
async def _settings(bot_client: RoxyBot, callbackQuery: CallbackQuery):
    try:
        lang_code = await getLang(callbackQuery.message.chat.id)
        parts = callbackQuery.data.split("|", 1)
        if len(parts) < 2:
            return await callbackQuery.answer()
        data = parts[1]

        if not (data.startswith("set|lang")) and (
            callbackQuery.message.chat.type != ChatType.PRIVATE
            and callbackQuery.from_user.id not in dm.ADMINS
        ):
            userStat = await bot_client.get_chat_member(
                callbackQuery.message.chat.id, callbackQuery.from_user.id
            )
            if userStat.status not in [
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.OWNER,
            ]:
                return await callbackQuery.answer("😑")

        if data == "B":  # Home|B will redirect to settings
            if not dataBASE.MONGODB_URI:
                defalt, _ = await translate(
                    text="SETTINGS['default'][0]", lang_code=lang_code
                )
                args = [
                    f"{callbackQuery.from_user.mention}",
                    f"{callbackQuery.from_user.id}",
                    f"@{callbackQuery.from_user.username}"
                    if callbackQuery.from_user.username
                    else "❌",
                    "❌",
                    disLang(lang_code),
                    defalt,
                    defalt,
                    defalt,
                    defalt,
                ]
                await callbackQuery.edit_message_media(
                    InputMediaPhoto(images.THUMBNAIL_URL)
                )

            else:
                user_data = await db.get_user_data(callbackQuery.message.chat.id)
                if not user_data:
                    error, errorCB = await translate(
                        text="SETTINGS['error']",
                        button="SETTINGS['back'][0]",
                        lang_code=lang_code,
                    )
                    return await callbackQuery.edit_message_caption(
                        caption=error, reply_markup=errorCB
                    )

                defalt, _ = await translate(
                    text="SETTINGS['default']", lang_code=lang_code
                )
                args = [
                    f"{callbackQuery.from_user.mention}",
                    f"{callbackQuery.from_user.id}",
                    f"@{callbackQuery.from_user.username}"
                    if callbackQuery.from_user.username
                    else "❌",
                    user_data.get("join_date", "N/A"),
                    disLang(lang_code),
                    f"`{user_data['api']}`" if user_data.get("api", 0) else defalt[0],
                    defalt[1] if user_data.get("thumb", 0) else defalt[0],
                    f"`{user_data['capt']}`" if user_data.get("capt", 0) else defalt[0],
                    f"`{user_data['fname']}`" if user_data.get("fname", 0) else defalt[0],
                ]
                await callbackQuery.edit_message_media(
                    InputMediaPhoto(user_data["thumb"])
                    if user_data.get("thumb", 0)
                    else InputMediaPhoto(images.THUMBNAIL_URL)
                )

            tTXT, tBTN = await translate(
                text="HOME['HomeB']", button="HOME['HomeBCB']", lang_code=lang_code
            )
            return await callbackQuery.edit_message_caption(
                caption=tTXT.format(*args), reply_markup=tBTN
            )

        if data == "B2S":
            _, tBTN = await translate(
                button="HOME['HomeBCB']", lang_code=lang_code
            )
            return await callbackQuery.message.edit_reply_markup(tBTN)

        if not data.startswith("lang") and not dataBASE.MONGODB_URI:
            tTXT, tBTN = await translate(
                text="STATUS_MSG['NO_DB']", lang_code=lang_code
            )
            return await callbackQuery.answer(tTXT)

        user_id = callbackQuery.from_user.id
        chat_id = callbackQuery.message.chat.id
        chat_type = callbackQuery.message.chat.type

        if data.startswith("lang"):
            if data == "lang":
                tTXT, change = await translate(
                    text="SETTINGS['lang']",
                    button="SETTINGS['chgLang']",
                    lang_code=lang_code,
                )
                from core.i18n import LANG_MAP
                from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

                keyboard = [
                    [InlineKeyboardButton(f"{LANG_MAP[key]['flag']} {LANG_MAP[key]['name']}", callback_data=f"set|lang|{key}")]
                    for key in LANG_MAP
                ]
                
                # change is an InlineKeyboardMarkup with a back button. We append its first row.
                if change and hasattr(change, 'inline_keyboard') and change.inline_keyboard:
                    keyboard.append(change.inline_keyboard[0])
                
                return await callbackQuery.message.edit(text=tTXT, reply_markup=InlineKeyboardMarkup(keyboard))
            else:
                lang = data.split("|", 1)[1]
                
                if dataBASE.MONGODB_URI:
                    if chat_type == ChatType.PRIVATE and lang != settings.DEFAULT_LANG:
                        await db.set_key(
                            id=callbackQuery.message.chat.id, key="lang", value=lang
                        )
                    elif chat_type != ChatType.PRIVATE and lang != settings.DEFAULT_LANG:
                        await db.set_key(
                            id=callbackQuery.message.chat.id,
                            key="lang",
                            value=lang,
                            typ="group",
                        )
                    elif chat_type == ChatType.PRIVATE and lang == settings.DEFAULT_LANG:
                        await db.dlt_key(id=callbackQuery.message.chat.id, key="lang")
                    elif chat_type != ChatType.PRIVATE and lang == settings.DEFAULT_LANG:
                        await db.dlt_key(
                            id=callbackQuery.message.chat.id, key="lang", typ="group"
                        )
            _, __ = await translate(
                text="SETTINGS['feedback']",
                button="SETTINGS['feedbtn']",
                lang_code=lang,
            )
            await callbackQuery.message.reply_text(
                text=_.format(disLang(lang)), reply_markup=__
            )

        elif data.startswith("thumb"):
            if data == "thumb":
                if user_id in CUSTOM_THUMBNAIL_U:
                    _, tBTN = await translate(
                        button="SETTINGS['thumb'][1]", order=121, lang_code=lang_code
                    )
                    return await callbackQuery.message.edit_reply_markup(tBTN)
                else:
                    _, tBTN = await translate(
                        button="SETTINGS['thumb'][0]", order=111, lang_code=lang_code
                    )
                    return await callbackQuery.message.edit_reply_markup(tBTN)
            elif data == "thumb+":
                tTXT, tBTN = await translate(
                    text="SETTINGS['ask']",
                    button="SETTINGS['wait']",
                    order=111,
                    lang_code=lang_code,
                )
                await callbackQuery.edit_message_caption(
                    caption=tTXT[0], reply_markup=tBTN
                )
                await asyncio.sleep(0.5)
                await callbackQuery.edit_message_caption(
                    caption=tTXT[1], reply_markup=tBTN
                )
                getThumb = await ask(bot_client, chat_id=user_id, text="Send me the new photo...")
                if getThumb and getThumb.photo:
                    await db.set_key(user_id, "thumb", getThumb.photo.file_id)
                    CUSTOM_THUMBNAIL_U.append(user_id)
                    await getThumb.delete()
            elif data == "thumb-":
                if user_id in CUSTOM_THUMBNAIL_U:
                    CUSTOM_THUMBNAIL_U.remove(user_id)
                await db.dlt_key(callbackQuery.message.chat.id, "thumb")

        elif data.startswith("api"):
            current = DATA.get(int(user_id), 0)
            if data == "api":
                if current and current[0]:
                    _, tBTN = await translate(
                        button="SETTINGS['api'][1]", order=121, lang_code=lang_code
                    )
                    return await callbackQuery.message.edit_reply_markup(tBTN)
                else:
                    _, tBTN = await translate(
                        button="SETTINGS['api'][0]", order=111, lang_code=lang_code
                    )
                    return await callbackQuery.message.edit_reply_markup(tBTN)
            elif data == "api+":
                tTXT, tBTN = await translate(
                    text="SETTINGS['ask']",
                    button="SETTINGS['waitApi']",
                    order=111,
                    lang_code=lang_code,
                )
                await callbackQuery.edit_message_caption(
                    caption=tTXT[0], reply_markup=tBTN
                )
                _, __ = await translate(
                    text="SETTINGS['askApi']", lang_code=lang_code
                )
                await asyncio.sleep(0.5)
                await callbackQuery.edit_message_caption(
                    caption=tTXT[1] + _, reply_markup=tBTN
                )
                getName = await ask(bot_client, chat_id=user_id, text="Send me the API key...")
                if getName and getName.text and getName.text != "/cancel":
                    await db.set_key(user_id, "api", f"{getName.text}"[:60])
                    if current:
                        DATA[user_id][0] = True
                    else:
                        DATA[user_id] = [True, 0, 0]
                    await getName.delete()
            elif data == "api-":
                if user_id in DATA:
                    DATA[user_id][0] = 0
                await db.dlt_key(callbackQuery.message.chat.id, "api")

        elif data.startswith("fname"):
            if settings.DEFAULT_NAME:
                cant, _ = await translate(
                    text="SETTINGS['cant']", lang_code=lang_code
                )
                return await callbackQuery.answer(cant)
            current = DATA.get(int(user_id), 0)
            if data == "fname":
                if current and current[1]:
                    _, tBTN = await translate(
                        button="SETTINGS['fname'][1]", order=121, lang_code=lang_code
                    )
                    return await callbackQuery.message.edit_reply_markup(tBTN)
                else:
                    _, tBTN = await translate(
                        button="SETTINGS['fname'][0]", order=111, lang_code=lang_code
                    )
                    return await callbackQuery.message.edit_reply_markup(tBTN)
            elif data == "fname+":
                tTXT, tBTN = await translate(
                    text="SETTINGS['ask']",
                    button="SETTINGS['wait']",
                    order=111,
                    lang_code=lang_code,
                )
                await callbackQuery.edit_message_caption(
                    caption=tTXT[0], reply_markup=tBTN
                )
                await asyncio.sleep(0.5)
                await callbackQuery.edit_message_caption(
                    caption=tTXT[1], reply_markup=tBTN
                )
                getName = await ask(bot_client, chat_id=user_id, text="Send me the default filename...")
                if getName and getName.text and getName.text != "/cancel":
                    await db.set_key(user_id, "fname", f"{getName.text}"[:60])
                    if current:
                        DATA[user_id][1] = True
                    else:
                        DATA[user_id] = [0, True, 0]
                    await getName.delete()
            elif data == "fname-":
                if user_id in DATA:
                    DATA[user_id][1] = 0
                await db.dlt_key(callbackQuery.message.chat.id, "fname")

        elif data.startswith("capt"):
            if settings.DEFAULT_CAPT:
                cant, _ = await translate(
                    text="SETTINGS['cant']", lang_code=lang_code
                )
                return await callbackQuery.answer(cant)
            current = DATA.get(int(user_id), 0)
            if data == "capt":
                if current and current[2]:
                    _, tBTN = await translate(
                        button="SETTINGS['capt'][1]", order=121, lang_code=lang_code
                    )
                    return await callbackQuery.message.edit_reply_markup(tBTN)
                else:
                    _, tBTN = await translate(
                        button="SETTINGS['capt'][0]", order=111, lang_code=lang_code
                    )
                    return await callbackQuery.message.edit_reply_markup(tBTN)
            elif data == "capt+":
                tTXT, tBTN = await translate(
                    text="SETTINGS['ask']",
                    button="SETTINGS['wait']",
                    order=111,
                    lang_code=lang_code,
                )
                await callbackQuery.edit_message_caption(
                    caption=tTXT[0], reply_markup=tBTN
                )
                await asyncio.sleep(0.5)
                await callbackQuery.edit_message_caption(
                    caption=tTXT[1], reply_markup=tBTN
                )
                getName = await ask(bot_client, chat_id=user_id, text="Send me the default caption...")
                if getName and getName.text and getName.text != "/cancel":
                    await db.set_key(user_id, "capt", f"{getName.text}"[:60])
                    if current:
                        DATA[user_id][2] = True
                    else:
                        DATA[user_id] = [0, 0, True]
                    await getName.delete()
            elif data == "capt-":
                if user_id in DATA:
                    DATA[user_id][2] = 0
                await db.dlt_key(callbackQuery.message.chat.id, "capt")

        if not data.endswith("+"):
            result, _ = await translate(
                text="SETTINGS['result'][1]", lang_code=lang_code
            )
            await callbackQuery.answer(result)
            
        if callbackQuery.message.chat.type == ChatType.PRIVATE:
            await callbackQuery.edit_message_media(InputMediaPhoto(images.WELCOME_PIC))
            tTXT, tBTN = await translate(
                text="HOME['HomeA']",
                lang_code=lang if data.startswith("lang") else lang_code,
                button="HOME['HomeACB']" if callbackQuery.message.chat.id not in dm.ADMINS else "HOME['HomeAdminCB']",
                order=2121 if callbackQuery.message.chat.id not in dm.ADMINS else 21221,
            )
        else:
            tTXT, tBTN = await translate(
                text="HomeG['HomeA']",
                button="HomeG['HomeACB']",
                lang_code=lang if data.startswith("lang") else lang_code,
            )
        return await callbackQuery.edit_message_caption(
            caption=tTXT.format(callbackQuery.from_user.mention, myID[0].mention),
            reply_markup=tBTN,
        )

    except Exception as Error:
        logger.error(f"Error in prefs: {Error}", exc_info=True)
