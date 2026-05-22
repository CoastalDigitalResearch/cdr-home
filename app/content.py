from pathlib import Path
import frontmatter

PAGES_DIR = Path(__file__).parent.parent / "content" / "pages"


def load_page(slug: str) -> dict | None:
    path = PAGES_DIR / f"{slug}.md"
    if not path.exists():
        return None
    post = frontmatter.load(str(path))
    return {
        "slug": slug,
        "title": post.metadata.get("title", slug.replace("-", " ").title()),
        "summary": post.metadata.get("summary", ""),
        "tags": post.metadata.get("tags", []),
        "content_md": post.content,
    }


def load_all_pages() -> list[dict]:
    pages = []
    for path in sorted(PAGES_DIR.glob("*.md")):
        slug = path.stem
        page = load_page(slug)
        if page:
            pages.append(page)
    return pages
