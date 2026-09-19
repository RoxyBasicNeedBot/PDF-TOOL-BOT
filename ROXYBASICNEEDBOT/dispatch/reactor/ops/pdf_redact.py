# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
from tracer import logger

async def pdf_redact(input_file: str, cDIR: str, redact_text: str) -> tuple:
    """
    Search and black-out/redact sensitive text across all pages.
    """
    try:
        output_path = f"{cDIR}/outPut.pdf"
        doc = fitz.open(input_file)
        
        redacted_count = 0
        for page in doc:
            rects = page.search_for(redact_text)
            for rect in rects:
                page.add_redact_annot(rect, fill=(0, 0, 0)) # black fill
                redacted_count += 1
            if rects:
                page.apply_redactions()
                
        if redacted_count == 0:
            doc.close()
            return False, "Target text not found in PDF file"
            
        doc.save(output_path, deflate=True)
        doc.close()
        return True, output_path
    except Exception as e:
        logger.error(f"Error in pdf_redact: {e}", exc_info=True)
        return False, str(e)
