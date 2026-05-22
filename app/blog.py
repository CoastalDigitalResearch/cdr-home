from datetime import date as date_cls
from pathlib import Path
import frontmatter
import markdown

BLOG_DIR = Path(__file__).parent.parent / "blog"

_md = markdown.Markdown(
    extensions=["fenced_code", "tables", "toc", "sane_lists", "smarty"],
    output_format="html5",
)


def _render(md_text: str) -> str:
    _md.reset()
    return _md.convert(md_text)


def _as_iso(value) -> str:
    if isinstance(value, date_cls):
        return value.isoformat()
    return str(value) if value is not None else ""


def load_post(slug: str) -> dict | None:
    path = BLOG_DIR / f"{slug}.md"
    if not path.exists():
        return None
    post = frontmatter.load(str(path))
    if post.metadata.get("unlisted") and post.metadata.get("unlisted") is True:
        # Still loadable by direct slug, but caller can filter from index.
        pass
    return {
        "slug": slug,
        "title": post.metadata.get("title", slug.replace("-", " ").title()),
        "date": _as_iso(post.metadata.get("date")),
        "summary": post.metadata.get("summary", ""),
        "tags": post.metadata.get("tags", []),
        "author": post.metadata.get("author", "Coastal Digital Research"),
        "unlisted": bool(post.metadata.get("unlisted", False)),
        "content_md": post.content,
        "content_html": _render(post.content),
    }


def load_all_posts(include_unlisted: bool = False) -> list[dict]:
    posts = []
    for path in BLOG_DIR.glob("*.md"):
        slug = path.stem
        post = load_post(slug)
        if post is None:
            continue
        if post["unlisted"] and not include_unlisted:
            continue
        posts.append(post)
    # Newest first
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts
