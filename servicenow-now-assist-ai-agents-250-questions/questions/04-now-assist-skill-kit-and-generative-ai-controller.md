# 04. Now Assist Skill Kit and Generative AI Controller

25 questions: 4 Beginner, 15 Intermediate, 6 Advanced. Click a question's answer to reveal it.

### 04-001. What is Now Assist Skill Kit?

**Level:** Beginner

<details>
<summary>Show answer</summary>

A tool for building, testing and managing custom generative AI skills on the Now Platform.

</details>

### 04-002. Where do you start creating a custom skill?

**Level:** Beginner

<details>
<summary>Show answer</summary>

Go to All, then Now Assist Skill Kit, then Home, and select Create new skill.

</details>

### 04-003. Which role is required to create a skill in Skill Kit?

**Level:** Beginner

<details>
<summary>Show answer</summary>

sn_skill_builder.admin.

</details>

### 04-004. What options exist for creating the prompt?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Write it from scratch, choose one from the prompt library, or use an AI-generated prompt.

</details>

### 04-005. Which providers can a skill use?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Now LLM and prebuilt spokes that connect to external LLMs, such as Azure OpenAI, OpenAI, Aleph Alpha, WatsonX and Google Gemini. Check the current list for your release.

</details>

### 04-006. Do LLM spokes consume Integration Hub transactions?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

No. According to the documentation, the spokes consume assists instead.

</details>

### 04-007. What user access options does a skill have?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Any authenticated user, or selected roles. A user needs only one of the selected roles to run the skill.

</details>

### 04-008. How do user access and role restrictions differ?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Access settings and ACLs control who may trigger the skill. Role restrictions define the roles the skill runs with during execution.

</details>

### 04-009. What are skill inputs and outputs?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Inputs are the values passed into the prompt. Outputs define the form of the result returned to the caller.

</details>

### 04-010. What is a skill prompt?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

The instructions, context and variables sent to the LLM to produce the result.

</details>

### 04-011. What is a tool in Skill Kit?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A component the skill can use to retrieve data or take an action, added alongside the prompt.

</details>

### 04-012. Why update the Generative AI Controller when you update Skill Kit?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

The documentation says to keep them aligned so custom skills continue to perform correctly.

</details>

### 04-013. What does the Skill Kit evaluation feature do?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

It lets you test and assess skill output quality. It uses an OEM third-party call, and errors from it do not consume assists.

</details>

### 04-014. What are good prompt design practices?

**Level:** Advanced

<details>
<summary>Show answer</summary>

State the role and task clearly, provide context and constraints, define the output format, add examples when useful, and test with varied inputs.

</details>

### 04-015. How do you reduce hallucinations in a custom skill?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Ground the prompt in retrieved data, instruct the model to say when information is missing, limit the scope, validate output, and test with edge cases.

</details>

### 04-016. What is few-shot prompting?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Including a few example inputs and outputs in the prompt to guide format and tone.

</details>

### 04-017. What is grounding?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Supplying trusted data or documents as context so the model answers from them instead of guessing.

</details>

### 04-018. Why should each skill do one job?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Single-purpose skills are easier to test, tune, reuse and secure.

</details>

### 04-019. What is a spoke in this context?

**Level:** Beginner

<details>
<summary>Show answer</summary>

An Integration Hub package that connects the platform to an external service, such as an LLM provider.

</details>

### 04-020. When would you use the generic LLM connector?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

When you want to connect to an LLM that has no prebuilt spoke, using its API.

</details>

### 04-021. How do you choose between Now LLM and an external LLM?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Consider quality for the task, language support, data and contractual requirements, cost, and integration effort. Now LLM is the managed default and external models add choice.

</details>

### 04-022. Who pays for third-party LLM usage?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

The customer, through their own provider subscription. Separate charges may apply in addition to assists.

</details>

### 04-023. How would you promote a custom skill to production?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Build and test in development, evaluate the output, then move the skill through your normal release process and verify access and consumption in production.

</details>

### 04-024. Why apply least privilege to skills?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A skill can reach data and actions through its roles. Narrow roles limit the damage of mistakes or misuse.

</details>

### 04-025. How would you test a custom skill before release?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Run it on varied, realistic inputs, use the evaluation feature, check access and role behavior, and review outputs for accuracy, tone and safety.

</details>


[Back to index](../README.md)
