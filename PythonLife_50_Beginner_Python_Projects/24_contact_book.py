# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 24 - Contact Book with Search (PythonLife)

What it does : save names, phones and emails; search by any part of the name.
Concepts     : dict of dicts, JSON, string cleaning, case-insensitive search.
Run          : python 24_contact_book.py      (add --demo for a sample run)
"""
import json
from pathlib import Path
from pythonlife import run, ask, choose, data_file


def clean_phone(phone):
    """Keep digits and a leading + only."""
    digits = "".join(ch for ch in phone if ch.isdigit())
    return ("+" if phone.strip().startswith("+") else "") + digits


class ContactBook:
    def __init__(self, path):
        self.path = Path(path)
        self.data = json.loads(self.path.read_text(encoding="utf-8")) if self.path.exists() else {}

    def _save(self):
        self.path.write_text(json.dumps(self.data, indent=2), encoding="utf-8")

    def add(self, name, phone, email=""):
        if not name.strip():
            raise ValueError("name cannot be empty")
        self.data[name.strip().title()] = {"phone": clean_phone(phone), "email": email.strip()}
        self._save()

    def search(self, term):
        term = term.lower()
        return {n: c for n, c in self.data.items() if term in n.lower()}

    def delete(self, name):
        del self.data[name.title()]
        self._save()


def show(contacts):
    if not contacts:
        print("  No contacts found.")
    for name, c in sorted(contacts.items()):
        print(f"  {name:<18} {c['phone']:<15} {c['email']}")


def main():
    book = ContactBook(data_file("contacts.json"))
    while True:
        pick = choose(["Add contact", "Search", "Delete", "List all"])
        if pick == 0:
            break
        try:
            if pick == 1:
                book.add(ask("Name: "), ask("Phone: "), ask("Email: "))
            elif pick == 2:
                show(book.search(ask("Search: ")))
            elif pick == 3:
                book.delete(ask("Exact name: "))
            else:
                show(book.data)
        except (ValueError, KeyError) as err:
            print("  Oops:", repr(err))


def demo():
    book = ContactBook(data_file("contacts.json"))
    book.add("ravi kumar", "+91 98765-43210", "ravi@example.com")
    book.add("sita devi", "(040) 2345 6789")
    book.add("ravi teja", "99999 88888")
    print("Search 'ravi':")
    show(book.search("ravi"))
    book.delete("Sita Devi")
    print("After delete:")
    show(book.data)


if __name__ == "__main__":
    run(24, "Contact Book", main, demo)
