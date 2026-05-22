---
title: Research
summary: What we're thinking about and writing about.
tags: [research, AI, infrastructure, agents]
---

## Research Focus

The work here is applied. We study the problems we hit while building and running agents, then we write up what we learn. Less paper-style research, more field notes. The questions that interest us are the ones that come back every week, in different shapes, in different projects.

## Agent Runtime Design

What's the right shape for an agent as a software component? Stateless agents are easier to reason about and easier to scale. Stateful agents do more interesting work but are harder to audit. There's no universal answer, but the tradeoff shows up every time, and most projects pick badly on the first pass and pay for it later. The agent manifests on this site try to make the tradeoff explicit by declaring the fields that actually matter: entrypoint, runtime, tools, inputs, outputs, SLOs.

The piece we keep coming back to is failure handling. When does an agent retry? When does it escalate? When does it stop and wait for a human? Most agent frameworks don't take this seriously enough, which is wild given that "what to do when you're confused" is roughly the whole point of having an agent.

## Content-Addressed Agent Memory

CDRcache is the experiment here. If an agent's output is a deterministic function of its inputs, that output can be hashed and stored. You skip the rerun next time, and you get an audit trail for free. That's a pretty good deal if you can pull it off.

The open questions are the ones you'd expect. What about agents that aren't fully deterministic, which is most of them? How do you invalidate cache entries when the underlying model or tool changes? When is the audit trail more valuable than the cache hit, and when is it the other way around? We don't have clean answers yet. We have working code and a growing list of cases where caching helped and a smaller list of cases where it hurt.

## Dual-Mode Web Infrastructure

Most websites are designed for humans. Agents browsing those sites have to parse around navigation chrome, ads, and layout to get to the content. That's slow, expensive in tokens, and error-prone. The fix is to serve the same content twice, in different shapes: HTML for people, JSON or Markdown for machines, with content negotiation so each visitor gets what they actually want.

This site is the implementation we keep iterating on. The `/.well-known/agent.json` convention is one half of the story. Content negotiation is the other. Neither is novel by itself. The interesting part is making both work in one codebase without compromise to either side.

## Minimal Agent Footprint

What's the smallest set of capabilities an agent needs to do its job? Permissions should be tight enough that an agent can't take an action it wasn't authorized for. Catching mistakes after the fact isn't enough, especially when the mistakes involve writing to a database or talking to a customer or moving money.

This is mostly an interface design problem. If your API makes the dangerous action just as easy as the safe action, agents will sometimes take the dangerous one. If the dangerous action requires extra ceremony, they mostly won't. We're interested in what that ceremony looks like in practice.

## Observability for AI Systems

Logs, metrics, and traces were built for deterministic software, where the same input produces the same output and you can replay a failure with confidence. Agent behavior is emergent. Context windows are large. The usual tooling doesn't quite fit.

We're working through what to log, at what granularity, and how to structure it so both a person reviewing an incident and another agent doing analysis can use it. The answer probably isn't "more logs." It's logs designed for the specific failure modes that agents have, which aren't the failure modes traditional services have.
