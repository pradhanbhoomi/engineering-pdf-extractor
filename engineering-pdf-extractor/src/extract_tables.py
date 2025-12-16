import camelot
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
PDF_DIR = BASE_DIR / "data" / "raw_pdfs"
TABLE_DIR = BASE_DIR / "data" / "tables"

TABLE_DIR.mkdir(exist_ok=True)

def extract_tables_from_pdf(pdf_path):
    tables = camelot.read_pdf(
        str(pdf_path),
        pages="all",
        flavor="lattice"  # works well for bordered tables
    )
    return tables

def main():
    pdf_files = list(PDF_DIR.glob("*.pdf"))

    for pdf in pdf_files:
        print(f"📄 Extracting tables from: {pdf.name}")
        tables = extract_tables_from_pdf(pdf)

        if tables.n == 0:
            print("⚠️ No tables found.")
            continue

        for i, table in enumerate(tables):
            output_file = TABLE_DIR / f"{pdf.stem}_table_{i}.csv"
            table.df.to_csv(output_file, index=False)
            print(f"✅ Saved: {output_file.name}")

if __name__ == "__main__":
    main()
