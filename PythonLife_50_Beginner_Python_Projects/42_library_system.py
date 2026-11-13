# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 42 - Library Management System (PythonLife)

What it does : add books, issue/return them to members, track due dates and
               calculate late fines.
Concepts     : classes & objects, dataclasses, custom errors, date arithmetic.
Run          : python 42_library_system.py    (add --demo for a sample run)
"""
from dataclasses import dataclass
from datetime import date, timedelta
from pythonlife import run, ask, choose

LOAN_DAYS = 14
FINE_PER_DAY = 2          # currency units per late day


class LibraryError(Exception):
    """Raised for rule violations (unknown book, already issued...)."""


@dataclass
class Book:
    isbn: str
    title: str
    author: str
    borrower: str = ""
    due: date = None


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author):
        if isbn in self.books:
            raise LibraryError("a book with this ISBN already exists")
        self.books[isbn] = Book(isbn, title, author)

    def _get(self, isbn):
        if isbn not in self.books:
            raise LibraryError("unknown ISBN")
        return self.books[isbn]

    def issue(self, isbn, member, today):
        book = self._get(isbn)
        if book.borrower:
            raise LibraryError(f"'{book.title}' is already issued to {book.borrower}")
        book.borrower, book.due = member, today + timedelta(days=LOAN_DAYS)
        return book.due

    def give_back(self, isbn, today):
        """Returns the fine (0 if on time)."""
        book = self._get(isbn)
        if not book.borrower:
            raise LibraryError("this book is not issued")
        late_days = max(0, (today - book.due).days)
        book.borrower, book.due = "", None
        return late_days * FINE_PER_DAY

    def available(self):
        return [b.title for b in self.books.values() if not b.borrower]


def main():
    lib = Library()
    while True:
        pick = choose(["Add book", "Issue book", "Return book", "List available"])
        if pick == 0:
            break
        try:
            if pick == 1:
                lib.add_book(ask("ISBN: "), ask("Title: "), ask("Author: "))
            elif pick == 2:
                print("  Due on", lib.issue(ask("ISBN: "), ask("Member: "), date.today()))
            elif pick == 3:
                print("  Fine:", lib.give_back(ask("ISBN: "), date.today()))
            else:
                print("  ", lib.available())
        except LibraryError as err:
            print("  Oops:", err)


def demo():
    lib = Library()
    lib.add_book("111", "Automate the Boring Stuff", "Al Sweigart")
    lib.add_book("222", "Python Crash Course", "Eric Matthes")
    due = lib.issue("111", "Ravi", date(2026, 11, 1))
    print("Issued '111' to Ravi, due", due)
    try:
        lib.issue("111", "Sita", date(2026, 11, 2))
    except LibraryError as err:
        print("Blocked:", err)
    print("Fine for returning 5 days late:", lib.give_back("111", due + timedelta(days=5)))
    print("Available now:", lib.available())


if __name__ == "__main__":
    run(42, "Library Management System", main, demo)
