# Guide

## Customize

1. Copy the template folder you want.
2. Open `index.html` in any editor and search for `{{`.
3. Replace each placeholder with your own text.
4. Open the file in a browser to preview. No server is needed.

Each project is a repeated block. To add a fourth project, copy one project block and number its placeholders `PROJECT_4_*`. To remove one, delete the block.

## Placeholders

| Placeholder | Meaning | Example |
|---|---|---|
| `{{NAME}}` | Your name | Jane Doe |
| `{{ROLE}}` | Your role | Python developer |
| `{{TAGLINE}}` | One line on what you do | I build reliable data tools |
| `{{ABOUT}}` | Two to four sentences about you | |
| `{{USERNAME}}` | GitHub username | janedoe |
| `{{LINKEDIN}}` | LinkedIn handle | janedoe |
| `{{EMAIL}}` | Contact email | jane@example.com |
| `{{OPEN_TO}}` | What you want | freelance work and full-time roles |
| `{{PROJECT_n_TITLE}}` | Project name | Expense Tracker |
| `{{PROJECT_n_URL}}` | Link to the repo or demo | https://github.com/janedoe/expense-tracker |
| `{{PROJECT_n_SUMMARY}}` | One sentence | A CLI that tracks spending in CSV |
| `{{PROJECT_n_TECH}}` | Main technology | pandas |
| `{{PROJECT_n_PROBLEM}}` | Case Study only: the problem | Spreadsheets were slow to update |
| `{{PROJECT_n_APPROACH}}` | Case Study only: what you did | Built a CLI with Click and tests |
| `{{PROJECT_n_RESULT}}` | Case Study only: the outcome | Cut monthly reporting from 2 hours to 5 minutes |
| `{{JOB_TITLE}}`, `{{COMPANY}}`, `{{DATES}}`, `{{JOB_SUMMARY}}` | Classic only: experience | |

## Publish on GitHub Pages

1. Create a public repository named `{{USERNAME}}.github.io`.
2. Upload your edited file as `index.html` in the repository root.
3. Go to Settings, then Pages. Set the source to the `main` branch and the `/ (root)` folder.
4. After a minute your site is live at `https://{{USERNAME}}.github.io`.

## Brand colors

The templates use the Python palette through CSS variables at the top of each file. Change `--blue` and `--yellow` to match your brand.

| Variable | Default |
|---|---|
| `--blue` | `#3776ab` |
| `--yellow` | `#ffd43b` |

## Before you publish

- No `{{` placeholders remain.
- Every link works.
- Each project links to a repository with a README.
- The page looks right in light and dark mode and on a phone.
- The `<title>` and meta description describe you in one sentence each.

## Writing good content

- Lead with what you build, not a list of technologies.
- Show three to four projects, not ten. Finished work beats a long list.
- Give each project one measurable result where you can.
- Keep the about section short and specific.

## SEO

- Set `<title>` to your name and role. Keep it under 60 characters.
- Write the meta description as one sentence under 160 characters.
- The Open Graph tags control how your link looks when shared on LinkedIn, Slack and other sites. They reuse your name, role and tagline.
- Add a custom domain in Settings, then Pages, once you own one.

## Accessibility

- Keep one `h1` per page and do not skip heading levels.
- Give every link text that makes sense out of context. Avoid "click here".
- If you add images, always include `alt` text.
- Test with the keyboard: press Tab and confirm each link shows a visible outline.

## Printing

All templates include print styles. Use your browser's Print dialog and choose "Save as PDF" for a one-page CV.

## Choosing a template

| If you are | Choose |
|---|---|
| A developer who wants a safe, general portfolio | Classic |
| Happy to show personality | Terminal |
| Applying for roles where reasoning matters | Case Study |
| A data scientist or analyst | Notebook |
| A backend or API developer | API Reference |
| Selling your services | Freelancer |
| Early in your career or switching careers | Journey |

## Placeholders for the newer templates

| Placeholder | Template | Meaning |
|---|---|---|
| `{{METRIC_n_VALUE}}`, `{{METRIC_n_LABEL}}` | Notebook | A result and what it measures, e.g. 38% and "faster reports" |
| `{{SERVICE_n_TITLE}}`, `{{SERVICE_n_DESC}}` | Freelancer | A service you offer and one sentence on it |
| `{{STEP_n_TITLE}}`, `{{STEP_n_DESC}}` | Freelancer | A step in your process |
| `{{CTA_TEXT}}` | Freelancer | Button text, e.g. "Book a call" |
| `{{TESTIMONIAL_QUOTE}}`, `{{TESTIMONIAL_AUTHOR}}` | Freelancer | A real client quote and who said it |
| `{{MILESTONE_n_DATE}}`, `{{MILESTONE_n_TITLE}}`, `{{MILESTONE_n_DESC}}` | Journey | A step in your learning timeline |
| `{{CERT_n}}` | Journey | A certification or course |

API Reference reuses the shared placeholders and shows your skills as a fixed list in the file. Edit that list directly.
