"""Rendering MCP tools: render_animation, preview_scene, render_gif."""

from __future__ import annotations

from math_animation_mcp.utils.sandbox import render_manim_code, RenderResult
from math_animation_mcp.utils.chinese_support import inject_chinese_support
from math_animation_mcp.styles.presets import get_preset


def _apply_style_to_code(code: str, style_name: str | None) -> str:
    """Prepend style configuration to Manim code."""
    if not style_name:
        return code
    preset = get_preset(style_name)
    if not preset:
        return code

    config_line = f'\nconfig.background_color = "{preset.background_color}"\n'

    lines = code.split('\n')
    insert_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('from manim') or line.startswith('import manim'):
            insert_idx = i + 1

    if insert_idx > 0:
        lines.insert(insert_idx, config_line)
    else:
        lines.insert(0, config_line)

    return '\n'.join(lines)


def render_animation(
    code: str,
    quality: str = "medium",
    fmt: str = "mp4",
    style: str | None = None,
    output_dir: str = "./animation_output",
    timeout: int = 120,
) -> dict:
    """Render a Manim animation from code.

    Args:
        code: Complete Manim Python code with a Scene subclass.
        quality: low (480p) | medium (720p) | high (1080p) | 4k
        fmt: mp4 | gif | webm
        style: Optional style preset name.
        output_dir: Where to save the output.
        timeout: Max render time in seconds.

    Returns:
        Dict with success, file_path, error_msg, etc.
    """
    code = inject_chinese_support(code)
    code = _apply_style_to_code(code, style)

    result = render_manim_code(
        code,
        quality=quality,
        fmt=fmt,
        output_dir=output_dir,
        timeout=timeout,
    )
    return {
        "success": result.success,
        "file_path": result.file_path,
        "error_msg": result.error_msg,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def preview_scene(code: str, style: str | None = None, output_dir: str = "./animation_output") -> dict:
    """Quick 480p preview render."""
    return render_animation(
        code,
        quality="low",
        fmt="mp4",
        style=style,
        output_dir=output_dir,
        timeout=60,
    )


def render_gif(code: str, style: str | None = None, output_dir: str = "./animation_output") -> dict:
    """Render as GIF for easy sharing."""
    return render_animation(
        code,
        quality="low",
        fmt="gif",
        style=style,
        output_dir=output_dir,
        timeout=60,
    )
