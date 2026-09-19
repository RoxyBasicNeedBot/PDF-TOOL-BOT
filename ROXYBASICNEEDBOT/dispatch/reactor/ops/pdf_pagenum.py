# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
from tracer import logger

async def pdf_pagenum(input_file: str, cDIR: str) -> tuple:
    """
    Inlay page numbers at the bottom-center of every page.
    """
    try:
        output_path = f"{cDIR}/outPut.pdf"
        doc = fitz.open(input_file)
        
        total_pages = doc.page_count
        for idx, page in enumerate(doc):
            pagenum_str = f"- {idx + 1} / {total_pages} -"
            text_width = fitz.get_text_length(pagenum_str, fontname="helv", fontsize=9)
            
            # Position at bottom-center (30px offset from bottom boundary)
            x = (page.rect.width - text_width) / 2
            y = page.rect.height - 30
            
            page.insert_text(fitz.Point(x, y), pagenum_str, fontsize=9, fontname="helv", color=(0.5, 0.5, 0.5))
            
        doc.save(output_path, deflate=True)
        doc.close()
        return True, output_path
    except Exception as e:
        logger.error(f"Error in pdf_pagenum: {e}", exc_info=True)
        return False, str(e)
