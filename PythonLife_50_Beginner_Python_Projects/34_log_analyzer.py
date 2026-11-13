# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 34 - Server Log Analyzer (PythonLife)

What it does : reads log lines such as
               "2026-11-10 14:05:33 ERROR Database timeout"
               and reports levels, busiest error hours and most common errors.
Concepts     : regular expressions with groups, Counter, file processing.
Run          : python 34_log_analyzer.py      (add --demo for a sample run)
"""
import re
from collections import Counter
from pathlib import Path
from pythonlife import run, ask

LINE = re.compile(r"^(\d{4}-\d{2}-\d{2}) (\d{2}):\d{2}:\d{2} (DEBUG|INFO|WARNING|ERROR|CRITICAL) (.*)$")


def analyze(lines):
    levels, error_hours, error_msgs, bad = Counter(), Counter(), Counter(), 0
    for line in lines:
        m = LINE.match(line.strip())
        if not m:
            bad += 1
            continue
        _, hour, level, message = m.groups()
        levels[level] += 1
        if level in ("ERROR", "CRITICAL"):
            error_hours[f"{hour}:00"] += 1
            error_msgs[message] += 1
    return {"levels": dict(levels), "error_hours": error_hours.most_common(3),
            "top_errors": error_msgs.most_common(3), "unparsed_lines": bad}


def show(report):
    for key, value in report.items():
        print(f"  {key:<15}: {value}")


def main():
    path = Path(ask("Path to log file: ")).expanduser()
    if path.is_file():
        show(analyze(path.read_text(encoding="utf-8", errors="replace").splitlines()))
    else:
        print("  File not found.")


SAMPLE_LOG = """2026-11-10 09:01:10 INFO Server started
2026-11-10 09:15:42 WARNING Disk usage at 82%
2026-11-10 14:05:33 ERROR Database timeout
2026-11-10 14:07:01 ERROR Database timeout
2026-11-10 14:30:00 ERROR Payment gateway unreachable
2026-11-10 15:10:12 INFO User login
2026-11-10 16:45:00 CRITICAL Out of memory
this line is not a valid log entry
"""


def demo():
    show(analyze(SAMPLE_LOG.splitlines()))


if __name__ == "__main__":
    run(34, "Server Log Analyzer", main, demo)
