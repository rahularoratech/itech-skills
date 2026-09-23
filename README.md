<div align="center">
  <a href="https://github.com/rahularoratech/itech-skills">
    <img src="./docs/assets/itech-logo.png" alt="itech-skills logo" width="132">
  </a>

  <h1>itech-skills</h1>

  <p><strong>Practical, composable agent skills for engineering and everyday work.</strong></p>
  <p>Help your agent clarify the work, plan a path, build in small steps, and review the result.</p>

  <p>
    <a href="https://rahularoratech.github.io/itech-skills/">Documentation</a> ·
    <a href="./docs/commands.md">Command reference</a> ·
    <a href="./LICENSE">MIT license</a>
  </p>

  <p>
    <a href="https://github.com/rahularoratech/itech-skills/actions/workflows/docs.yml"><img src="https://github.com/rahularoratech/itech-skills/actions/workflows/docs.yml/badge.svg" alt="Documentation build"></a>
    <a href="./LICENSE"><img src="https://img.shields.io/github/license/rahularoratech/itech-skills" alt="MIT license"></a>
  </p>
</div>

## Get started

Choose one installation route. Installing through both can create duplicate copies of the skills.

### Claude Code

Add the itech-skills marketplace and install its plugin:

```sh
claude plugin marketplace add rahularoratech/itech-skills
claude plugin install itech-skills@itech-skills
```

Or run the same commands from a Claude Code session:

```text
/plugin marketplace add rahularoratech/itech-skills
/plugin install itech-skills@itech-skills
```

### Codex and other agents

Use the skills CLI to copy selected skills into your project:

```sh
npx skills@latest add rahularoratech/itech-skills
```

Choose the skills and agent harnesses to install. Include `setup-itech-skills` if you plan to use the engineering workflows.

### Set up a repository

Run the setup skill once in each repository where you will use the engineering workflows:

- Claude Code plugin: `/itech-skills:setup-itech-skills`
- Skills CLI: `/setup-itech-skills`

It configures the issue tracker, triage labels, and documentation locations used by the engineering skills.

## Choose a starting point

| If you want to... | Start with |
| --- | --- |
| Find the right skill or workflow | [`ask-itech-skills`](./skills/engineering/ask-itech-skills/SKILL.md) |
| Shape an idea and record project decisions | [`grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) |
| Turn a conversation into a plan for delivery | [`to-spec`](./skills/engineering/to-spec/SKILL.md), then [`to-tickets`](./skills/engineering/to-tickets/SKILL.md) |
| Implement a spec or ticket set | [`implement`](./skills/engineering/implement/SKILL.md) |
| Investigate a hard bug | [`diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md) |
| Explore a design question before committing to it | [`prototype`](./skills/engineering/prototype/SKILL.md) |
| Get interviewed about a non-code decision | [`grill-me`](./skills/productivity/grill-me/SKILL.md) |

## Common workflows

| Work | Suggested path |
| --- | --- |
| Shape and ship a small change | `grill-with-docs` → `implement` → `code-review` |
| Plan work across sessions | `grill-with-docs` → `to-spec` → `to-tickets` → `implement` → `code-review` |
| Investigate and fix a difficult bug | `diagnosing-bugs` → `implement` → `code-review` |
| Triage incoming work | `setup-itech-skills` → `triage` |
| Explore a large codebase improvement | `improve-codebase-architecture`, then `wayfinder` or `to-tickets` |

## Browse all 26 skills

User-invoked skills run when you select them. Model-invoked skills can also be selected automatically when the task fits. Claude Code plugin commands use the `/itech-skills:` prefix; skills installed with the CLI use the short command name. The [command reference](./docs/commands.md) lists every command and its full guide.

<details>
<summary><strong>Engineering</strong></summary>

### User-invoked

| Skill | Purpose |
| --- | --- |
| [`ask-itech-skills`](./skills/engineering/ask-itech-skills/SKILL.md) | Routes you to a skill or workflow. |
| [`grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) | Clarifies a project idea and records useful decisions in its docs. |
| [`triage`](./skills/engineering/triage/SKILL.md) | Moves incoming issues through a defined triage flow. |
| [`improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md) | Finds architecture improvements and helps explore a chosen one. |
| [`setup-itech-skills`](./skills/engineering/setup-itech-skills/SKILL.md) | Configures the tracker, triage labels, and documentation locations. |
| [`to-spec`](./skills/engineering/to-spec/SKILL.md) | Turns the current discussion into a spec. |
| [`to-tickets`](./skills/engineering/to-tickets/SKILL.md) | Splits a plan or spec into tickets with clear dependencies. |
| [`implement`](./skills/engineering/implement/SKILL.md) | Implements work from a spec or tickets, then reviews the result. |
| [`wayfinder`](./skills/engineering/wayfinder/SKILL.md) | Maps a large effort into decision tickets that can be resolved in sequence. |

### Model-invoked

| Skill | Purpose |
| --- | --- |
| [`prototype`](./skills/engineering/prototype/SKILL.md) | Builds a disposable prototype to answer a design question. |
| [`diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md) | Investigates hard bugs and performance regressions with a disciplined feedback loop. |
| [`research`](./skills/engineering/research/SKILL.md) | Researches a question against primary sources and saves cited findings. |
| [`tdd`](./skills/engineering/tdd/SKILL.md) | Builds or fixes behavior with a red-green-refactor loop. |
| [`domain-modeling`](./skills/engineering/domain-modeling/SKILL.md) | Sharpens project language and records durable decisions. |
| [`codebase-design`](./skills/engineering/codebase-design/SKILL.md) | Designs deep modules with useful behavior behind clear interfaces. |
| [`code-review`](./skills/engineering/code-review/SKILL.md) | Reviews changes against repository standards and the work's spec. |
| [`first-release-prep`](./skills/engineering/first-release-prep/SKILL.md) | Prepares an inherited or rebranded repository for its first release. |
| [`resolving-merge-conflicts`](./skills/engineering/resolving-merge-conflicts/SKILL.md) | Resolves an active merge or rebase conflict by tracing each change's intent. |
| [`wizard`](./skills/engineering/wizard/SKILL.md) | Creates an interactive guide for setup steps that need a human. |

</details>

<details>
<summary><strong>Productivity</strong></summary>

### User-invoked

| Skill | Purpose |
| --- | --- |
| [`grill-me`](./skills/productivity/grill-me/SKILL.md) | Interviews you until the branches of a plan or decision are resolved. |
| [`handoff`](./skills/productivity/handoff/SKILL.md) | Captures work in a portable handoff for another session or colleague. |
| [`teach`](./skills/productivity/teach/SKILL.md) | Teaches a concept over multiple sessions in a learning workspace. |
| [`to-questionnaire`](./skills/productivity/to-questionnaire/SKILL.md) | Creates a questionnaire for the person who has missing information. |
| [`wait-what`](./skills/productivity/wait-what/SKILL.md) | Re-explains a message using the project's vocabulary. |

### Model-invoked

| Skill | Purpose |
| --- | --- |
| [`grilling`](./skills/productivity/grilling/SKILL.md) | Provides the interview method used by several planning workflows. |
| [`writing-for-agents`](./skills/productivity/writing-for-agents/SKILL.md) | Guides writing skills, instructions, and other documents agents consume. |

</details>

## Documentation

The [documentation site](https://rahularoratech.github.io/itech-skills/) includes the [getting-started guide](./docs/getting-started.md), a [complete command reference](./docs/commands.md), and a guide for every skill.

## License

itech-skills is released under the [MIT License](./LICENSE).
