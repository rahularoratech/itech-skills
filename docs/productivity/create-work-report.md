## What it does

`create-work-report` turns your notes into a daily development update with the project, date, status, completed work, current work, plans, blockers, and a total of completed-task hours. It does not search Git history or pull requests to fill gaps; report facts come from you unless you ask it to verify something.

## When to reach for it

You invoke this skill by typing `/create-work-report`; the agent will not start it on its own. Reach for it when you have work notes to turn into a daily update for a team or stakeholder. For context another person needs to continue the work, use [handoff](https://github.com/rahularoratech/itech-skills/blob/main/docs/productivity/handoff.md) instead.

## Evidence before polish

The report can improve wording, but it cannot improve the facts. Missing project, status, task hours, progress, planned work, or blocker details become concise follow-up questions. A PR number stays a PR reference, and a commit hash stays a commit reference.

`Total Hours` is the sum of completed-task durations only. Work in progress and planned work do not count. If that calculation disagrees with a supplied total, the mismatch is resolved before the final report is written.

## Common questions

**Will it find my tasks in Git or GitHub automatically?**

No. It uses the notes you provide. It checks repository or PR data only when you ask.

**What if I have no PR or commit for a task?**

References are optional. The report omits the reference line when you have not supplied one.

## It's working if

- The report keeps the supplied project name, status, task details, and date.
- `Total Hours` matches the completed-task durations, with in-progress and planned work excluded.
- Every included PR or commit reference has the correct label.
- Missing facts are asked for instead of guessed.

## Where it fits

`create-work-report` is a standalone productivity skill for communicating what happened today. It produces a status update; [handoff](https://github.com/rahularoratech/itech-skills/blob/main/docs/productivity/handoff.md) carries the context needed to continue work. The [ask-itech-skills router](https://github.com/rahularoratech/itech-skills/blob/main/docs/engineering/ask-itech-skills.md) maps it with the rest of the skill set.
