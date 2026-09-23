# Getting started

Choose one installation route. Installing through both routes can create duplicate copies of the same skills.

## Claude Code

Add the itech-skills marketplace and install the plugin:

    claude plugin marketplace add rahularoratech/itech-skills
    claude plugin install itech-skills@itech-skills

You can also run those commands in a Claude Code session:

    /plugin marketplace add rahularoratech/itech-skills
    /plugin install itech-skills@itech-skills

## Codex and other agents

Install selected skills into your project with the skills CLI:

    npx skills@latest add rahularoratech/itech-skills

Choose the skills and agent harnesses you want. Include setup-itech-skills if you plan to use the engineering workflows.

## Configure a repository

After installation, run /setup-itech-skills once in each repository where you will use the engineering workflows. It configures the issue tracker, triage labels, and documentation locations used by those skills.

## Invoke a skill

In Claude Code, plugin commands include the plugin namespace, for example `/itech-skills:grill-with-docs` or `/itech-skills:code-review`. Skills installed as files with the skills CLI use the unqualified form, such as `/grill-with-docs`. [Claude Code plugin skills use namespaced commands](https://code.claude.com/docs/en/plugins).

Other agents expose installed skills through their own skill interface. User-invoked skills require you to select them; model-invoked skills can also be selected automatically when a task fits.

See the [complete command reference](commands.md) for all available skills.
