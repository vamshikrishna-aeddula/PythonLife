# 08. Orchestration, Multi-Agent and Agentic Workflows

25 questions: 1 Beginner, 14 Intermediate, 10 Advanced. Click a question's answer to reveal it.

### 08-001. What does the AI Agent Orchestrator do?

**Level:** Beginner

<details>
<summary>Show answer</summary>

It coordinates collaboration among agents, routes requests between them, and manages iterative problem solving.

</details>

### 08-002. What does the dynamic orchestrator do?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

It maps the right agents to the user's agentic workflow to improve performance and accuracy.

</details>

### 08-003. What does the orchestrator handle between agents?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Sequencing of tasks, handoffs, retries on failure and keeping agents on track.

</details>

### 08-004. What does the orchestrator do when it lacks information?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

It can seek additional context, including by asking the user, before continuing.

</details>

### 08-005. What is a use case in an agentic workflow?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

The record, in sn_aia_usecase, that defines the workflow's objective and its team of agents.

</details>

### 08-006. Describe a simple multi-agent workflow.

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A password reset flow where one agent verifies the user, another finds the account, another resets the password, and a fourth notifies the user.

</details>

### 08-007. What are the tradeoffs of one agent versus several?

**Level:** Advanced

<details>
<summary>Show answer</summary>

One agent is simpler and cheaper. Several specialized agents are easier to tune and reuse but add coordination overhead.

</details>

### 08-008. How do you split a workflow into agents?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Give each agent a single responsibility, with its own tools and instructions, and keep handoffs explicit.

</details>

### 08-009. What is a handoff?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

The transfer of work and context from one agent to another through the orchestrator.

</details>

### 08-010. How can you monitor workflows across the enterprise?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Use the AI Agent Orchestrator and AI Control Tower to track progress and agent behavior.

</details>

### 08-011. What happens when an agent cannot continue?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

It can fall back, and an interactive agent can ask the user for information and re-trigger the flow.

</details>

### 08-012. How do you avoid circular handoffs?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Define clear responsibilities and stop conditions, and test workflows with cases designed to loop.

</details>

### 08-013. How do you evaluate a multi-agent workflow?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Build test cases with expected outcomes, run them repeatedly, use evaluation tooling, and review traces for poor decisions.

</details>

### 08-014. Why should tools be idempotent?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Retries or repeated steps should not create duplicate records or repeat harmful actions.

</details>

### 08-015. When do parallel or sequential steps make sense?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Sequential when each step depends on the last. Parallel when tasks are independent and speed matters.

</details>

### 08-016. What are agentic workflow templates?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Prebuilt workflows in AI Agent Studio that you can activate and adjust for triggers and display settings.

</details>

### 08-017. What drives latency and cost in multi-agent flows?

**Level:** Advanced

<details>
<summary>Show answer</summary>

The number of LLM calls, tool calls and retries. Fewer, clearer steps reduce both.

</details>

### 08-018. Why is runtime observability needed for agents?

**Level:** Advanced

<details>
<summary>Show answer</summary>

It shows how agents reason and decide so teams can correct course. ServiceNow added this through the Traceloop acquisition.

</details>

### 08-019. What does mining agentic AI logs mean?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Analyzing agent activity logs, including with process mining capabilities, to find patterns and improvement opportunities.

</details>

### 08-020. What is AI Agent Fabric?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A capability that connects agents across systems, and supports MCP to link ServiceNow agents with external tools and resources.

</details>

### 08-021. What is Action Fabric?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

A mechanism that opens ServiceNow's workflow engine to external AI agents, with actions governed through AI Control Tower.

</details>

### 08-022. What does governance of Action Fabric include?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Identity verification, permission scoping and a full audit trail for actions that external agents perform.

</details>

### 08-023. Is the MCP server available to customers?

**Level:** Intermediate

<details>
<summary>Show answer</summary>

Reports from May 2026 say an MCP server is included in every Now Assist and AI Native SKU. Verify against your own entitlements.

</details>

### 08-024. How would you govern external agents that call ServiceNow?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Require verified identities, scope permissions narrowly, route actions through Control Tower, and keep audit trails and approvals for sensitive actions.

</details>

### 08-025. How do you test an orchestrated flow end to end?

**Level:** Advanced

<details>
<summary>Show answer</summary>

Create realistic scenarios, run them in a non-production instance, check outcomes and traces at every handoff, and include failure cases.

</details>


[Back to index](../README.md)
