# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 32 - Bulk File Renamer (PythonLife)

What it does : renames many files to  prefix_001.ext, prefix_002.ext ...
               with a preview first. Great for photos and lecture notes.
Concepts     : pathlib, sorting, f-string number padding, safe two-step renaming.
Run          : python 32_bulk_renamer.py      (add --demo for a sample run)
"""
import tempfile
from pathlib import Path
from pythonlife import run, ask, ask_int


def plan_renames(folder, prefix, start=1, extension=None):
    """Return [(old_path, new_path)] without touching any file."""
    files = [p for p in sorted(Path(folder).iterdir())
             if p.is_file() and (extension is None or p.suffix.lower() == extension.lower())]
    sources = set(files)
    plan = []
    for n, old in enumerate(files, start):
        new = old.with_name(f"{prefix}_{n:03d}{old.suffix.lower()}")
        if new.exists() and new not in sources:
            raise FileExistsError(f"{new.name} already exists - choose another prefix")
        plan.append((old, new))
    return plan


def apply_renames(plan):
    """Two steps (old -> temp -> new) so names can never collide halfway."""
    temps = []
    for old, new in plan:
        tmp = old.with_name(old.name + ".pltmp")
        old.rename(tmp)
        temps.append((tmp, new))
    for tmp, new in temps:
        tmp.rename(new)


def show(plan):
    for old, new in plan:
        print(f"  {old.name:<22} -> {new.name}")


def main():
    folder = Path(ask("Folder: ")).expanduser()
    if not folder.is_dir():
        print("  That folder does not exist.")
        return
    ext = ask("Only this extension, e.g. .jpg (Enter = all files): ") or None
    plan = plan_renames(folder, ask("New name prefix: "), ask_int("Start number: ", 0), ext)
    show(plan)
    if plan and ask("Rename now? (y/n): ").lower() == "y":
        apply_renames(plan)
        print("  Done!")


def demo():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for name in ["IMG_8841.JPG", "IMG_8842.JPG", "holiday.png", "notes.txt"]:
            (root / name).write_text("x")
        plan = plan_renames(root, "goa_trip", 1, ".jpg")
        show(plan)
        apply_renames(plan)
        print("Folder now:", sorted(p.name for p in root.iterdir()))


if __name__ == "__main__":
    run(32, "Bulk File Renamer", main, demo)
