"""MCP Server for math animation generation with Manim."""

from __future__ import annotations

import json
import os
from typing import Any

from mcp.server.fastmcp import FastMCP

from math_animation_mcp.tools import render_tools, template_tools, input_tools, repair_tools, personalization_tools, export_tools

mcp = FastMCP(
    "math-animation",
    instructions="Generate 3Blue1Brown-style math teaching animations with Manim. "
                 "Supports text, LaTeX, PDF, images as input. Chinese math exams supported.",
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "./animation_output")

# ── Render Tools ───────────────────────────────────────────────

@mcp.tool()
def render_animation(
    code: str,
    quality: str = "medium",
    format: str = "mp4",
    style: str | None = None,
) -> str:
    """Render a Manim animation from Python code.

    Args:
        code: Complete Manim Python code containing a Scene subclass with construct().
        quality: Render quality - low (480p), medium (720p), high (1080p), 4k.
        format: Output format - mp4, gif, webm.
        style: Visual style preset - three_blue_one_brown, khan_academy, textbook, playful, dark_tech, blackboard.

    Returns:
        JSON with success status and file path or error message.
    """
    result = render_tools.render_animation(code, quality=quality, fmt=format, style=style, output_dir=OUTPUT_DIR)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def preview_scene(code: str, style: str | None = None) -> str:
    """Quick 480p preview render of a Manim scene (faster, lower quality).

    Args:
        code: Complete Manim Python code.
        style: Optional visual style preset.
    """
    result = render_tools.preview_scene(code, style=style, output_dir=OUTPUT_DIR)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def render_gif(code: str, style: str | None = None) -> str:
    """Render a Manim scene as GIF for easy sharing.

    Args:
        code: Complete Manim Python code.
        style: Optional visual style preset.
    """
    result = render_tools.render_gif(code, style=style, output_dir=OUTPUT_DIR)
    return json.dumps(result, ensure_ascii=False)


# ── Template Tools ─────────────────────────────────────────────

@mcp.tool()
def list_templates(category: str | None = None, difficulty: int | None = None) -> str:
    """List available animation templates.

    Args:
        category: Filter by category - geometry, algebra, calculus, trigonometry, statistics, physics, cs.
        difficulty: Filter by max difficulty level (1=小学 to 5=竞赛).
    """
    results = template_tools.list_templates(category=category, difficulty=difficulty)
    return json.dumps(results, ensure_ascii=False)


@mcp.tool()
def get_template(template_id: str) -> str:
    """Get a template's source code and metadata.

    Args:
        template_id: Template identifier, e.g. "geometry/pythagorean", "calculus/derivative_tangent".
    """
    result = template_tools.get_template(template_id)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def search_templates(keyword: str) -> str:
    """Search templates by keyword.

    Args:
        keyword: Search term in any language, e.g. "勾股", "derivative", "正弦".
    """
    results = template_tools.search_templates(keyword)
    return json.dumps(results, ensure_ascii=False)


# ── Input Processing Tools ─────────────────────────────────────

@mcp.tool()
def detect_input_type(content: str) -> str:
    """Auto-detect input type: math_problem, latex_formula, animation_request, modification, article, concept_description.

    Args:
        content: Raw text input from user.
    """
    result = input_tools.detect_input_type(content)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def parse_pdf(file_path: str, page_range: str | None = None) -> str:
    """Extract text and math formulas from a PDF file.

    Args:
        file_path: Absolute path to the PDF file.
        page_range: Optional page range, e.g. "1-3" or "5".
    """
    result = input_tools.parse_pdf(file_path, page_range=page_range)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def parse_image(file_path: str) -> str:
    """OCR an image to extract text and math formulas.

    Args:
        file_path: Absolute path to the image file (PNG, JPG, etc.).
    """
    result = input_tools.parse_image(file_path)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def fix_ocr_errors(text: str) -> str:
    """Fix common OCR errors in math text (rule-based).

    Args:
        text: OCR output text that may contain recognition errors.
    """
    result = input_tools.fix_ocr_errors(text)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def normalize_content(raw_text: str) -> str:
    """Normalize raw text into structured format with extracted formulas and text segments.

    Args:
        raw_text: Raw text possibly containing LaTeX, Chinese, math formulas.
    """
    result = input_tools.normalize_content(raw_text)
    return json.dumps(result, ensure_ascii=False)


# ── Self-Repair Tools ──────────────────────────────────────────

@mcp.tool()
def analyze_error(code: str, error_msg: str) -> str:
    """Analyze a Manim render error and suggest fixes.

    Args:
        code: The Manim code that failed.
        error_msg: The error message or traceback.
    """
    result = repair_tools.analyze_error(code, error_msg)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def fix_latex_error(code: str, error_msg: str) -> str:
    """Auto-fix common LaTeX errors in Manim code.

    Args:
        code: The failing Manim code.
        error_msg: The LaTeX-related error message.
    """
    result = repair_tools.fix_latex_error(code, error_msg)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def fix_python_error(code: str, error_msg: str) -> str:
    """Auto-fix common Python/Manim API errors in code.

    Args:
        code: The failing Manim code.
        error_msg: The Python error message.
    """
    result = repair_tools.fix_python_error(code, error_msg)
    return json.dumps(result, ensure_ascii=False)


# ── Personalization Tools ──────────────────────────────────────

@mcp.tool()
def set_style(style_name: str) -> str:
    """Switch visual style preset for animations.

    Args:
        style_name: One of: three_blue_one_brown, khan_academy, textbook, playful, dark_tech, blackboard.
    """
    result = personalization_tools.set_style(style_name)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def set_preferences(preferences_json: str) -> str:
    """Update user preferences (partial merge). Pass a JSON string.

    Args:
        preferences_json: JSON string with partial preferences, e.g. '{"audience": {"level": 2}, "output": {"default_quality": "high"}}'.
    """
    try:
        updates = json.loads(preferences_json)
    except json.JSONDecodeError as e:
        return json.dumps({"success": False, "error": f"Invalid JSON: {e}"})
    result = personalization_tools.set_preferences(updates)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def get_preferences() -> str:
    """Get current user preferences including style and audience info."""
    result = personalization_tools.get_preferences()
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def set_branding(
    watermark: str | None = None,
    logo_path: str | None = None,
    intro_text: str | None = None,
    outro_text: str | None = None,
) -> str:
    """Set branding options for generated videos.

    Args:
        watermark: Text watermark to overlay on videos.
        logo_path: Path to a logo image file.
        intro_text: Text for the intro slide.
        outro_text: Text for the outro slide.
    """
    result = personalization_tools.set_branding(watermark=watermark, logo_path=logo_path, intro_text=intro_text, outro_text=outro_text)
    return json.dumps(result, ensure_ascii=False)


# ── Export Tools ───────────────────────────────────────────────

@mcp.tool()
def export_video(
    file_path: str,
    format: str = "mp4",
    aspect_ratio: str | None = None,
) -> str:
    """Export/convert a rendered video to a different format or aspect ratio.

    Args:
        file_path: Path to the source video file.
        format: Target format - mp4, webm, gif.
        aspect_ratio: Target aspect ratio - 16:9, 9:16 (vertical), 1:1 (square), 4:3.
    """
    result = export_tools.export_video(file_path, fmt=format, aspect_ratio=aspect_ratio, output_dir=OUTPUT_DIR)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def add_subtitles(video_path: str, text: str) -> str:
    """Add subtitles to a video.

    Args:
        video_path: Path to the source video.
        text: Subtitle text, one line per segment (each line becomes a 3-second subtitle).
    """
    result = export_tools.add_subtitles(video_path, text, output_dir=OUTPUT_DIR)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def add_tts_narration(video_path: str, script: str, voice: str = "default") -> str:
    """Add TTS voice narration to a video (coming soon).

    Args:
        video_path: Path to the source video.
        script: Narration script.
        voice: Voice selection.
    """
    result = export_tools.add_tts_narration(video_path, script, voice=voice)
    return json.dumps(result, ensure_ascii=False)


# ── Server Entry ───────────────────────────────────────────────

def run():
    """Run the MCP server via stdio."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    run()
