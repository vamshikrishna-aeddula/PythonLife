# 07. AI Agent Studio, Tools and Triggers

30 questions: 4 Beginner, 22 Intermediate, 4 Advanced. Click a question's answer to reveal it.

### 07-001. What is AI Agent Studio?

**Level:** Beginner

<details>
<summary>Show answer</summary>

A unified environment to create, manage, test and configure AI agents and agentic workflows.

</details>

### 07-002. What does Guided Setup configure?

**Level:** Beginner

<details>
<summary>Show answer</summary>

Triggers, data sources, tools and display locations for agents and workflows.

</details>

### 07-003. Where do results appear after an agentic workflow runs?

**Level:** Beginner

<details>
<summary>Show answer</summary>

In the Otto (Now Assist) panel.

</details>

### 07-004. Which trigger types exist in the SDK?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

record_create, record_create_or_update, record_update, email, scheduled, daily, weekly and monthly. Users can also start agents manually.

</details>

### 07-005. Give an example of a record event trigger.

**Level:** Intermediate

<details>
<summary>Show answer</summary>

An agent that starts when a new incident is created or an existing one is updated.

</details>

### 07-006. What is a manual trigger?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A user starts the agent on demand, for example from the panel.

</details>

### 07-007. What is an email trigger?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

It starts an agent when an email event occurs, such as a message that arrives.

</details>

### 07-008. When would you use a scheduled trigger?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

For periodic work, such as a daily review of stale tickets.

</details>

### 07-009. Which kinds of tools can agents use?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Knowledge retrieval, web search, REST and other APIs, Integration Hub actions, record operations (CRUD), scripts and out-of-the-box tools.

</details>

### 07-010. What is a CRUD tool?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A tool that creates, reads, updates or deletes records on a table.

</details>

### 07-011. What is a script tool?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A tool that runs custom server-side logic for cases other tools cannot handle.

</details>

### 07-012. What does the web search tool give an agent?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Access to up-to-date public information.

</details>

### 07-013. What does the knowledge tool give an agent?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

The ability to search internal knowledge articles and documentation.

</details>

### 07-014. What does Integration Hub add to agents?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Connections to external systems through actions and spokes.

</details>

### 07-015. Why do tool descriptions matter?

**Level:** Advanced

<details>
<summary>Show answer</summary>

The model chooses tools based on their names and descriptions, so clear, accurate descriptions improve selection.

</details>

### 07-016. How do you test an agent?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Test and debug inside AI Agent Studio, starting with a simple agent with no tools before adding complexity.

</details>

### 07-017. Can AI help build agents?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Yes. Studio supports a natural language experience and AI help to generate names, roles and instructions that you then review.

</details>

### 07-018. Which Fluent SDK objects cover AI agents?

**Level:** Beginner

<details>
<summary>Show answer</summary>

AiAgent for single agents and AiAgenticWorkflow for orchestrated multi-agent workflows.

</details>

### 07-019. What does an AiAgent definition include?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A role, instructions, tools, optional triggers and data access settings, with support for versions.

</details>

### 07-020. What is the Base Plan?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

The initial instructions that set the orchestrator's plan at the workflow level.

</details>

### 07-021. Why start with a small agent?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Simple steps are easier to test and debug and reduce the chance of unpredictable behavior.

</details>

### 07-022. Why reuse agents instead of creating duplicates?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Reuse keeps behavior consistent and reduces maintenance and governance effort.

</details>

### 07-023. Design a trigger for automatic incident triage.

**Level:** Advanced

<details>
<summary>Show answer</summary>

Use a record_create trigger on incident with conditions, so a triage agent categorizes and routes new incidents.

</details>

### 07-024. How do you avoid trigger loops?

**Level:** Advanced

<details>
<summary>Show answer</summary>

If the agent updates the record that triggers it, add conditions or filters so the update does not start the agent again.

</details>

### 07-025. What are display locations?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Settings that decide where users can reach the agent, such as the panel or Virtual Agent.

</details>

### 07-026. How should roles be assigned to an agent?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Grant only the roles needed for its tools and data, using the agent's ACL and data access settings.

</details>

### 07-027. What are data sources in Guided Setup?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

The data the agent can use, configured so it works with the right information.

</details>

### 07-028. How many tools should an agent have?

**Level:** Advanced

<details>
<summary>Show answer</summary>

As few as needed, each with one clear purpose, to improve selection accuracy and reduce risk.

</details>

### 07-029. Why define clear exit conditions in instructions?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

They tell the agent when the task is done, which prevents unnecessary steps and cost.

</details>

### 07-030. What happens at runtime?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Triggers start agentic workflows, agents execute with orchestrator support, and results are shown in the panel.

</details>


[Back to index](../README.md)
