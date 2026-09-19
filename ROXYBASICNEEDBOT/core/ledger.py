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

import os
from typing import Any
from pyrogram.types import Message
from pyrogram.enums import ChatType
from tracer import logger

class EventLedger:
    def __init__(self):
        self.LOG_CHANNEL = os.environ.get("LOG_CHANNEL", False)
        self.LOG_FILE = os.environ.get("LOG_FILE", False)
        self.LOG_TEXT = "#newUser @roxybasicneedbot1/ROXYBASICNEEDBOT\n\nID: `{}`\nView Profile: {}"
        self.LOG_TEXT_C = "#newChat @roxybasicneedbot1/ROXYBASICNEEDBOT\n\nID: `{}`\nGroup Title: {}\nTotal Users: {}\nUserName: {}"

    async def newUser(self, bot_client: Any, message: Message, lang_code: str, referID: int) -> None:
        try:
            from ledger.safebox import db
            if message.chat.type != ChatType.PRIVATE:
                if not await db.is_chat_exist(message.chat.id):
                    await db.add_chat(message.chat.id, message.chat.title)
                return

            if not await db.is_user_exist(message.chat.id):
                await db.add_user(
                    message.chat.id, message.chat.first_name, lang_code
                )
                if self.LOG_CHANNEL:
                    profile = message.chat.first_name if not message.chat.username else f"[{message.chat.first_name}](tg://user?id={message.chat.id})"
                    await bot_client.send_message(
                        chat_id=int(self.LOG_CHANNEL),
                        text=self.LOG_TEXT.format(message.chat.id, profile),
                        disable_web_page_preview=True
                    )
        except Exception as e:
            logger.error(f"Error in EventLedger.newUser: {e}")

    async def newChat(self, bot_client: Any, message: Message, lang_code: str) -> None:
        try:
            from ledger.safebox import db
            if not await db.is_chat_exist(message.chat.id):
                await db.add_chat(message.chat.id, message.chat.title)
                if self.LOG_CHANNEL:
                    users_count = await bot_client.get_chat_members_count(message.chat.id)
                    username = f"@{message.chat.username}" if message.chat.username else "Private Group"
                    await bot_client.send_message(
                        chat_id=int(self.LOG_CHANNEL),
                        text=self.LOG_TEXT_C.format(
                            message.chat.id, message.chat.title, users_count, username
                        ),
                        disable_web_page_preview=True
                    )
        except Exception as e:
            logger.error(f"Error in EventLedger.newChat: {e}")

log = EventLedger()
