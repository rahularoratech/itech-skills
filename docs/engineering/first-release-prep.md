## What it does

**first-release-prep** prepares an inherited or rebranded repository for its first release under a new identity. It distinguishes a fresh release from a migration, because the right version and history depend on whether existing users need to move with the project.

An old name alone is not a reason to delete a file. Release notes, project documentation, and legal attribution need separate decisions.

## When to reach for it

Type /first-release-prep, or the agent reaches for it automatically when a renamed or inherited repository is being prepared for its first public release.

Reach for it to review project identity, starting versions, changelogs, and pending changesets. For routine version bumps, use the repository's documented release procedure.

## Prerequisites

Open the repository being prepared. The skill reads its release configuration and edits its local files; registry checks are only needed when the starting version depends on package availability.

## Common questions

**Does it always reset the version to 1.0.0?**

No. It checks the release target and its registry state, then distinguishes a new product identity from a migration of an existing release line.

**Does preparing a release publish or tag anything?**

No. The skill prepares local project files and reports the checks. Publishing, pushing, and tagging require a separate explicit request.

**Can I remove every reference to the previous project?**

The identity scan finds those references, then classifies them. License terms, required copyright notices, third-party credits, and other provenance may need to remain.

## It's working if

- The project has one clear release identity across its manifests, links, and install instructions.
- The first changelog and pending changesets describe this project's release history.
- Version values agree across files that share a release target.
- Required license and attribution notices remain intact.
- No release was published, pushed, or tagged during preparation.

## Where it fits

**first-release-prep** is a run-once release preparation skill. It covers project identity and release history; [setup-itech-skills](https://github.com/rahularoratech/itech-skills/blob/main/docs/engineering/setup-itech-skills.md) configures the engineering skill workflow inside a repository.

For the wider skill map, see [ask-itech-skills](https://github.com/rahularoratech/itech-skills/blob/main/docs/engineering/ask-itech-skills.md).
