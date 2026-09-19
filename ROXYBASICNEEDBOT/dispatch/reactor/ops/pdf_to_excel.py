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
    import scriptorium as engineplumber
    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment
    PDFPLUMBER_AVAILABLE = True
except ImportError:
    PDFPLUMBER_AVAILABLE = False
    logger.warning("pdfplumber or openpyxl not installed. PDF to Excel conversion will not work.")


async def pdfToExcel(input_file: str, cDIR: str) -> (bool, str):
    """
    Convert PDF to Excel file, extracting tables and structured data.
    
    This function uses pdfplumber to detect and extract tables from PDF files,
    then creates an Excel workbook with openpyxl. Each table becomes a separate sheet.
    
    Args:
        input_file: Path to input PDF file
        cDIR: User's working directory for temporary files
    
    Returns:
        (True, output_path) on success
        (False, error_message) on failure
    """
    try:
        # Check if libraries are available
        if not PDFPLUMBER_AVAILABLE:
            return False, "PDF to Excel converter not available. Please contact bot admin."
        
        # Check if input file exists (with retry for Docker filesystem sync issues)
        for attempt in range(3):
            if os.path.exists(input_file):
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
        
        logger.debug(f"📂 Opening PDF for Excel conversion: {input_file}, Size: {os.path.getsize(input_file)}")
        
        output_path = f"{cDIR}/output.xlsx"
        
        # Create Excel workbook
        wb = Workbook()
        wb.remove(wb.active)  # Remove default sheet
        
        tables_found = 0
        text_pages = 0
        
        # Open PDF and extract tables
        with pdfplumber.open(input_file) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                # Extract tables from this page
                tables = page.extract_tables()
                
                if tables:
                    for table_num, table in enumerate(tables, start=1):
                        # Create new sheet for each table
                        sheet_name = f"P{page_num}_T{table_num}"[:31]  # Excel sheet name limit
                        ws = wb.create_sheet(title=sheet_name)
                        
                        # Write table data to sheet
                        for row_idx, row in enumerate(table, start=1):
                            for col_idx, cell in enumerate(row, start=1):
                                cell_value = cell if cell else ""
                                ws.cell(row=row_idx, column=col_idx, value=cell_value)
                                
                                # Format header row
                                if row_idx == 1:
                                    ws.cell(row=row_idx, column=col_idx).font = Font(bold=True)
                                    ws.cell(row=row_idx, column=col_idx).alignment = Alignment(horizontal='center')
                        
                        # Auto-adjust column widths
                        for column in ws.columns:
                            max_length = 0
                            column_letter = column[0].column_letter
                            for cell in column:
                                if cell.value:
                                    max_length = max(max_length, len(str(cell.value)))
                            adjusted_width = min(max_length + 2, 50)  # Cap at 50
                            ws.column_dimensions[column_letter].width = adjusted_width
                        
                        tables_found += 1
                else:
                    # If no tables, extract all text as fallback
                    text = page.extract_text()
                    if text and text.strip():
                        sheet_name = f"Page_{page_num}"[:31]
                        ws = wb.create_sheet(title=sheet_name)
                        
                        # Split text into lines and add to cells
                        lines = text.split('\n')
                        for row_idx, line in enumerate(lines[:1000], start=1):  # Limit to 1000 lines per page
                            ws.cell(row=row_idx, column=1, value=line)
                        
                        text_pages += 1
        
        # Check if any content was extracted
        if len(wb.sheetnames) == 0:
            return False, "No tables or text content found in PDF"
        
        # Save workbook
        wb.save(output_path)
        
        # Verify output
        if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
            return False, "Conversion failed: Output file is empty"
        
        return True, output_path
        
    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(Error)
