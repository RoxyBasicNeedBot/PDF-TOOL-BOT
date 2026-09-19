# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import os
import fitz
import asyncio
from tracer import tracer

try:
    from pdf2docx import Converter
    PDF2DOCX_AVAILABLE = True
except ImportError:
    PDF2DOCX_AVAILABLE = False
    logger.warning("pdf2docx not installed. PDF to Word conversion will not work.")


async def pdfToWord(input_file: str, cDIR: str) -> (bool, str):
    """
    Convert PDF to editable Word document (DOCX) with preserved formatting.
    
    This function uses pdf2docx library to convert PDF files to Microsoft Word format,
    attempting to preserve the original layout, formatting, images, and tables.
    
    Args:
        input_file: Path to input PDF file
        cDIR: User's working directory for temporary files
    
    Returns:
        (True, output_path) on success
        (False, error_message) on failure
    """
    try:
        # Check if library is available
        if not PDF2DOCX_AVAILABLE:
            return False, "PDF to Word converter not available. Please contact bot admin."
        
        # Check if input file exists (with retry for Docker filesystem sync issues)
        for attempt in range(3):
            if os.path.exists(input_file):
                # Force filesystem sync by opening and closing the file
                try:
                    with open(input_file, 'rb') as f:
                        f.read(1)  # Read 1 byte to ensure file is accessible
                    break
                except Exception:
                    pass
            await asyncio.sleep(0.5)
        
        if not os.path.exists(input_file):
            logger.error(f"Input file not found after retries: {input_file}")
            return False, "Input file not found. Please try again."
        
        logger.debug(f"📂 Opening PDF for Word conversion: {input_file}, Size: {os.path.getsize(input_file)}")
        
        output_path = f"{cDIR}/output.docx"
        cv = None
        
        try:
            # First attempt: Try with multi-processing for speed
            cv = Converter(input_file)
            cv.convert(
                output_path,
                start=0,
                end=None,
                multi_processing=True
            )
            cv.close()
            cv = None
            
        except TypeError as te:
            # Handle PDFs with malformed color/shape data (NoneType errors)
            # This is a known issue with certain PDFs that have None color values
            if cv:
                cv.close()
                cv = None
            
            logger.warning(f"Multi-processing conversion failed, trying single-threaded: {te}")
            
            # Clean up partial output if exists
            if os.path.exists(output_path):
                os.remove(output_path)
            
            # Second attempt: Try without multi-processing (often helps with problematic PDFs)
            cv = Converter(input_file)
            try:
                cv.convert(
                    output_path,
                    start=0,
                    end=None,
                    multi_processing=False  # Disable multi-processing
                )
            except TypeError as te2:
                cv.close()
                # If still failing, it's a PDF with unsupported color/shape elements
                error_msg = str(te2)
                if "NoneType" in error_msg and "len" in error_msg:
                    return False, "⚠️ This PDF contains unsupported graphics/shapes that cannot be converted. Try using 'PDF to Images' instead."
                raise te2
            cv.close()
            cv = None
        
        # Verify output file was created and is not empty
        if not os.path.exists(output_path):
            return False, "Conversion failed: Output file not created"
        
        if os.path.getsize(output_path) == 0:
            return False, "Conversion failed: Output file is empty"
        
        return True, output_path
        
    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        error_str = str(Error)
        
        # Provide user-friendly messages for common errors
        if "NoneType" in error_str and "len" in error_str:
            return False, "⚠️ This PDF contains unsupported graphics/shapes that cannot be converted. Try using 'PDF to Images' instead."
        elif "encrypted" in error_str.lower():
            return False, "⚠️ This PDF is encrypted. Please decrypt it first."
        elif "password" in error_str.lower():
            return False, "⚠️ This PDF requires a password. Please decrypt it first."
        
        return False, f"Conversion failed: {error_str}"
