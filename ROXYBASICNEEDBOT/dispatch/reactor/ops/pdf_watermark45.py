# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
from tracer import tracer 


async def add_text_watermark(input_file, output_file, watermark_text):
    try:
        with fitz.open(input_file) as pdf:
            for page in pdf:

                font = fitz.Font(fontname="tiit")
                text_width = font.text_length(
                    watermark_text, fontsize=int(page.bound().height // 20)
                )

                tw = fitz.TextWriter(page.rect, opacity=0.5, color=(0, 0, 0))

                txt_bottom, txt_left = int((page.bound().width - text_width) / 2), int(
                    (page.bound().height - page.bound().height / 20) / 2
                )

                tw.append(
                    (txt_bottom, txt_left),
                    watermark_text,
                    fontsize=int(page.bound().height // 20),
                    font=font,
                )
                tw.write_text(page)

            pdf.save(output_file)
        return True, output_file
    except Exception as e:
        logger.error(f"1️⃣ 🐞 Error: {e}", exc_info=True)
        return False, str(e)


async def watermarkPDF(input_file: str, cDIR: str, watermark) -> (bool, str):
    try:
        output_path = f"{cDIR}/outPut.pdf"

        success, output_file = await add_text_watermark(
            input_file=input_file, output_file=output_path, watermark_text=watermark
        )
        if not success:
            return False, output_file
        return True, output_file
    except Exception as e:
        logger.error(f"2️⃣ 🐞 Error: {e}", exc_info=True)
        return False, str(e)
