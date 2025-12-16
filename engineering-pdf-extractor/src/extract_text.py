import pdfplumber
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parents[1]
PDF_DIR = BASE_DIR / "data" / "raw_pdfs"
TEXT_DIR = BASE_DIR / "data" / "extracted_text"

TEXT_DIR.mkdir(exist_ok=True)

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from all pages of a PDF
    """
    full_text = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text()
            if page_text:
                full_text.append(f"\n--- Page {page_number} ---\n")
                full_text.append(page_text)

    return "\n".join(full_text)

def main():
    pdf_files = list(PDF_DIR.glob("*.pdf"))

    if not pdf_files:
        print("❌ No PDF files found in raw_pdfs folder.")
        return

    for pdf in pdf_files:
        print(f"📄 Processing: {pdf.name}")
        extracted_text = extract_text_from_pdf(pdf)

        output_file = TEXT_DIR / f"{pdf.stem}.txt"
        output_file.write_text(extracted_text, encoding="utf-8")

        print(f"✅ Text saved to: {output_file.name}")

if __name__ == "__main__":
    main()
