# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 28 - Python Learning Roadmap Study Planner (PythonLife)

What it does : turns the PythonLife beginner roadmap into a dated study plan
               based on your start date and daily study hours.
Concepts     : lists of tuples, timedelta, while loops, weekday().
Run          : python 28_study_planner.py     (add --demo for a sample run)
"""
from datetime import date, timedelta
from pythonlife import run, ask, ask_float

# (topic, estimated hours) - edit freely to match your own pace
ROADMAP = [
    ("Setup, print() and variables", 3), ("Numbers, strings and input()", 4),
    ("Conditions: if / elif / else", 3), ("Loops: for and while", 4),
    ("Lists, tuples and sets", 5), ("Dictionaries", 4),
    ("Functions and scope", 5), ("Modules and packages", 3),
    ("File handling and JSON", 4), ("Exceptions and debugging", 3),
    ("Object-oriented programming", 8), ("Mini project: build one from this series", 10),
]


def build_schedule(topics, start, hours_per_day, skip_sunday=True):
    """Return a list of (date, topic, hours) rows."""
    if hours_per_day <= 0:
        raise ValueError("hours_per_day must be positive")

    def next_study_day(d):
        while skip_sunday and d.weekday() == 6:
            d += timedelta(days=1)
        return d

    day, free, plan = next_study_day(start), hours_per_day, []
    for topic, hours in topics:
        left = hours
        while left > 0:
            use = min(left, free)
            plan.append((day, topic, use))
            left -= use
            free -= use
            if free <= 0:
                day = next_study_day(day + timedelta(days=1))
                free = hours_per_day
    return plan


def show(plan):
    for d, topic, hrs in plan:
        print(f"  {d:%a %d %b %Y}  {hrs:>4g} h  {topic}")
    print(f"\nFinish date: {plan[-1][0]:%A, %d %B %Y}")


def main():
    start = date.fromisoformat(ask("Start date (YYYY-MM-DD): "))
    show(build_schedule(ROADMAP, start, ask_float("Hours per day: ", 0.5)))


def demo():
    show(build_schedule(ROADMAP[:4], date(2026, 11, 14), 2))


if __name__ == "__main__":
    run(28, "Python Roadmap Study Planner", main, demo)
