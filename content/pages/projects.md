---
title: Projects
summary: Open-source repos I maintain under Coastal Digital Research.
tags: [projects, open-source, repos]
---

## Active Projects

### mae

A persistent agent for long-running tasks on Linux boxes. Keeps context across sessions, runs shell commands, reads and writes files, returns results in structured form. I use it daily for supervised dev and ops work.

Repository: github.com/coastal-digital-research/mae

---

### rlm-linux

A remote Linux machine agent. Gives AI systems a standardized way to operate on a Linux host: sandboxed shell, file ops, process management, audit logs. Meant to be a building block inside bigger agent pipelines.

Repository: github.com/coastal-digital-research/rlm-linux

---

### CDRcache

Content-addressed cache for agent outputs. If an agent produces the same result for the same input, you should only have to run it once. CDRcache stores those outputs by hash and gives you back a stable record of what was produced and when.

Repository: github.com/coastal-digital-research/CDRcache

---

### CDRbrowser

A browser automation agent that returns clean structured data instead of raw HTML. Built because most browser agents I tried gave back too much noise.

Repository: github.com/coastal-digital-research/CDRbrowser

---

### CDRdistill

Turns messy web pages and files into clean Markdown and JSON. Sits in front of retrieval pipelines and knowledge bases so they get usable input instead of soup.

Repository: github.com/coastal-digital-research/CDRdistill

---

### CDRmem

A small vector memory store for agents. Local-first, no extra services to run. Agents use it to remember facts and pull context across sessions.

Repository: github.com/coastal-digital-research/CDRmem

---

### cdr-home

This site. A FastAPI app that serves the same content as HTML for humans and as JSON or Markdown for agents. Reference implementation for the dual-mode approach.

Repository: github.com/coastal-digital-research/cdr-home
