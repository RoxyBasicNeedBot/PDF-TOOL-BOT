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

import gc
import psutil
from tracer import logger

class RamGuard:
    @staticmethod
    def get_available_memory_mb() -> float:
        try:
            return psutil.virtual_memory().available / (1024 * 1024)
        except Exception:
            return 0.0

    @staticmethod
    def get_percent() -> float:
        try:
            return psutil.virtual_memory().percent
        except Exception:
            return 100.0

    @classmethod
    def check_memory(cls, file_size_bytes: int, multiplier: float = 3.0) -> bool:
        try:
            needed = (file_size_bytes * multiplier) / (1024 * 1024)
            available = cls.get_available_memory_mb()
            
            logger.debug(f"Memory check: need ~{needed:.0f}MB, available {available:.0f}MB")
            if available < needed:
                logger.warning(f"Insufficient memory! Need {needed:.0f}MB but only {available:.0f}MB is free.")
                return False
            return True
        except Exception as e:
            logger.error(f"Memory guard check failed: {e}")
            return True

    @staticmethod
    def cleanup():
        collected = gc.collect()
        logger.debug(f"GC collected {collected} objects.")

def get_available_memory_mb():
    return RamGuard.get_available_memory_mb()

def get_memory_usage_percent():
    return RamGuard.get_percent()

def check_memory_for_file(file_size_bytes: int, multiplier: float = 3.0) -> bool:
    return RamGuard.check_memory(file_size_bytes, multiplier)

def force_cleanup():
    RamGuard.cleanup()
