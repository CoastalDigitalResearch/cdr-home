---
title: Mission
summary: Why we started Coastal Digital Research and what we're working on.
tags: [mission, values, vision]
---

## Mission

We build open-source infrastructure for AI agents. Tools, runtimes, protocols. The stuff that runs underneath the model.

This is where most of the interesting work is right now. Agents need to read files, run commands, cache results, remember things between sessions, and stay within scope. Each one is an engineering problem with consequences when it goes wrong. We'd rather get those right than ship another model wrapper.

## Vision

Agents deployed with the same care we apply to databases. We should be able to audit what they did and roll back when something breaks. Most agent infrastructure today is closer to a demo than a system. We want to fix that.

## Values

**Open by default.** Code is public. Manifests are public. Agent behavior is inspectable. If you can't see how something works, you can't trust it.

**Correctness over speed.** We'd rather ship one thing that works than five that mostly work. AI infrastructure that misbehaves isn't a bug. It's a governance failure.

**Human legibility.** Logs should read like English. APIs should explain themselves. A system a person can't audit doesn't deserve to run unattended.

**Minimal footprint.** Agents get the smallest set of permissions and tools that get the job done. Anything more is a future incident waiting.

## What We Don't Do

We don't train foundation models. We don't sell hosted inference. We work on the layer above. The runtime and the protocols that let models do useful work without breaking things.
