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
import urllib.request
import re
from typing import List
from tracer import logger

class BotCredentials:
    def __init__(self):
        self.API_ID = os.environ.get("API_ID")
        if self.API_ID:
            self.API_ID = int(self.API_ID)
        self.API_HASH = os.environ.get("API_HASH")
        self.API_TOKEN = os.environ.get("API_TOKEN")

class AccessControl:
    def __init__(self):
        self.ADMINS: List[int] = list(set(int(x) for x in os.environ.get("ADMINS", "").split() if x.strip().isdigit()))
        owner_str = os.environ.get("OWNER_ID", "").strip()
        if owner_str.isdigit():
            self.ADMINS.append(int(owner_str))
        self.ADMINS = list(set(self.ADMINS))
        
        self.ADMIN_ONLY: bool = os.environ.get("ADMIN_ONLY", "False").lower() == "true"
        self.BANNED_USERS: List[int] = list(set(int(x) for x in os.environ.get("BANNED_USERS", "").split() if x.strip().isdigit()))
        self.ADMIN_GROUPS: List[int] = list(set(int(x) for x in os.environ.get("ADMIN_GROUPS", "").split() if x.strip().lstrip("-").isdigit()))
        self.ADMIN_GROUP_ONLY: bool = os.environ.get("ADMIN_GROUP_ONLY", "False").lower() == "true"
        self.BANNED_GROUP: List[int] = list(set(int(x) for x in os.environ.get("BANNED_GROUP", "").split() if x.strip().lstrip("-").isdigit()))
        self.ONLY_GROUP_ADMIN: bool = os.environ.get("ONLY_GROUP_ADMIN", "False").lower() == "true"

class MediaAssets:
    def __init__(self):
        self.PDF_THUMBNAIL: str = None
        self.THUMBNAIL_URL: str = "https://i.ibb.co/Q7HwWbLB/file-29499.jpg"
        self.BANNED_PIC: str = "https://i.ibb.co/7th09cw3/file-29663.jpg"
        self.BIG_FILE: str = "https://i.ibb.co/6797w47D/file-29662.jpg"
        
        # Scrape dynamic welcome image
        self.WELCOME_PIC = self.fetch_welcome_image()

    def fetch_welcome_image(self) -> str:
        # Load welcome image dynamically from the official Telegram post
        # This keeps the image verified and prevents copy-pasted versions from bypassing ownership
        try:
            # Post link encoded to prevent simple text replacement
            url_parts = [104, 116, 116, 112, 115, 58, 47, 47, 116, 46, 109, 101, 47, 114, 111, 120, 121, 98, 97, 115, 105, 99, 110, 101, 101, 100, 98, 111, 116, 49, 47, 49, 54, 57]
            url = "".join(chr(x) for x in url_parts)
            
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            with urllib.request.urlopen(req, timeout=8) as response:
                html = response.read().decode('utf-8')
            match = re.search(r'<meta\s+property="og:image"\s+content="([^"]+)"', html)
            if match:
                img_url = match.group(1)
                if "telesco.pe" not in img_url:
                    logger.info(f"Dynamic Welcome Photo Loaded: {img_url}")
                    return img_url
                else:
                    logger.warning("Dynamic photo is a temporary telesco.pe link. Using internal fallback.")
        except Exception as e:
            logger.warning(f"Unable to fetch dynamic welcome photo: {e}. Using internal fallback.")
        return "https://i.ibb.co/Fk0k6qnz/file-29661.jpg"

class BotSettings:
    def __init__(self):
        self.COFFEE: bool = os.environ.get("COFFEE", "True").lower() == "true"
        self.SEND_RESTART: bool = os.environ.get("SEND_RESTART", "True").lower() == "true"
        self.PROTECT_CONTENT: bool = os.environ.get("PROTECT_CONTENT", "False").lower() == "true"
        self.UPDATE_CHANNEL: int = int(os.environ.get("UPDATE_CHANNEL", 0)) or False
        self.UPDATE_CHANNEL_2: int = int(os.environ.get("UPDATE_CHANNEL_2", 0)) or False
        self.FORCE_SUB_CHANNELS: list = []
        self.CONVERT_API: str = os.environ.get("CONVERT_API", False)
        self.MAX_FILE_SIZE: int = int(os.environ.get("MAX_FILE_SIZE", 200))
        self.DEFAULT_NAME: str = os.environ.get("DEFAULT_NAME", False)
        self.DEFAULT_CAPT: str = os.environ.get("DEFAULT_CAPTION", False)
        self.DEFAULT_LANG: str = os.environ.get("DEFAULT_LANG", "eng").lower()
        self.MULTI_LANG_SUP: bool = os.environ.get("MULTI_LANG_SUP", "True").lower() == "true"
        self.REPORT: str = "https://t.me/roxybasicneedbot1"
        self.FEEDBACK: str = "https://t.me/roxybasicneedbot1"
        self.SOURCE_CODE: str = "https://github.com/RoxyBasicNeedBot"
        owner_str = os.environ.get("OWNER_ID", "").strip()
        self.OWNER_ID: int = int(owner_str) if owner_str.isdigit() else 0
        self.OWNER_USERNAME: str = os.environ.get("OWNER_USERNAME", "@roxybasicneedbot1")
        self.OWNED_CHANNEL: str = "https://t.me/roxybasicneedbot1"
        self.REFER_BETA: bool = os.environ.get("REFER_BETA", "False").lower() == "true"
        self.STOP_BOT: bool = os.environ.get("STOP_BOT", "False").lower() == "true"
        self.INLINE_SEARCH: bool = os.environ.get("INLINE_SEARCH", "True").lower() == "true"

class RoxyNexus:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.creds = BotCredentials()
            cls._instance.access = AccessControl()
            cls._instance.media = MediaAssets()
            cls._instance.runtime = BotSettings()
        return cls._instance

nexus = RoxyNexus()
bot = nexus.creds
dm = nexus.access
group = nexus.access
images = nexus.media
settings = nexus.runtime
