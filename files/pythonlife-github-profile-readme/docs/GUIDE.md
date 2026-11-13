# Guide

## Using a template

1. Create a public repository named exactly like your GitHub username, with a `README.md`.
2. Copy a file from `templates/` into that `README.md`.
3. Replace each `{{PLACEHOLDER}}`. Search for `{{` to find them all.
4. Commit. Your profile updates immediately.

## Placeholders

| Placeholder | Meaning | Example |
|---|---|---|
| `{{NAME}}` | Display name | Jane Doe |
| `{{USERNAME}}` | GitHub username | janedoe |
| `{{TAGLINE}}` | One line on what you do | small tools in Python |
| `{{ROLE}}` | Role or focus | Backend developer |
| `{{CURRENT_PROJECT}}` | What you are building | A habit tracker CLI |
| `{{LEARNING}}` | What you are studying | FastAPI |
| `{{BLOG_URL}}` | Blog or website | https://example.com |
| `{{LINKEDIN}}` | LinkedIn handle | janedoe |
| `{{EMAIL}}` | Contact email | jane@example.com |
| `{{START_DATE}}` | Start date (Template 3) | 2026-11-14 |

## Automatic latest posts

Template 4 includes a section that can update itself from an RSS feed.

1. Copy `scripts/update_posts.py` to `scripts/` in your profile repository.
2. Copy `examples/update-readme.yml` to `.github/workflows/update-readme.yml`.
3. Replace the feed URL in the workflow.
4. Run the workflow once from the Actions tab.

The script uses only the Python standard library. To run it locally:

```bash
python scripts/update_posts.py https://example.com/feed.xml 5
```

## Colors

Default palette, based on the Python logo. Replace with your brand colors if they differ.

| Use | Hex |
|---|---|
| Blue | `3776AB` |
| Yellow | `FFD43B` |
| Dark | `0D1117` |

## Before you publish

- No `{{` placeholders remain.
- Every link works.
- The profile reads well in light and dark mode.
- Images have alt text.
- The first screen explains who you are and what you do.

## Recommendations

- Lead with what you build and what you are learning.
- Use two or three badges at most. Third-party image widgets can go offline.
- Review the "Currently" section monthly so it stays accurate.
- Link only to repositories that have a README.
