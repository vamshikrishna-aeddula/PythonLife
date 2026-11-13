# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 46 - Searchable Notes App with Tags (SQLite) (PythonLife)

What it does : save notes with tags, search by words, filter by tag.
Concepts     : sqlite3, LIKE queries, datetime timestamps, simple data modelling.
Run          : python 46_notes_app.py         (add --demo for a sample run)
"""
import sqlite3
from datetime import datetime
from pythonlife import run, ask, choose, data_file


class Notes:
    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(str(path))
        self.conn.execute("""CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL,
            body TEXT, tags TEXT, created TEXT)""")

    def add(self, title, body="", tags=""):
        tags = ",".join(t.strip().lower() for t in tags.split(",") if t.strip())
        cur = self.conn.execute("INSERT INTO notes (title, body, tags, created) VALUES (?,?,?,?)",
                                (title, body, tags, datetime.now().isoformat(timespec="seconds")))
        self.conn.commit()
        return cur.lastrowid

    def search(self, term):
        like = f"%{term}%"
        return self.conn.execute(
            "SELECT id, title, tags FROM notes WHERE title LIKE ? OR body LIKE ? OR tags LIKE ? ORDER BY id",
            (like, like, like)).fetchall()

    def by_tag(self, tag):
        tag = tag.strip().lower()
        rows = self.conn.execute("SELECT id, title, tags FROM notes").fetchall()
        return [r for r in rows if tag in r[2].split(",")]


def main():
    notes = Notes(data_file("notes.db"))
    while True:
        pick = choose(["Add note", "Search text", "Filter by tag"])
        if pick == 0:
            break
        if pick == 1:
            notes.add(ask("Title: "), ask("Body: "), ask("Tags (comma separated): "))
        elif pick == 2:
            print(" ", notes.search(ask("Search for: ")))
        else:
            print(" ", notes.by_tag(ask("Tag: ")))


def demo():
    notes = Notes()
    notes.add("List comprehension trick", "[x*x for x in range(5)] builds squares", "python, tips")
    notes.add("Project idea", "Build an expense tracker with CSV", "projects, python")
    notes.add("Grocery list", "milk, rice, dal", "home")
    print("Search 'range':", notes.search("range"))
    print("Tag 'python'  :", notes.by_tag("python"))
    print("Tag 'home'    :", notes.by_tag("home"))


if __name__ == "__main__":
    run(46, "Searchable Notes App", main, demo)
