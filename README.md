<!--
=================================================================
                 PDF TOOL BOT v2.0
       The Ultimate Telegram Document Engineering Suite
=================================================================
Live Demo  : https://t.me/pdfroxybot
GitHub     : https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT
Telegram   : https://t.me/roxybasicneedbot1
Website    : https://roxybasicneedbot.unaux.com/?i=1
YouTube    : @roxybasicneedbot
Portfolio  : https://aratt.ai/@roxybasicneedbot
(C) 2026 RoxyBasicNeedBot. All Rights Reserved.
=================================================================
-->

<div align="center">

  <img src="assets/banner.svg" alt="PDF TOOL BOT Banner" width="100%" />

  <br /><br />

  <p align="center">
    <a href="https://t.me/pdfroxybot">
      <img src="https://img.shields.io/badge/Live%20Demo-@pdfroxybot-6366f1?style=for-the-badge&logo=telegram&logoColor=white&labelColor=16140a" alt="Live Demo Bot" />
    </a>
    <a href="https://t.me/roxybasicneedbot1">
      <img src="https://img.shields.io/badge/Channel-@roxybasicneedbot1-06b6d4?style=for-the-badge&logo=telegram&logoColor=white&labelColor=16140a" alt="Channel" />
    </a>
    <a href="https://roxybasicneedbot.unaux.com/?i=1">
      <img src="https://img.shields.io/badge/Website-roxybasicneedbot-ec4899?style=for-the-badge&logo=firefox-browser&logoColor=white&labelColor=16140a" alt="Website" />
    </a>
    <a href="https://t.me/roxycontactbot">
      <img src="https://img.shields.io/badge/Support-@roxycontactbot-a855f7?style=for-the-badge&logo=telegram&logoColor=white&labelColor=16140a" alt="Support" />
    </a>
  </p>

  <p align="center">
    <strong>The Ultimate Telegram Document Engineering Suite.</strong><br />
    <em>44 Atomic Operations &bull; Tesseract OCR &bull; Universal Converters &bull; 17 Languages &bull; Academic LibGen Hub</em>
  </p>

  <p align="center">
    <a href="#overview"><b>Overview</b></a> &bull;
    <a href="#features--capabilities"><b>Features</b></a> &bull;
    <a href="#44-operations-catalog"><b>44+ Ops</b></a> &bull;
    <a href="#commands-guide"><b>Commands</b></a> &bull;
    <a href="#deployment"><b>Deploy</b></a> &bull;
    <a href="#configuration--environment"><b>Configuration</b></a> &bull;
    <a href="#local-installation"><b>Setup</b></a>
  </p>

  <div align="center">
    <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white&labelColor=14120a" />
    <img src="https://img.shields.io/badge/Engine-PyMuPDF%20fitz-f97316?style=flat-square&labelColor=14120a" />
    <img src="https://img.shields.io/badge/Client-Kurigram%20v2.2-2CA5E0?style=flat-square&logo=telegram&logoColor=white&labelColor=14120a" />
    <img src="https://img.shields.io/badge/OCR-Tesseract%205-22c55e?style=flat-square&labelColor=14120a" />
    <img src="https://img.shields.io/badge/Database-MongoDB%20Async-47A248?style=flat-square&logo=mongodb&logoColor=white&labelColor=14120a" />
    <img src="https://img.shields.io/badge/Compression-Ghostscript-d97706?style=flat-square&labelColor=14120a" />
    <img src="https://img.shields.io/badge/Office-LibreOffice%20Headless-10b981?style=flat-square&labelColor=14120a" />
    <img src="https://img.shields.io/github/stars/RoxyBasicNeedBot/PDF-TOOL-BOT?style=flat-square&color=a855f7&labelColor=14120a&logo=github" />
    <img src="https://img.shields.io/badge/License-GNU%20GPL%20v3-6366f1?style=flat-square&labelColor=14120a" />
  </div>

</div>

<br />

<div align="center">
  <img src="assets/divider.svg" width="100%" />
</div>

<br />

<div align="center">
  <img src="assets/stickers/duck_06.gif" width="70" alt="Animated Sticker" />
  &nbsp;&nbsp;
  <img src="assets/stickers/duck_03.gif" width="70" alt="Animated Sticker" />
  &nbsp;&nbsp;
  <img src="assets/stickers/duck_02.gif" width="70" alt="Animated Sticker" />
  &nbsp;&nbsp;
  <img src="assets/stickers/duck_04.gif" width="70" alt="Animated Sticker" />
  &nbsp;&nbsp;
  <img src="assets/stickers/duck_05.gif" width="70" alt="Animated Sticker" />
  &nbsp;&nbsp;
  <img src="assets/stickers/duck_01.gif" width="70" alt="Animated Sticker" />
</div>

<br />

## <img src="assets/icons/preview.svg" width="22" height="22" valign="middle" /> Overview

**PDF TOOL BOT** is an asynchronous document engineering system built natively for Telegram. Powered by **Python 3.11**, **Kurigram** (asynchronous Pyrogram framework), **PyMuPDF (fitz)**, **Tesseract 5 OCR**, **Ghostscript**, and **Motor (async MongoDB)**, it delivers 44 production-grade document transformations with sub-second execution speeds and zero quality degradation.

Send any PDF file to the bot. An interactive inline keyboard generates dynamically. Select an operation, and the result is delivered back instantly.

> [!IMPORTANT]
> **Production Requirements:** Telegram Bot Token from @BotFather, API ID and API Hash from [my.telegram.org](https://my.telegram.org), an active MongoDB instance, and Ghostscript on the host system.

<br />

<div align="center">
  <img src="assets/divider.svg" width="100%" />
</div>

<br />

## <img src="assets/icons/pipeline.svg" width="22" height="22" valign="middle" /> Features & Capabilities

<div align="center">
<table>
  <tr>
    <!-- CARD 1: CORE PDF SURGERY -->
    <td width="50%" valign="top">
      <div align="left">
        <h3><img src="assets/icons/extract.svg" width="20" height="20" valign="middle" /> Core PDF Surgery & Manipulation</h3>
        <p>
          <img src="https://img.shields.io/badge/Engine-PyMuPDF%20fitz-6366f1?style=flat-square" />
          <img src="https://img.shields.io/badge/Quality-Lossless%20Vector-10b981?style=flat-square" />
        </p>
        <ul>
          <li>
            <img src="assets/icons/merge.svg" width="18" height="18" valign="middle" /> <b>Multi-File Merge:</b> Send multiple PDF files into the active session queue and merge them into a single ordered master document.
          </li>
          <br />
          <li>
            <img src="assets/icons/split.svg" width="18" height="18" valign="middle" /> <b>Precision Splitter:</b> Slice documents by arbitrary page ranges (e.g. <code>1-10</code>, <code>15,22,30</code>) or split on demand.
          </li>
          <br />
          <li>
            <img src="assets/icons/extract.svg" width="18" height="18" valign="middle" /> <b>Selective Page Extractor:</b> Isolate specific pages or chapters into a brand-new standalone PDF without quality loss.
          </li>
          <br />
          <li>
            <img src="assets/icons/delete.svg" width="18" height="18" valign="middle" /> <b>Page Deleter:</b> Remove unwanted blank sheets, copyright disclaimers, or cover pages by index.
          </li>
          <br />
          <li>
            <img src="assets/icons/rotate.svg" width="18" height="18" valign="middle" /> <b>360 Degree Rotator:</b> Reorient orientation clockwise or counter-clockwise (<code>90 deg</code>, <code>180 deg</code>, <code>270 deg</code>, <code>360 deg</code>).
          </li>
          <br />
          <li>
            <img src="assets/icons/zoom.svg" width="18" height="18" valign="middle" /> <b>Zoom & Margin Calibrator:</b> Dynamically scale document viewport bounding boxes with custom margin expansion.
          </li>
          <br />
          <li>
            <img src="assets/icons/flatten.svg" width="18" height="18" valign="middle" /> <b>Form Field Flattening:</b> Convert dynamic, interactive fillable PDF forms into immutable static printable pages.
          </li>
          <br />
          <li>
            <img src="assets/icons/numbering.svg" width="18" height="18" valign="middle" /> <b>Automatic Page Numbering:</b> Stamp uniform, sequential numbering across every page header or footer automatically.
          </li>
          <br />
          <li>
            <img src="assets/icons/bookmarks.svg" width="18" height="18" valign="middle" /> <b>Bookmark & TOC Inspector:</b> Inspect and extract the embedded table-of-contents hierarchy from technical books and papers.
          </li>
          <br />
          <li>
            <img src="assets/icons/striplinks.svg" width="18" height="18" valign="middle" /> <b>Hyperlink Stripper:</b> Scrub all embedded promotional web links and tracking URLs with a single tap.
          </li>
          <br />
          <li>
            <img src="assets/icons/preview.svg" width="18" height="18" valign="middle" /> <b>Cover Page Preview:</b> Generate high-resolution graphical preview images of document cover pages.
          </li>
        </ul>
      </div>
    </td>
    <!-- CARD 2: COMPRESSION & VISUAL STYLING -->
    <td width="50%" valign="top">
      <div align="left">
        <h3><img src="assets/icons/compress.svg" width="20" height="20" valign="middle" /> Smart Compression & Visual Studio</h3>
        <p>
          <img src="https://img.shields.io/badge/Backend-Ghostscript%2010-f59e0b?style=flat-square" />
          <img src="https://img.shields.io/badge/Profiles-Printer%20%7C%20Ebook%20%7C%20Screen-ec4899?style=flat-square" />
        </p>
        <ul>
          <li>
            <img src="assets/icons/compress.svg" width="18" height="18" valign="middle" /> <b>Multi-Tier Compression:</b> Ghostscript backend engine with calculated size savings feedback:
            <ul>
              <li><code>Low (Best Quality)</code>: Uses <code>/printer</code> profile for high-res print outputs.</li>
              <li><code>Medium (Balanced)</code>: Uses <code>/ebook</code> profile for crystal-clear digital reading.</li>
              <li><code>High (Smallest Size)</code>: Uses <code>/screen</code> profile for compact email attachments.</li>
            </ul>
          </li>
          <br />
          <li>
            <img src="assets/icons/watermark.svg" width="18" height="18" valign="middle" /> <b>Tri-Modal Watermark Studio:</b>
            <ul>
              <li><b>Text Watermark:</b> Custom text overlay with 10% to 100% opacity tuning and Top, Middle, or Bottom alignment.</li>
              <li><b>Image Watermark:</b> Stamp your personal logo or brand PNG directly across all pages.</li>
              <li><b>PDF Watermark:</b> Merge a transparent background template PDF under each page.</li>
            </ul>
          </li>
          <br />
          <li>
            <img src="assets/icons/stamp.svg" width="18" height="18" valign="middle" /> <b>Official Stamp Presets:</b> 14 bureaucratic stamps (<i>Approved, Confidential, Top Secret, Draft, Expired, Final, Sold, For Public Release...</i>) across 6 colors (Red, Blue, Green, Yellow, Pink, Black).
          </li>
          <br />
          <li>
            <img src="assets/icons/darkmode.svg" width="18" height="18" valign="middle" /> <b>Dark Mode Inverter:</b> Inverts color schemes for comfortable reading in dark environments.
          </li>
          <br />
          <li>
            <img src="assets/icons/grayscale.svg" width="18" height="18" valign="middle" /> <b>Black & White Grayscale:</b> Converts documents into pure monochrome for ink-saving printing.
          </li>
          <br />
          <li>
            <img src="assets/icons/sketch.svg" width="18" height="18" valign="middle" /> <b>Artistic Sketch Filter:</b> Transforms pages into stylized hand-drawn pencil sketches.
          </li>
          <br />
          <li>
            <img src="assets/icons/margins.svg" width="18" height="18" valign="middle" /> <b>Header & Footer Injector:</b> Injects custom text banners at top or bottom page margins.
          </li>
        </ul>
      </div>
    </td>
  </tr>
  <tr>
    <!-- CARD 3: UNIVERSAL CONVERTERS & N-UP -->
    <td width="50%" valign="top">
      <div align="left">
        <h3><img src="assets/icons/word.svg" width="20" height="20" valign="middle" /> Universal Converters & N-Up Imposition</h3>
        <p>
          <img src="https://img.shields.io/badge/Converter-LibreOffice%20Headless-10b981?style=flat-square" />
          <img src="https://img.shields.io/badge/Output-DOCX%20%7C%20XLSX%20%7C%20PPTX-3b82f6?style=flat-square" />
        </p>
        <ul>
          <li>
            <img src="assets/icons/word.svg" width="18" height="18" valign="middle" /> <b>PDF to Microsoft Word (DOCX):</b> Converts documents into fully editable Word files with intact paragraphs and formatting.
          </li>
          <br />
          <li>
            <img src="assets/icons/excel.svg" width="18" height="18" valign="middle" /> <b>PDF to Microsoft Excel (XLSX):</b> Detects tabular layouts and extracts raw data directly into structured spreadsheets.
          </li>
          <br />
          <li>
            <img src="assets/icons/ppt.svg" width="18" height="18" valign="middle" /> <b>PDF to PowerPoint (PPTX):</b> Transforms document presentation slides into editable PowerPoint decks.
          </li>
          <br />
          <li>
            <img src="assets/icons/images.svg" width="18" height="18" valign="middle" /> <b>PDF to High-DPI Images:</b> Renders every page into PNG or JPEG image files. Export as single images, document formats, or compressed <code>.ZIP</code> / <code>.TAR</code> packages.
          </li>
          <br />
          <li>
            <img src="assets/icons/images.svg" width="18" height="18" valign="middle" /> <b>Images to Single PDF:</b> Send multiple pictures (JPG, PNG) in chat and click generate to create an aggregated PDF document.
          </li>
          <br />
          <li>
            <img src="assets/icons/text.svg" width="18" height="18" valign="middle" /> <b>Text to Formatted PDF:</b> Paste raw text directly into the bot to produce an elegant PDF with custom fonts and font sizes.
          </li>
          <br />
          <li>
            <img src="assets/icons/text.svg" width="18" height="18" valign="middle" /> <b>Structured Text Extraction:</b> Exports embedded text as plain text (<code>.TXT</code>), web-ready markup (<code>.HTML</code>), or machine-readable <code>.JSON</code>.
          </li>
          <br />
          <li>
            <img src="assets/icons/nup.svg" width="18" height="18" valign="middle" /> <b>N-Up Sheet Imposition (Study Handouts):</b>
            <ul>
              <li><code>1 x 2</code> & <code>2 x 1</code>: Two pages per sheet (Horizontal / Vertical).</li>
              <li><code>1 x 3</code> & <code>3 x 1</code>: Three pages per sheet (Horizontal / Vertical).</li>
              <li><code>2 x 2</code>: Four pages per sheet in a compact 4-quadrant grid.</li>
            </ul>
          </li>
        </ul>
      </div>
    </td>
    <!-- CARD 4: OCR, RESEARCH & SECURITY -->
    <td width="50%" valign="top">
      <div align="left">
        <h3><img src="assets/icons/ocr.svg" width="20" height="20" valign="middle" /> OCR, Academic Research & Security</h3>
        <p>
          <img src="https://img.shields.io/badge/OCR-Tesseract%205%20Engine-22c55e?style=flat-square" />
          <img src="https://img.shields.io/badge/Security-AES--256%20Military-ef4444?style=flat-square" />
        </p>
        <ul>
          <li>
            <img src="assets/icons/ocr.svg" width="18" height="18" valign="middle" /> <b>Tesseract 5 OCR Engine:</b> Converts scanned, photographed, or unselectable PDFs into copyable, searchable text layers without distortion.
          </li>
          <br />
          <li>
            <img src="assets/icons/academic.svg" width="18" height="18" valign="middle" /> <b>Library Genesis (LibGen) Research Hub:</b> Search academic research papers, journals, and books directly from Telegram with mirror selection and Cloudflare bypass.
          </li>
          <br />
          <li>
            <img src="assets/icons/download.svg" width="18" height="18" valign="middle" /> <b>Web URL to PDF Ingest:</b> Send direct download links or document URLs; the bot fetches and converts them into Telegram documents automatically.
          </li>
          <br />
          <li>
            <img src="assets/icons/chat.svg" width="18" height="18" valign="middle" /> <b>Telegram Message to PDF:</b> Render formatted Telegram messages into clean PDF documents.
          </li>
          <br />
          <li>
            <img src="assets/icons/lock.svg" width="18" height="18" valign="middle" /> <b>Cryptographic AES Encryption:</b> Lock documents with user and owner passwords via military-grade AES-256 encryption.
          </li>
          <br />
          <li>
            <img src="assets/icons/unlock.svg" width="18" height="18" valign="middle" /> <b>Instant Password Decryption:</b> Remove password restrictions from your owned protected files.
          </li>
          <br />
          <li>
            <img src="assets/icons/redact.svg" width="18" height="18" valign="middle" /> <b>Irreversible Redaction:</b> Permanently black out confidential data, names, figures, and sensitive sections before public distribution.
          </li>
          <br />
          <li>
            <img src="assets/icons/signature.svg" width="18" height="18" valign="middle" /> <b>Digital Signature:</b> Insert verified signature blocks and embed dynamic scannable QR codes anywhere on your pages.
          </li>
          <br />
          <li>
            <img src="assets/icons/qrcode.svg" width="18" height="18" valign="middle" /> <b>QR Code Stamping:</b> Synthesizes and stamps a custom QR code onto pages.
          </li>
          <br />
          <li>
            <img src="assets/icons/pipeline.svg" width="18" height="18" valign="middle" /> <b>Unified AIO (All-in-One) Pipeline:</b> Handles password-protected files and applies continuous chains of operations (decrypt, compress, watermark, rename) in a single session.
          </li>
          <br />
          <li>
            <img src="assets/icons/deeplink.svg" width="18" height="18" valign="middle" /> <b>Deep Linking & Shareable URLs:</b> Generate secure Telegram deep links allowing others to open specific processed files right inside the bot.
          </li>
        </ul>
      </div>
    </td>
  </tr>
</table>
</div>

<br />

<div align="center">
  <img src="assets/divider.svg" width="100%" />
</div>

<br />

## <img src="assets/icons/extract.svg" width="22" height="22" valign="middle" /> 44+ Operations Catalog

Every operation implemented directly in the source code (<code>dispatch/reactor/ops/</code>):

<details>
<summary><b>Click to expand the complete 44+ Operations Catalog</b></summary>

<br />

### 1. Document Architecture & Assembly
| File | Operation | Description |
|---|---|---|
| `pdf_merge.py` | <img src="assets/icons/merge.svg" width="16" height="16" valign="middle" /> **Merge** | Concatenates multiple PDF files into one ordered master file |
| `pdf_split.py` | <img src="assets/icons/split.svg" width="16" height="16" valign="middle" /> **Split** | Slices PDF documents by custom page range or specific pages |
| `pdf_extract.py` | <img src="assets/icons/extract.svg" width="16" height="16" valign="middle" /> **Extract** | Pulls out designated pages into a new standalone PDF |
| `pdf_combine.py` | <img src="assets/icons/merge.svg" width="16" height="16" valign="middle" /> **Combine** | Interleaves and combines disparate page batches |
| `pdf_deletepage.py` | <img src="assets/icons/delete.svg" width="16" height="16" valign="middle" /> **Delete Page** | Removes unwanted single pages or ranges by index |
| `pdf_compress.py` | <img src="assets/icons/compress.svg" width="16" height="16" valign="middle" /> **Compress** | Ghostscript compression: Low (<code>/printer</code>), Medium (<code>/ebook</code>), High (<code>/screen</code>) |
| `pdf_rotate.py` | <img src="assets/icons/rotate.svg" width="16" height="16" valign="middle" /> **Rotate** | Corrects document orientation: 90 deg, 180 deg, 270 deg, 360 deg |
| `pdf_zoom.py` | <img src="assets/icons/zoom.svg" width="16" height="16" valign="middle" /> **Zoom** | Adjusts inner page zoom scale and border padding margins |
| `pdf_rename.py` | <img src="assets/icons/text.svg" width="16" height="16" valign="middle" /> **Rename** | Safely renames files without modifying internal binary payloads |
| `pdf_preview.py` | <img src="assets/icons/preview.svg" width="16" height="16" valign="middle" /> **Preview** | Renders high-fidelity graphical preview of the cover page |
| `pdf_metadata.py` | <img src="assets/icons/text.svg" width="16" height="16" valign="middle" /> **Metadata** | Inspects document metadata (Title, Author, Subject, Keywords, Creator) |
| `pdf_flatten.py` | <img src="assets/icons/flatten.svg" width="16" height="16" valign="middle" /> **Flatten** | Flattens interactive form fields into static immutable pages |
| `pdf_pagenum.py` | <img src="assets/icons/numbering.svg" width="16" height="16" valign="middle" /> **Page Numbers** | Automatically inserts page numbers across every page |
| `pdf_bookmarks.py` | <img src="assets/icons/bookmarks.svg" width="16" height="16" valign="middle" /> **Bookmarks** | Reads and exports the document Table of Contents outline |
| `pdf_striplinks.py` | <img src="assets/icons/striplinks.svg" width="16" height="16" valign="middle" /> **Strip Links** | Purges all clickable hyperlinks and tracking URLs from pages |

### 2. Visual Enhancements & Artistry
| File | Operation | Description |
|---|---|---|
| `pdf_bw.py` | <img src="assets/icons/grayscale.svg" width="16" height="16" valign="middle" /> **Black & White** | Converts color pages to ink-saving monochrome grayscale |
| `pdf_invert.py` | <img src="assets/icons/darkmode.svg" width="16" height="16" valign="middle" /> **Invert Colors** | Inverts colors for eye-friendly dark/night mode reading |
| `pdf_saturate.py` | <img src="assets/icons/preview.svg" width="16" height="16" valign="middle" /> **Saturate** | Adjusts color vibrancy and saturation levels |
| `pdf_draw.py` | <img src="assets/icons/sketch.svg" width="16" height="16" valign="middle" /> **Draw / Sketch** | Applies an artistic pencil-sketch visual filter |

### 3. Watermarking, Stamps & Identity
| File | Operation | Description |
|---|---|---|
| `pdf_watermark.py` | <img src="assets/icons/watermark.svg" width="16" height="16" valign="middle" /> **Watermark (Text/Image/PDF)** | Full watermark engine with 10% to 100% opacity and Top/Mid/Bottom alignment |
| `pdf_watermark45.py` | <img src="assets/icons/watermark.svg" width="16" height="16" valign="middle" /> **Watermark 45 deg** | Classic diagonal 45-degree watermark positioning |
| `pdf_stamp.py` | <img src="assets/icons/stamp.svg" width="16" height="16" valign="middle" /> **Official Stamp** | 14 official bureaucratic stamps in 6 selectable colors |
| `pdf_header.py` | <img src="assets/icons/margins.svg" width="16" height="16" valign="middle" /> **Header** | Injects custom banner text across top page margins |
| `pdf_footer.py` | <img src="assets/icons/margins.svg" width="16" height="16" valign="middle" /> **Footer** | Injects custom banner text across bottom page margins |
| `pdf_redact.py` | <img src="assets/icons/redact.svg" width="16" height="16" valign="middle" /> **Redact** | Permanently censors and blacks out sensitive document regions |
| `pdf_sign.py` | <img src="assets/icons/signature.svg" width="16" height="16" valign="middle" /> **Digital Sign** | Inserts a visual signature block for document approval |
| `pdf_qr.py` | <img src="assets/icons/qrcode.svg" width="16" height="16" valign="middle" /> **QR Code** | Synthesizes and stamps a custom QR code onto pages |

### 4. Sheet Imposition (N-Up Layouts)
| File | Operation | Description |
|---|---|---|
| `pdf_format.py` | <img src="assets/icons/nup.svg" width="16" height="16" valign="middle" /> **Format Hub** | Master selection router for 1x1, 1x2, 2x1, 1x3, 3x1, 2x2 |
| `pdf_2in1.py` | <img src="assets/icons/nup.svg" width="16" height="16" valign="middle" /> **2-in-1 Vertical** | 2 pages printed vertically on a single sheet |
| `pdf_2in1h.py` | <img src="assets/icons/nup.svg" width="16" height="16" valign="middle" /> **2-in-1 Horizontal** | 2 pages printed horizontally on a single sheet |
| `pdf_3in1.py` | <img src="assets/icons/nup.svg" width="16" height="16" valign="middle" /> **3-in-1 Vertical** | 3 pages printed vertically on a single sheet |
| `pdf_3in1h.py` | <img src="assets/icons/nup.svg" width="16" height="16" valign="middle" /> **3-in-1 Horizontal** | 3 pages printed horizontally on a single sheet |

### 5. Format Conversion & Data Extraction
| File | Operation | Description |
|---|---|---|
| `pdf_to_word.py` | <img src="assets/icons/word.svg" width="16" height="16" valign="middle" /> **PDF to DOCX** | Headless LibreOffice conversion to editable Microsoft Word |
| `pdf_to_excel.py` | <img src="assets/icons/excel.svg" width="16" height="16" valign="middle" /> **PDF to XLSX** | Extracts tabular layouts into Microsoft Excel spreadsheets |
| `pdf_to_ppt.py` | <img src="assets/icons/ppt.svg" width="16" height="16" valign="middle" /> **PDF to PPTX** | Converts presentation slides into editable PowerPoint files |
| `pdf_to_images.py` | <img src="assets/icons/images.svg" width="16" height="16" valign="middle" /> **PDF to Images** | Converts pages to PNG/JPEG images (Individual, Document, ZIP, TAR) |
| `pdf_text.py` | <img src="assets/icons/text.svg" width="16" height="16" valign="middle" /> **PDF to Text** | Extracts document text and exports as TXT, HTML, or JSON |
| `pdf_encrypt.py` | <img src="assets/icons/lock.svg" width="16" height="16" valign="middle" /> **Encrypt** | Applies cryptographic password lock with AES-256 |
| `pdf_decrypt.py` | <img src="assets/icons/unlock.svg" width="16" height="16" valign="middle" /> **Decrypt** | Unlocks encrypted PDFs using verified user password |
| `pdf_archive.py` | <img src="assets/icons/download.svg" width="16" height="16" valign="middle" /> **Archive** | Bundles and compresses PDF files into ZIP or TAR archives |

### 6. OCR, Intelligence & Academic Search
| File | Operation | Description |
|---|---|---|
| `pdf_ocr.py` | <img src="assets/icons/ocr.svg" width="16" height="16" valign="middle" /> **Tesseract OCR** | Converts non-selectable scanned PDFs into searchable text documents |
| `pdf_deeplink.py` | <img src="assets/icons/deeplink.svg" width="16" height="16" valign="middle" /> **Deep Link** | Generates shareable bot deep links to retrieve stored documents |
| `pdf_message.py` | <img src="assets/icons/chat.svg" width="16" height="16" valign="middle" /> **Message to PDF** | Converts long chat text messages into clean PDF documents |
| `fetcher.py` | <img src="assets/icons/download.svg" width="16" height="16" valign="middle" /> **URL Downloader** | Direct remote HTTP/HTTPS document fetcher |
| `finder.py` | <img src="assets/icons/academic.svg" width="16" height="16" valign="middle" /> **LibGen Search** | Library Genesis paper & book search with Cloudflare bypass |

</details>

<br />

<div align="center">
  <img src="assets/divider.svg" width="100%" />
</div>

<br />

## <img src="assets/icons/chat.svg" width="22" height="22" valign="middle" /> Commands Guide

### User Commands

| Command | Action | Details |
|:---:|---|---|
| `/start` | <img src="assets/icons/chat.svg" width="16" height="16" valign="middle" /> **Initialize Bot** | Displays welcome panel, language detection, and quick setup guide |
| `/lang` | <img src="assets/icons/academic.svg" width="16" height="16" valign="middle" /> **Change Language** | Opens language selection menu supporting 17 international languages |
| `/help` | <img src="assets/icons/preview.svg" width="16" height="16" valign="middle" /> **Operations Guide** | Explains available features and gives direct inline keyboard tips |

> [!NOTE]
> **No Command Memorization Needed:** Simply upload any PDF document to the bot. An interactive inline keyboard appears with instant buttons for every tool.

### Administrator Commands

| Command | Syntax | Description |
|:---:|---|---|
| `/stats` | `/stats` | <img src="assets/icons/pipeline.svg" width="16" height="16" valign="middle" /> Displays real-time server health (Disk storage, RAM usage, CPU load, Active database users) |
| `/ban` | `/ban <user_id>` | <img src="assets/icons/delete.svg" width="16" height="16" valign="middle" /> Permanently bans a user from accessing the bot infrastructure |
| `/unban` | `/unban <user_id>` | <img src="assets/icons/unlock.svg" width="16" height="16" valign="middle" /> Restores access permissions for a previously banned user |
| `/donate` | `/donate` | <img src="assets/icons/stamp.svg" width="16" height="16" valign="middle" /> Displays donation and support options |

<br />

<div align="center">
  <img src="assets/divider.svg" width="100%" />
</div>

<br />

## <img src="assets/icons/academic.svg" width="22" height="22" valign="middle" /> 17 Supported Languages

Full localized interface covering menus, buttons, status indicators, and prompts:

<div align="center">

| Language | Code | Language | Code | Language | Code |
|---|:---:|---|:---:|---|:---:|
| **English** | `en` | **Hindi** (Hindi) | `hi` | **Arabic** (Arabic) | `ar` |
| **Spanish** (Espanol) | `es` | **French** (Francais) | `fr` | **German** (Deutsch) | `de` |
| **Russian** (Russian) | `ru` | **Chinese** (Chinese) | `zh` | **Japanese** (Japanese) | `ja` |
| **Portuguese** (Portugues) | `pt` | **Korean** (Korean) | `ko` | **Italian** (Italiano) | `it` |
| **Turkish** (Turkce) | `tr` | **Persian** (Farsi) | `fa` | **Bengali** (Bengali) | `bn` |
| **Urdu** (Urdu) | `ur` | **Indonesian** (Bahasa) | `id` | | |

</div>

<br />

<div align="center">
  <img src="assets/divider.svg" width="100%" />
</div>

<br />

## <img src="assets/icons/download.svg" width="22" height="22" valign="middle" /> Deployment

Deploy your own high-performance instance with a single click:

<div align="center">
<table>
  <thead>
    <tr>
      <th align="center">Render</th>
      <th align="center">Koyeb</th>
      <th align="center">Railway</th>
      <th align="center">Heroku</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <a href="https://render.com/deploy?repo=https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT">
          <img src="https://render.com/images/deploy-to-render-button.svg" height="42" alt="Deploy to Render" />
        </a>
      </td>
      <td align="center">
        <a href="https://app.koyeb.com/deploy?type=git&repository=github.com/RoxyBasicNeedBot/PDF-TOOL-BOT&branch=main&name=pdf-tool-bot">
          <img src="https://www.koyeb.com/static/images/deploy/button.svg" height="42" alt="Deploy to Koyeb" />
        </a>
      </td>
      <td align="center">
        <a href="https://railway.app/new/template?template=https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT">
          <img src="https://railway.app/button.svg" height="42" alt="Deploy on Railway" />
        </a>
      </td>
      <td align="center">
        <a href="https://heroku.com/deploy?template=https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT">
          <img src="https://img.shields.io/badge/Deploy%20to%20Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" height="42" alt="Deploy to Heroku" />
        </a>
      </td>
    </tr>
  </tbody>
</table>
</div>

<br />

<div align="center">
  <img src="assets/divider.svg" width="100%" />
</div>

<br />

## <img src="assets/icons/lock.svg" width="22" height="22" valign="middle" /> Configuration & Environment

Copy the template and fill in your credentials:

```bash
cp config.env.example config.env
```

### Core Variables (Required)

| Variable | Type | Description |
|---|:---:|---|
| `B_TOKEN` | `String` | Telegram Bot Token obtained from [@BotFather](https://t.me/BotFather) |
| `API_ID` | `Integer` | Telegram API App ID from [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | `String` | Telegram API Hash string from [my.telegram.org](https://my.telegram.org) |
| `MONGODB_URI` | `String` | MongoDB connection URI (<code>mongodb+srv://...</code>) for storing user preferences |
| `ADMINS` | `String` | Space-separated Telegram user IDs who have admin permissions |

### Optional Configuration

| Variable | Type | Default | Description |
|---|:---:|:---:|---|
| `LOG_CHANNEL` | `Integer` | `None` | Telegram channel ID to receive operational and error logs |
| `FORCE_SUB` | `String` | `None` | Telegram channel username for compulsory subscription verification |
| `FORCE_SUB2` | `String` | `None` | Second channel username for dual force-subscription check |
| `MAX_FILE_SIZE` | `Integer` | `200` | Maximum allowable input file size in megabytes (MB) |
| `MULTI_LANG_SUP` | `Boolean` | `True` | Automatically detect client language from user profile |
| `SOURCE_CODE` | `String` | `""` | Repository URL displayed in information and about panels |
| `OWNED_CHANNEL` | `String` | `""` | Official updates channel URL linked in menus |
| `PORT` | `Integer` | `8080` | Keep-alive HTTP pulse server port for Render and Koyeb platforms |

<br />

<div align="center">
  <img src="assets/divider.svg" width="100%" />
</div>

<br />

## <img src="assets/icons/pipeline.svg" width="22" height="22" valign="middle" /> Local Installation

### Prerequisites
- <img src="assets/icons/pipeline.svg" width="16" height="16" valign="middle" /> **Python 3.11+**
- <img src="assets/icons/compress.svg" width="16" height="16" valign="middle" /> **Ghostscript** (<code>gs</code> binary for PDF level-compression)
- <img src="assets/icons/ocr.svg" width="16" height="16" valign="middle" /> **Tesseract OCR** (<code>tesseract</code> engine for OCR text layer generation)
- <img src="assets/icons/word.svg" width="16" height="16" valign="middle" /> **LibreOffice** (Headless engine for DOCX, XLSX, PPTX conversion)

```bash
# 1. Clone repository
git clone https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT.git
cd PDF-TOOL-BOT

# 2. Setup virtual environment
python -m venv venv
venv\Scripts\activate          # Windows PowerShell / CMD
# source venv/bin/activate     # Linux / macOS

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp config.env.example config.env
# Edit config.env with your real credentials

# 5. Start the bot
python -m ROXYBASICNEEDBOT
```

<br />

<div align="center">
  <img src="assets/divider.svg" width="100%" />
</div>

<br />

## <img src="assets/icons/signature.svg" width="22" height="22" valign="middle" /> Acknowledgments

- <img src="assets/icons/extract.svg" width="16" height="16" valign="middle" /> [**PyMuPDF (fitz)**](https://pymupdf.readthedocs.io) - High-performance C-backed PDF rendering and manipulation library
- <img src="assets/icons/chat.svg" width="16" height="16" valign="middle" /> [**Kurigram**](https://github.com/KuriGohan-Kamehameha/Kurigram) - Asynchronous Pyrogram MTProto client fork
- <img src="assets/icons/ocr.svg" width="16" height="16" valign="middle" /> [**Tesseract OCR**](https://github.com/tesseract-ocr/tesseract) - World-class optical character recognition engine
- <img src="assets/icons/compress.svg" width="16" height="16" valign="middle" /> [**Ghostscript**](https://www.ghostscript.com) - PostScript and PDF compression engine
- <img src="assets/icons/word.svg" width="16" height="16" valign="middle" /> [**LibreOffice**](https://www.libreoffice.org) - Headless office document conversion system
- <img src="assets/icons/pipeline.svg" width="16" height="16" valign="middle" /> [**Motor**](https://motor.readthedocs.io) - Asynchronous MongoDB driver for Python

<br />

<div align="center">
  <img src="assets/divider.svg" width="100%" />
</div>

<br />

<!-- ==================== PREMIUM FOOTER ==================== -->
<div align="center">

  <p align="center">
    <img src="assets/stickers/duck_07.gif" width="65" alt="Duck Sticker" />
    &nbsp;&nbsp;&nbsp;&nbsp;
    <img src="assets/stickers/duck_08.gif" width="65" alt="Duck Sticker" />
    &nbsp;&nbsp;&nbsp;&nbsp;
    <img src="assets/stickers/duck_09.gif" width="65" alt="Duck Sticker" />
    &nbsp;&nbsp;&nbsp;&nbsp;
    <img src="assets/stickers/duck_10.gif" width="65" alt="Duck Sticker" />
  </p>

  <br />

  <p align="center">
    <a href="https://t.me/pdfroxybot">
      <img src="https://img.shields.io/badge/Try%20Live%20Demo-@pdfroxybot-6366f1?style=for-the-badge&logo=telegram&logoColor=white&labelColor=16140a" alt="Live Demo" />
    </a>
    &nbsp;
    <a href="https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT/stargazers">
      <img src="https://img.shields.io/github/stars/RoxyBasicNeedBot/PDF-TOOL-BOT?style=for-the-badge&color=f59e0b&logo=github&labelColor=16140a" alt="GitHub Stars" />
    </a>
    &nbsp;
    <a href="https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT/network/members">
      <img src="https://img.shields.io/github/forks/RoxyBasicNeedBot/PDF-TOOL-BOT?style=for-the-badge&color=ec4899&logo=github&labelColor=16140a" alt="GitHub Forks" />
    </a>
    &nbsp;
    <a href="https://t.me/roxybasicneedbot1">
      <img src="https://img.shields.io/badge/Updates%20Channel-Join%20Now-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white&labelColor=16140a" alt="Telegram Channel" />
    </a>
    &nbsp;
    <a href="https://roxybasicneedbot.unaux.com/?i=1">
      <img src="https://img.shields.io/badge/Official%20Website-Visit-ec4899?style=for-the-badge&logo=firefox-browser&logoColor=white&labelColor=16140a" alt="Website" />
    </a>
  </p>

  <p align="center">
    <a href="#overview">Back to Top</a> &bull;
    <a href="https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT/issues">Report Issue</a> &bull;
    <a href="https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT/pulls">Submit Pull Request</a>
  </p>

  <p align="center">
    <strong>If PDF TOOL BOT improved your workflow, consider giving it a Star on GitHub.</strong>
  </p>

  <sub>(C) 2026 <a href="https://t.me/roxybasicneedbot1">RoxyBasicNeedBot</a>. All Rights Reserved.</sub>

</div>

<!--
=================================================================
                 PDF TOOL BOT v2.0
Live Demo  : https://t.me/pdfroxybot
GitHub     : https://github.com/RoxyBasicNeedBot/PDF-TOOL-BOT
Telegram   : https://t.me/roxybasicneedbot1
(C) 2026 RoxyBasicNeedBot. All Rights Reserved.
=================================================================
-->
