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
from typing import Optional, Callable
from pyrogram import filters
from pyrogram.types import Message
from collections import defaultdict
from tracer import logger

class DialogStream:
    def __init__(self):
        self._conversations = defaultdict(dict)
        self._locks = defaultdict(asyncio.Lock)

    async def ask(
        self,
        client,
        chat_id: int,
        text: str,
        filters: Optional[Callable] = None,
        timeout: int = 300,
        reply_to_message_id: Optional[int] = None,
        reply_markup=None
    ) -> Optional[Message]:
        async with self._locks[chat_id]:
            try:
                sent_msg = await client.send_message(
                    chat_id=chat_id,
                    text=text,
                    reply_to_message_id=reply_to_message_id,
                    reply_markup=reply_markup
                )
                
                future = asyncio.get_event_loop().create_future()
                self._conversations[chat_id] = {
                    "future": future,
                    "filters": filters
                }
                
                try:
                    response = await asyncio.wait_for(future, timeout=timeout)
                    return response
                except asyncio.TimeoutError:
                    logger.warning(f"DialogStream: Timeout waiting for response from {chat_id}")
                    return None
                finally:
                    self._conversations.pop(chat_id, None)
            except Exception as e:
                logger.error(f"Error in DialogStream.ask: {e}")
                return None

    def resolve_response(self, client, chat_id: int, message: Message) -> bool:
        if chat_id in self._conversations:
            conv = self._conversations[chat_id]
            fut = conv["future"]
            fil = conv["filters"]
            
            if not fut.done():
                try:
                    if fil is None or fil(client, message):
                        fut.set_result(message)
                        return True
                except Exception as e:
                    logger.error(f"Error evaluating filter in DialogStream: {e}")
        return False

dialog = DialogStream()

async def ask(client, chat_id, text, filters=None, timeout=300, reply_to_message_id=None, reply_markup=None):
    return await dialog.ask(client, chat_id, text, filters, timeout, reply_to_message_id, reply_markup)

def setup_conversation_handler(client):
    @client.on_message(filters.private & filters.incoming, group=-100)
    async def conv_handler(bot, message):
        chat_id = message.chat.id
        if dialog.resolve_response(bot, chat_id, message):
            message.stop_propagation()
