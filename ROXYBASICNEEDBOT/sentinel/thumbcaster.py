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

from PIL import Image
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from pyrogram.enums import ChatType
from core.nexus import settings, images
from core.corestate import CUSTOM_THUMBNAIL_U, dataBASE
from tracer import logger
import os

class ThumbCaster:
    @staticmethod
    async def thumbMeta(thumbPath: str) -> int:
        try:
            parser = createParser(thumbPath)
            if parser:
                metadata = extractMetadata(parser)
                if metadata:
                    return metadata.get("height", 320)
            return 320
        except Exception as e:
            logger.error(f"Error in thumbMeta: {e}")
            return 320

    @classmethod
    async def formatThumb(cls, location: str) -> str:
        try:
            height = await cls.thumbMeta(location)
            img = Image.open(location)
            img.convert("RGB").save(location, "JPEG")
            
            img = Image.open(location)
            img.thumbnail((320, height))
            img.save(location, "JPEG")
            return location
        except Exception as e:
            logger.error(f"Error formatting thumbnail: {e}")
            return location

    @classmethod
    async def thumbName(cls, message, fileName: str, getAPI: bool = False) -> tuple:
        from ledger.safebox import db
        try:
            chat_id = message.chat.id
            chat_type = message.chat.type
            _, fileExt = os.path.splitext(fileName)
            
            info = {}
            if dataBASE.MONGODB_URI:
                info = await db.get_user_data(chat_id)
            
            file_name_out = settings.DEFAULT_NAME + fileExt if settings.DEFAULT_NAME else (info.get("fname") + fileExt if info.get("fname") else fileName)
            file_capt_out = settings.DEFAULT_CAPT if settings.DEFAULT_CAPT else (info.get("capt") if info.get("capt") else "")
            
            thumbnail_out = images.PDF_THUMBNAIL
            if dataBASE.MONGODB_URI and chat_type == ChatType.PRIVATE and chat_id in CUSTOM_THUMBNAIL_U:
                thumbnail_out = info.get("thumb", images.PDF_THUMBNAIL)
                
            if getAPI:
                return file_name_out, file_capt_out, thumbnail_out, info.get("api", 0)
            return file_name_out, file_capt_out, thumbnail_out
        except Exception as e:
            logger.error(f"Error in thumbName: {e}")
            return fileName, "", images.PDF_THUMBNAIL

async def thumbMeta(thumbPath: str) -> int:
    return await ThumbCaster.thumbMeta(thumbPath)

async def formatThumb(location: str) -> str:
    return await ThumbCaster.formatThumb(location)

async def thumbName(message, fileName: str, getAPI: bool = False) -> tuple:
    return await ThumbCaster.thumbName(message, fileName, getAPI)
