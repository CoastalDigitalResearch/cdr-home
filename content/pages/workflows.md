---
title: Workflows
summary: How CDR actually runs.
tags: [workflows, operations, process]
---

## How CDR Works

Small, asynchronous, mostly code-based. Almost no meetings. Communication happens in repos and in the agent task logs.

## Development Workflow

**Trunk-based.** One main branch per repo. Short-lived feature branches. No long-lived branches.

**Commit hygiene.** Each commit should be one coherent change with a message that says why. Typos and formatting get squashed before merge.

**Tests before ship.** Nothing merges without tests passing. Infrastructure pieces get integration tests against realistic environments, not just unit tests.

**Agents in the loop.** We use our own agents for the work we can hand off. mae does file edits and code searches. CDRbrowser handles web research. CDRcache memoizes intermediate steps in long pipelines.

## Release Workflow

Semantic versioning. We cut a release when:

1. Tests pass on main.
2. The changelog is current.
3. The container image builds cleanly.
4. The agent manifest, if there is one, reflects the new version.

Releases are tagged in git and published as container images where it makes sense.

## Incident Workflow

When an agent misbehaves or a service goes down:

1. Figure out the blast radius. What was affected, for how long, what's at risk.
2. Contain it. Disable the agent. Roll back to the last known good state.
3. Read the logs and reconstruct what happened.
4. Write a short incident note in the repo's incident log.
5. Fix the root cause before turning anything back on.

## Communication

GitHub issues and discussions on the relevant repo. No Slack, no Discord, no mailing list. If you need to reach us about a project, open an issue.
