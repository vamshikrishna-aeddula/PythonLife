# 06. AI Agents Fundamentals

30 questions: 9 Beginner, 18 Intermediate, 3 Advanced. Click a question's answer to reveal it.

### 06-001. What is an AI agent in ServiceNow?

**Level:** Beginner

<details>
<summary>Show answer</summary>

A software entity that uses an LLM to reason, plans steps, uses tools and data, and completes tasks toward a goal.

</details>

### 06-002. How does agentic AI differ from generative AI?

**Level:** Beginner

<details>
<summary>Show answer</summary>

Generative AI produces content. Agentic AI plans, decides and acts across steps by using tools.

</details>

### 06-003. What is an agentic workflow?

**Level:** Beginner

<details>
<summary>Show answer</summary>

A workflow in which a team of AI agents, coordinated by the orchestrator, works toward a defined objective.

</details>

### 06-004. Which table stores AI agents?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

sn_aia_agent.

</details>

### 06-005. Which table stores agentic workflows?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

sn_aia_usecase.

</details>

### 06-006. Which reasoning pattern do agents follow?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

ReAct: thought, action and observation loops that repeat until the problem is solved.

</details>

### 06-007. What is a tool for an AI agent?

**Level:** Beginner

<details>
<summary>Show answer</summary>

A capability the agent can call to read data, take an action or get information.

</details>

### 06-008. What is the difference between interactive and autonomous agents?

**Level:** Beginner

<details>
<summary>Show answer</summary>

Interactive agents reach out to users for information when needed. Autonomous agents work in the background without conversation.

</details>

### 06-009. What is the AI agent background channel?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A channel that lets agents be invoked and run conversations in the background, without a user being present.

</details>

### 06-010. What is an AI agent team?

**Level:** Beginner

<details>
<summary>Show answer</summary>

Several agents with different roles that collaborate to complete a larger task.

</details>

### 06-011. Why use teams of agents?

**Level:** Beginner

<details>
<summary>Show answer</summary>

ServiceNow states that teams deliver better results than single agents on simple to complex workflows, with each agent specialized.

</details>

### 06-012. What do an agent's instructions do?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

They describe how the agent should behave and what steps it should follow.

</details>

### 06-013. What does the agent's role define?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

The agent's purpose and persona, which helps the orchestrator and the model decide how to use it.

</details>

### 06-014. How does an agent get its identity and data access?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Through a run-as user or a data access configuration. In the SDK, data access is required when no run-as user is set.

</details>

### 06-015. Does an agent have its own ACL?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Yes. An ACL derived from the agent's internal name is created, with role records that control who can use it.

</details>

### 06-016. Why should tools have a single purpose?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Multipurpose tools confuse agents and make tool selection and debugging harder.

</details>

### 06-017. Which model framework underlies AI Agent Studio, according to the release notes?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A GPT-4o-based framework, and localization follows the support of that model.

</details>

### 06-018. Which browsers are supported for AI agents and Studio?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Google Chrome and Microsoft Edge, among others. Internet Explorer is not supported.

</details>

### 06-019. Give examples of out-of-the-box agents.

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Release notes mention agents such as Platform Approval Assistance and Platform Request status, plus password reset in example scenarios.

</details>

### 06-020. What is AI Agent Advisor?

**Level:** Beginner

<details>
<summary>Show answer</summary>

A capability that analyzes business data, surfaces high-impact automation opportunities and helps build and deploy agents. It became generally available in 2026.

</details>

### 06-021. What is AI Agent Evaluator?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

An Australia release component for assessing the quality of agents. Check current documentation for details.

</details>

### 06-022. What is the Autonomous Workforce?

**Level:** Beginner

<details>
<summary>Show answer</summary>

ServiceNow's set of AI specialists announced at Knowledge 2026 that run on shared platform infrastructure and governance.

</details>

### 06-023. How does an agent differ from a flow?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A flow is deterministic and predefined. An agent reasons dynamically and chooses its next step.

</details>

### 06-024. When should you not use an agent?

**Level:** Advanced

<details>
<summary>Show answer</summary>

For fixed, high-volume or compliance-critical steps where a deterministic flow is more predictable and cheaper.

</details>

### 06-025. What are the main risks of agentic AI?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Wrong or unauthorized actions, excessive permissions, prompt injection, unpredictable behavior and cost. Mitigate with least privilege, approvals, testing and monitoring.

</details>

### 06-026. How do you keep a human in the loop?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Add approval steps for sensitive actions, use features such as Intelligent Approvals, and let interactive agents ask users for confirmation.

</details>

### 06-027. What are Intelligent Approvals?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

An Australia release capability for AI-assisted approvals. Check the release notes for current scope.

</details>

### 06-028. How can you reuse an existing agent?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Duplicate it in AI Agent Studio. Cloned agents can reference their source agent.

</details>

### 06-029. Does AI Agent Studio support versions?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Yes. Agents can have multiple versions with different configurations.

</details>

### 06-030. What kind of task suits a first AI agent project?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A narrow, low-risk task with clear tools and success criteria, such as checking request status or suggesting triage.

</details>


[Back to index](../README.md)
