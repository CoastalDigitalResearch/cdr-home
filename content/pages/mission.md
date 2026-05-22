---
title: Mission
summary: Why I started Coastal Digital Research and what I'm working on.
tags: [mission, values, vision]
---

## Mission

I build open-source infrastructure for AI agents. Tools, runtimes, protocols. The stuff that runs underneath the model.

This is where most of the interesting work is right now. Agents need to read files, run commands, cache results, remember things between sessions, and stay within scope. Each of those is a real engineering problem with real consequences when it goes wrong. I'd rather get those right than ship another model wrapper.

## Vision

Agents deployed with the same care we apply to databases. Observed like production services. Governed like software that touches real money. Most agent infrastructure today is closer to a demo than a system. I want to fix that.

## Values

**Open by default.** Code is public. Manifests are public. Agent behavior is inspectable. If you can't see how something works, you can't trust it.

**Correctness over speed.** I'd rather ship one thing that works than five that mostly work. AI infrastructure that misbehaves isn't a bug. It's a governance failure.

**Human legibility.** Logs should read like English. APIs should explain themselves. A system a person can't audit doesn't deserve to run unattended.

**Minimal footprint.** Agents get the smallest set of permissions and tools that get the job done. Anything more is a future incident waiting.

## What I Don't Do

I don't train foundation models. I don't sell hosted inference. I work on the layer above. The runtime, the memory, the tooling, and the protocols that let models do useful work without breaking things.
