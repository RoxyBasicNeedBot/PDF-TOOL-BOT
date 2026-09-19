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
import shutil
from pathlib import Path
from pyrogram import enums
from tracer import logger

class WorkspaceManager:
    _base_dir = Path("work/roxybasicneedbot")

    @classmethod
    def resolve_path(cls, message, mtype: bool = True) -> Path:
        if mtype:
            if message.chat.type == enums.ChatType.PRIVATE:
                return cls._base_dir / str(message.chat.id)
            else:
                return cls._base_dir / str(message.chat.id) / str(message.from_user.id)
        else:
            if message.message is None:
                token = message.data.split('|')[2] if len(message.data.split('|')) > 2 else "inline"
                return cls._base_dir / f"inline{token}"
            elif message.message.chat.type == enums.ChatType.PRIVATE:
                return cls._base_dir / str(message.message.chat.id)
            else:
                return cls._base_dir / str(message.message.chat.id) / str(message.message.from_user.id)

    @classmethod
    async def create(cls, message, mtype: bool = True) -> str:
        path = cls.resolve_path(message, mtype)
        if path.exists():
            return False
        path.mkdir(parents=True, exist_ok=True)
        return str(path)

    @classmethod
    async def check(cls, message, mtype: bool = True) -> str:
        path = cls.resolve_path(message, mtype)
        return str(path) if path.exists() else False

    @classmethod
    async def delete(cls, message, mtype: bool = True) -> None:
        path = cls.resolve_path(message, mtype)
        
        # Group deletion safety checks
        if mtype and message.chat.type != enums.ChatType.PRIVATE:
            parent = path.parent
            if parent.exists() and len(os.listdir(parent)) == 1:
                shutil.rmtree(parent, ignore_errors=True)
                return
        elif not mtype and message.message is not None and message.message.chat.type != enums.ChatType.PRIVATE:
            parent = path.parent
            if parent.exists() and len(os.listdir(parent)) == 1:
                shutil.rmtree(parent, ignore_errors=True)
                return
                
        shutil.rmtree(path, ignore_errors=True)

class WorkProxy:
    async def __call__(self, message, work: str = "check", mtype: bool = True):
        if work == "create":
            return await WorkspaceManager.create(message, mtype)
        elif work == "check":
            return await WorkspaceManager.check(message, mtype)
        elif work == "delete":
            return await WorkspaceManager.delete(message, mtype)

    async def work(self, message, work: str = "check", mtype: bool = True):
        return await self.__call__(message, work, mtype)

    async def create(self, message, mtype: bool = True):
        return await WorkspaceManager.create(message, mtype)

    async def check(self, message, mtype: bool = True):
        return await WorkspaceManager.check(message, mtype)

    async def delete(self, message, mtype: bool = True):
        return await WorkspaceManager.delete(message, mtype)

work = WorkProxy()
