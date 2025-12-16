import pandas as pd
import re
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
TABLE_DIR = BASE_DIR / "data" / "tables"
OUTPUT_DIR = BASE_DIR / "data" / "output"
LOG_DIR = BASE_DIR / "logs"

OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "process.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

EXERCISE_PATTERN = r"^\d+\.\d+\.\d+$"

def clean_and_validate(df, filename):
    # Drop fully empty rows
    df = df.dropna(how="all")

    # If more than 3 columns, keep first 3
    if df.shape[1] > 3:
        logging.warning(f"{filename}: Extra columns detected, trimming to first 3")
        df = df.iloc[:, :3]

    # If less than 3 columns, skip
    if df.shape[1] < 3:
        logging.warning(f"{filename}: Not enough columns, skipping")
        return None

    df.columns = ["Exercise_No", "Topic", "Page_No"]

    # Strip whitespace safely (no deprecated applymap)
    for col in df.columns:
        df[col] = df[col].astype(str).str.strip()

    # Validation flags
    df["valid_exercise_no"] = df["Exercise_No"].apply(
        lambda x: bool(re.match(EXERCISE_PATTERN, x))
    )

    df["missing_topic"] = df["Topic"] == ""
    df["missing_page"] = df["Page_No"] == ""

    return df

def main():
    for file in TABLE_DIR.glob("*.csv"):
        logging.info(f"Processing {file.name}")
        df = pd.read_csv(file)

        cleaned_df = clean_and_validate(df, file.name)

        if cleaned_df is None:
            print(f"⚠️ Skipped: {file.name}")
            continue

        output_file = OUTPUT_DIR / f"validated_{file.name}"
        cleaned_df.to_csv(output_file, index=False)

        print(f"✅ Validated: {output_file.name}")
        logging.info(f"Saved {output_file.name}")

if __name__ == "__main__":
    main()
