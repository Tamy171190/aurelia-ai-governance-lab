"""Load the synthetic inventory and produce classified records.

Requires only Python standard library modules.
"""

import csv
from pathlib import Path

from src.classification_engine import classify_records


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "data" / "ai_inventory.csv"
OUTPUT_FILE = BASE_DIR / "data" / "classified_inventory.csv"


with INPUT_FILE.open(newline="", encoding="utf-8") as handle:
    records = list(csv.DictReader(handle))

classified = classify_records(records)

fieldnames = list(classified[0].keys())
with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(classified)

print(f"Classified {len(classified)} AI systems")
print(f"Output written to {OUTPUT_FILE}")
