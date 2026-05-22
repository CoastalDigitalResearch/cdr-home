---
title: Policies
summary: Open source, data, and governance policies.
tags: [policy, governance, open-source, data]
---

## Open Source Policy

All CDR software is Apache License 2.0 unless explicitly noted. The license allows commercial use, requires attribution, and includes a patent grant. We chose it for all three reasons. The patent grant is the part most people overlook, and it's the part that matters most as soon as anything you build starts touching real customers.

Contributors keep copyright on what they wrote. Opening a pull request means you're agreeing your work can be distributed under the project's license. We don't ask for CLAs.

We don't dual-license. We don't sell closed versions of the open-source tools. If you see a CDR repository, what's there is what we build with too.

## Data Policy

This site doesn't collect user data beyond standard server access logs. Logs are kept for 30 days. They're not shared with third parties.

Agent manifests contain only what's declared in the YAML. No telemetry is embedded.

CDRcache stores content hashes and agent outputs. No PII should ever go in there, and we treat that as a hard rule, not a guideline. Cache entries are content-addressed and immutable once written, so a leak would be permanent. Better to not let it happen in the first place.

## Governance Policy

Decisions on project direction, releases, and governance are made by the CDR maintainers. We're small enough that this is a sentence, not a chart.

External contributions via pull request are welcome. Correctness, documentation, and test coverage improvements get prioritized. Anything that increases attack surface needs a security review before we'll merge it, even if the code itself looks fine.

Security issues should go through GitHub's private vulnerability reporting on the affected repo. We aim to respond inside 72 hours. We'll write up disclosed issues publicly once they're fixed; we don't sit on them.

## Agent Behavior Policy

Agents we operate:

- Act only on tasks they were explicitly authorized to do
- Log enough detail to reconstruct what happened
- Don't store credentials or secrets in plaintext
- Don't reach out to domains that aren't in their manifest
- Respect rate limits and terms of service for any external service they touch

Manifests are public. If CDR is running an agent, its capabilities, entrypoint, and runtime show up in the registry at /agents. If an agent isn't listed there, we aren't running it.
