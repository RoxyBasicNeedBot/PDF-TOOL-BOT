# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import asyncio
from tracer import tracer
from concurrent.futures import ThreadPoolExecutor

try:
    roxybasicneedbot = False  # Change to False else never work
    import ocrmypdf
except Exception:
    roxybasicneedbot = True

# Thread pool for CPU-intensive OCR work (limit to 2 concurrent OCR jobs)
_ocr_executor = ThreadPoolExecutor(max_workers=2)


def _run_ocr_sync(input_file: str, output_path: str) -> str:
    """
    Synchronous OCR wrapper for thread pool execution.
    Uses file PATHS, not file handles.
    """
    ocrmypdf.ocr(
        input_file,    # Pass file PATH, not handle
        output_path,   # Pass file PATH, not handle
        deskew=True,
    )
    return output_path


async def ocrPDF(input_file: str, cDIR: str) -> (bool, str):
    """
    Add OCR layer to PDF asynchronously.
    Runs in thread pool to avoid blocking the event loop.
    """
    try:
        output_path = f"{cDIR}/outPut.pdf"
        
        # Run OCR in thread pool to avoid blocking event loop
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(_ocr_executor, _run_ocr_sync, input_file, output_path)
        
        return True, output_path

    except ocrmypdf.exceptions.PriorOcrFoundError:
        # PDF already has OCR layer
        logger.warning(f"OCR already exists in PDF: {input_file}")
        return False, "PDF already contains OCR text layer"
    
    except ocrmypdf.exceptions.EncryptedPdfError:
        # PDF is encrypted
        logger.warning(f"Cannot OCR encrypted PDF: {input_file}")
        return False, "Cannot add OCR to encrypted PDF. Please decrypt first."
    
    except ocrmypdf.exceptions.InputFileError as e:
        # Input file issue
        logger.error(f"OCR input file error: {e}")
        return False, f"Invalid PDF file: {str(e)}"
    
    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, f"OCR failed: {str(Error)}"
