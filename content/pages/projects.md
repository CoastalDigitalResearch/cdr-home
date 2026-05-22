---
title: Projects
summary: Open-source repositories maintained by Coastal Digital Research.
tags: [projects, open-source, repos]
---

## Active Projects

### mae

A persistent AI agent designed for long-running tasks on Linux systems. mae maintains context across sessions, executes shell commands, reads and writes files, and reports results in structured formats. Built for supervised automation of development and operations work.

Repository: github.com/coastal-digital-research/mae

---

### rlm-linux

A remote Linux machine agent that exposes a standardized interface for AI systems to operate on Linux hosts. Provides sandboxed shell access, file system operations, process management, and audit logging. Designed to be embedded in larger agent pipelines.

Repository: github.com/coastal-digital-research/rlm-linux

---

### CDRcache

A content-addressed cache for AI agent outputs. Agents that produce deterministic results given fixed inputs can store and retrieve those results from CDRcache, reducing redundant computation and providing a stable record of what was produced and when.

Repository: github.com/coastal-digital-research/CDRcache

---

### CDRbrowser

A browser automation agent built for AI systems. CDRbrowser exposes a structured API for navigating pages, extracting content, and interacting with web interfaces in a way that produces clean, structured output rather than raw HTML.

Repository: github.com/coastal-digital-research/CDRbrowser

---

### CDRdistill

A document processing agent that converts raw web and file content into clean, structured Markdown and JSON. Designed to serve as a preprocessing stage for retrieval pipelines and knowledge bases.

Repository: github.com/coastal-digital-research/CDRdistill

---

### CDRmem

A vector memory store for AI agents. CDRmem provides a lightweight, local-first embedding and retrieval layer that agents can use to store facts, retrieve context, and build persistent knowledge across sessions.

Repository: github.com/coastal-digital-research/CDRmem

---

### cdr-home

This site. A FastAPI application serving both human-readable HTML and machine-readable JSON/Markdown endpoints for the same content, demonstrating dual-mode design for AI-accessible web infrastructure.

Repository: github.com/coastal-digital-research/cdr-home
