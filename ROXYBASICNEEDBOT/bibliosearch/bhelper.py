# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import re
from urllib.parse import unquote_plus

class Util:
    """
    Utility helpers for parsing Libgen headers and filtering search queries.
    """
    @staticmethod
    async def get_filename(con_disp: str) -> str:
        """
        Extract and unquote file name from HTTP Content-Disposition header.
        """
        if not con_disp:
            return "document.pdf"
            
        fname_match = re.findall(r"filename\*=([^;]+)", con_disp, flags=re.IGNORECASE)
        if not fname_match:
            fname_match = re.findall(r"filename=([^;]+)", con_disp, flags=re.IGNORECASE)
            
        if not fname_match:
            return "document.pdf"
            
        name = fname_match[0].strip().strip('"')
        if "utf-8''" in name.lower():
            name = re.sub(r"utf-8''", "", name, flags=re.IGNORECASE)
            name = unquote_plus(name)
            
        return name.strip()

    @staticmethod
    async def filter_result(result: dict, filters: dict) -> bool:
        """
        Verify if a search item satisfies matching keywords criteria.
        """
        for field, target in filters.items():
            if str(target).lower() not in str(result.get(field, "")).lower():
                return False
        return True

    @staticmethod
    async def raise_error(status_code: int, resp: str) -> None:
        """
        Raise a ConnectionError with status codes.
        """
        raise ConnectionError(f"HTTP Error {status_code}: {resp}")
