import subprocess
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
LOG_FILE = BASE_DIR / "logs" / "process.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

scripts = [
    "extract_text.py",
    "extract_tables.py",
    "validate_data.py"
]

def main():
    for script in scripts:
        logging.info(f"Running {script}")
        subprocess.run(["python", script], check=True)

    print("🚀 Batch processing completed successfully!")

if __name__ == "__main__":
    main()
