---
name: first-release-prep
description: Prepare an inherited or rebranded repository for its first public release under a new identity. Use for launch version, changelog, changeset, or identity audits, not routine releases.
---

# First Release Prep

Prepare an inherited or rebranded repository for its first independent release without confusing a fresh launch with a migration of an existing product.

## Classify the release

Inspect the repository instructions, release manifests, configured registries, and available tags. Classify each release target independently, since a package and a plugin can have different histories:

- **First release under a distinct identity**: no existing users or release line need to migrate.
- **Migration under a new identity**: an existing product and its users continue under a new name or owner.
- **Routine release**: the product identity and release line already exist.

If resetting the version or removing history depends on which case applies, ask one focused question before changing those records. An empty changelog alone does not prove the project has never shipped.

When the starting version depends on whether a package name is already published, check the target registry using an authoritative source. If registry status cannot be confirmed, report that uncertainty and leave the version decision open.

## Audit identity and provenance

Search the current working tree for previous project names, owners, domains, package identifiers, plugin identifiers, install commands, badges, and file paths. Include hidden project configuration and filenames. Exclude Git internals, dependencies, and generated output from the ordinary identity scan, and inspect release history separately.

Inspect package manifests and lockfiles, plugin and marketplace manifests, repository links, CI configuration, documentation, skill frontmatter, release scripts, changelogs, and pending changesets. Find each source of truth before editing so mirrored values stay aligned.

Classify old-name references before changing them. Preserve license terms, copyright notices, third-party attribution, credits, and notices required for vendored or derived work. Do not replace an attribution with the new brand unless the project owner has established that the rights allow it. Keep Git history intact during ordinary rebrands; handle history rewriting as a separately scoped task with an explicit request.

## Reset or migrate

For a first release under a distinct identity:

- Choose a starting version for each release target after checking registry state and the project's stability policy. A new identity may start at 1.0.0, but an inherited version is not evidence that 1.0.0 is available or required.
- Remove pending changesets only when they describe changes already released by the source project or otherwise do not belong to this project's first release. Keep changesets for current, unreleased work when they are intended for the upcoming release.
- Clear imported changelog entries only when the release history belongs to the source project and the user wants a clean history for this product. Keep the changelog file and its configured release process intact.
- Avoid a rebrand-only major changeset when no prior release under this identity exists. Keep a major migration note when existing users are moving across a breaking release line.

For a migration of an existing product, keep its version line and release history, then add a migration note that explains the identity change and any compatibility impact. For a routine release, use the repository's documented release procedure without resetting history.

Present a concise file-level plan when the cleanup touches release history or legal provenance. Apply the user's stated choices and leave unresolved choices visible rather than guessing.

## Verify the release state

Use the repository's documented validators and version-sync commands. Check that:

- edited manifests parse and all version sources agree where the repository expects them to;
- repository URLs, install instructions, plugin paths, and documentation links point to the intended project;
- the old identity is gone from active project surfaces, with preserved attribution identified explicitly;
- the changelog and pending changesets match the chosen fresh-release or migration path;
- no publish, push, or tag was created unless the user explicitly requested that external action.

Report the release mode, the files changed, the checks run, and any registry or attribution decision that remains unresolved.
