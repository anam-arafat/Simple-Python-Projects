# Project Overview

This repository contains three GUI applications built with Python and `tkinter`:

1. **QR Code Generator** (`qrmaker.py`)
2. **URL Shortener** (`shortenurl.py`)
3. **PDF Reader** (`pdfreader.py`)

## Requirements

- Python 3.x
- `qrcode` library (for QR Code Generator)
- `Pillow` library (for QR Code Generator)
- `requests` library (for URL Shortener)
- `PyPDF2` library (for PDF Reader)
- `tkinter` library (standard with Python)

## Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required libraries:
   ```bash
   pip install qrcode[pil] pillow requests PyPDF2
   ```

## Applications

### QR Code Generator

**File:** `qrmaker.py`

#### Description

This application allows users to generate QR codes from text input. Users can customize the foreground and background colors of the QR code.

#### Usage

1. Run the application:
   ```bash
   python qrmaker.py
   ```
2. Enter the text for the QR code in the text entry field.
3. Click "Generate QR Code" to create and view the QR code.
4. Use the "Download QR Code" button to save the QR code image.

### URL Shortener

**File:** `shortenurl.py`

#### Description

This application shortens URLs using the Cutt.ly API. Users can input a long URL, shorten it, and copy the shortened URL to the clipboard.

#### Usage

1. Update the `API_KEY` variable in `shortenurl.py` with your Cutt.ly API key.
2. Run the application:
   ```bash
   python shortenurl.py
   ```
3. Enter the URL you want to shorten in the text entry field.
4. Click "Shorten URL" to generate and view the shortened URL.
5. Use the "Copy to Clipboard" button to copy the shortened URL.

### PDF Reader

**File:** `pdfreader.py`

#### Description

This application extracts text from PDF files. Users can select a PDF file, view its text content in a scrollable text box, and copy the extracted text to the clipboard.

#### Usage

1. Run the application:
   ```bash
   python pdfreader.py
   ```
2. Click "Select PDF" to open a file dialog and choose a PDF file.
3. View the extracted text in the scrollable text box.
4. Use the "Copy to Clipboard" button to copy the text.
