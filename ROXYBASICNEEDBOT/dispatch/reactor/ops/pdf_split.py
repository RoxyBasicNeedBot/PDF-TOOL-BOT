# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import gc
from tracer import tracer
from PyPDF2 import PdfWriter, PdfReader


async def splitPDF(input_file: str, cDIR: str, imageList: list) -> (bool, str):
    """
     The function to split a PDF file into smaller PDF files based on the number of pages or a specific
     range of pages is a useful tool for managing large PDF files

    parameter:
        input_file    : Here is the path of the file that the user entered
        cDIR          : This is the location of the directory that belongs to the specific user.
        imageList     : List of page numbers that the user requires

    return:
        bool        : Return True when the request is successful
        output_path : This is the path where the output file can be found.
    """
    splitInputPdf = None
    splitOutput = None
    try:
        output_path = f"{cDIR}/outPut.pdf"
        splitInputPdf = PdfReader(input_file, strict=False)
        splitOutput = PdfWriter()

        for i in imageList:
            if i <= len(splitInputPdf.pages):
                splitOutput.add_page(splitInputPdf.pages[i - 1])

        with open(output_path, "wb") as output_stream:
            splitOutput.write(output_stream)

        return True, output_path

    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(e)

    finally:
        # Explicitly free memory
        del splitOutput
        del splitInputPdf
        gc.collect()
