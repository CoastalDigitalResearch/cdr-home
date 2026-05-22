---
title: Projects
summary: Open-source repos we maintain under Coastal Digital Research.
tags: [projects, open-source, repos]
---

## Active Projects

### mae

A persistent agent for long-running tasks on Linux boxes. It keeps context across sessions, runs shell commands, reads and writes files, and returns results in structured form. We use it daily for supervised development and ops work. It started as a way to bridge the gap between "the model can help you code" and "the model can actually finish a multi-step task without you babysitting every step," and that's still what it's for.

Repository: github.com/coastal-digital-research/mae

---

### rlm-linux

A remote Linux machine agent. It gives AI systems a standardized way to operate on a Linux host: sandboxed shell, file ops, process management, and audit logging. Meant to be a building block inside bigger agent pipelines, not a standalone product. If you're wiring an agent up to act on real machines and you want a sane permission model, this is the layer to start with.

Repository: github.com/coastal-digital-research/rlm-linux

---

### CDRcache

Content-addressed cache for agent outputs. If an agent produces the same result for the same input, you should only have to run it once. CDRcache stores those outputs by hash and gives you back a stable record of what was produced and when. The audit trail is the part we care about most: you can ask exactly what input produced exactly what output, at exactly what time, and get a real answer.

Repository: github.com/coastal-digital-research/CDRcache

---

### CDRbrowser

A browser automation agent that returns clean structured data instead of raw HTML. We built it because most browser agents we tried gave back too much noise. They'd hand you back the whole page when what you wanted was three fields, and you'd spend the next 5,000 tokens cleaning it up. CDRbrowser does the cleanup on its side.

Repository: github.com/coastal-digital-research/CDRbrowser

---

### CDRdistill

Turns messy web pages and files into clean Markdown and JSON. It sits in front of retrieval pipelines and knowledge bases so they get usable input instead of soup. Same theory as CDRbrowser, applied to anything you can throw at it: PDFs, HTML, mixed-format documents, scanned junk.

Repository: github.com/coastal-digital-research/CDRdistill

---

### CDRmem

A small vector memory store for agents. Local-first, no extra services to run. Agents use it to remember facts and pull context across sessions. We wanted something we could embed directly in an agent process without standing up a separate database, and there wasn't anything quite that lightweight, so we built one.

Repository: github.com/coastal-digital-research/CDRmem

---

### CDRmix

An open-source Mixture-of-Experts (MoE) language model architecture built on RWKV-style blocks. Designed for streaming-capable, long-context reasoning. Most small models are minor variations on the same handful of transformer recipes, so it was refreshing to push on the architecture itself. The space needs more experiments like this, not fewer.

Repository: github.com/coastal-digital-research/CDRmix

---

### cdr-home

This site. A FastAPI app that serves the same content as HTML for humans and as JSON or Markdown for agents. Reference implementation for the dual-mode approach: human pages and agent endpoints sharing the same source of truth, with proper content negotiation so each kind of visitor gets what they actually want.

Repository: github.com/coastal-digital-research/cdr-home
