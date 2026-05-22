---
title: Workflows
summary: How CDR actually runs.
tags: [workflows, operations, process]
---

## How CDR Works

Small and asynchronous. Most work happens in code and in agent task logs, not in meetings. The whole point of building agent infrastructure is that you should be able to coordinate work without sitting on calls all day, so we try to live that as much as we can.

## Development Workflow

**Trunk-based.** One main branch per repo. Short-lived feature branches. No long-lived branches sitting around collecting conflicts.

**Commit hygiene.** Each commit should be one coherent change with a message that says why. Typos and formatting get squashed before merge. The git history is the audit trail, so it has to actually be readable.

**Tests before ship.** Nothing merges without tests passing. Infrastructure pieces get integration tests against realistic environments, not just unit tests. Mocked tests catch the easy cases but miss the bugs that actually take production down.

**Agents in the loop.** We use our own agents for the work we can hand off. mae does file edits and code searches. CDRbrowser handles web research. CDRcache memoizes intermediate steps in long pipelines. If we're not eating our own dog food, we don't really understand what we're building.

## Release Workflow

Semantic versioning. We cut a release when:

1. Tests pass on main.
2. The changelog is current.
3. The container image builds cleanly.
4. The agent manifest, if there is one, reflects the new version.

Releases are tagged in git and published as container images where it makes sense. Nothing exotic.

## Incident Workflow

When an agent misbehaves or a service goes down:

1. Figure out the blast radius. What was affected, for how long, what's at risk.
2. Contain it. Disable the agent. Roll back to the last known good state.
3. Read the logs and reconstruct what happened.
4. Write a short incident note in the repo's incident log.
5. Fix the root cause before turning anything back on.

The order matters. Containment before forensics. Forensics before fix. Fix before restart. Most agent incidents we've seen got worse because someone skipped a step.

## Communication

GitHub issues and discussions on the relevant repo. No Slack, no Discord, no mailing list. If you need to reach us about a project, open an issue. We respond faster to a clearly written issue than to a chat ping, every time.
