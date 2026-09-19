# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
from tracer import tracer


async def rotatePDF(input_file: str, angle: str, cDIR: str) -> (bool, str):
    """
    If a PDF file is rotated incorrectly, rotating it can help to correct the orientation of the pages so that they are displayed properly.
    Rotating a PDF file can also allow you to change the viewing angle of the document, which can be helpful when examining images or graphics.

    parameter:
        input_file : Here is the path of the file that the user entered
        cDIR       : This is the location of the directory that belongs to the specific user

    return:
        bool        : Return True when the request is successful
        output_path : This is the path where the output file can be found
    """
    try:
        output_path = f"{cDIR}/outPut.pdf"
        with fitz.open(input_file) as iNPUT:
            if angle == "rot90":
                for page in iNPUT:
                    page.set_rotation(90)
            elif angle == "rot180":
                for page in iNPUT:
                    page.set_rotation(180)
            elif angle == "rot270":
                for page in iNPUT:
                    page.set_rotation(-90)
            iNPUT.save(output_path)
        return True, output_path

    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(e)
