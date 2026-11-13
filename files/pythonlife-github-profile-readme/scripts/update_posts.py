"""
update_posts.py — PythonLife profile README updater.

Reads an RSS feed and rewrites the section between the
<!-- BLOG-POST-LIST:START --> and <!-- BLOG-POST-LIST:END --> markers
in README.md. Standard library only.

Usage:
    python scripts/update_posts.py https://example.com/feed.xml 5
"""

from __future__ import annotations

import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

README = Path("README.md")
START = "<!-- BLOG-POST-LIST:START -->"
END = "<!-- BLOG-POST-LIST:END -->"


def fetch_posts(feed_url: str, limit: int) -> list[tuple[str, str]]:
    """Return up to `limit` (title, link) pairs from an RSS 2.0 feed."""
    req = urllib.request.Request(feed_url, headers={"User-Agent": "pythonlife-readme"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        root = ET.fromstring(resp.read())

    posts = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if title and link:
            posts.append((title, link))
        if len(posts) >= limit:
            break
    return posts


def render(posts: list[tuple[str, str]]) -> str:
    if not posts:
        return "_No posts yet. Check back soon!_"
    return "\n".join(f"- [{title}]({link})" for title, link in posts)


def update_readme(content: str, block: str) -> str:
    pattern = re.compile(f"{re.escape(START)}.*?{re.escape(END)}", re.DOTALL)
    if not pattern.search(content):
        raise SystemExit(f"Markers not found in {README}. Add {START} and {END}.")
    # A function replacement avoids backslash issues in post titles.
    return pattern.sub(lambda _: f"{START}\n{block}\n{END}", content)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Usage: update_posts.py FEED_URL [LIMIT]")

    feed_url = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    block = render(fetch_posts(feed_url, limit))
    original = README.read_text(encoding="utf-8")
    README.write_text(update_readme(original, block), encoding="utf-8")
    print(f"Updated README with {limit} posts max.")
