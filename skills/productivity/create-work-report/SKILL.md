---
name: create-work-report
description: Create a daily development update from user-provided work notes. Use when the user asks to draft, format, or revise a work report.
disable-model-invocation: true
---

# Create Work Report

Turn the user's notes into a clear daily development update. Return the report as Markdown in chat. Do not create a file, send the report, or inspect repository, Git, tracker, or pull request data unless the user asks.

## Evidence first

Use only facts the user supplies or asks you to verify. Keep task descriptions faithful to the work described. Never invent work, time, progress, status, project names, blockers, or PR and commit references.

Use a work date from the notes when present. Otherwise, use today's date in the user's local timezone and format it as `DD MMM YYYY`. Treat project names such as `Mind GTC` in examples as examples, not defaults.

Map the user's stated status to the matching marker:

- `On Track`: 🟢
- `At Risk`: 🟡
- `Blocked`: 🔴

Match these labels case-insensitively while preserving the user's wording. For a different status, keep the user's text and any marker they supplied, and do not invent a color. Ask for the status if none was provided. Do not infer status from task progress or blockers.

## Resolve gaps before drafting

Before writing the report, gather missing required details in one concise set of follow-up questions. Ask for:

- The project name, overall status, or completed-task details that are missing.
- The duration for each completed task, since those durations determine the total.
- The completion percentage for each in-progress task.
- Whether any section with no listed items should say `None`, including completed work, in-progress work, planned work, and blockers.

PR and commit references are optional. Include them when supplied, label a PR as `PR: #452` and a commit hash as `Commit: abc123`, and omit the reference line when there is no reference. Never label a PR number as a commit ID.

Calculate `Total Hours` from completed tasks only. Exclude in-progress and planned work. If the user also supplies a total and it differs from the calculation, show the arithmetic and ask which value or task duration needs correction before producing the final report.

## Report format

Keep these sections in this order. Use `- None` for an empty section only after the user confirms that it is empty. Keep each task concise and preserve its outcome, duration, progress, and supplied reference.

```markdown
Daily Development Update – {Project} – {DD MMM YYYY}

{Status marker} Status: {Status}

**Tasks Completed Today:**

- {Completed task}. [{hours} hrs]
  - PR: #{number}

Total Hours [{sum of completed task hours} Hours]

**Tasks In Progress:**

- {In-progress task}. [{percent}% Complete]
  - Commit: {short hash}

**Tasks Planned:**

- {Planned task}

**Blockers:**

- {Blocker}
```

Include only reference sub-bullets the user supplied. When the user confirms a section has no items, use `- None`. Do not add explanatory prose around the report unless a mismatch or unresolved detail needs attention.
