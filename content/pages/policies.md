---
title: Policies
summary: Open source, data, and governance policies for Coastal Digital Research.
tags: [policy, governance, open-source, data]
---

## Open Source Policy

All Coastal Digital Research software is published under the Apache License 2.0 unless otherwise noted. We chose Apache 2.0 because it permits broad use, including commercial use, while requiring attribution and providing an explicit patent grant.

Contributors retain copyright on their contributions. By submitting a pull request, contributors agree that their work may be distributed under the project license.

We do not dual-license our software. We do not sell closed versions of our open-source tools.

## Data Policy

We do not collect user data on this site beyond standard server access logs. Logs are retained for 30 days and are not shared with third parties.

Agent manifest files contain only what is explicitly declared in YAML. No telemetry is embedded in agent manifests.

CDRcache stores content hashes and agent outputs. No personally identifiable information should be stored in CDRcache. Cache entries are content-addressed and immutable once written.

## Governance Policy

Coastal Digital Research is currently operated as a sole proprietorship. Decisions about project direction, releases, and governance are made by the maintainer.

We accept external contributions via pull request. Contributions that improve correctness, documentation, or test coverage are prioritized. We do not accept contributions that increase attack surface without a corresponding security review.

Security vulnerabilities should be reported via GitHub's private vulnerability reporting feature on the relevant repository. We aim to respond to security reports within 72 hours.

## Agent Behavior Policy

Agents operated by Coastal Digital Research:

- Act only on explicitly authorized tasks
- Log actions taken with sufficient detail to reconstruct what happened
- Do not store credentials or secrets in plaintext
- Do not initiate outbound connections to domains not specified in their manifest
- Respect rate limits and terms of service of external services they interact with

Agent manifests are public. If an agent is deployed by CDR, its capabilities, entrypoint, and runtime are listed in the registry at /agents.
