---
title: Mission
summary: Why we started Coastal Digital Research and what we're working on.
tags: [mission, values, vision]
---

## Mission

We build open-source infrastructure for AI agents. Tools, runtimes, protocols, the unglamorous stuff that runs underneath the model and decides whether the model can actually do anything useful.

That's where most of the interesting work is right now. Agents need to read files, run commands, cache results, remember things between sessions, and stay within their authorized scope. Each one of those is a real engineering problem with real consequences when it breaks, and most of them aren't going to be solved by training a bigger model. They get solved by people writing careful infrastructure code. We'd rather be those people than ship another model wrapper.

## Vision

Agents deployed with the same care we apply to databases. We should be able to see what an agent did, audit why it did it, and roll back when something breaks. That's table stakes for software that touches real money, real systems, and real decisions. Today most agent infrastructure is closer to a demo than a system. We want to close that gap.

## Values

**Open by default.** Code is public. Manifests are public. Agent behavior is inspectable. If you can't see how something works, you can't trust it, and trust matters more for agents than for almost any other class of software.

**Correctness over speed.** We'd rather ship one thing that works than five that mostly work. AI infrastructure that misbehaves isn't a bug, it's a governance failure. The blast radius for a misbehaving agent is bigger than people give it credit for.

**Human legibility.** Logs should read like English. APIs should explain themselves. A system that a person can't audit doesn't deserve to run unattended, no matter how impressive the model behind it.

**Minimal footprint.** Agents get the smallest set of permissions and tools that get the job done. Anything more is a future incident waiting to happen. The right question is never "what should this agent be able to do?" It's "what's the smallest thing this agent can do and still finish its task?"

## What We Don't Do

We don't train foundation models. We don't sell hosted inference. We work on the layer above, which is the runtime, the memory, and the protocols that let models actually do useful work without breaking things.

Agents aren't chatbots. They're infrastructure. We want to build them like infrastructure.
