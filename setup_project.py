from pathlib import Path

# Root project directory
PROJECT_NAME = "engineering-pdf-extractor"
BASE_DIR = Path(PROJECT_NAME)

# Folder structure
folders = [
    BASE_DIR / "data" / "raw_pdfs",
    BASE_DIR / "data" / "extracted_text",
    BASE_DIR / "data" / "tables",
    BASE_DIR / "data" / "output",
    BASE_DIR / "src",
    BASE_DIR / "logs"
]

# Files to create
files = [
    BASE_DIR / "src" / "extract_text.py",
    BASE_DIR / "src" / "extract_tables.py",
    BASE_DIR / "src" / "validate_data.py",
    BASE_DIR / "src" / "batch_process.py",
    BASE_DIR / "logs" / "process.log",
    BASE_DIR / "requirements.txt",
    BASE_DIR / "README.md"
]

def create_structure():
    # Create folders
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    # Create files
    for file in files:
        file.touch(exist_ok=True)

    print("✅ Project structure created successfully!")

if __name__ == "__main__":
    create_structure()
