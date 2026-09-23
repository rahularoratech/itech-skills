# Command reference

The command column shows the direct invocation form for each skill. In Claude Code, the exact command depends on how you installed the skills:

- **Claude Code plugin:** add the plugin namespace, for example `/itech-skills:grill-with-docs`.
- **Claude Code via the skills CLI:** type the command shown, for example `/grill-with-docs`.
- **Other agents:** select or invoke the skill by its name using that agent's skill interface.

User-invoked skills run when you select them. Model-invoked skills can also be selected automatically when a task fits.

## Engineering commands

### User-invoked

| Command name | What it does | Guide |
| --- | --- | --- |
| [/ask-itech-skills](engineering/ask-itech-skills.md) | Routes you to a skill or workflow. | [Guide](engineering/ask-itech-skills.md) |
| [/grill-with-docs](engineering/grill-with-docs.md) | Sharpens an idea in a repository and records useful decisions in its docs. | [Guide](engineering/grill-with-docs.md) |
| [/triage](engineering/triage.md) | Moves incoming issues and requests through triage. | [Guide](engineering/triage.md) |
| [/improve-codebase-architecture](engineering/improve-codebase-architecture.md) | Finds architecture improvements and helps work through a chosen one. | [Guide](engineering/improve-codebase-architecture.md) |
| [/setup-itech-skills](engineering/setup-itech-skills.md) | Configures tracker, triage labels, and documentation locations for these workflows. | [Guide](engineering/setup-itech-skills.md) |
| [/to-spec](engineering/to-spec.md) | Turns the current discussion into a spec. | [Guide](engineering/to-spec.md) |
| [/to-tickets](engineering/to-tickets.md) | Splits a plan or spec into tickets and records their blocking relationships. | [Guide](engineering/to-tickets.md) |
| [/implement](engineering/implement.md) | Implements work from a spec or tickets, then reviews the result. | [Guide](engineering/implement.md) |
| [/wayfinder](engineering/wayfinder.md) | Maps decisions for a large effort that cannot be planned in one session. | [Guide](engineering/wayfinder.md) |

### Model-invoked

| Command | What it does | Guide |
| --- | --- | --- |
| [/prototype](engineering/prototype.md) | Builds a disposable prototype to answer a design question. | [Guide](engineering/prototype.md) |
| [/diagnosing-bugs](engineering/diagnosing-bugs.md) | Investigates hard bugs and performance regressions with a tight feedback loop. | [Guide](engineering/diagnosing-bugs.md) |
| [/research](engineering/research.md) | Researches a question against primary sources and writes cited findings. | [Guide](engineering/research.md) |
| [/tdd](engineering/tdd.md) | Builds or fixes behavior test-first, one slice at a time. | [Guide](engineering/tdd.md) |
| [/domain-modeling](engineering/domain-modeling.md) | Sharpens a project's domain language and records durable decisions. | [Guide](engineering/domain-modeling.md) |
| [/codebase-design](engineering/codebase-design.md) | Helps design deep modules with clear interfaces and seams. | [Guide](engineering/codebase-design.md) |
| [/code-review](engineering/code-review.md) | Reviews changes against repository standards and the work's spec. | [Guide](engineering/code-review.md) |
| [/first-release-prep](engineering/first-release-prep.md) | Prepares an inherited or rebranded repository for its first release. | [Guide](engineering/first-release-prep.md) |
| [/resolving-merge-conflicts](engineering/resolving-merge-conflicts.md) | Resolves an active merge or rebase conflict by tracing each hunk's intent. | [Guide](engineering/resolving-merge-conflicts.md) |
| [/wizard](engineering/wizard.md) | Guides human-only setup steps such as credentials and service configuration. | [Guide](engineering/wizard.md) |

## Productivity commands

### User-invoked

| Command | What it does | Guide |
| --- | --- | --- |
| [/create-work-report](productivity/create-work-report.md) | Turns supplied notes into a daily development update and checks completed-task hours. | [Guide](productivity/create-work-report.md) |
| [/grill-me](productivity/grill-me.md) | Interviews you to resolve a plan or decision without writing project docs. | [Guide](productivity/grill-me.md) |
| [/handoff](productivity/handoff.md) | Writes a portable handoff for another session, harness, or colleague. | [Guide](productivity/handoff.md) |
| [/teach](productivity/teach.md) | Teaches a concept over multiple sessions in a learning workspace. | [Guide](productivity/teach.md) |
| [/to-questionnaire](productivity/to-questionnaire.md) | Creates a questionnaire for the person who has missing information. | [Guide](productivity/to-questionnaire.md) |
| [/wait-what](productivity/wait-what.md) | Re-explains a message that did not land, using the project's vocabulary. | [Guide](productivity/wait-what.md) |

### Model-invoked

| Command | What it does | Guide |
| --- | --- | --- |
| [/grilling](productivity/grilling.md) | Provides the interview method used by several planning workflows. | [Guide](productivity/grilling.md) |
| [/writing-for-agents](productivity/writing-for-agents.md) | Guides writing skills, instructions, and docs that agents consume. | [Guide](productivity/writing-for-agents.md) |

## Common workflows

| Goal | Suggested route |
| --- | --- |
| Share a daily development update | /create-work-report |
| Shape and ship a small idea | /grill-with-docs, then /implement |
| Plan work across sessions | /grill-with-docs, /to-spec, /to-tickets, /implement, then /code-review |
| Investigate a difficult bug | /diagnosing-bugs, then /implement and /code-review when a fix is clear |
| Explore an unanswered design question | /handoff, /prototype, then /handoff back to the original work |
| Prepare an inherited project's first release | /first-release-prep |

Run /setup-itech-skills once before workflows that rely on an issue tracker or repository documentation conventions.
