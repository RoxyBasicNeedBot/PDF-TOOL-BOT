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
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from tracer import logger

class AiogramNexus:
    def __init__(self):
        self.token = os.environ.get("BRIDGE_TOKEN")
        self.bot = None
        self.dp = None
        if self.token:
            self.bot = Bot(token=self.token)
            self.dp = Dispatcher()
            self._register_handlers()
            logger.info("aiogram bridge instance initialized successfully")

    def _register_handlers(self):
        @self.dp.message(Command("bridge_status"))
        async def status_handler(message: types.Message):
            await message.reply("🔄 Roxy B2B Bridge is Active and Listening!")

        @self.dp.message(lambda msg: msg.document is not None)
        async def document_relay_receiver(message: types.Message):
            # Receives relayed files from secondary bots and forward to log channel or process
            logger.info(f"Bridge received relayed document from user/bot {message.from_user.id}: {message.document.file_name}")
            # Automatically forward/save or process
            log_channel = os.environ.get("LOG_CHANNEL")
            if log_channel:
                await message.bot.send_document(
                    chat_id=int(log_channel),
                    document=message.document.file_id,
                    caption=f"📡 **Relayed via Bridge B2B**\nFrom: `{message.from_user.id}`\nFile Name: `{message.document.file_name}`"
                )
                await message.reply("✅ Relayed document successfully logged to channel!")

    async def start_polling(self):
        if self.dp and self.bot:
            logger.info("Starting aiogram bridge long polling...")
            await self.dp.start_polling(self.bot)

nexus_aiogram = AiogramNexus()
