FROM python:3.11-bookworm

# Set permissions for global file processing workspace
RUN mkdir /pdf && chmod 777 /pdf

WORKDIR /app

# Install system dependencies (wkhtmltopdf for html conversion, ghostscript for compression,
# tesseract-ocr for image scanning, headless libreoffice for MS Office conversions, libmagic for file type detection)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ocrmypdf \
        wkhtmltopdf \
        ghostscript \
        tesseract-ocr \
        tesseract-ocr-eng \
        libreoffice-nogui \
        libmagic1 \
        tree && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements template and update pip packaging tools
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy full application source files
COPY . .

# Grant permissions to execute initialization script
RUN chmod +x start.sh

# Set PYTHONPATH to resolve parent package namespace references
ENV PYTHONPATH="/app:/app/ROXYBASICNEEDBOT"

CMD ["/bin/bash", "start.sh"]
