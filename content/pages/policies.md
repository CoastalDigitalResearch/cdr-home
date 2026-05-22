---
title: Policies
summary: Open source, data, and governance policies.
tags: [policy, governance, open-source, data]
---

## Open Source Policy

All CDR software is Apache License 2.0 unless explicitly noted. The license allows commercial use, requires attribution, and includes a patent grant. We chose it for all three.

Contributors keep copyright on what they wrote. Opening a pull request means you're agreeing your work can be distributed under the project's license.

We don't dual-license. We don't sell closed versions of the open-source tools.

## Data Policy

This site doesn't collect user data beyond standard server access logs. Logs are kept for 30 days. They're not shared with third parties.

Agent manifests contain only what's declared in the YAML. No telemetry is embedded.

CDRcache stores content hashes and agent outputs. No PII should ever go in there. Cache entries are content-addressed and immutable once written.

## Governance Policy

Decisions on project direction, releases, and governance are made by the CDR maintainers.

External contributions via pull request are welcome. Correctness, documentation, and test coverage improvements get prioritized. Anything that increases attack surface needs a security review before we'll merge it.

Security issues should go through GitHub's private vulnerability reporting on the affected repo. We aim to respond inside 72 hours.

## Agent Behavior Policy

Agents we operate:

- Act only on tasks they were explicitly authorized to do
- Log enough detail to reconstruct what happened
- Don't store credentials or secrets in plaintext
- Don't reach out to domains that aren't in their manifest
- Respect rate limits and terms of service for any external service they touch

Manifests are public. If CDR is running an agent, its capabilities, entrypoint, and runtime show up in the registry at /agents.
