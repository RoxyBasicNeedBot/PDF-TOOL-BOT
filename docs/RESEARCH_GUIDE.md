# 🔬 Academic Researcher & Student Handbook

<div align="center">
  <h3>Accelerating Literature Review, Data Extraction & Manuscript Preparation with RoxyBasicNeedBot</h3>
</div>

---

## 🎯 Purpose of this Guide

This handbook provides practical recipes for researchers, academics, graduate students, and scientists using **RoxyBasicNeedBot v2** for daily scientific workflows.

---

## 📚 1. Literature Discovery & Retrieval

When gathering papers, monographs, and textbooks for literature reviews:

```
[Telegram Search Query] ──► [Bibliosearch Cloudscraper] ──► [Libgen Mirrors] ──► [Direct PDF Delivery]
```

1. Send `/start` and select **Library Genesis Search** or trigger the inline query `@roxybasicneedbot <book title or ISBN>`.
2. The bot scrapes active mirrors (`libgen.lc`, `libgen.rs`, `libgen.st`) bypassing Cloudflare challenges.
3. Select your target document; the bot fetches the PDF and delivers it straight to your Telegram chat.

---

## 📊 2. Extracting Data & Tables from Scientific Papers

Scientific papers published on PubMed, arXiv, IEEE, or Nature often lock empirical datasets inside PDF tables.

### Extracting to Excel:
1. Forward the PDF paper to the bot.
2. Select the **PDF to Excel (.xlsx)** button (`#pdf2excel`).
3. The bot utilizes `pdfplumber` and `openpyxl` to extract numerical columns, headers, and statistical tables into an editable `.xlsx` spreadsheet.

### Extracting to Editable Word:
1. Select **PDF to Word (.docx)** (`#pdf2word`).
2. The bot converts the manuscript into an editable Microsoft Word document while preserving font formatting and mathematical alignments.

---

## 👁️ 3. Digitizing Scanned Archival Papers & Theses

Historical papers, older conference proceedings, and photocopied books often lack a searchable text layer.

1. Send the scanned PDF to the bot.
2. Click **OCR Scanner** (`#ocr`).
3. The bot initiates the **Tesseract OCR / ocrmypdf** engine, performing deskewing, binarization, and OCR text layering.
4. The output PDF allows you to search text, copy quotes, and generate citations directly.

---

## 🕵️ 4. Double-Blind Peer Review Preparation

When submitting a manuscript for double-blind peer review, you must eliminate all traces of author identity, institutions, and metadata.

```
Original Manuscript 
  ├── 1. Text Redaction (#redact)      ──► Blackout author names, grant numbers, affiliations
  ├── 2. Metadata Sanitizer (#metadata) ──► Scrub Author, Producer, and Date tags
  └── Output: Completely Anonymous PDF ready for blind review
```

1. **Text Redaction (`#redact`):** Permanently blackout names and affiliations. The underlying vector text stream is scrubbed, preventing copy-paste extraction.
2. **Metadata Sanitizer (`#metadata`):** Wipe the embedded PDF metadata tags (`Author`, `Creator`, `Producer`, `CreationDate`) to guarantee full anonymity.
3. **Form Flattening (`#flatten`):** Flatten form annotations into static vector art to ensure no hidden author comments remain.

---

## 📚 5. Thesis & Chapter Assembly

When compiling a multi-part thesis, dissertation, or conference proceedings:

- **Sequential Merge (`#merge`):** Concatenate Title Page, Abstract, Chapters 1-N, Appendices, and References into a single submission file.
- **Split & Supplementary Isolation (`#split`):** Extract supplementary tables, figures, and high-resolution graphs for separate portal uploads.
- **Dynamic Page Numbering (`#pagenum`):** Apply continuous `Page X of Y` numbering across all combined thesis sections.
- **TOC & Bookmarks Editor (`#bookmarks`):** Inject hierarchical PDF bookmarks for fast navigation across chapters and subheadings.

---

## 🌙 6. Eye-Friendly Reading & Eco Printing

- **Dark Mode Color Invert (`#invert`):** Reading dense research papers late at night? Trigger Dark Mode to invert bright whites into deep dark backgrounds without distorting text.
- **Grayscale / B&W (`#bw`):** Convert full-color papers to pure monochrome before printing to save printer ink.
- **N-up Study Handouts (`#2in1`, `#3in1`):** Combine 2 or 3 pages per sheet to print compact, eco-friendly lecture and seminar study packs.

---

## 📝 7. Research Notes to PDF (`/txt2pdf`)

When compiling reading notes, lecture summaries, or literature briefs:
1. Run `/txt2pdf`.
2. The interactive TextCraft wizard lets you set custom headers, font sizes, colors, and background themes.
3. Fully supports **Right-to-Left (RTL)** languages (Arabic, Persian, Hebrew, Urdu) using native bi-directional reshaping.
