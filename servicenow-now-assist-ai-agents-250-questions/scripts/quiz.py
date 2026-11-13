"""
quiz.py: practice the ServiceNow Now Assist and AI Agents question bank.

Usage:
    python scripts/quiz.py                          # 10 random questions
    python scripts/quiz.py -n 25 --level Advanced   # 25 advanced questions
    python scripts/quiz.py --category 07            # one topic (id prefix)
    python scripts/quiz.py --stats                  # counts by topic and level
    python scripts/quiz.py --no-prompt -n 5         # print Q&A without interaction

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import random
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "questions.json"


def load() -> list[dict]:
    return json.loads(DATA.read_text(encoding="utf-8"))


def show_stats(rows: list[dict]) -> None:
    by_cat = Counter((r["id"].split("-")[0], r["category"]) for r in rows)
    for (cid, name), n in sorted(by_cat.items()):
        print(f"{cid}  {name}: {n}")
    levels = Counter(r["level"] for r in rows)
    print("\nTotal:", len(rows), "|", ", ".join(f"{k}: {v}" for k, v in levels.items()))


def run_quiz(rows: list[dict], interactive: bool) -> None:
    score = 0
    for i, r in enumerate(rows, 1):
        print(f"\nQ{i}/{len(rows)} [{r['level']}] ({r['id']})\n{r['question']}")
        if interactive:
            input("Think of your answer, then press Enter to reveal... ")
        print(f"Answer: {r['answer']}")
        if interactive:
            score += input("Did you know it? (y/n) ").strip().lower().startswith("y")
    if interactive:
        print(f"\nScore: {score}/{len(rows)}")


def main() -> None:
    p = argparse.ArgumentParser(description="Practice quiz.")
    p.add_argument("-n", type=int, default=10, help="number of questions")
    p.add_argument("--level", choices=["Beginner", "Intermediate", "Advanced"])
    p.add_argument("--category", help="topic id prefix, for example 07")
    p.add_argument("--seed", type=int, help="seed for repeatable order")
    p.add_argument("--stats", action="store_true")
    p.add_argument("--no-prompt", action="store_true")
    a = p.parse_args()

    rows = load()
    if a.stats:
        show_stats(rows)
        return
    if a.level:
        rows = [r for r in rows if r["level"] == a.level]
    if a.category:
        rows = [r for r in rows if r["id"].startswith(a.category)]
    if not rows:
        raise SystemExit("No questions match those filters.")
    random.Random(a.seed).shuffle(rows)
    run_quiz(rows[: a.n], interactive=not a.no_prompt)


if __name__ == "__main__":
    main()
