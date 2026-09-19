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

from pyrogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeChat
from core.nexus import dm
from tracer import logger

class CommandVault:
    @staticmethod
    async def set_bot_commands(client):
        user_commands = [
            BotCommand("start", "🚀 Start the bot"),
            BotCommand("cancel", "❌ Cancel current PDF operation"),
            BotCommand("delete", "🗑️ Delete image to PDF queue"),
            BotCommand("donate", "☕ Support the bot with Stars"),
            BotCommand("txt2pdf", "📝 Convert text to PDF"),
            BotCommand("hd", "🖼️ High quality photo processing"),
            BotCommand("beta", "🔰 Become a beta user"),
        ]
        
        admin_commands = user_commands + [
            BotCommand("stop", "⏹️ Stop/Start the bot"),
            BotCommand("send", "📢 Broadcast message to users"),
            BotCommand("ban", "🚫 Ban a user"),
            BotCommand("unban", "✅ Unban a user"),
            BotCommand("set", "⚙️ Re-register bot commands"),
        ]
        
        try:
            await client.set_bot_commands(commands=user_commands, scope=BotCommandScopeAllPrivateChats())
            logger.info("✅ User commands registered")
            
            for admin_id in dm.ADMINS:
                try:
                    await client.set_bot_commands(commands=admin_commands, scope=BotCommandScopeChat(chat_id=admin_id))
                    logger.info(f"✅ Admin commands registered for {admin_id}")
                except Exception as e:
                    logger.warning(f"⚠️ Could not set admin commands for {admin_id}: {e}")
        except Exception as e:
            logger.error(f"❌ Error in CommandVault: {e}")
            raise e

async def set_bot_commands(client):
    await CommandVault.set_bot_commands(client)
