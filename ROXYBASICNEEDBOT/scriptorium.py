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

from core.nexus import bot
from telebot import async_telebot

class LazyTeleBot:
    def __init__(self, token, parse_mode="Markdown"):
        self.token = token
        self.parse_mode = parse_mode
        self._client = None

    def _ensure_client(self):
        if self._client is None and self.token:
            self._client = async_telebot.AsyncTeleBot(self.token, parse_mode=self.parse_mode)
        return self._client

    def __getattr__(self, name):
        client = self._ensure_client()
        if client is None:
            raise AttributeError("API_TOKEN is not configured for telebot")
        return getattr(client, name)

class RoxyScriptorium:
    def __init__(self):
        self.PDF = {}
        self.works = {"u": [], "g": []}
        self.telebot = LazyTeleBot(bot.API_TOKEN, parse_mode="Markdown") if bot.API_TOKEN else None

_engine = RoxyScriptorium()
PDF = _engine.PDF
works = _engine.works
roxyTeleBot = _engine.telebot
