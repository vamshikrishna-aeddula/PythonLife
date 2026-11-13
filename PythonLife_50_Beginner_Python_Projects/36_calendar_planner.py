# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 36 - Monthly Calendar Planner (PythonLife)

What it does : prints a month calendar with * on days that have events, then
               lists the events below it. Monday is the first day.
Concepts     : the calendar module, dictionaries, string formatting.
Run          : python 36_calendar_planner.py  (add --demo for a sample run)
"""
import calendar
from datetime import date
from pythonlife import run, ask, ask_int


def render_month(year, month, events=None):
    """Return the calendar as text. events = {day_number: 'description'}."""
    events = events or {}
    cal = calendar.Calendar(firstweekday=0)
    title = f"{calendar.month_name[month]} {year}"
    lines = [title.center(21), "Mo Tu We Th Fr Sa Su"]
    for week in cal.monthdayscalendar(year, month):
        cells = []
        for day in week:
            if day == 0:
                cells.append("   ")
            else:
                cells.append(f"{day:>2}{'*' if day in events else ' '}")
        lines.append("".join(cells).rstrip())
    if events:
        lines.append("")
        lines += [f"* {day:>2} {calendar.month_abbr[month]}: {text}" for day, text in sorted(events.items())]
    return "\n".join(lines)


def main():
    today = date.today()
    year = ask_int(f"Year ({today.year}): ", 1)
    month = ask_int("Month (1-12): ", 1)
    events = {}
    while True:
        day = ask("Event day number (blank to finish): ")
        if not day.isdigit():
            break
        events[int(day)] = ask("  Description: ")
    print(render_month(year, month, events))


def demo():
    print(render_month(2026, 11, {14: "Python class", 26: "Project submission", 30: "Revision"}))


if __name__ == "__main__":
    run(36, "Monthly Calendar Planner", main, demo)
