"""Secure sandbox for executing Manim code via subprocess with timeout control."""

from __future__ import annotations

import os
import subprocess
import tempfile
import shutil
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class RenderResult:
    success: bool
    file_path: str = ""
    error_msg: str = ""
    duration_seconds: float = 0.0
    stdout: str = ""
    stderr: str = ""


def _find_output_video(media_dir: Path, scene_name: str) -> str | None:
    """Walk media_dir looking for the rendered video file."""
    videos_dir = media_dir / "videos"
    if not videos_dir.exists():
        return None
    for root, _dirs, files in os.walk(videos_dir):
        for f in files:
            if f.endswith((".mp4", ".gif", ".webm")) and scene_name in f:
                return os.path.join(root, f)
    # Fallback: return any video found
    for root, _dirs, files in os.walk(videos_dir):
        for f in files:
            if f.endswith((".mp4", ".gif", ".webm")):
                return os.path.join(root, f)
    return None


def render_manim_code(
    code: str,
    *,
    quality: str = "medium",
    fmt: str = "mp4",
    output_dir: str = "./animation_output",
    timeout: int = 120,
    python_bin: str | None = None,
) -> RenderResult:
    """Execute Manim code in a subprocess and return the result."""
    quality_flags = {
        "low": "-ql",
        "medium": "-qm",
        "high": "-qh",
        "4k": "-qk",
    }
    qflag = quality_flags.get(quality, "-qm")

    fmt_flag = {"mp4": "", "gif": "--format=gif", "webm": "--format=webm"}
    fflag = fmt_flag.get(fmt, "")

    scene_name = _extract_scene_name(code)
    if not scene_name:
        return RenderResult(success=False, error_msg="No Scene subclass found in code")

    os.makedirs(output_dir, exist_ok=True)

    tmpdir = tempfile.mkdtemp(prefix="manim_render_")
    script_path = os.path.join(tmpdir, "scene.py")
    media_dir = os.path.join(tmpdir, "media")

    try:
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(code)

        if python_bin is None:
            venv_python = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))))), ".venv", "bin", "python")
            if os.path.exists(venv_python):
                python_bin = venv_python
            else:
                python_bin = "python"

        cmd = [
            python_bin, "-m", "manim", "render",
            qflag,
            "--media_dir", media_dir,
        ]
        if fflag:
            cmd.append(fflag)
        cmd.extend([script_path, scene_name])

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=tmpdir,
        )

        if result.returncode != 0:
            return RenderResult(
                success=False,
                error_msg=result.stderr[-2000:] if result.stderr else "Unknown render error",
                stdout=result.stdout[-1000:],
                stderr=result.stderr[-2000:],
            )

        video_path = _find_output_video(Path(media_dir), scene_name)
        if not video_path:
            return RenderResult(
                success=False,
                error_msg="Render succeeded but no output file found",
                stdout=result.stdout[-1000:],
                stderr=result.stderr[-1000:],
            )

        final_name = f"{scene_name}.{fmt}"
        final_path = os.path.join(output_dir, final_name)
        counter = 1
        while os.path.exists(final_path):
            final_path = os.path.join(output_dir, f"{scene_name}_{counter}.{fmt}")
            counter += 1

        shutil.copy2(video_path, final_path)

        return RenderResult(
            success=True,
            file_path=os.path.abspath(final_path),
            stdout=result.stdout[-500:],
            stderr=result.stderr[-500:],
        )

    except subprocess.TimeoutExpired:
        return RenderResult(success=False, error_msg=f"Render timed out after {timeout}s")
    except Exception as e:
        return RenderResult(success=False, error_msg=str(e))
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def _extract_scene_name(code: str) -> str | None:
    """Extract the first Scene subclass name from code."""
    import re
    match = re.search(r'class\s+(\w+)\s*\(\s*\w*Scene\s*\)', code)
    if match:
        return match.group(1)
    match = re.search(r'class\s+(\w+)\s*\(\s*Scene\s*\)', code)
    if match:
        return match.group(1)
    # Fallback: any class that likely extends a Manim base
    match = re.search(r'class\s+(\w+)\s*\(', code)
    if match:
        return match.group(1)
    return None
