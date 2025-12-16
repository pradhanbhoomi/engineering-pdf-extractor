📘 Engineering PDF Data Extraction & Validation
🔍 Overview

This project automates the extraction, cleaning, and validation of structured engineering information from multi-page PDF documents. It handles inconsistent table layouts, malformed data, and mixed formatting commonly found in real-world engineering drawings.

🛠️ Tech Stack

Python

pdfplumber / PyMuPDF

Camelot

Pandas

Regex

Logging & Automation

📂 Pipeline

Extracts raw text from engineering PDFs

Extracts tabular data (BOM-like tables)

Cleans semi-structured tables

Validates data consistency using regex & rules

Batch processes entire folders via one command

▶️ How to Run
pip install -r requirements.txt
cd src
python batch_process.py

✅ Output

Validated CSV files

Error-tolerant processing

Detailed logs

📌 Notes

Publicly available government engineering PDFs were used for demonstration purposes.
