# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
from tracer import tracer
from ..actionhub import annotSet

colorSet = {
    "r": (1, 0, 0),
    "b": (0, 0, 1),
    "g": (0, 1, 0),
    "c1": (1, 1, 0),
    "c2": (1, 0, 1),
    "c3": (0, 1, 1),
    "c4": (1, 1, 1),
    "c5": (0, 0, 0),
}


async def stampPDF(input_file: str, cDIR: str, data: str) -> (bool, str):
    """
    The pdf stamp is a digital tool that enables users to apply a customizable stamp to a PDF document.
    The stamp can be used to indicate the document's status, such as "approved," "confidential," or "draft,".

    parameter:
        input_file : Here is the path of the file that the user entered
        cDIR       : This is the location of the directory that belongs to the specific user.

    return:
        bool        : Return True when the request is successful
        output_path : This is the path where the output file can be found.
    """
    try:
        output_path = f"{cDIR}/outPut.pdf"

        _, annot, colr = data.split("|")
        color = colorSet.get(f"{colr}", (1, 0, 0))

        annotation = annotSet.get(int(annot), 1)
        r = fitz.Rect(72, 72, 440, 200)

        with fitz.open(input_file) as doc:
            page = doc.load_page(0)
            annot = page.add_stamp_annot(r, stamp=int(f"{annot}"))
            annot.set_colors(stroke=color)
            annot.set_opacity(0.5)
            annot.update()
            doc.save(output_path)

        return True, output_path

    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(e)
