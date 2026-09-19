# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

"""
Compatibility shim layer mapping old legacy imports to restructured v2 paths.
"""

import os
import sys
import math
import shutil
import asyncio
import time
import re
from pyrogram import Client as RoxyBot, filters, enums
from tracer import logger

__all__ = [
    "os",
    "sys",
    "math",
    "shutil",
    "asyncio",
    "filters",
    "logger",
    "enums",
    "time",
    "re",
    "RoxyBot"
]
