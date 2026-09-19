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

# Core state variables (renamed from statestore)

import os
from typing import Dict, List, Any

# MongoDB check
class DatabaseState:
    def __init__(self):
        self.MONGODB_URI = os.environ.get("MONGODB_URI", False)

dataBASE = DatabaseState()

# Active queues & lists
BANNED_USR_DB: List[int] = []
BANNED_GRP_DB: List[int] = []
CUSTOM_THUMBNAIL_U: List[int] = []
CUSTOM_THUMBNAIL_C: List[int] = []
GROUPS: List[int] = []
BETA: List[int] = []

# Global user states: [has_api, custom_filename, custom_caption]
DATA: Dict[int, List[int]] = {}

# Active operations tracking
works: Dict[str, List[Any]] = {
    "u": [], # private users list
    "g": []  # groups list
}

# Bot self identity info
myID: List[Any] = []

# Force sub channels invite links cache
invite_link: List[Dict[str, Any]] = []

# Admins requesting notification when bot restarts
ping_list: List[int] = []
