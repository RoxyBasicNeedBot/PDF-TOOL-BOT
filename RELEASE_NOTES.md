# PDF TOOL BOT v2.0.0 - The Ultimate Telegram Document Engineering Suite

> **Release Tag:** `v2.0.0`  
> **Date:** September 2026  
> **License:** GNU General Public License v3.0 (`GPL-3.0`)  
> **Live Demo:** [@pdfroxybot](https://t.me/pdfroxybot)  
> **Updates Channel:** [@roxybasicneedbot1](https://t.me/roxybasicneedbot1)

---

## Highlights & Overview

We are thrilled to announce the official **v2.0.0 release of PDF TOOL BOT** &mdash; a fully asynchronous, enterprise-grade Telegram document engineering suite powered by **Python 3.11**, **Kurigram v2.2** (high-throughput Pyrogram framework), **PyMuPDF (fitz)**, **Ghostscript 10**, **Tesseract 5 OCR**, **LibreOffice Headless**, and **Motor (async MongoDB)**.

Unlike basic file-renaming bots, **PDF TOOL BOT** executes 44 verified, atomic document manipulation routines with sub-second execution speeds, zero quality loss, and an interactive inline keyboard UI.

---

## What's New in v2.0.0

### 1. Document Architecture & Surgery
- **Multi-File Merge:** Session-based queue system to merge unlimited PDF documents into an ordered master file.
- **Precision Splitter:** Page-range slicing (`1-10`, `15,22,30`) or single-page separation on demand.
- **Selective Extractor & Deleter:** Extract designated chapters or delete unwanted cover pages, blank sheets, and disclaimers.
- **360 Degree Rotator & Zoom:** Correct orientation (`90`, `180`, `270`, `360`) and dynamically calibrate viewport margins.
- **Form Flattening:** Bake fillable PDF forms into immutable static printable pages.
- **Automatic Page Numbering:** Inject uniform sequential numbering across all headers or footers.
- **Bookmarks & Hyperlink Scrubbing:** Inspect document Table-of-Contents hierarchy and strip tracking/promotional URLs.

### 2. Ghostscript Smart Compression Studio
- **Low Profile (`/printer`):** High-resolution rasterization preservation for printing.
- **Medium Profile (`/ebook`):** Balanced optimization for digital e-readers and tablets.
- **High Profile (`/screen`):** Extreme compression for compact email attachments and quick bandwidth transfer.
- Real-time feedback calculating original vs compressed file size and percentage saved.

### 3. Visual Styling, Watermarks & Bureaucratic Stamps
- **Tri-Modal Watermark Studio:**
  - *Text Watermark:* Custom text with 10% to 100% opacity tuning and Top/Middle/Bottom positioning.
  - *Image Watermark:* Custom PNG brand logo overlay.
  - *PDF Watermark:* Vector background template underlay across all pages.
- **14 Official Bureaucratic Stamps:** Approved, Confidential, Top Secret, Draft, Expired, Final, Sold, For Public Release, etc., available in 6 colorways (Red, Blue, Green, Yellow, Pink, Black).
- **Artistic & Visual Filters:** Dark Mode color inverter, B&W grayscale conversion, and pencil-sketch visual filter.
- **Header & Footer Injector:** Custom text banner stamping along top or bottom page margins.

### 4. Universal Document Converter Suite
- **PDF to Microsoft Office:** Native conversion to editable Word (`.docx`), Excel spreadsheets (`.xlsx`), and PowerPoint slides (`.pptx`) via LibreOffice headless.
- **PDF to High-DPI Images:** Extract pages as high-resolution PNG or JPEG files, delivered individually, as documents, or bundled into `.zip` / `.tar` archives.
- **Images to PDF Album:** Assemble multi-image uploads into a consolidated PDF.
- **Text to Formatted PDF:** Convert raw pasted text or code snippets into styled PDF documents with custom typography.
- **Structured Data Export:** Dump document text into plain text (`.txt`), web-ready markup (`.html`), or machine-readable (`.json`).
- **N-Up Imposition:** Study handouts and booklet preparation supporting `1x2`, `2x1`, `1x3`, `3x1`, and `2x2` grid sheets.

### 5. Tesseract 5 OCR & Academic Discovery Hub
- **Optical Character Recognition (OCR):** Tesseract 5 engine converts scanned photos or rasterized PDFs into selectable, searchable text-layered documents.
- **Library Genesis (LibGen) Integration:** Built-in paper and textbook discovery engine with Cloudflare bypass and mirror selection.
- **Web URL Ingestion:** Fetch and convert remote HTTP/HTTPS documents into Telegram files automatically.
- **Telegram Message to PDF:** Render long chat messages into clean, printable PDFs.

### 6. Security, Cryptography & All-In-One (AIO) Pipeline
- **AES-256 Encryption & Decryption:** Military-grade password protection and instant password removal.
- **Permanent Redaction:** Irreversible black-bar censorship of sensitive information and figures.
- **Digital Signatures & Dynamic QR Codes:** Burn signature approval blocks and generate dynamic scannable QR codes.
- **Unified AIO Pipeline:** Process protected documents through consecutive operations (decrypt &rarr; compress &rarr; watermark &rarr; rename) in a single session.

### 7. Global Localization & UI Polish
- **17 Supported Languages:** English, Hindi, Arabic, Spanish, French, German, Russian, Chinese, Japanese, Portuguese, Korean, Italian, Turkish, Persian, Bengali, Urdu, Indonesian.
- **35 Native Vector SVG Icons:** Clean, modern vector icons for every feature point in the documentation.
- **Zero Unicode Emojis in Documentation:** Professional enterprise aesthetic using SVG visual indicators.

---

## Verified Operations Inventory (44 Files)

```
ROXYBASICNEEDBOT/dispatch/reactor/ops/
├── pdf_2in1.py          ├── pdf_flatten.py       ├── pdf_rotate.py
├── pdf_2in1h.py         ├── pdf_footer.py        ├── pdf_saturate.py
├── pdf_3in1.py          ├── pdf_format.py        ├── pdf_sign.py
├── pdf_3in1h.py         ├── pdf_header.py        ├── pdf_split.py
├── pdf_archive.py       ├── pdf_invert.py        ├── pdf_stamp.py
├── pdf_bookmarks.py     ├── pdf_merge.py         ├── pdf_striplinks.py
├── pdf_bw.py            ├── pdf_message.py       ├── pdf_text.py
├── pdf_combine.py       ├── pdf_metadata.py      ├── pdf_to_excel.py
├── pdf_compress.py      ├── pdf_ocr.py           ├── pdf_to_images.py
├── pdf_decrypt.py       ├── pdf_pagenum.py       ├── pdf_to_ppt.py
├── pdf_deeplink.py      ├── pdf_preview.py       ├── pdf_to_word.py
├── pdf_deletepage.py    ├── pdf_qr.py            ├── pdf_watermark.py
├── pdf_draw.py          ├── pdf_redact.py        ├── pdf_watermark45.py
├── pdf_encrypt.py       ├── pdf_rename.py        └── pdf_zoom.py
└── pdf_extract.py

bibliosearch/
├── fetcher.py (Direct URL Downloader)
└── finder.py  (LibGen Search Engine)
```

---

## One-Click Deployment

| Platform | Deployment Template |
|:---:|---|
| **Render** | [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT) |
| **Koyeb** | [![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/RoxyBasicNeedBot/PDF-TOOL-BOT&branch=main&name=pdf-tool-bot) |
| **Railway** | [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT) |
| **Heroku** | [![Deploy to Heroku](https://img.shields.io/badge/Deploy%20to%20Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/deploy?template=https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT) |

---

## Quick Setup & Execution

```bash
# 1. Clone repository
git clone https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT.git
cd PDF-TOOL-BOT

# 2. Virtual environment setup
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate # Linux / macOS

# 3. Dependencies
pip install -r requirements.txt

# 4. Configure credentials
cp config.env.example config.env

# 5. Launch bot
python -m ROXYBASICNEEDBOT
```

---

## Contributors & Acknowledgments

- **Lead Developer & Maintainer:** [@RoxyBasicNeedBot](https://t.me/roxybasicneedbot1)
- Built on top of [PyMuPDF](https://pymupdf.readthedocs.io), [Kurigram](https://github.com/KuriGohan-Kamehameha/Kurigram), [Tesseract OCR](https://github.com/tesseract-ocr/tesseract), [Ghostscript](https://www.ghostscript.com), and [LibreOffice](https://www.libreoffice.org).
