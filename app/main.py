from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .content import load_all_pages, load_page
from .registry import load_all_agents, load_agent

BASE_DIR = Path(__file__).parent.parent

app = FastAPI(title="Coastal Digital Research")
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


# --- Human routes ---

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    pages = load_all_pages()
    agents = load_all_agents()
    return templates.TemplateResponse("home.html", {
        "request": request,
        "pages": pages,
        "agents": agents,
    })


@app.get("/page/{slug}", response_class=HTMLResponse)
async def page(request: Request, slug: str):
    page = load_page(slug)
    if page is None:
        return HTMLResponse("Not found", status_code=404)
    return templates.TemplateResponse("page.html", {"request": request, "page": page})


@app.get("/agents", response_class=HTMLResponse)
async def agents_list(request: Request):
    agents = load_all_agents()
    return templates.TemplateResponse("agents.html", {"request": request, "agents": agents})


@app.get("/agents/{name}", response_class=HTMLResponse)
async def agent_detail(request: Request, name: str):
    agent = load_agent(name)
    if agent is None:
        return HTMLResponse("Not found", status_code=404)
    return templates.TemplateResponse("agent_detail.html", {"request": request, "agent": agent})


# --- Agent JSON/Markdown routes ---

@app.get("/agent/pages.json")
async def agent_pages():
    pages = load_all_pages()
    return JSONResponse([{k: v for k, v in p.items() if k != "content_md"} for p in pages])


@app.get("/agent/page/{slug}.json")
async def agent_page_json(slug: str):
    page = load_page(slug)
    if page is None:
        return JSONResponse({"error": "not found"}, status_code=404)
    return JSONResponse(page)


@app.get("/agent/page/{slug}.md")
async def agent_page_md(slug: str):
    page = load_page(slug)
    if page is None:
        return PlainTextResponse("Not found", status_code=404)
    return PlainTextResponse(page["content_md"], media_type="text/markdown")


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
        "url": "https://coastaldigital.co",
        "description": "AI agent company building open-source infrastructure for AI systems.",
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
