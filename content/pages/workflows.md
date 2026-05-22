---
title: Workflows
summary: How Coastal Digital Research operates day to day.
tags: [workflows, operations, process]
---

## How CDR Works

Coastal Digital Research operates as a small, asynchronous organization. Most work happens through code, documentation, and structured agent tasks rather than meetings or synchronous communication.

## Development Workflow

**Trunk-based development.** All repositories use a single main branch. Features are developed in short-lived branches and merged via pull request after review. Long-running feature branches are avoided.

**Commit hygiene.** Every commit should represent a coherent unit of change with a message that explains why the change was made. Commits that fix typos, apply formatting, or change whitespace are squashed before merge.

**Testing before shipping.** Nothing merges without passing automated tests. For infrastructure components, tests include integration tests against realistic environments, not only unit tests.

**Agent-assisted development.** CDR uses its own agents for development tasks where appropriate. mae handles file operations, code searches, and structured edits. CDRbrowser is used for web research tasks. CDRcache is used to store and retrieve intermediate results in multi-step pipelines.

## Release Workflow

Projects follow semantic versioning. A release is cut when:

1. All tests pass on the main branch.
2. The changelog is up to date.
3. The container image builds cleanly.
4. The agent manifest (if applicable) has been updated to reflect the new version.

Releases are tagged in git and published as container images where appropriate.

## Incident Workflow

If an agent misbehaves or a service goes down:

1. Identify the scope: what was affected, for how long, and what data or operations are at risk.
2. Contain: disable the agent, roll back to the last known good state.
3. Review logs to reconstruct what happened.
4. Write a brief incident report in the repository's incident log.
5. Fix the root cause before re-enabling the affected system.

## Communication

External communication happens via GitHub issues and discussions on the relevant repository. There is no Slack, Discord, or mailing list. If you need to reach CDR about a project, open an issue.
