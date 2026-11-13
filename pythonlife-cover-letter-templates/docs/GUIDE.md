# Guide

## How to use a template

1. Pick the template that matches your situation (see the table below).
2. Copy the text between the code fences into a document or email.
3. Replace every `{{PLACEHOLDER}}`. Search for `{{` to find them.
4. Delete any sentence you cannot support with a fact.
5. Check the result with the linter (below), then send.

## Which template?

| Situation | Template |
|---|---|
| First Python job | [01 Junior Python Developer](../templates/01-junior-python-developer.md) |
| Changing careers | [02 Career Switcher](../templates/02-career-switcher.md) |
| Experienced engineer | [03 Backend and API Developer](../templates/03-backend-api-developer.md) |
| Data roles | [04 Data Analyst and Data Scientist](../templates/04-data-analyst-scientist.md) |
| Student or intern | [05 Student and Internship](../templates/05-student-internship.md) |
| Client project | [06 Freelance Proposal](../templates/06-freelance-proposal.md) |
| No open role, or a referral | [07 Referral and Cold Outreach](../templates/07-referral-or-cold-outreach.md) |

See a filled-in version in [EXAMPLE.md](EXAMPLE.md).

## The structure that works

Every template follows four parts:

1. **Hook:** one sentence showing you know this company.
2. **Proof:** two or three specific results, with numbers.
3. **Fit:** map your proof to the posting's requirements.
4. **Close:** one clear next step.

## Tailor in ten minutes

1. Read the posting and underline the two requirements that appear most often.
2. Find one real example from your work for each.
3. Find one fact about the company: a launch, a blog post, an open-source project.
4. Put those three things into the template. Cut everything else.

## Write placeholders well

| Placeholder | Weak | Strong |
|---|---|---|
| `{{SPECIFIC_THING}}` | is growing fast | launched a public API for invoicing |
| `{{RESULT_OR_USERS}}` | works well | is used by 14 freelancers |
| `{{ACHIEVEMENT_1}}` | worked on performance | reduced API response time from 900 ms to 220 ms |

## Format

- One page, about 200 to 350 words. Outreach messages: under 150.
- Send as PDF unless told otherwise. Name it `Firstname-Lastname-CoverLetter-Company.pdf`.
- Use plain text or a simple layout. Many applicant tracking systems struggle with tables, columns and images.
- Address a named person when you can. Check the posting, the company page or LinkedIn. If you cannot find one, use "Dear {{COMPANY}} Hiring Team".

## Check your letter with the linter

```bash
python scripts/check_letter.py my_letter.txt --company "Brightline"
python scripts/check_letter.py outreach.txt --short
```

It reports leftover placeholders, length, generic phrases, repetitive openings and missing numbers. It uses only the Python standard library.

## Follow-up message

Send one follow-up about a week after applying:

```text
Subject: Following up on the {{ROLE}} application

Hi {{HIRING_MANAGER}},

I applied for the {{ROLE}} role on {{DATE_APPLIED}} and wanted to confirm that my application arrived. I remain very interested in {{TEAM_OR_PRODUCT}}, and I am happy to share more about {{PROJECT_1}} if useful.

Thank you,
{{YOUR_NAME}}
```

## Before you send

- No `{{` placeholders remain.
- The company name and role are spelled correctly.
- Every claim is true and can be backed up in an interview.
- Links work and the GitHub profile is tidy.
- The file name is professional.
- Someone else has read it once.

## Common mistakes

- Repeating your CV instead of adding the story behind it.
- Opening with "I am writing to apply for...".
- Listing skills without proof.
- Using the same letter for every company.
- Exceeding one page.
