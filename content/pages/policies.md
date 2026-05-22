---
title: Policies
summary: Open source, data, and governance policies.
tags: [policy, governance, open-source, data]
---

## Open Source Policy

All CDR software is Apache License 2.0 unless explicitly noted. I picked Apache 2.0 because it's permissive (commercial use is fine), requires attribution, and includes an explicit patent grant.

Contributors keep copyright on what they wrote. Opening a pull request means you're agreeing your work can be distributed under the project's license.

I don't dual-license. I don't sell closed versions of the open-source tools.

## Data Policy

This site doesn't collect user data beyond standard server access logs. Logs are kept for 30 days. They're not shared with third parties.

Agent manifests contain only what's declared in the YAML. No telemetry is embedded.

CDRcache stores content hashes and agent outputs. No PII should ever go in there. Cache entries are content-addressed and immutable once written.

## Governance Policy

CDR is currently a sole proprietorship. I make the call on project direction, releases, and governance.

External contributions via pull request are welcome. Correctness, documentation, and test coverage improvements get prioritized. Anything that increases attack surface needs a security review before I'll merge it.

Security issues should go through GitHub's private vulnerability reporting on the affected repo. I aim to respond inside 72 hours.

## Agent Behavior Policy

Agents I operate:

- Act only on tasks they were explicitly authorized to do
- Log enough detail to reconstruct what happened
- Don't store credentials or secrets in plaintext
- Don't reach out to domains that aren't in their manifest
- Respect rate limits and terms of service for any external service they touch

Manifests are public. If CDR is running an agent, its capabilities, entrypoint, and runtime show up in the registry at /agents.
