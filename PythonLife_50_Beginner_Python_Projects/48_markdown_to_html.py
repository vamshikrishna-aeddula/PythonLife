# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 48 - Mini Markdown to HTML Converter (PythonLife)

What it does : converts headings, **bold**, *italic*, `code`, links, bullet
               lists and ``` code blocks to safe HTML.
Concepts     : regular expressions & substitution, html.escape (security!),
               state machines (are we inside a list / code block?).
Run          : python 48_markdown_to_html.py  (add --demo for a sample run)
"""
import html
import re
from pathlib import Path
from pythonlife import run, ask


def inline(text):
    text = html.escape(text)                                  # stops <script> injection
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', text)
    return text


def md_to_html(md):
    out, para, items, code = [], [], [], None

    def flush():
        nonlocal para, items
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []
        if items:
            out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>")
            items = []

    for line in md.splitlines():
        if line.startswith("```"):
            if code is None:
                flush()
                code = []
            else:
                out.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
                code = None
            continue
        if code is not None:
            code.append(line)
            continue
        heading = re.match(r"(#{1,6})\s+(.*)", line)
        if heading:
            flush()
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
        elif re.match(r"[-*]\s+", line):
            if para:
                flush()
            items.append(re.sub(r"^[-*]\s+", "", line))
        elif not line.strip():
            flush()
        else:
            if items:
                flush()
            para.append(line.strip())
    flush()
    return "\n".join(out)


def main():
    path = Path(ask("Markdown file path: ")).expanduser()
    if not path.is_file():
        print("  File not found.")
        return
    target = path.with_suffix(".html")
    target.write_text(md_to_html(path.read_text(encoding="utf-8")), encoding="utf-8")
    print("  Saved", target)


SAMPLE = """# PythonLife Notes
Learning **Python** is *fun*. Visit [Python](https://www.python.org).

## Shopping
- use `print()`
- avoid <script>alert(1)</script>

```
for i in range(3):
    print(i)
```
"""


def demo():
    print(md_to_html(SAMPLE))


if __name__ == "__main__":
    run(48, "Markdown to HTML Converter", main, demo)
