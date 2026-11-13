# 09. Governance, Security and Responsible AI

30 questions: 3 Beginner, 18 Intermediate, 9 Advanced. Click a question's answer to reveal it.

### 09-001. Which five areas does AI Control Tower cover in the Australia release?

**Level:** Beginner

<details>
<summary>Show answer</summary>

Discovery, observation, governance, security and measurement.

</details>

### 09-002. When was AI Control Tower introduced?

**Level:** Beginner

<details>
<summary>Show answer</summary>

It was introduced in 2025, around Knowledge 2025, and expanded in the Australia release.

</details>

### 09-003. What do the new AI Control Tower connectors do?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

They let it discover and govern AI beyond ServiceNow. About 30 new enterprise connectors span AWS, Google Cloud, Microsoft Azure and apps such as SAP.

</details>

### 09-004. What financial visibility does AI Control Tower add?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Cost tracking and ROI dashboards that show model spend.

</details>

### 09-005. What did the Traceloop acquisition add?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Deep observability into AI agent behavior at runtime.

</details>

### 09-006. What did the Veza acquisition add?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Identity and access security capabilities for governing what agents and people can access.

</details>

### 09-007. What is publishing to Microsoft Agent 365?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

An Australia Patch 2 capability that sends ServiceNow agents to the Microsoft external registry.

</details>

### 09-008. What can you customize about the AI security score?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Its calculation, so it reflects your own security requirements.

</details>

### 09-009. What do the new security metrics monitor?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

LLM and agent output for security policy violations, personal data and potential threats.

</details>

### 09-010. What is Now Assist Guardian?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A guardrail layer that screens requests and responses for problems such as harmful content or attempts to misuse the model.

</details>

### 09-011. What is prompt injection?

**Level:** Beginner

<details>
<summary>Show answer</summary>

An attack that hides instructions in input or retrieved content to make the model ignore its rules or misuse tools.

</details>

### 09-012. How do you reduce prompt injection risk in agents?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Give least-privilege access, limit tools, treat retrieved text as data, add approvals for sensitive actions, use guardrails and monitor behavior.

</details>

### 09-013. What does least privilege mean for an agent?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

The agent has only the roles, tools and data it needs for its task and nothing more.

</details>

### 09-014. How is an agent's ACL named?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

From its internal name in the form domain.scope.agentName, with matching role records.

</details>

### 09-015. What do role restrictions do for skills?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

They define the roles under which a skill runs, which limits the data it can touch.

</details>

### 09-016. Where can you read how ServiceNow handles your data with Now Assist?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

In the Data Handling and Security documentation for Now Assist.

</details>

### 09-017. What is ServiceNow's responsible AI commitment?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

It publishes a responsible AI white paper and says its LLMs are developed with responsible AI guidelines.

</details>

### 09-018. Where can you find information on how Now LLM was built?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

In the Now LLM model cards in the documentation.

</details>

### 09-019. Why is auditability important for AI actions?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

It lets you trace what an agent did, why and with whose permissions, for troubleshooting and compliance.

</details>

### 09-020. What does risk classification do for AI assets?

**Level:** Advanced

<details>
<summary>Show answer</summary>

It categorizes AI assets by risk so controls, reviews and approvals match the level of risk.

</details>

### 09-021. How do you relate AI governance to regulation?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Use the governance records to inventory AI systems and map them to risk categories, and involve legal and compliance teams for obligations.

</details>

### 09-022. What identity checks apply to Action Fabric?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Every action carries identity verification, permission scoping and an audit trail through AI Control Tower.

</details>

### 09-023. How do you handle personal data in prompts?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Minimize what is sent, mask or exclude it where possible, apply privacy controls and review provider data terms.

</details>

### 09-024. How do you red team an agent?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Test with adversarial inputs, injection attempts and boundary cases, record failures, then fix instructions, tools and permissions.

</details>

### 09-025. Which agent actions need human approval?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Destructive, financial, security-sensitive or hard-to-reverse actions, such as deleting records or changing access.

</details>

### 09-026. Why consider log retention for AI interactions?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Logs help investigation but may contain sensitive data, so retention and access need policy.

</details>

### 09-027. Why test for bias?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Models can produce uneven results for different groups, so testing supports fair and responsible outcomes.

</details>

### 09-028. Why separate builders from approvers?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Segregation of duties reduces the chance that one person can deploy a risky agent without review.

</details>

### 09-029. What does AI lifecycle management involve?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Tracking assets from idea through development, testing, production and retirement with approvals at each stage.

</details>

### 09-030. What would you do if an agent behaves badly in production?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Disable or restrict it, review traces and logs, find the root cause, fix and retest, and document the lessons.

</details>


[Back to index](../README.md)
