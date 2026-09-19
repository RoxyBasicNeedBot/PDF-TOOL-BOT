#!/usr/bin/env python3
# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

"""
Formatter utility to apply Telegram HTML italic tags to headings inside blockquotes.
"""

import re
from typing import Dict

class TelegramItalicFormatter:
    def __init__(self):
        self.header_regex = re.compile(r"<blockquote>([⚙️📋⚠️🛈⛔].*?)</blockquote>")

    def make_header_italic(self, content: str) -> str:
        """
        Embed italic HTML tags inside all blockquoted headings.
        """
        return self.header_regex.sub(r"<blockquote><i>\1</i></blockquote>", content)

if __name__ == "__main__":
    formatter = TelegramItalicFormatter()
    sample = "<blockquote>⚙️ SETTINGS PAGE ⚙️</blockquote>"
    formatted = formatter.make_header_italic(sample)
    print("Formatted Italic Heading:\n", formatted)
