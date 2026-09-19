# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
from tracer import logger

async def pdf_flatten(input_file: str, cDIR: str) -> tuple:
    """
    Flatten interactive form fields (widgets) and annotations in PDF to static elements.
    """
    try:
        output_path = f"{cDIR}/outPut.pdf"
        doc = fitz.open(input_file)
        
        # Flatten page contents
        for page in doc:
            page.flatten()
            
        doc.save(output_path, deflate=True)
        doc.close()
        return True, output_path
    except Exception as e:
        logger.error(f"Error in pdf_flatten: {e}", exc_info=True)
        return False, str(e)
