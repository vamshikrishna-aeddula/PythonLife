# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 33 - CSV Data Analyzer (PythonLife)

What it does : reads any CSV file and prints a summary for every column
               (min / max / mean / median for numbers, top values for text).
Concepts     : csv.DictReader, statistics module, try/except for type detection.
Run          : python 33_csv_analyzer.py      (add --demo for a sample run)
"""
import csv
import statistics
import tempfile
from collections import Counter
from pathlib import Path
from pythonlife import run, ask


def analyze_csv(path):
    """Return {column: summary-dict}."""
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    summary = {}
    for column in (rows[0].keys() if rows else []):
        values = [r[column].strip() for r in rows if r[column] and r[column].strip()]
        try:
            numbers = [float(v) for v in values]
            summary[column] = {"type": "number", "count": len(numbers), "min": min(numbers),
                               "max": max(numbers), "mean": round(statistics.mean(numbers), 2),
                               "median": statistics.median(numbers)}
        except ValueError:
            summary[column] = {"type": "text", "count": len(values),
                               "unique": len(set(values)), "top": Counter(values).most_common(3)}
    return summary


def show(summary):
    for column, info in summary.items():
        details = ", ".join(f"{k}={v}" for k, v in info.items() if k != "type")
        print(f"  {column:<10} [{info['type']}] {details}")


def main():
    path = Path(ask("Path to CSV file: ")).expanduser()
    if path.is_file():
        show(analyze_csv(path))
    else:
        print("  File not found.")


SAMPLE = """city,product,units,price
Hyderabad,Notebook,12,45.5
Chennai,Pen,40,10
Hyderabad,Pen,25,10
Pune,Notebook,8,45.5
Chennai,Bag,3,650
"""


def demo():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "sales.csv"
        path.write_text(SAMPLE, encoding="utf-8")
        show(analyze_csv(path))


if __name__ == "__main__":
    run(33, "CSV Data Analyzer", main, demo)
