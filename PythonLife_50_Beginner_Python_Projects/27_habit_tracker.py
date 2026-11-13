# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 27 - Daily Habit Tracker with Streaks (PythonLife)

What it does : tick off habits each day and see current + longest streaks.
Concepts     : sets, sorting, date arithmetic, JSON.
Run          : python 27_habit_tracker.py     (add --demo for a sample run)
"""
import json
from datetime import date, timedelta
from pathlib import Path
from pythonlife import run, ask, choose, data_file


def streaks(dates, today):
    """Return (current_streak, longest_streak) from a list of ISO date strings."""
    days = sorted({date.fromisoformat(d) for d in dates})
    longest = chain = 0
    previous = None
    for d in days:
        chain = chain + 1 if previous and (d - previous).days == 1 else 1
        longest = max(longest, chain)
        previous = d
    current = 0
    if days and (today - days[-1]).days <= 1:      # today or yesterday keeps it alive
        current = 1
        i = len(days) - 1
        while i > 0 and (days[i] - days[i - 1]).days == 1:
            current += 1
            i -= 1
    return current, longest


class HabitTracker:
    def __init__(self, path):
        self.path = Path(path)
        self.habits = json.loads(self.path.read_text(encoding="utf-8")) if self.path.exists() else {}

    def check_in(self, habit, day):
        days = self.habits.setdefault(habit.lower(), [])
        if day not in days:
            days.append(day)
        self.path.write_text(json.dumps(self.habits, indent=2), encoding="utf-8")


def show(tracker, today):
    for habit, days in tracker.habits.items():
        cur, best = streaks(days, today)
        print(f"  {habit:<18} current streak: {cur:>3}   longest: {best:>3}   total days: {len(set(days))}")


def main():
    tracker = HabitTracker(data_file("habits.json"))
    while True:
        pick = choose(["Check in a habit for today", "Show streaks"])
        if pick == 0:
            break
        if pick == 1:
            tracker.check_in(ask("Habit (e.g. coding 1 hour): "), date.today().isoformat())
        else:
            show(tracker, date.today())


def demo():
    tracker = HabitTracker(data_file("habits.json"))
    today = date(2026, 11, 13)
    for offset in [0, 1, 2, 3, 6, 7, 8, 9, 10, 11]:      # a gap on day 4-5
        tracker.check_in("practice python", (today - timedelta(days=offset)).isoformat())
    for offset in [1, 2]:
        tracker.check_in("read docs", (today - timedelta(days=offset)).isoformat())
    show(tracker, today)


if __name__ == "__main__":
    run(27, "Daily Habit Tracker", main, demo)
