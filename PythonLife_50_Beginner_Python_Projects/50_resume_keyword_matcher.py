# SPDX-License-Identifier: MIT
# Copyright (c) 2026 PythonLife - see LICENSE in the project root.
"""Project 50 - Resume vs Job Description Keyword Matcher (ATS Score) (PythonLife)

What it does : compares your resume text with a job description, scores the
               skill match (like an ATS) and lists the skills you should add
               - only if you truly have them!
Concepts     : regular expressions with word boundaries, sets, text files.
Run          : python 50_resume_keyword_matcher.py (add --demo for a sample run)
"""
import re
from pathlib import Path
from pythonlife import run, ask

SKILLS = ["python", "java", "spring boot", "hibernate", "microservices", "rest api", "sql", "mysql",
          "postgresql", "mongodb", "html", "css", "javascript", "react", "angular", "git", "github",
          "docker", "kubernetes", "aws", "junit", "maven", "linux", "ci/cd", "jenkins", "django",
          "flask", "fastapi", "pandas", "numpy", "machine learning", "generative ai", "agile", "c++"]


def find_skills(text):
    """Return the set of known skills that appear as whole words in text."""
    text = text.lower()
    found = set()
    for skill in SKILLS:
        pattern = r"(?<![a-z0-9+#])" + re.escape(skill) + r"(?![a-z0-9+#])"
        if re.search(pattern, text):
            found.add(skill)
    return found


def match_report(resume, job):
    wanted, have = find_skills(job), find_skills(resume)
    matched, missing = sorted(wanted & have), sorted(wanted - have)
    score = round(len(matched) / len(wanted) * 100) if wanted else 0
    return {"score": score, "matched": matched, "missing": missing,
            "extra_skills": sorted(have - wanted)}


def show(report):
    print(f"  Match score  : {report['score']}%")
    print(f"  Matched      : {', '.join(report['matched']) or '-'}")
    print(f"  Missing      : {', '.join(report['missing']) or '-'}")
    print(f"  Extra skills : {', '.join(report['extra_skills']) or '-'}")
    print("  Tip: add a missing skill only if you genuinely have it, in a real project or role.")


def main():
    resume = Path(ask("Resume .txt path: ")).expanduser()
    job = Path(ask("Job description .txt path: ")).expanduser()
    if resume.is_file() and job.is_file():
        show(match_report(resume.read_text(encoding="utf-8"), job.read_text(encoding="utf-8")))
    else:
        print("  One of the files was not found.")


RESUME = "Java full stack developer. Skills: Java, Spring Boot, Hibernate, MySQL, HTML, CSS, JavaScript, Git, Maven, JUnit."
JOB = "Looking for a developer with Java, Spring Boot, REST API, Microservices, MySQL, Docker, Git and JavaScript experience."


def demo():
    show(match_report(RESUME, JOB))
    print("  Note: 'java' alone is NOT matched inside 'javascript':", find_skills("I know javascript only"))


if __name__ == "__main__":
    run(50, "Resume Keyword Matcher (ATS)", main, demo)
