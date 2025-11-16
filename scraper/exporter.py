import csv
from typing import List

def export_to_csv(path: str, rows: List[str]):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title"])
        for row in rows:
            writer.writerow([row])
