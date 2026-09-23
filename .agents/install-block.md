# The canonical install block

`README.md` is the user-facing source for install instructions. Keep these commands and claims aligned with it.

## Claude Code: the plugin

This repository includes its own marketplace manifest. Add the GitHub repository as a marketplace and install the plugin:

```bash
claude plugin marketplace add rahularoratech/itech-skills
claude plugin install itech-skills@itech-skills
```

Or, from inside a Claude Code session:

```
/plugin marketplace add rahularoratech/itech-skills
/plugin install itech-skills@itech-skills
```

To refresh the marketplace catalog after a release, run `/plugin marketplace update`.

## Codex and other agents: skills.sh

The Claude Code plugin is Claude Code only. Everywhere else, [skills.sh](https://skills.sh/docs) copies editable skill files into the project. Use the whole-set form in `README.md`:

```bash
npx skills@latest add rahularoratech/itech-skills
```

The installer lets people choose which skills and coding agents to install. Include `setup-itech-skills` when using the engineering skills that depend on per-repo configuration.

For one skill:

```bash
npx skills@latest add rahularoratech/itech-skills --skill=<name>
npx skills@latest update <name>
```

## The two routes are exclusive

The plugin is a managed bundle. skills.sh writes files people own and edit. Installing both leaves the same skills installed twice, so choose one route.

## Marketplace metadata

`.claude-plugin/marketplace.json` declares this repository's marketplace and plugin. The marketplace name and plugin name are both `itech-skills`.
