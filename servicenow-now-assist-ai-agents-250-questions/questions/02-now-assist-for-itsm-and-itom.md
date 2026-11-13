# 02. Now Assist for ITSM and ITOM

20 questions: 6 Beginner, 10 Intermediate, 4 Advanced. Click a question's answer to reveal it.

### 02-001. What does incident summarization do?

**Level:** Beginner

<details>
<summary>Show answer</summary>

It generates a concise summary of an incident's details and activity so a fulfiller can understand the case quickly.

</details>

### 02-002. What is resolution notes generation?

**Level:** Beginner

<details>
<summary>Show answer</summary>

A skill that drafts resolution notes from the record's activity when an agent resolves or closes it.

</details>

### 02-003. What is knowledge article generation from a record?

**Level:** Beginner

<details>
<summary>Show answer</summary>

A skill that creates a draft knowledge article from a resolved record so the solution can be reused. A human reviews it before publishing.

</details>

### 02-004. What is the goal of Now Assist for ITSM?

**Level:** Beginner

<details>
<summary>Show answer</summary>

To help ITSM agents resolve incidents faster using generative AI.

</details>

### 02-005. What does chat summarization help with?

**Level:** Beginner

<details>
<summary>Show answer</summary>

It summarizes a live conversation so an agent who joins or follows up gets context without rereading everything.

</details>

### 02-006. Why does summary quality depend on record quality?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

The model works from the record content. Sparse or inconsistent work notes produce weak summaries, so good data practices still matter.

</details>

### 02-007. How can you limit Now Assist to licensed fulfillers?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Create a custom role for agents and assign it only to fulfillers who hold licensed seats, then use it in skill access settings.

</details>

### 02-008. How can you turn off Now Assist for a specific catalog item?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Use the Now Assist setting on the catalog item (the field to turn off Now Assist conversation for the item).

</details>

### 02-009. What should you check if Virtual Agent and AI Search give different Now Assist results?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Make sure the Now Assist plugins are up to date, then re-index the AI Search sources.

</details>

### 02-010. Why should agents review generated content?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

LLM output can be wrong or incomplete. A human in the loop confirms accuracy before it is saved or sent.

</details>

### 02-011. What is a typical activation flow for a Now Assist skill?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Install the Now Assist plugin from the Store, confirm entitlements, activate the skill in AI Admin Hub, assign access roles, test in a non-production instance, then roll out.

</details>

### 02-012. Why test skills in a sub-production instance first?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

To check output quality, access control, and assist consumption before real users depend on it.

</details>

### 02-013. How would you measure the return on summarization skills?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Baseline handle time and resolution time first. Then track usage, acceptance and edit rates, user feedback and assist consumption, and compare them with the baseline.

</details>

### 02-014. What is the aim of Now Assist for ITOM?

**Level:** Beginner

<details>
<summary>Show answer</summary>

To help operations teams understand and resolve issues faster using generative AI. Available features vary by release, so check the documentation.

</details>

### 02-015. Should a generated summary replace the underlying record?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

No. The record remains the system of record. The summary is a convenience layer.

</details>

### 02-016. What prevents a user from seeing data through a skill that they cannot normally access?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Access controls and role restrictions. User access decides who can run the skill, and role restrictions decide which roles the skill runs with.

</details>

### 02-017. How would you roll out Now Assist for ITSM in phases?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Start with one skill and a pilot group, measure adoption and quality, collect feedback, adjust prompts and access, then expand to more skills and teams.

</details>

### 02-018. How should sensitive information in work notes be handled?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Use the platform's data privacy controls, rely on the guardrails, train users not to paste secrets into tickets, and review the product's data handling documentation.

</details>

### 02-019. How can you keep assist consumption under control?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Activate only the skills you need, restrict them to the right roles, and avoid automatic triggering where users gain little value.

</details>

### 02-020. Which adoption metrics would you report to leadership?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Skill usage, acceptance versus edit rates, time to resolve, user satisfaction and assist consumption per skill.

</details>


[Back to index](../README.md)
