# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 31 - Duplicate File Finder (PythonLife)

What it does : finds files with identical content (even with different names)
               and shows how much space you could save.
Concepts     : hashing (SHA-256), reading files in chunks, grouping with dicts.
Run          : python 31_duplicate_finder.py  (add --demo for a sample run)
"""
import hashlib
import tempfile
from collections import defaultdict
from pathlib import Path
from pythonlife import run, ask


def file_hash(path, chunk=65536):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while block := f.read(chunk):
            h.update(block)
    return h.hexdigest()


def find_duplicates(folder):
    """Return a list of groups; each group is a list of identical files."""
    by_size = defaultdict(list)
    for p in Path(folder).rglob("*"):
        if p.is_file():
            by_size[p.stat().st_size].append(p)          # cheap check first
    by_hash = defaultdict(list)
    for same_size in by_size.values():
        if len(same_size) > 1:
            for p in same_size:
                by_hash[file_hash(p)].append(p)
    return [sorted(group) for group in by_hash.values() if len(group) > 1]


def show(groups):
    if not groups:
        print("  No duplicates found.")
    wasted = 0
    for i, group in enumerate(groups, 1):
        size = group[0].stat().st_size
        wasted += size * (len(group) - 1)
        print(f"  Group {i} ({size} bytes each):")
        for p in group:
            print("     ", p)
    print(f"  Space you could free: {wasted} bytes")


def main():
    folder = Path(ask("Folder to scan: ")).expanduser()
    if folder.is_dir():
        show(find_duplicates(folder))
    else:
        print("  That folder does not exist.")


def demo():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "sub").mkdir()
        (root / "a.txt").write_text("hello PythonLife")
        (root / "copy_of_a.txt").write_text("hello PythonLife")
        (root / "sub" / "a_backup.txt").write_text("hello PythonLife")
        (root / "b.txt").write_text("different content")
        (root / "c.txt").write_text("same size!!!!!!!!!")        # same size as nothing else
        groups = find_duplicates(root)
        show(groups)


if __name__ == "__main__":
    run(31, "Duplicate File Finder", main, demo)
