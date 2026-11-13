# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 45 - Student Database with SQLite (PythonLife)

What it does : create, read, update and delete students stored in a real
               SQL database, plus averages per course and the topper.
Concepts     : sqlite3, SQL (CREATE/INSERT/SELECT/UPDATE/DELETE/GROUP BY),
               parameterised queries (protects against SQL injection).
Run          : python 45_student_database.py  (add --demo for a sample run)
"""
import sqlite3
from pythonlife import run, ask, ask_float, ask_int, choose, data_file


class StudentDB:
    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(str(path))
        self.conn.execute("""CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            marks REAL CHECK (marks BETWEEN 0 AND 100))""")

    def add(self, name, course, marks):
        cur = self.conn.execute("INSERT INTO students (name, course, marks) VALUES (?, ?, ?)",
                                (name, course, marks))
        self.conn.commit()
        return cur.lastrowid

    def all(self):
        return self.conn.execute("SELECT id, name, course, marks FROM students ORDER BY id").fetchall()

    def update_marks(self, student_id, marks):
        cur = self.conn.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, student_id))
        self.conn.commit()
        return cur.rowcount == 1

    def delete(self, student_id):
        cur = self.conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
        self.conn.commit()
        return cur.rowcount == 1

    def average_by_course(self):
        return self.conn.execute(
            "SELECT course, ROUND(AVG(marks), 2), COUNT(*) FROM students GROUP BY course ORDER BY course"
        ).fetchall()

    def topper(self):
        return self.conn.execute("SELECT name, course, marks FROM students ORDER BY marks DESC LIMIT 1").fetchone()


def show(rows):
    for row in rows:
        print("  ", row)


def main():
    db = StudentDB(data_file("students.db"))
    while True:
        pick = choose(["Add student", "List all", "Update marks", "Delete", "Course averages"])
        if pick == 0:
            break
        try:
            if pick == 1:
                db.add(ask("Name: "), ask("Course: "), ask_float("Marks (0-100): ", 0))
            elif pick == 2:
                show(db.all())
            elif pick == 3:
                print("  Updated" if db.update_marks(ask_int("Id: "), ask_float("New marks: ", 0)) else "  No such id")
            elif pick == 4:
                print("  Deleted" if db.delete(ask_int("Id: ")) else "  No such id")
            else:
                show(db.average_by_course())
        except sqlite3.IntegrityError as err:
            print("  Oops:", err)


def demo():
    db = StudentDB()                       # in-memory database: nothing saved to disk
    for name, course, marks in [("Anil", "Java", 82), ("Bhavya", "Python", 91),
                                ("Charan", "Python", 76), ("Divya", "Java", 88)]:
        db.add(name, course, marks)
    db.update_marks(3, 79)
    db.delete(1)
    print("Students:")
    show(db.all())
    print("Averages (course, avg, count):", db.average_by_course())
    print("Topper:", db.topper())


if __name__ == "__main__":
    run(45, "Student Database (SQLite)", main, demo)
