# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 30 - Downloads Folder Organizer (PythonLife)

What it does : sorts files into Images / Documents / Videos / Audio / Code /
               Archives / Others folders. Has a safe DRY-RUN mode.
Concepts     : pathlib, shutil, dictionaries of sets, avoiding overwrites.
Run          : python 30_file_organizer.py    (add --demo for a sample run)
"""
import shutil
import tempfile
from pathlib import Path
from pythonlife import run, ask

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi"},
    "Audio": {".mp3", ".wav", ".m4a"},
    "Code": {".py", ".java", ".js", ".html", ".css", ".sql"},
    "Archives": {".zip", ".rar", ".tar", ".gz", ".7z"},
}


def category_for(filename):
    ext = Path(filename).suffix.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"


def unique_path(dest):
    """file.txt -> file_1.txt if file.txt already exists."""
    n = 1
    while dest.exists():
        dest = dest.with_name(f"{dest.stem}_{n}{dest.suffix}")
        n += 1
    return dest


def organize(folder, dry_run=True):
    """Move files into category folders; returns the list of (source, destination)."""
    folder, moves = Path(folder), []
    for item in sorted(folder.iterdir()):
        if item.is_file():
            target_dir = folder / category_for(item.name)
            dest = unique_path(target_dir / item.name)
            moves.append((item, dest))
            if not dry_run:
                target_dir.mkdir(exist_ok=True)
                shutil.move(str(item), str(dest))
    return moves


def show(moves, root):
    for src, dest in moves:
        print(f"  {src.name:<22} -> {dest.relative_to(root)}")
    print(f"  {len(moves)} file(s)")


def main():
    folder = Path(ask("Folder to organize: ")).expanduser()
    if not folder.is_dir():
        print("  That folder does not exist.")
        return
    show(organize(folder, dry_run=True), folder)
    if ask("Move the files now? (y/n): ").lower() == "y":
        organize(folder, dry_run=False)
        print("  Done!")


def demo():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for name in ["photo.JPG", "notes.txt", "song.mp3", "app.py", "backup.zip", "mystery.xyz", "report.pdf"]:
            (root / name).write_text("sample")
        print("Dry run:")
        show(organize(root, dry_run=True), root)
        organize(root, dry_run=False)
        print("\nAfter organizing:", sorted(p.name for p in root.iterdir()))


if __name__ == "__main__":
    run(30, "Folder Organizer", main, demo)
