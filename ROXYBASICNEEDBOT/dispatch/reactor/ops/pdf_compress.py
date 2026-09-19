# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import os
import subprocess
from PIL import Image
from tracer import tracer
from sentinel import *

async def compressPDF(
    input_file: str, cDIR: str, returnRatio: bool = False, compression_level: str = "medium"
) -> (bool, str):
    """
    Compressing a PDF file can significantly reduce its file size, making it
    easier to share and store. This can be especially useful when sending files over
    the internet, as smaller file sizes can lead to faster uploading and downloading times.

    parameter:
        input_file : Here is the path of the file that the user entered
        cDIR       : This is the location of the directory that belongs to the specific user.
        compression_level : Compression quality level - "low" (best quality), "medium" (balanced), "high" (smallest size)

    return:
        bool        : Return True when the request is successful
        output_path : This is the path where the output file can be found.
    """
    try:
        # Compression level mapping
        COMPRESSION_SETTINGS = {
            "low": "/printer",      # Best quality, less compression
            "medium": "/ebook",     # Balanced (default)
            "high": "/screen"       # Maximum compression, lower quality
        }
        
        # Validate compression level
        if compression_level not in COMPRESSION_SETTINGS:
            logger.error(f"Invalid compression level: {compression_level}")
            return False, f"Invalid compression level: {compression_level}"
        
        
        # /screen, /ebook, /printer, /prepress, and /default.
        output_path = f"{cDIR}/outPut.pdf"

        # Set the Ghostscript command and options to compress the PDF
        gs_command = "gs"
        gs_options = [
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS={COMPRESSION_SETTINGS[compression_level]}",  # Dynamic compression level
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            "-sOutputFile={}".format(output_path),
            input_file,
        ]

        # Call Ghostscript to compress the PDF with enhanced error handling
        try:
            result = subprocess.call([gs_command] + gs_options, 
                                    stderr=subprocess.PIPE, 
                                    stdout=subprocess.PIPE)
            if result != 0:
                return False, "Ghostscript compression failed"
        except FileNotFoundError:
            return False, "Ghostscript not installed on server"
        except Exception as e:
            logger.error(f"Ghostscript error: {e}")
            return False, f"Compression error: {str(e)}"

        # FILE SIZE COMPARISON (RATIO)
        initialSize = os.path.getsize(input_file)
        compressedSize = os.path.getsize(output_path)
        ratio = (1 - (compressedSize / initialSize)) * 100

        if returnRatio:
            if (initialSize - compressedSize) > 1000000 or ratio >= 5:
                return (
                    [
                        await render.gSF(initialSize),
                        await render.gSF(compressedSize),
                        f"{ratio:.2f}",
                        compression_level  # Include compression level in result
                    ],
                    output_path,
                )
            else:
                return False, "cantCompressMore"

        return True, output_path

    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(e)
