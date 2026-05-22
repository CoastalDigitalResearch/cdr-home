# cdr-home

AI agent company landing page for Coastal Digital Research.

A dual-mode web application built with FastAPI + HTMX + Jinja2 that serves both human-readable HTML and agent-friendly JSON/Markdown endpoints for the same content.

## Features

- Human UI: Clean HTML pages with HTMX navigation
- Agent UI: `/agent/...` endpoints returning JSON and Markdown
- Agent manifest registry with YAML-backed agent profiles
- YAML frontmatter + Markdown content pages
- `/.well-known/agent.json` for agent discovery

## Stack

- FastAPI
- Jinja2 templates
- HTMX
- python-frontmatter (Markdown + YAML)
- PyYAML

## Running Locally

```bash
pip install .
uvicorn app.main:app --reload
```

Visit http://localhost:8000

## Endpoints

### Human

| URL | Description |
|-----|-------------|
| `/` | Home page with page grid and agent registry |
| `/page/{slug}` | Content page |
| `/agents` | Agent registry |
| `/agents/{name}` | Single agent manifest |

### Agent

| URL | Description |
|-----|-------------|
| `/.well-known/agent.json` | Agent discovery manifest |
| `/agent/pages.json` | All content pages (JSON) |
| `/agent/page/{slug}.json` | Single page (JSON) |
| `/agent/page/{slug}.md` | Single page (Markdown) |
| `/agent/agents.json` | All agent manifests (JSON) |
| `/agent/agents/{name}.json` | Single agent manifest (JSON) |

## Container

```bash
podman build -f Containerfile -t cdr-home .
podman run -p 8000:8000 cdr-home
```

## Project Structure

```
cdr-home/
├── app/
│   ├── main.py       # FastAPI routes
│   ├── content.py    # Markdown page loader
│   └── registry.py   # Agent manifest registry
├── templates/        # Jinja2 HTML templates
├── static/           # CSS
├── content/pages/    # Markdown content pages
├── agents/manifests/ # Agent YAML manifests
├── blog/             # Blog posts
├── pyproject.toml
└── Containerfile
```

## License

Apache-2.0
