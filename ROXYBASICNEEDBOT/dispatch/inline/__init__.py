# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𕕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

from pyrogram import Client as RoxyBot, filters, errors
from core.nexus import settings, images
from core.corestate import myID
from core.ledger import log
from sentinel import getLang, translate
from sentinel.workspace import work

from core.i18n import LANG_MAP as langList
from typing import Union
import asyncio

DATA = {}