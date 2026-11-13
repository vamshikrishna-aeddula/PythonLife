# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 26 - Attendance Tracker with Shortage Alerts (PythonLife)

What it does : mark attendance per day, see each student's percentage and who
               is below the required minimum (default 75%).
Concepts     : classes, JSON, sets, percentage maths.
Run          : python 26_attendance_tracker.py (add --demo for a sample run)
"""
import json
from pathlib import Path
from pythonlife import run, ask, choose, data_file


class Attendance:
    def __init__(self, path, students=None):
        self.path = Path(path)
        if self.path.exists():
            saved = json.loads(self.path.read_text(encoding="utf-8"))
            self.students, self.days = saved["students"], saved["days"]
        else:
            self.students, self.days = list(students or []), {}

    def _save(self):
        self.path.write_text(json.dumps({"students": self.students, "days": self.days}, indent=2),
                             encoding="utf-8")

    def mark_day(self, day, absent=()):
        """Everyone is present except the names listed in `absent`."""
        absent = {a.strip().title() for a in absent}
        unknown = absent - set(self.students)
        if unknown:
            raise ValueError(f"unknown students: {sorted(unknown)}")
        self.days[day] = {s: ("A" if s in absent else "P") for s in self.students}
        self._save()

    def percentage(self, student):
        marks = [d[student] for d in self.days.values() if student in d]
        return round(marks.count("P") / len(marks) * 100, 1) if marks else 0.0

    def shortage(self, minimum=75):
        return {s: self.percentage(s) for s in self.students if self.percentage(s) < minimum}


def show(att):
    print(f"Classes held: {len(att.days)}")
    for s in att.students:
        flag = "  <-- below 75%" if s in att.shortage() else ""
        print(f"  {s:<10} {att.percentage(s):>6}%{flag}")


def main():
    path = data_file("attendance.json")
    if not Path(path).exists():
        names = ask("Student names (comma separated): ")
        att = Attendance(path, [n.strip().title() for n in names.split(",") if n.strip()])
    else:
        att = Attendance(path)
    while True:
        pick = choose(["Mark a day", "Show report"])
        if pick == 0:
            break
        if pick == 1:
            try:
                day = ask("Date (YYYY-MM-DD): ")
                absent = ask("Absent names (comma separated, Enter = none): ")
                att.mark_day(day, [n for n in absent.split(",") if n.strip()])
            except ValueError as err:
                print("  Oops:", err)
        else:
            show(att)


def demo():
    att = Attendance(data_file("attendance.json"), ["Asha", "Bharat", "Chitra"])
    att.mark_day("2026-11-02", ["Bharat"])
    att.mark_day("2026-11-03", ["Bharat", "Chitra"])
    att.mark_day("2026-11-04", [])
    att.mark_day("2026-11-05", ["Bharat"])
    show(att)


if __name__ == "__main__":
    run(26, "Attendance Tracker", main, demo)
