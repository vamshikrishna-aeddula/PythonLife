# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 25 - Student Marks, Grades & Rank List (PythonLife)

What it does : totals, percentage, grade, pass/fail and class ranking.
Concepts     : nested dictionaries, sorted(), list comprehensions, enumerate.
Run          : python 25_grade_calculator.py  (add --demo for a sample run)
"""
from pythonlife import run, ask, ask_int

PASS_MARK = 35        # minimum marks needed in EVERY subject


def grade_for(percentage):
    for limit, letter in ((90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D")):
        if percentage >= limit:
            return letter
    return "F"


def build_report(students, max_marks=100):
    """students = {name: {subject: marks}} -> ranked list of result dicts."""
    rows = []
    for name, marks in students.items():
        total = sum(marks.values())
        pct = round(total / (len(marks) * max_marks) * 100, 2)
        failed = [s for s, m in marks.items() if m < PASS_MARK]
        rows.append({"name": name, "total": total, "percentage": pct, "grade": grade_for(pct),
                     "result": "FAIL" if failed else "PASS", "failed_in": failed})
    rows.sort(key=lambda r: r["percentage"], reverse=True)
    for rank, row in enumerate(rows, 1):
        row["rank"] = rank
    return rows


def show(rows):
    print(f"{'Rank':<5}{'Name':<12}{'Total':>6}{'%':>8}{'Grade':>7}  Result")
    for r in rows:
        extra = f" (low in {', '.join(r['failed_in'])})" if r["failed_in"] else ""
        print(f"{r['rank']:<5}{r['name']:<12}{r['total']:>6}{r['percentage']:>8}{r['grade']:>7}  {r['result']}{extra}")


def main():
    subjects = [s.strip() for s in ask("Subjects (comma separated): ").split(",") if s.strip()]
    students = {}
    while True:
        name = ask("Student name (blank to finish): ")
        if not name:
            break
        students[name] = {s: ask_int(f"  {s} marks (0-100): ", 0) for s in subjects}
    if students:
        show(build_report(students))


def demo():
    show(build_report({
        "Anil": {"Maths": 92, "Science": 88, "English": 79},
        "Bhavya": {"Maths": 67, "Science": 72, "English": 80},
        "Charan": {"Maths": 30, "Science": 65, "English": 58},
        "Divya": {"Maths": 95, "Science": 91, "English": 97},
    }))


if __name__ == "__main__":
    run(25, "Student Grade & Rank Calculator", main, demo)
