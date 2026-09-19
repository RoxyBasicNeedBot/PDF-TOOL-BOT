#!/usr/bin/env python3
# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

"""
Batch URL patcher to find and normalize project repository links recursively.
"""

import os
from typing import List

class URLPatcher:
    def __init__(self, target_dir: str):
        self.target_dir = target_dir
        self.old_url = "github.com/RoxyBasicNeedBot"
        self.new_url = "github.com/RoxyBasicNeedBot"

    def scan_and_patch(self) -> int:
        """
        Scan directories recursively and patch target repository links.
        """
        patched_count = 0
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    if self._patch_file(file_path):
                        patched_count += 1
        return patched_count

    def _patch_file(self, file_path: str) -> bool:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            if self.old_url in content:
                content = content.replace(self.old_url, self.new_url)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                return True
        except Exception:
            pass
        return False

if __name__ == "__main__":
    patcher = URLPatcher(".")
    count = patcher.scan_and_patch()
    print(f"Patched {count} files successfully.")
