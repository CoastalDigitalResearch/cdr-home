---
title: Research
summary: What we're thinking about and writing about.
tags: [research, AI, infrastructure, agents]
---

## Research Focus

The work here is applied. We study the problems we hit while building and running agents, then we write up what we learn. Less paper-style research, more field notes.

## Agent Runtime Design

What's the right shape for an agent as a software component? Stateless agents are easier to reason about and easier to scale. Stateful agents do more interesting work but are harder to audit. The agent manifests on this site capture the dimensions we care about: entrypoint, runtime, tools, inputs, outputs, SLOs.

The piece we keep coming back to is failure handling. When does an agent retry, when does it escalate, when does it stop and wait for a human?

## Content-Addressed Agent Memory

CDRcache is the experiment here. If an agent's output is a deterministic function of its inputs, that output can be hashed and stored. You skip the rerun next time, and you get an audit trail for free.

Open questions: what to do about agents that aren't fully deterministic, and how to invalidate cache entries when the underlying model or tool moves.

## Dual-Mode Web Infrastructure

Most websites are designed for humans. Agents browsing those sites have to parse around navigation, ads, and layout to get to the content. The fix is to serve the same content twice in different shapes: HTML for people, JSON or Markdown for machines.

This site is the implementation we keep iterating on. The `/.well-known/agent.json` convention is one half of the story. Content negotiation is the other.

## Minimal Agent Footprint

What's the smallest set of capabilities an agent needs to do its job? We're interested in how to scope agent permissions tightly, how to spot when an agent is operating outside its scope, and how to design interfaces that make over-privileged behavior hard by default.

## Observability for AI Systems

Logs, metrics, and traces were built for deterministic software. Agents are not deterministic. Context windows are large. Behavior is emergent. The usual tooling doesn't quite fit.

We're working through what to log, at what granularity, and how to structure it so both a person reviewing an incident and another agent doing analysis can use it.
