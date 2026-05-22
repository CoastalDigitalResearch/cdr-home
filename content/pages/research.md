---
title: Research
summary: Research focus areas at Coastal Digital Research.
tags: [research, AI, infrastructure, agents]
---

## Research Focus

Coastal Digital Research works at the intersection of AI systems and software infrastructure. Our research is applied: we study problems we encounter building and operating AI agents, and we publish what we learn.

## Agent Runtime Design

How should AI agents be structured as software components? We study the tradeoffs between stateless agents (easier to reason about, easier to scale) and stateful agents (more capable for long-running tasks, harder to audit). Our agent manifests capture the key dimensions: entrypoint, runtime, tools, inputs, outputs, and SLOs.

We are particularly interested in how agents should handle failure — when to retry, when to escalate, when to halt and wait for human review.

## Content-Addressed Agent Memory

CDRcache explores using content-addressed storage for agent outputs. If an agent's output is a deterministic function of its inputs, that output can be cached and reused. This reduces compute cost and creates a stable audit trail: you can inspect exactly what an agent produced given a specific input at a specific time.

Open questions: how do you handle agents that are not fully deterministic? How do you invalidate cache entries when the underlying model or tool changes?

## Dual-Mode Web Infrastructure

Most web infrastructure is designed for human browsers. As AI agents increasingly browse the web programmatically, there is a mismatch: HTML is rich with navigation chrome, ads, and layout that agents do not need; JSON is clean for machines but unusable by humans without tooling.

We are exploring patterns for dual-mode endpoints — the same content served as HTML for humans and as JSON or Markdown for agents. This site is an early implementation. The /.well-known/agent.json convention is one approach to agent discovery.

## Minimal Agent Footprint

What is the smallest set of capabilities an agent needs to accomplish a given task? We study how to scope agent permissions tightly, how to detect when agents are operating outside their intended scope, and how to design agent interfaces that make over-privileged operation difficult by default.

## Observability for AI Systems

Standard observability tooling (logs, metrics, traces) was designed for deterministic software. AI agents introduce non-determinism, long context windows, and emergent behavior that does not fit neatly into these models.

We are studying how to adapt observability practices for AI systems: what should be logged, at what granularity, and how to structure that data for both human review and automated analysis.
