---
title: "Launching cdr-home: A Web Site for Humans and Agents"
date: 2026-03-07
author: Coastal Digital Research
tags: [announcement, architecture, agents, fastapi, htmx]
unlisted: true
---

# Launching cdr-home: A Web Site for Humans and Agents

Most web sites are built for one kind of reader: the human visitor arriving via a browser. The architecture reflects this — HTML templates, JavaScript for interactivity, CSS for layout. When an AI agent navigates the same URL, it receives the same HTML, must parse navigation chrome, skip sidebars, and extract the actual content from a document designed for eyes rather than parsers.

This asymmetry matters more than it used to. AI agents are browsing the web to gather information, verify facts, and coordinate work. They deserve infrastructure designed for them, not infrastructure that merely tolerates them.

cdr-home is our attempt to build a web site that serves both audiences equally well.

## Why Dual Endpoints Matter

When an AI agent fetches a typical web page, a substantial fraction of what it receives is noise: navigation menus, footers, cookie banners, advertising markup, and layout elements. The agent has to parse all of this to find the content it actually needs. This is slow, error-prone, and wastes context window tokens.

There is a better way. If a web site knows that some of its traffic is agentic, it can serve a clean, structured representation of the same content at a predictable URL. The agent gets exactly what it needs. The human gets a well-designed page. Neither audience has to compromise.

This is the core idea behind cdr-home: every piece of content is available in two forms, at two URLs, served by the same application.

## The Architecture

cdr-home is a FastAPI application. The stack is intentionally minimal:

- **FastAPI** for routing and response handling
- **Jinja2** for HTML template rendering
- **HTMX** for lightweight browser interactivity (loaded from CDN, no build step)
- **python-frontmatter** for parsing Markdown content with YAML metadata
- **PyYAML** for loading agent manifest files

Content lives in `content/pages/*.md` files with YAML frontmatter declaring title, summary, and tags. Agent manifests live in `agents/manifests/*.yaml`. Neither requires a database. The application reads from disk on startup and serves the results.

The routing pattern is consistent across all content types:

```
Human HTML:  GET /page/{slug}
Agent JSON:  GET /agent/page/{slug}.json
Agent MD:    GET /agent/page/{slug}.md

Human HTML:  GET /agents
Agent JSON:  GET /agent/agents.json

Human HTML:  GET /agents/{name}
Agent JSON:  GET /agent/agents/{name}.json
```

The human routes return `TemplateResponse` with a dark-professional HTML layout. The agent routes return `JSONResponse` or `PlainTextResponse` with `text/markdown` content type. The underlying data is the same — only the representation differs.

## Agent Discovery

Beyond the dual endpoints, cdr-home implements a discovery convention at `/.well-known/agent.json`. This file describes the site's agent capabilities: what endpoints exist, what they return, and how to navigate the content programmatically.

An AI agent browsing cdr-home for the first time can fetch `/.well-known/agent.json` and immediately understand the full structure of the site without parsing any HTML. The discovery manifest lists every agent endpoint, the URL pattern, and the response format.

This follows the same logic as `/.well-known/robots.txt` for crawlers or `/.well-known/openid-configuration` for authentication. A well-known location for a structured capability description is a small convention with large payoff for agent interoperability.

## The Agent Manifest Registry

One of the more unusual features of cdr-home is the agent manifest registry at `/agents`. This lists the AI agents operated by Coastal Digital Research: what they do, what models they use, what tools they have access to, what their inputs and outputs look like, and what their SLOs are.

Manifests are YAML files with a normalized schema:

```yaml
name: mae
description: Persistent AI agent for long-running development and operations tasks.
owner: Coastal Digital Research
entrypoint: mae
runtime: python3.12
models:
  - claude-sonnet-4-6
tools:
  - bash
  - file_read
  - file_write
inputs:
  - task description (natural language)
outputs:
  - structured action log (JSON)
slo: best-effort; no hard latency guarantees
```

Making agent capabilities public serves two purposes. First, it creates accountability: if an agent is listed as having bash access, you can verify that claim against its actual behavior. Second, it enables interoperability: another agent that wants to delegate work to a CDR agent can read the manifest and understand exactly what that agent can do.

## How to Run It

The application runs with a single command:

```bash
uvicorn app.main:app --reload
```

For production, a Containerfile is included:

```bash
podman build -f Containerfile -t cdr-home .
podman run -p 8000:8000 cdr-home
```

Dependencies are declared in `pyproject.toml` and install cleanly with pip:

```bash
pip install .
```

No build step, no asset pipeline, no database migrations. The application starts, reads content from disk, and serves requests.

## What Comes Next

cdr-home is a starting point. A few things we expect to add:

**A blog route.** The `blog/` directory exists; the route does not yet. Blog posts follow the same Markdown-with-frontmatter pattern and will expose the same dual endpoints.

**Structured agent links in HTTP headers.** Rather than requiring agents to know the `/agent/...` URL convention in advance, we can add a `Link` header to every HTML response pointing to the corresponding agent endpoint. This mirrors how `<link rel="alternate">` works for RSS feeds.

**Content negotiation.** A client that sends `Accept: application/json` to a human URL could receive the agent JSON directly, without needing to know the `/agent/...` URL structure.

The underlying principle stays the same: the same content, served cleanly to both humans and the AI systems that increasingly act on their behalf.

---

The source code is available at github.com/coastal-digital-research/cdr-home under the Apache 2.0 license.
