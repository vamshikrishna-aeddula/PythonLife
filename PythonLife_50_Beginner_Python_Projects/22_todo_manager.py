# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 22 - To-Do Manager with Priorities & Due Dates (PythonLife)

What it does : add, complete, delete and list tasks; data is saved in a JSON file.
Concepts     : classes, JSON persistence, sorting with key=, dates.
Run          : python 22_todo_manager.py      (add --demo for a sample run)
"""
import json
from datetime import date
from pathlib import Path
from pythonlife import run, ask, choose, data_file

PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


class TodoList:
    def __init__(self, path):
        self.path = Path(path)
        self.tasks = json.loads(self.path.read_text(encoding="utf-8")) if self.path.exists() else []

    def _save(self):
        self.path.write_text(json.dumps(self.tasks, indent=2), encoding="utf-8")

    def add(self, title, priority="medium", due=None):
        if priority not in PRIORITY_ORDER:
            raise ValueError("priority must be high, medium or low")
        task_id = max((t["id"] for t in self.tasks), default=0) + 1
        self.tasks.append({"id": task_id, "title": title, "priority": priority,
                           "due": due, "done": False})
        self._save()
        return task_id

    def _find(self, task_id):
        for t in self.tasks:
            if t["id"] == task_id:
                return t
        raise KeyError(f"no task with id {task_id}")

    def complete(self, task_id):
        self._find(task_id)["done"] = True
        self._save()

    def remove(self, task_id):
        self.tasks.remove(self._find(task_id))
        self._save()

    def pending(self):
        """Not-done tasks: high priority first, then earliest due date."""
        todo = [t for t in self.tasks if not t["done"]]
        return sorted(todo, key=lambda t: (PRIORITY_ORDER[t["priority"]], t["due"] or "9999-99-99"))


def show(tasks):
    if not tasks:
        print("  (nothing here - enjoy your day!)")
    today = date.today().isoformat()
    for t in tasks:
        flag = " OVERDUE" if t["due"] and t["due"] < today and not t["done"] else ""
        print(f"  [{'x' if t['done'] else ' '}] #{t['id']} {t['title']} ({t['priority']}, due {t['due'] or '-'}){flag}")


def main():
    todo = TodoList(data_file("todo.json"))
    while True:
        pick = choose(["Add task", "Show pending", "Complete task", "Delete task"])
        if pick == 0:
            break
        try:
            if pick == 1:
                todo.add(ask("Title: "), ask("Priority (high/medium/low): ").lower() or "medium",
                         ask("Due date YYYY-MM-DD (optional): ") or None)
            elif pick == 2:
                show(todo.pending())
            elif pick == 3:
                todo.complete(int(ask("Task id: ")))
            else:
                todo.remove(int(ask("Task id: ")))
        except (ValueError, KeyError) as err:
            print("  Oops:", err)


def demo():
    todo = TodoList(data_file("todo.json"))
    todo.add("Finish Python project 22", "high", "2026-11-15")
    a = todo.add("Revise loops", "medium", "2026-11-20")
    todo.add("Watch a PythonLife class recording", "low")
    todo.complete(a)
    print("Pending tasks:")
    show(todo.pending())
    reloaded = TodoList(todo.path)
    print(f"\nReloaded from disk: {len(reloaded.tasks)} tasks saved.")


if __name__ == "__main__":
    run(22, "To-Do Manager", main, demo)
