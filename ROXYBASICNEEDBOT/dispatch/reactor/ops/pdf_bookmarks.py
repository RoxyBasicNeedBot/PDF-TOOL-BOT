# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
from tracer import logger

async def pdf_bookmarks(input_file: str, cDIR: str) -> tuple:
    """
    Extract existing Table of Contents/bookmarks from PDF and save as a text document.
    """
    try:
        doc = fitz.open(input_file)
        toc = doc.get_toc() # Returns list of [level, title, page]
        doc.close()
        
        if not toc:
            return False, "No Table of Contents (bookmarks) found in this PDF"
            
        output_path = f"{cDIR}/bookmarks.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("📚 RoxyBasicNeedBot PDF Table of Contents 📚\n")
            f.write("==============================================\n\n")
            for lvl, title, page in toc:
                indent = "  " * (lvl - 1)
                f.write(f"{indent}• {title} (Page {page})\n")
                
        return True, output_path
    except Exception as e:
        logger.error(f"Error in pdf_bookmarks: {e}", exc_info=True)
        return False, str(e)
