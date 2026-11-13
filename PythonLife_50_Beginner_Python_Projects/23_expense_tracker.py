# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 23 - Expense Tracker with Category & Monthly Reports (PythonLife)

What it does : records expenses in a CSV file and summarises spending.
Concepts     : csv module, defaultdict, date strings, formatted reports.
Run          : python 23_expense_tracker.py   (add --demo for a sample run)
"""
import csv
from collections import defaultdict
from datetime import date
from pathlib import Path
from pythonlife import run, ask, ask_float, choose, data_file

FIELDS = ["date", "category", "amount", "note"]


def add_expense(path, day, category, amount, note=""):
    path = Path(path)
    new_file = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow({"date": day, "category": category.title(),
                         "amount": f"{float(amount):.2f}", "note": note})


def load_expenses(path):
    if not Path(path).exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return [{**row, "amount": float(row["amount"])} for row in csv.DictReader(f)]


def by_category(rows, month=None):
    """Total per category; month like '2026-11' limits the report."""
    totals = defaultdict(float)
    for r in rows:
        if month is None or r["date"].startswith(month):
            totals[r["category"]] += r["amount"]
    return dict(sorted(totals.items(), key=lambda kv: kv[1], reverse=True))


def show_report(rows, month=None):
    totals = by_category(rows, month)
    grand = sum(totals.values())
    for cat, amt in totals.items():
        share = amt / grand * 100
        print(f"  {cat:<14}{amt:>10,.2f}  {share:5.1f}%  {'#' * int(share // 5)}")
    print(f"  {'TOTAL':<14}{grand:>10,.2f}")


def main():
    path = data_file("expenses.csv")
    while True:
        pick = choose(["Add expense", "Report for a month", "Report for all time"])
        if pick == 0:
            break
        if pick == 1:
            add_expense(path, ask("Date (YYYY-MM-DD, Enter = today): ") or date.today().isoformat(),
                        ask("Category: "), ask_float("Amount: ", 0), ask("Note: "))
        else:
            month = ask("Month (YYYY-MM): ") if pick == 2 else None
            show_report(load_expenses(path), month)


def demo():
    path = data_file("expenses.csv")
    for d, c, a, n in [("2026-11-01", "food", 450, "groceries"), ("2026-11-03", "travel", 1200, "bus pass"),
                       ("2026-11-05", "food", 320, "dinner"), ("2026-11-09", "learning", 2500, "course book"),
                       ("2026-10-28", "food", 700, "last month")]:
        add_expense(path, d, c, a, n)
    print("November 2026:")
    show_report(load_expenses(path), "2026-11")


if __name__ == "__main__":
    run(23, "Expense Tracker", main, demo)
