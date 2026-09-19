# 📖 RoxyBasicNeedBot v2 — Complete 44+ Operations Catalog

<div align="center">
  <h3>Exhaustive Technical & Operational Reference for all 44 PDF Manipulation Tools</h3>
  <p><i>Every operation is accessible via reactive Telegram inline button callbacks.</i></p>
</div>

---

## 📑 Quick Navigation

- [1. Document Assembly & Restructuring](#1-document-assembly--restructuring)
- [2. Multi-Format Conversions & Extraction](#2-multi-format-conversions--extraction)
- [3. Security, Anonymization & Integrity](#3-security-anonymization--integrity)
- [4. Optical Enhancements, OCR & Filters](#4-optical-enhancements-ocr--filters)
- [5. Annotations, Branding & Dynamic Elements](#5-annotations-branding--dynamic-elements)
- [6. Academic Discovery & Specialized Engines](#6-academic-discovery--specialized-engines)

---

## 1. Document Assembly & Restructuring

### 1.1 Merge PDF (`pdf_merge.py`)
- **Callback Trigger:** `#merge`
- **Engine:** PyMuPDF (`fitz.insert_pdf`)
- **Functionality:** Sequentially merges two or more PDF files into a single unified output document.
- **Memory Management:** Auto-flushes temporary memory chunks once merged.

### 1.2 Split PDF (`pdf_split.py`)
- **Callback Trigger:** `#split`
- **Engine:** PyMuPDF
- **Modes:** 
  - Single page extraction (e.g. `5`)
  - Continuous ranges (e.g. `1-10`)
  - Comma-separated arbitrary pages (e.g. `1, 3, 5, 8-12`)
  - Odd / Even split patterns

### 1.3 Combine Pages (`pdf_combine.py`)
- **Callback Trigger:** `#combine`
- **Functionality:** Takes distinct uploaded single-page or multi-page documents and concatenates them into an indexed portfolio.

### 1.4 Delete Pages (`pdf_deletepage.py`)
- **Callback Trigger:** `#deletepg`
- **Functionality:** Removes specified pages or ranges from the document and outputs a repaired document without blank gaps.

### 1.5 Extract Pages (`pdf_extract.py`)
- **Callback Trigger:** `#extract`
- **Functionality:** Extracts selected pages, high-resolution figures, or embedded image streams into a standalone PDF.

### 1.6 Rotate Pages (`pdf_rotate.py`)
- **Callback Trigger:** `#rot`
- **Angles:** `90° Clockwise`, `180° Inverted`, `270° Counter-Clockwise`.
- **Scope:** Rotate all pages uniformly or select specific target pages.

### 1.7 2-in-1 Vertical Layout (`pdf_2in1.py`)
- **Callback Trigger:** `#2in1`
- **Functionality:** Stacks 2 consecutive pages vertically onto a single A4/Letter sheet. Ideal for printing slides and study summaries.

### 1.8 2-in-1 Horizontal Layout (`pdf_2in1h.py`)
- **Callback Trigger:** `#2in1h`
- **Functionality:** Places 2 pages side-by-side in landscape orientation, preserving readable text sizing.

### 1.9 3-in-1 Vertical Layout (`pdf_3in1.py`)
- **Callback Trigger:** `#3in1`
- **Functionality:** Fits 3 consecutive pages vertically onto a single sheet for high-density document consolidation.

### 1.10 3-in-1 Horizontal Layout (`pdf_3in1h.py`)
- **Callback Trigger:** `#3in1h`
- **Functionality:** Fits 3 pages horizontally across a widescreen sheet.

### 1.11 Format Adjustment (`pdf_format.py`)
- **Callback Trigger:** `#format`
- **Supported Standards:** `A3`, `A4`, `A5`, `Letter`, `Legal`, `Tabloid`.
- **Orientation:** Portrait & Landscape reflow.

### 1.12 Zoom & Rescale Margins (`pdf_zoom.py`)
- **Callback Trigger:** `#zoom`
- **Functionality:** Scales inner content margins up or down from 50% to 150% without altering page vector coordinates.

---

## 2. Multi-Format Conversions & Extraction

### 2.1 PDF to Word (.docx) (`pdf_to_word.py`)
- **Callback Trigger:** `#pdf2word`
- **Engine:** `pdf2docx` & LibreOffice
- **Output:** Fully editable Microsoft Word document preserving fonts, paragraphs, and inline tables.

### 2.2 PDF to Excel (.xlsx) (`pdf_to_excel.py`)
- **Callback Trigger:** `#pdf2excel`
- **Engine:** `pdfplumber` + `openpyxl`
- **Functionality:** Scans tables and numerical matrix blocks in scientific papers and dumps them directly into structured spreadsheets.

### 2.3 PDF to PowerPoint (.pptx) (`pdf_to_ppt.py`)
- **Callback Trigger:** `#pdf2ppt`
- **Engine:** `python-pptx`
- **Functionality:** Transforms presentation slide PDFs into native editable PowerPoint slide decks.

### 2.4 PDF to Images (`pdf_to_images.py`)
- **Callback Trigger:** `#pdf2img`
- **Formats:** `PNG`, `JPEG`, `WEBP`, or bundled as a single `.zip` archive.
- **Resolution:** Customizable DPI (150 DPI for web, 300 DPI for print quality).

### 2.5 Text Extraction (`pdf_text.py`)
- **Callback Trigger:** `#pdf2txt`
- **Functionality:** Extracts plain text strings while filtering out layout artifacts for quick summary generation.

### 2.6 Rename Document (`pdf_rename.py`)
- **Callback Trigger:** `#rename`
- **Functionality:** Prompts for a clean new filename, preserving appropriate MIME types and file extensions.

---

## 3. Security, Anonymization & Integrity

### 3.1 Text Redactor (`pdf_redact.py`)
- **Callback Trigger:** `#redact`
- **Functionality:** Irreversibly blacks out selected text strings, PII, author affiliations, or sensitive numbers. The underlying vector text is permanently destroyed to prevent copy-paste recovery.

### 3.2 Metadata Sanitizer (`pdf_metadata.py`)
- **Callback Trigger:** `#metadata`
- **Options:** 
  - View current metadata tags
  - Wipe all metadata (Author, Producer, Software, Dates) for anonymous submissions
  - Inset custom copyright or author tags

### 3.3 AES Encryption (`pdf_encrypt.py`)
- **Callback Trigger:** `#encrypt`
- **Algorithm:** 128-bit or 256-bit AES password encryption.
- **Permissions:** Restrict printing, copying, or modifying without owner password.

### 3.4 Decrypt PDF (`pdf_decrypt.py`)
- **Callback Trigger:** `#decrypt`
- **Functionality:** Strips user/owner password restrictions when provided with the correct key.

### 3.5 Form Flattening (`pdf_flatten.py`)
- **Callback Trigger:** `#flatten`
- **Functionality:** Converts dynamic form fields (checkboxes, text inputs, radio buttons) into fixed vector drawings, freezing inputs permanently.

### 3.6 Hyperlink Stripper (`pdf_striplinks.py`)
- **Callback Trigger:** `#striplinks`
- **Functionality:** Removes active web URLs, tracking parameters, and hyperlinks from document texts.

---

## 4. Optical Enhancements, OCR & Filters

### 4.1 Tesseract OCR (`pdf_ocr.py`)
- **Callback Trigger:** `#ocr`
- **Engine:** `tesseract-ocr` + `ocrmypdf`
- **Functionality:** Generates invisible searchable text layers behind scanned raster pages, enabling full search and selection.

### 4.2 Ghostscript Smart Compression (`pdf_compress.py`)
- **Callback Trigger:** `#compress`
- **Quality Profiles:** 
  - Low (Maximum size reduction for email)
  - Medium (Balanced for web viewing)
  - High (Preserves maximum image fidelity)

### 4.3 Black & White / Grayscale (`pdf_bw.py`)
- **Callback Trigger:** `#bw`
- **Functionality:** Desaturates all raster and vector elements into grayscale, reducing printing costs and file size.

### 4.4 Dark Mode Inversion (`pdf_invert.py`)
- **Callback Trigger:** `#invert`
- **Functionality:** Inverts page luminosities for comfortable reading in low-light environments without degrading text clarity.

### 4.5 Contrast & Saturation Booster (`pdf_saturate.py`)
- **Callback Trigger:** `#saturate`
- **Functionality:** Re-balances washed-out or aged scanned pages by deepening ink levels and brightening backgrounds.

### 4.6 Multi-Page Grid Preview (`pdf_preview.py`)
- **Callback Trigger:** `#preview`
- **Functionality:** Generates an overview contact sheet grid showcasing thumbnails of all pages in the PDF.

---

## 5. Annotations, Branding & Dynamic Elements

### 5.1 Custom Watermark (`pdf_watermark.py`)
- **Callback Trigger:** `#watermark`
- **Modes:** Custom text string or transparent PNG logo.
- **Customization:** Configurable opacity, font size, and placement coordinates.

### 5.2 45° Diagonal Watermark (`pdf_watermark45.py`)
- **Callback Trigger:** `#watermark45`
- **Functionality:** Stamps an angled diagonal security watermark across every page of the document.

### 5.3 Dynamic Page Numbering (`pdf_pagenum.py`)
- **Callback Trigger:** `#pagenum`
- **Formats:** `Page X`, `X of Y`, Roman numerals (`i, ii, iii`), or plain digits.
- **Positioning:** Top-center, top-right, bottom-center, bottom-right.

### 5.4 Header & Footer Branding (`pdf_header.py`, `pdf_footer.py`)
- **Callback Trigger:** `#header`, `#footer`
- **Functionality:** Injects persistent running headers or footers with confidentiality statements, dates, or organizational titles.

### 5.5 Dynamic QR Code Embedder (`pdf_qr.py`)
- **Callback Trigger:** `#qr`
- **Functionality:** Generates high-density QR codes encoding URLs or text and stamps them onto designated page corners.

### 5.6 Pre-Built Enterprise Stamps (`pdf_stamp.py`)
- **Callback Trigger:** `#stamp`
- **Stamps:** `CONFIDENTIAL`, `APPROVED`, `DRAFT`, `TOP SECRET`, `FINAL REVIEW`.

### 5.7 Digital Signature Stamp (`pdf_sign.py`)
- **Callback Trigger:** `#sign`
- **Functionality:** Injects digital signature images or transparent signatures directly onto contract signature lines.

### 5.8 Freehand Annotator & Draw (`pdf_draw.py`)
- **Callback Trigger:** `#draw`
- **Functionality:** Adds bounding boxes, highlighting rectangles, and circle markers around key data points.

### 5.9 TOC & Bookmarks Manager (`pdf_bookmarks.py`)
- **Callback Trigger:** `#bookmarks`
- **Functionality:** Extracts, edits, or builds hierarchical Table of Contents (TOC) bookmarks for effortless document navigation.

### 5.10 Archival PDF/A Formatter (`pdf_archive.py`)
- **Callback Trigger:** `#archive`
- **Functionality:** Converts standard PDFs to ISO-compliant PDF/A standards for long-term digital preservation, or bundles files into `.zip` archives.

---

## 6. Academic Discovery & Specialized Engines

### 6.1 Bibliosearch Engine (`ROXYBASICNEEDBOT/bibliosearch/`)
- **Integration:** Library Genesis mirrors (`libgen.lc`, `libgen.st`, `libgen.rs`, `libgen.li`).
- **Features:** Direct paper, book, and dissertation lookup by Title, Author, ISBN, or MD5 hash with Cloudflare bypass.

### 6.2 TextCraft Engine (`ROXYBASICNEEDBOT/dispatch/textcraft/`)
- **Command:** `/txt2pdf`
- **Capabilities:** Interactive step-by-step PDF composition wizard with RTL Arabic/Persian reshaper algorithms and custom background color palettes.

### 6.3 Telegram Chat to PDF (`pdf_message.py`)
- **Callback Trigger:** `#msg2pdf`
- **Functionality:** Converts conversation transcripts, message batches, and group discussions into clean, printable PDFs.

### 6.4 Web & Drive Ingestion (`webnab.py`)
- **Supported Links:** Any public HTTP/HTTPS URL, Google Drive direct download links.
- **Engine:** `pdfkit` (wkhtmltopdf headless browser snapshot engine).
