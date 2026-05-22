import re
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .content import load_all_pages, load_page
from .registry import load_all_agents, load_agent

BASE_DIR = Path(__file__).parent.parent

app = FastAPI(title="Coastal Digital Research")
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


# --- Content negotiation helpers ---

# LLM / agent crawlers that prefer Markdown when given a choice.
# Match is case-insensitive substring on User-Agent.
_LLM_BOT_PATTERNS = re.compile(
    r"GPTBot|ChatGPT-User|OAI-SearchBot|ClaudeBot|Claude-Web|anthropic-ai|"
    r"PerplexityBot|YouBot|Amazonbot|Applebot-Extended|cohere-ai|Bytespider|"
    r"FacebookBot|Meta-ExternalAgent|DiffBot|Omgilibot|Omgili|MistralAI-User",
    re.IGNORECASE,
)

# Search-engine indexers. They want the same HTML humans see, so ranking is accurate.
_SEARCH_BOT_PATTERNS = re.compile(
    r"Googlebot|Bingbot|Slurp|DuckDuckBot|Baiduspider|YandexBot|Sogou|Exabot|"
    r"facebookexternalhit|Twitterbot|LinkedInBot|Discordbot|Slackbot",
    re.IGNORECASE,
)


def _alt_link_header(slug: str) -> str:
    return (
        f'</agent/page/{slug}.md>; rel="alternate"; type="text/markdown", '
        f'</agent/page/{slug}.json>; rel="alternate"; type="application/json"'
    )


def _wants_format(request: Request, slug: str) -> str:
    """Return one of: 'html', 'markdown', 'json'."""
    # Explicit query override always wins (handy for users to force a format).
    fmt = request.query_params.get("format")
    if fmt in {"html", "markdown", "json"}:
        return fmt

    accept = request.headers.get("accept", "")
    if "application/json" in accept:
        return "json"
    if "text/markdown" in accept:
        return "markdown"

    ua = request.headers.get("user-agent", "")
    # Search bots get the human HTML so ranking reflects real content.
    if _SEARCH_BOT_PATTERNS.search(ua):
        return "html"
    # LLM bots without an explicit Accept get the cleaner markdown payload.
    if _LLM_BOT_PATTERNS.search(ua):
        return "markdown"

    return "html"


# --- Human routes ---

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    pages = load_all_pages()
    agents = load_all_agents()
    return templates.TemplateResponse(request, "home.html", {
        "pages": pages,
        "agents": agents,
    })


@app.get("/page/{slug}")
async def page(request: Request, slug: str):
    page = load_page(slug)
    if page is None:
        return HTMLResponse("Not found", status_code=404)

    link_header = _alt_link_header(slug)
    fmt = _wants_format(request, slug)

    if fmt == "json":
        return JSONResponse(
            {k: v for k, v in page.items() if k != "content_html"},
            headers={"Link": link_header, "Vary": "Accept, User-Agent"},
        )
    if fmt == "markdown":
        body = f"# {page['title']}\n\n"
        if page["summary"]:
            body += f"> {page['summary']}\n\n"
        body += page["content_md"]
        return PlainTextResponse(
            body,
            media_type="text/markdown; charset=utf-8",
            headers={"Link": link_header, "Vary": "Accept, User-Agent"},
        )

    response = templates.TemplateResponse(request, "page.html", {"page": page})
    response.headers["Link"] = link_header
    response.headers["Vary"] = "Accept, User-Agent"
    return response


@app.get("/agents", response_class=HTMLResponse)
async def agents_list(request: Request):
    agents = load_all_agents()
    return templates.TemplateResponse(request, "agents.html", {"agents": agents})


@app.get("/agents/{name}", response_class=HTMLResponse)
async def agent_detail(request: Request, name: str):
    agent = load_agent(name)
    if agent is None:
        return HTMLResponse("Not found", status_code=404)
    return templates.TemplateResponse(request, "agent_detail.html", {"agent": agent})


# --- Agent JSON/Markdown routes (explicit, stable contract) ---

@app.get("/agent/pages.json")
async def agent_pages():
    pages = load_all_pages()
    return JSONResponse([
        {k: v for k, v in p.items() if k not in ("content_html",)}
        for p in pages
    ])


@app.get("/agent/page/{slug}.json")
async def agent_page_json(slug: str):
    page = load_page(slug)
    if page is None:
        return JSONResponse({"error": "not found"}, status_code=404)
    return JSONResponse({k: v for k, v in page.items() if k != "content_html"})


@app.get("/agent/page/{slug}.md")
async def agent_page_md(slug: str):
    page = load_page(slug)
    if page is None:
        return PlainTextResponse("Not found", status_code=404)
    return PlainTextResponse(page["content_md"], media_type="text/markdown; charset=utf-8")


@app.get("/agent/agents.json")
async def agent_agents():
    return JSONResponse(load_all_agents())


@app.get("/agent/agents/{name}.json")
async def agent_agent_json(name: str):
    agent = load_agent(name)
    if agent is None:
        return JSONResponse({"error": "not found"}, status_code=404)
    return JSONResponse(agent)


# --- Agent discovery ---

@app.get("/.well-known/agent.json")
async def well_known_agent():
    return JSONResponse({
        "name": "Coastal Digital Research",
        "url": "https://coastaldigital.ai",
        "description": "AI agent company building open-source infrastructure for AI systems.",
        "content_negotiation": {
            "human": "Send Accept: text/html (default).",
            "markdown": "Send Accept: text/markdown, or append ?format=markdown.",
            "json": "Send Accept: application/json, or append ?format=json.",
            "note": "LLM crawler user-agents (GPTBot, ClaudeBot, PerplexityBot, ...) "
                    "are auto-served Markdown. Search-engine crawlers get HTML.",
        },
        "agent_endpoints": {
            "pages": "/agent/pages.json",
            "page": "/agent/page/{slug}.json",
            "page_md": "/agent/page/{slug}.md",
            "agents": "/agent/agents.json",
            "agent": "/agent/agents/{name}.json",
        },
        "human_endpoints": {
            "home": "/",
            "page": "/page/{slug}",
            "agents": "/agents",
            "agent": "/agents/{name}",
        },
    })
