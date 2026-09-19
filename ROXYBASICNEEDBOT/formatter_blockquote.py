#!/usr/bin/env python3
# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

"""
Formatter utility to apply Telegram HTML blockquote tags dynamically to text files.
"""

import re
from typing import Dict, List, Tuple

class TelegramBlockquoteFormatter:
    def __init__(self):
        self.rules: Dict[str, List[Tuple[str, str]]] = {
            "overload": [
                (r"(☠.*?☠)", r"<blockquote>\1</blockquote>"),
                (r"(\n\n)([^\n]+queue[^\n]+)", r"\1<blockquote>\2</blockquote>")
            ],
            "greeting": [
                (r"^(Hey[^!\n]+!)", r"<blockquote>\1</blockquote>")
            ]
        }

    def format_string(self, text: str, rule_name: str) -> str:
        """
        Apply regex blockquote rules to the specified text string.
        """
        if rule_name not in self.rules:
            return text
        for pattern, replacement in self.rules[rule_name]:
            text = re.sub(pattern, replacement, text)
        return text

if __name__ == "__main__":
    formatter = TelegramBlockquoteFormatter()
    sample = "☠ OVERLOAD DETECTED ☠\n\nI noticed that your work was also in queue"
    formatted = formatter.format_string(sample, "overload")
    print("Formatted Blockquote:\n", formatted)
