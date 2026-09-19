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

import datetime
import os
import asyncio
import time
from core.nexus import settings, dm
from core.corestate import dataBASE, ping_list, BANNED_USR_DB, BANNED_GRP_DB
from pyrogram import Client as RoxyBot, filters, enums
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid
from sentinel import set_bot_commands, ask
from tracer import logger

if dataBASE.MONGODB_URI:
    from ledger.safebox import db

BROADCAST = False

@RoxyBot.on_message(filters.command("stop") & filters.user(dm.ADMINS) & filters.private & filters.incoming, group=0)
async def stop_bot_toggle(bot_client: RoxyBot, message: Message):
    logger.debug(f"🛑 /stop toggle command received from admin {message.from_user.id}")
    try:
        global BROADCAST
        if message.text == "/stop" and BROADCAST:
            return await message.reply(
                "MESSAGE FOR ADMIN: Currently Broadcasting Something.. 🥱", quote=True
            )
        settings.STOP_BOT = not settings.STOP_BOT
        reply = "MESSAGE FOR ADMIN: `bot stopped..` 🗽" if settings.STOP_BOT else "MESSAGE FOR ADMIN: `bot started..` ✨"
        await message.reply(reply, quote=True)

        if not settings.STOP_BOT:
            for user in ping_list:
                try:
                    await bot_client.send_message(chat_id=user, text="💡")
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                except Exception:
                    pass
    except Exception as error:
        logger.error(f"Error in stop_bot_toggle: {error}")

@RoxyBot.on_message(filters.command("set") & filters.user(dm.ADMINS) & filters.private & filters.incoming, group=0)
async def set_commands_admin(bot_client: RoxyBot, message: Message):
    logger.debug(f"⚙️ /set command received from admin {message.from_user.id}")
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        processing_msg = await message.reply("⚙️ `Registering bot commands...`", quote=True)
        await set_bot_commands(bot_client)
        await processing_msg.edit(
            "✅ **Commands configured successfully!**\n\n"
            "• User commands set for all private chats\n"
            "• Admin commands set for all admins"
        )
    except Exception as error:
        logger.error(f"Error in set_commands_admin: {error}")
        await message.reply(f"❌ Error setting commands: `{error}`", quote=True)

@RoxyBot.on_message(filters.command("send") & filters.user(dm.ADMINS) & filters.private & filters.incoming, group=0)
async def send_broadcast_cmd(bot_client: RoxyBot, message: Message):
    logger.debug(f"📤 /send command received from admin {message.from_user.id}")
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        if not message.reply_to_message:
            error = await message.reply("⚙️ `Processing..`", quote=True)
            await asyncio.sleep(1)
            return await error.edit("__please, reply to a message__ 🥲")

        msg = await message.reply_to_message.reply("⚙️ `Processing..`", quote=True)
        await message.delete()
        
        return await msg.edit(
            text="⚙️ SEND MESSAGE: \n\n`Now, Select any Option Below.. `",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("📢 ↓ BROADCAST ↓ 📢", callback_data="roxybasicneedbot")
                ],[
                    InlineKeyboardButton("🔸 COPY 🔸", callback_data="send|copy|broad"),
                    InlineKeyboardButton("🔸 FORWARD 🔸", callback_data="send|forw|broad"),
                ],[
                    InlineKeyboardButton("👤 ↓ PM ↓ 👤", callback_data="roxybasicneedbot"),
                ],[
                    InlineKeyboardButton("🔸 COPY 🔸", callback_data="send|copy|pm"),
                    InlineKeyboardButton("🔸 FORWARD 🔸", callback_data="send|forw|pm"),
                ],[
                    InlineKeyboardButton("📢 NoN SUBSCRIBERS 📢", callback_data="roxybasicneedbot"),
                ],[
                    InlineKeyboardButton("🔸 COPY 🔸", callback_data="send|copy|not"),
                    InlineKeyboardButton("🔸 FORWARD 🔸", callback_data="send|forw|not"),
                ],]
            ),
        )
    except Exception as error:
        logger.error(f"Error in send_broadcast_cmd: {error}")

async def broadcast_messages(bot_client, user_id: int, message, info, force=False):
    try:
        if force:
            from core.corestate import invite_link
            for ch_info in invite_link:
                try:
                    user_status = await bot_client.get_chat_member(
                        str(ch_info["channel_id"]), user_id
                    )
                    if user_status.status == enums.ChatMemberStatus.BANNED:
                        return False, "Subscribed"
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                except UserNotParticipant:
                    pass
                except Exception:
                    pass
        
        if info == "copy":
            await message.copy(chat_id=user_id)
            return True, "Success"
        else:
            await message.forward(chat_id=user_id)
            return True, "Success"
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await broadcast_messages(bot_client, user_id, message, info, force)
    except InputUserDeactivated:
        await db.delete_user(int(user_id))
        return False, "Deleted"
    except UserIsBlocked:
        return False, "Blocked"
    except PeerIdInvalid:
        await db.delete_user(int(user_id))
        return False, "Error"
    except Exception as e:
        logger.error(f"Error broadcasting message to {user_id}: {e}")
        return False, "Error"

@RoxyBot.on_callback_query(filters.regex("^send"))
async def execute_broadcast(bot_client: RoxyBot, callback_query: CallbackQuery):
    try:
        global BROADCAST
        data = callback_query.data
        _, __, ___ = callback_query.data.split("|")

        if ___ == "broad" and not dataBASE.MONGODB_URI:
            return await callback_query.answer("Can't Use this feature ={")
        
        if ___ in ["broad", "not"]:
            if ___ == "not" and not (settings.FORCE_SUB_CHANNELS):
                return await callback_query.answer("First ADD updates channel.. 😏")
            if BROADCAST:
                return await callback_query.answer("Broadcasting Some Other Message.. 🙄")
            await callback_query.answer("⚙️ Processing.. ")
            BROADCAST = not BROADCAST
            
            work_path = "./work/roxybasicneedbot"
            if os.path.exists(work_path):
                for chat in os.listdir(work_path):
                    try:
                        await bot_client.send_message(
                            chat_id=chat, text="⏳ Broadcasting in progress... Your work will continue shortly."
                        )
                    except Exception:
                        pass
            else:
                os.makedirs(work_path, exist_ok=True)

            users = await db.get_all_users()
            broadcast_msg = callback_query.message.reply_to_message
            total_users = await db.total_users_count()
            await callback_query.message.edit(
                text=f"⚙️ Started Broadcasting..\nTOTAL {total_users} USERS 😍\n\n↓ MESSAGE ↓"
                     f"\n`{broadcast_msg.text if broadcast_msg.text else '📂 Media 📂'}`",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            "🔸 asForward 🔸" if __ == "forw" else "🔸 asCopy 🔸",
                            callback_data="roxybasicneedbot",
                        )
                    ]]
                ),
            )
            
            start_time = time.time()
            done, blocked, deleted, failed, success, subscribed = 0, 0, 0, 0, 0, 0

            async for user in users:
                i_success, feed = await broadcast_messages(
                    bot_client,
                    user_id=int(user["id"]), message=broadcast_msg,
                    info=__, force=True if ___ == "not" else False
                )
                if i_success:
                    success += 1
                else:
                    if feed == "Blocked":
                        blocked += 1
                    elif feed == "Deleted":
                        deleted += 1
                    elif feed == "Error":
                        failed += 1
                    elif feed == "Subscribed":
                        subscribed += 1

                done += 1
                await asyncio.sleep(0.3) # rate limit helper
                if done % 20 == 0:
                    try:
                        await callback_query.message.edit_reply_markup(
                            InlineKeyboardMarkup(
                                [[
                                    InlineKeyboardButton(
                                        f"🔸 asForward({done}/{total_users}) 🔸"
                                        if __ == "forw"
                                        else f"🔸 asCopy({done}/{total_users}) 🔸",
                                        callback_data="roxybasicneedbot"
                                    )
                                ]]
                            )
                        )
                    except Exception:
                        pass
            time_taken = datetime.timedelta(seconds=int(time.time() - start_time))
            await callback_query.message.edit(
                text=f"`Broadcast Completed:`\n"
                     f"__Completed in__ {time_taken} __seconds ⏰__\n\n"
                     f"__Total Users:__ {total_users} 😎\n"
                     f"__Completed:__   {done} / {total_users} 👑\n"
                     f"__Success:__     {success} ✅\n"
                     f"__Blocked:__     {blocked} ❌\n"
                     f"__Deleted:__     {deleted} ⚰️\n\n" + 
                     (f"__Subscribed:__  {subscribed} 🎉" if ___ == "not" else ""),
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            "🔸 asForward 🔸" if __ == "forw" else "🔸 asCopy 🔸",
                            callback_data="roxybasicneedbot",)
                    ]]
                ),
            )
            BROADCAST = not BROADCAST
            return
        
        elif ___ == "pm":
            await callback_query.answer("⚙️ Processing.. ")
            user_id_msg = await ask(
                bot_client,
                chat_id=callback_query.from_user.id,
                text="__Now Send me the target ID/Username__ 😅\n\n/cancel to exit"
            )
            if not user_id_msg or not user_id_msg.text or user_id_msg.text == "/cancel":
                return
            
            chat = user_id_msg.text
            try:
                chat = int(user_id_msg.text)
            except Exception:
                pass
            
            try:
                try:
                    user_info = await bot_client.get_users(chat)
                except Exception:
                    user_info = await bot_client.get_chat(chat)
            except Exception as e:
                return await user_id_msg.reply(
                    f"__Can't Process This message__\n\n__REASON:__ `{e}`",
                    quote=True
                )
            
            forward_msg = callback_query.message.reply_to_message
            try:
                if __ == "copy":
                    await forward_msg.copy(user_info.id)
                else:
                    await forward_msg.forward(user_info.id)
            except Exception as error:
                return await user_id_msg.reply(
                    f"__Can't forward message__\n__REASON:__ `{error}`"
                )
            else:
                return await user_id_msg.reply("Successfully forwarded")
    except Exception as e:
        logger.error(f"Error executing broadcast: {e}", exc_info=True)

@RoxyBot.on_message(filters.command("ban") & filters.user(dm.ADMINS) & filters.private & filters.incoming, group=0)
async def ban_user_cmd(bot_client: RoxyBot, message: Message):
    try:
        params = message.text.split(" ", 2)
        if len(params) < 2:
            return await message.reply("Format: `/ban <user_id> <reason>`", quote=True)
        user_id = int(params[1])
        reason = params[2] if len(params) > 2 else "No reason provided."
        
        if dataBASE.MONGODB_URI:
            await db.set_key(user_id, "banned", reason)
            BANNED_USR_DB.append(user_id)
        await message.reply(f"🚫 User `{user_id}` successfully restricted.", quote=True)
    except Exception as e:
        await message.reply(f"❌ Error banning user: `{e}`", quote=True)

@RoxyBot.on_message(filters.command("unban") & filters.user(dm.ADMINS) & filters.private & filters.incoming, group=0)
async def unban_user_cmd(bot_client: RoxyBot, message: Message):
    try:
        params = message.text.split(" ")
        if len(params) < 2:
            return await message.reply("Format: `/unban <user_id>`", quote=True)
        user_id = int(params[1])
        
        if dataBASE.MONGODB_URI:
            await db.dlt_key(user_id, "banned")
            if user_id in BANNED_USR_DB:
                BANNED_USR_DB.remove(user_id)
        await message.reply(f"✅ User `{user_id}` successfully unrestricted.", quote=True)
    except Exception as e:
        await message.reply(f"❌ Error unbanning user: `{e}`", quote=True)

@RoxyBot.on_message(filters.command("report") & filters.user(dm.ADMINS) & filters.private & filters.incoming, group=0)
async def report_dashboard_cmd(bot_client: RoxyBot, message: Message):
    try:
        total_users = await db.total_users_count() if dataBASE.MONGODB_URI else 0
        total_chats = await db.total_chat_count() if dataBASE.MONGODB_URI else 0
        total, used, free = shutil.disk_usage(".")
        used_p = (used / total) * 100
        
        # Format summary
        summary = (
            "📊 **Daily RoxyBot Report**\n\n"
            f"👤 **Users in DB:** `{total_users}`\n"
            f"👥 **Groups in DB:** `{total_chats}`\n\n"
            f"💿 **Disk Space:** `{used_p:.1f}% used`\n"
            f"• Total: `{total / (1024**3):.1f} GB`\n"
            f"• Used: `{used / (1024**3):.1f} GB`\n"
            f"• Free: `{free / (1024**3):.1f} GB`\n"
        )
        await message.reply(summary, quote=True)
    except Exception as e:
        await message.reply(f"Error compiling report: `{e}`", quote=True)
