"""Template management MCP tools."""

from __future__ import annotations

import os
import re
from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent.parent / "templates"

_TEMPLATE_REGISTRY: dict[str, dict] = {}


def _scan_templates() -> None:
    """Scan templates directory and build registry."""
    global _TEMPLATE_REGISTRY
    if _TEMPLATE_REGISTRY:
        return

    for category_dir in TEMPLATES_DIR.iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith("_"):
            continue
        category = category_dir.name
        for f in category_dir.glob("*.py"):
            if f.name.startswith("_"):
                continue
            content = f.read_text(encoding="utf-8")
            # Extract metadata from docstring
            title = f.stem.replace("_", " ").title()
            desc = ""
            keywords: list[str] = []
            difficulty = 3

            doc_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
            if doc_match:
                doclines = doc_match.group(1).strip().split("\n")
                title = doclines[0] if doclines else title
                for line in doclines[1:]:
                    line = line.strip()
                    if line.startswith("Keywords:"):
                        keywords = [k.strip() for k in line.split(":", 1)[1].split(",")]
                    elif line.startswith("Difficulty:"):
                        try:
                            difficulty = int(line.split(":", 1)[1].strip())
                        except ValueError:
                            pass
                    elif line and not desc:
                        desc = line

            template_id = f"{category}/{f.stem}"
            _TEMPLATE_REGISTRY[template_id] = {
                "id": template_id,
                "category": category,
                "title": title,
                "description": desc,
                "keywords": keywords,
                "difficulty": difficulty,
                "file_path": str(f),
            }


def list_templates(category: str | None = None, difficulty: int | None = None) -> list[dict]:
    """List available templates, optionally filtered by category and difficulty.

    Args:
        category: geometry, algebra, calculus, trigonometry, statistics, physics, cs
        difficulty: 1-5 (maps to audience level)

    Returns:
        List of template metadata dicts.
    """
    _scan_templates()
    results = list(_TEMPLATE_REGISTRY.values())
    if category:
        results = [t for t in results if t["category"] == category]
    if difficulty:
        results = [t for t in results if t["difficulty"] <= difficulty]
    return results


def get_template(template_id: str) -> dict:
    """Get template source code and metadata.

    Args:
        template_id: e.g. "geometry/pythagorean"

    Returns:
        Dict with metadata + code field.
    """
    _scan_templates()
    meta = _TEMPLATE_REGISTRY.get(template_id)
    if not meta:
        return {"error": f"Template '{template_id}' not found", "available": list(_TEMPLATE_REGISTRY.keys())}

    code = Path(meta["file_path"]).read_text(encoding="utf-8")
    return {**meta, "code": code}


def search_templates(keyword: str) -> list[dict]:
    """Search templates by keyword (matches title, description, keywords).

    Args:
        keyword: Search term, e.g. "勾股", "derivative", "抛物线"

    Returns:
        Matching templates.
    """
    _scan_templates()
    keyword_lower = keyword.lower()
    results = []
    for t in _TEMPLATE_REGISTRY.values():
        searchable = f"{t['title']} {t['description']} {' '.join(t['keywords'])}".lower()
        if keyword_lower in searchable:
            results.append(t)
    return results
