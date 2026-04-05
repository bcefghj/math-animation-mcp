"""Output file management and cleanup utilities."""

from __future__ import annotations

import os
import time
from pathlib import Path


def ensure_output_dir(output_dir: str = "./animation_output") -> str:
    os.makedirs(output_dir, exist_ok=True)
    return os.path.abspath(output_dir)


def cleanup_old_files(output_dir: str, max_age_hours: float = 24) -> int:
    """Remove files older than max_age_hours. Returns count of removed files."""
    cutoff = time.time() - max_age_hours * 3600
    removed = 0
    for f in Path(output_dir).iterdir():
        if f.is_file() and f.stat().st_mtime < cutoff:
            f.unlink()
            removed += 1
    return removed


def list_outputs(output_dir: str = "./animation_output") -> list[dict]:
    """List all output files with metadata."""
    result = []
    out = Path(output_dir)
    if not out.exists():
        return result
    for f in sorted(out.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True):
        if f.is_file() and f.suffix in (".mp4", ".gif", ".webm", ".png"):
            stat = f.stat()
            result.append({
                "name": f.name,
                "path": str(f.absolute()),
                "size_mb": round(stat.st_size / (1024 * 1024), 2),
                "created": time.ctime(stat.st_mtime),
            })
    return result
