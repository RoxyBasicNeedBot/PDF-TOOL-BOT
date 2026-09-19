# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
from tracer import logger

async def pdf_sign(input_file: str, cDIR: str, sign_text: str, page_num: int = 0, x: float = 50.0, y: float = 700.0) -> tuple:
    """
    Overlay a custom signature text on a specific PDF page.
    """
    try:
        output_path = f"{cDIR}/outPut.pdf"
        doc = fitz.open(input_file)
        
        if page_num < 0 or page_num >= doc.page_count:
            page_num = doc.page_count - 1
            
        page = doc[page_num]
        
        # Add signature overlay text
        # Black color, Outfit/Helvetica-like size 11
        page.insert_text(fitz.Point(x, y), sign_text, fontsize=11, color=(0.1, 0.1, 0.1))
        
        doc.save(output_path, deflate=True)
        doc.close()
        return True, output_path
    except Exception as e:
        logger.error(f"Error in pdf_sign: {e}", exc_info=True)
        return False, str(e)
