from pathlib import Path
import yaml

MANIFESTS_DIR = Path(__file__).parent.parent / "agents" / "manifests"

FIELDS = ["name", "description", "owner", "entrypoint", "runtime", "models",
          "tools", "inputs", "outputs", "slo", "tags"]


def _normalize(raw: dict) -> dict:
    return {field: raw.get(field) for field in FIELDS}


def load_agent(name: str) -> dict | None:
    path = MANIFESTS_DIR / f"{name}.yaml"
    if not path.exists():
        return None
    with path.open() as f:
        raw = yaml.safe_load(f)
    return _normalize(raw)


def load_all_agents() -> list[dict]:
    agents = []
    for path in sorted(MANIFESTS_DIR.glob("*.yaml")):
        with path.open() as f:
            raw = yaml.safe_load(f)
        agents.append(_normalize(raw))
    return agents
