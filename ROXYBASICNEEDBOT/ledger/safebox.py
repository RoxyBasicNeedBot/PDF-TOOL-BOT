# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
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

import datetime
from core.corestate import dataBASE
from core.nexus import settings
from typing import Dict, Any, Tuple
from motor.motor_asyncio import AsyncIOMotorClient

class RoxySafebox:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_db()
        return cls._instance

    def _init_db(self):
        self._client = None
        self._client_loop = None
        self.db = None
        self.col = None
        self.grp = None

    def _ensure_connected(self):
        if not dataBASE.MONGODB_URI:
            return
        if self._client is None:
            try:
                self._client = AsyncIOMotorClient(dataBASE.MONGODB_URI)
                self.db = self._client["roxybasicneedbot-pdftool"]
                self.col = self.db.users
                self.grp = self.db.groups
            except Exception as e:
                from tracer import logger
                logger.debug(f"⚠️ MongoDB connection init warning: {e}")

    def new_user(self, id: int, name: str, lang_code: str) -> Dict[str, Any]:
        user_info = {
            "id": id,
            "name": name,
            "join_date": datetime.date.today().isoformat()
        }
        if lang_code and lang_code != settings.DEFAULT_LANG:
            user_info["lang"] = lang_code
        return user_info

    def new_group(self, id: int, title: str) -> dict:
        return dict(
            id=id,
            title=title,
            join_date=datetime.date.today().isoformat()
        )

    async def add_user(self, id: int, name: str, lang_code: str) -> None:
        self._ensure_connected()
        if self.col is not None:
            try:
                import asyncio
                user = self.new_user(id, name, lang_code)
                await asyncio.wait_for(self.col.insert_one(user), timeout=5.0)
            except Exception as e:
                from tracer import logger
                logger.debug(f"⚠️ MongoDB add_user error: {e}")

    async def delete_user(self, id: int) -> None:
        self._ensure_connected()
        if self.col is not None:
            try:
                import asyncio
                await asyncio.wait_for(self.col.delete_one({'id': int(id)}), timeout=5.0)
            except Exception as e:
                from tracer import logger
                logger.debug(f"⚠️ MongoDB delete_user error: {e}")

    async def is_user_exist(self, id: int) -> bool:
        self._ensure_connected()
        if self.col is None:
            return False
        try:
            import asyncio
            user = await asyncio.wait_for(self.col.find_one({'id': int(id)}), timeout=5.0)
            return True if user else False
        except Exception as e:
            from tracer import logger
            logger.debug(f"⚠️ MongoDB is_user_exist error: {e}")
            return False

    async def get_user_data(self, id: int) -> dict:
        self._ensure_connected()
        if self.col is None:
            return {}
        try:
            import asyncio
            user = await asyncio.wait_for(self.col.find_one({'id': int(id)}), timeout=5.0)
            return user or {}
        except Exception as e:
            from tracer import logger
            logger.debug(f"⚠️ MongoDB get_user_data error: {e}")
            return {}

    async def get_all_users(self):
        self._ensure_connected()
        if self.col is None:
            return
        return self.col.find({})

    async def get_banned(self) -> Tuple[list, list]:
        self._ensure_connected()
        if self.col is None:
            return [], []
        try:
            import asyncio
            b_users = []
            async for user in self.col.find({'banned': {'$exists': True}}):
                b_users.append(user['id'])
            b_chats = []
            if self.grp is not None:
                async for chat in self.grp.find({'banned': {'$exists': True}}):
                    b_chats.append(chat['id'])
            return b_users, b_chats
        except Exception as e:
            from tracer import logger
            logger.debug(f"⚠️ MongoDB get_banned error: {e}")
            return [], []

    async def set_key(self, id: int, key: str, value: Any, typ: str = "user") -> None:
        self._ensure_connected()
        cluster = self.col if typ == "user" else self.grp
        if cluster is not None:
            try:
                import asyncio
                await asyncio.wait_for(cluster.update_one({'id': int(id)}, {'$set': {key: value}}, upsert=True), timeout=5.0)
            except Exception as e:
                from tracer import logger
                logger.debug(f"⚠️ MongoDB set_key error: {e}")

    async def get_key(self, id: int, key: str, typ: str = "user") -> Any:
        self._ensure_connected()
        cluster = self.col if typ == "user" else self.grp
        if cluster is not None:
            try:
                import asyncio
                data = await asyncio.wait_for(cluster.find_one({'id': int(id)}), timeout=5.0)
                return data.get(key, False) if data else False
            except Exception as e:
                from tracer import logger
                logger.debug(f"⚠️ MongoDB get_key error: {e}")
                return False
        return False

    async def dlt_key(self, id: int, key: str, typ: str = "user") -> None:
        self._ensure_connected()
        cluster = self.col if typ == "user" else self.grp
        if cluster is not None:
            try:
                import asyncio
                await asyncio.wait_for(cluster.update_one({'id': int(id)}, {'$unset': {key: ""}}), timeout=5.0)
            except Exception as e:
                from tracer import logger
                logger.debug(f"⚠️ MongoDB dlt_key error: {e}")

    async def add_chat(self, id: int, title: str) -> None:
        self._ensure_connected()
        if self.grp is not None:
            try:
                import asyncio
                chat = self.new_group(id, title)
                await asyncio.wait_for(self.grp.insert_one(chat), timeout=5.0)
            except Exception as e:
                from tracer import logger
                logger.debug(f"⚠️ MongoDB add_chat error: {e}")

    async def is_chat_exist(self, id: int) -> bool:
        self._ensure_connected()
        if self.grp is None:
            return False
        try:
            import asyncio
            chat = await asyncio.wait_for(self.grp.find_one({'id': int(id)}), timeout=5.0)
            return True if chat else False
        except Exception as e:
            from tracer import logger
            logger.debug(f"⚠️ MongoDB is_chat_exist error: {e}")
            return False

    async def get_all_chats(self):
        self._ensure_connected()
        if self.grp is None:
            return
        return self.grp.find({})

    async def get_beta(self) -> list:
        self._ensure_connected()
        if self.col is None:
            return []
        try:
            import asyncio
            beta_users = []
            async for user in self.col.find({'beta': True}):
                beta_users.append(user['id'])
            return beta_users
        except Exception as e:
            from tracer import logger
            logger.debug(f"⚠️ MongoDB get_beta error: {e}")
            return []

    async def get_db_size(self) -> int:
        self._ensure_connected()
        if self.db is None:
            return 0
        try:
            import asyncio
            stats = await asyncio.wait_for(self.db.command("dbstats"), timeout=5.0)
            return stats.get("dataSize", 0)
        except Exception as e:
            from tracer import logger
            logger.debug(f"⚠️ MongoDB get_db_size error: {e}")
            return 0

    async def total_users_count(self) -> int:
        self._ensure_connected()
        if self.col is None:
            return 0
        try:
            import asyncio
            return await asyncio.wait_for(self.col.count_documents({}), timeout=5.0)
        except Exception as e:
            from tracer import logger
            logger.debug(f"⚠️ MongoDB total_users_count error: {e}")
            return 0

    async def total_chat_count(self) -> int:
        self._ensure_connected()
        if self.grp is None:
            return 0
        try:
            import asyncio
            return await asyncio.wait_for(self.grp.count_documents({}), timeout=5.0)
        except Exception as e:
            from tracer import logger
            logger.debug(f"⚠️ MongoDB total_chat_count error: {e}")
            return 0

db = RoxySafebox()
