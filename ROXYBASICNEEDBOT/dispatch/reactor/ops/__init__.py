# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𕕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

class ModuleMeta:
    FILE_PATH = "ROXYBASICNEEDBOT/dispatch/reactor/ops/__init__.py"
    AUTHOR = "roxybasicneedbot"
    TELEGRAM = "telegram.dog/roxybasicneedbot"
    LICENSE = "Copyright © 2026, roxybasicneedbot"

file_name = ModuleMeta.FILE_PATH
__author__ = ModuleMeta.AUTHOR

# Explicit imports of all PDF operations to satisfy runtime package exposure
from .pdf_preview import previewPDF
from .pdf_text import textPDF
from .pdf_zoom import zoomPDF
from .pdf_format import formatPDF
from .pdf_encrypt import encryptPDF
from .pdf_decrypt import decryptPDF
from .pdf_combine import combinePages
from .pdf_bw import blackAndWhitePdf
from .pdf_compress import compressPDF
from .pdf_draw import drawPDF
from .pdf_ocr import ocrPDF
from .pdf_rotate import rotatePDF
from .pdf_saturate import saturatePDF
from .pdf_to_images import pdfToImages
from .pdf_rename import renamePDF
from .pdf_split import splitPDF
from .pdf_merge import mergePDF
from .pdf_stamp import stampPDF
from .pdf_2in1 import twoPagesToOne
from .pdf_3in1 import threePagesToOne
from .pdf_3in1h import threePagesToOneH
from .pdf_2in1h import twoPagesToOneH
from .pdf_watermark import watermarkPDF
from .pdf_deletepage import deletePDFPg
from .pdf_archive import zipTarPDF
from .pdf_message import messagePDF
from .pdf_metadata import metadataPDF
from . import pdf_watermark45 as watermark45
from .pdf_invert import invertPDF
from .pdf_footer import pdfFooter
from .pdf_header import pdfHeader
from .pdf_extract import partPDF
from .pdf_striplinks import urlRemover

__all__ = [
    "previewPDF",
    "textPDF",
    "zoomPDF",
    "formatPDF",
    "encryptPDF",
    "decryptPDF",
    "combinePages",
    "blackAndWhitePdf",
    "compressPDF",
    "drawPDF",
    "ocrPDF",
    "rotatePDF",
    "saturatePDF",
    "pdfToImages",
    "renamePDF",
    "splitPDF",
    "mergePDF",
    "stampPDF",
    "twoPagesToOne",
    "threePagesToOne",
    "threePagesToOneH",
    "twoPagesToOneH",
    "watermarkPDF",
    "deletePDFPg",
    "zipTarPDF",
    "messagePDF",
    "metadataPDF",
    "watermark45",
    "invertPDF",
    "pdfFooter",
    "pdfHeader",
    "partPDF",
    "urlRemover",
]
