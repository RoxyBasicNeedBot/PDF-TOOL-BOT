# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
import qrcode
import os
from tracer import logger

async def pdf_qr(input_file: str, cDIR: str, url: str, page_num: int = 0) -> tuple:
    """
    Generate QR code image from URL and embed it in a PDF page corner.
    """
    try:
        output_path = f"{cDIR}/outPut.pdf"
        
        # Build QR code image
        qr = qrcode.QRCode(version=1, box_size=5, border=1)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        qr_img_path = f"{cDIR}/qr_code.png"
        img.save(qr_img_path)
        
        doc = fitz.open(input_file)
        if page_num < 0 or page_num >= doc.page_count:
            page_num = doc.page_count - 1
            
        page = doc[page_num]
        
        # Position at top-right corner (size 80x80)
        rect = fitz.Rect(page.rect.width - 100, 20, page.rect.width - 20, 100)
        page.insert_image(rect, filename=qr_img_path)
        
        doc.save(output_path, deflate=True)
        doc.close()
        
        if os.path.exists(qr_img_path):
            os.remove(qr_img_path)
            
        return True, output_path
    except Exception as e:
        logger.error(f"Error in pdf_qr: {e}", exc_info=True)
        return False, str(e)
