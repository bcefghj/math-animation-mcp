"""Export and sharing MCP tools."""

from __future__ import annotations

import os
import tempfile

from math_animation_mcp.utils.ffmpeg_postprocess import (
    convert_format,
    change_aspect_ratio,
    add_watermark,
    add_subtitles_to_video,
)


def export_video(
    file_path: str,
    fmt: str = "mp4",
    aspect_ratio: str | None = None,
    output_dir: str = "./animation_output",
) -> dict:
    """Export video in a specific format and aspect ratio.

    Args:
        file_path: Source video path.
        fmt: Target format (mp4, webm, gif).
        aspect_ratio: Optional target ratio (16:9, 9:16, 1:1, 4:3).
        output_dir: Where to save the result.

    Returns:
        Dict with success and output file_path.
    """
    if not os.path.exists(file_path):
        return {"success": False, "error": f"File not found: {file_path}"}

    current_path = file_path

    if aspect_ratio:
        ok, result = change_aspect_ratio(current_path, aspect_ratio)
        if not ok:
            return {"success": False, "error": f"Aspect ratio change failed: {result}"}
        current_path = result

    current_ext = os.path.splitext(current_path)[1].lstrip(".")
    if current_ext != fmt:
        ok, result = convert_format(current_path, fmt)
        if not ok:
            return {"success": False, "error": f"Format conversion failed: {result}"}
        current_path = result

    return {"success": True, "file_path": current_path}


def add_subtitles(video_path: str, text: str, output_dir: str = "./animation_output") -> dict:
    """Add subtitles to a video.

    Args:
        video_path: Source video path.
        text: Subtitle text (one line per timestamp or plain text for full video).

    Returns:
        Dict with success and output file_path.
    """
    if not os.path.exists(video_path):
        return {"success": False, "error": f"File not found: {video_path}"}

    srt_path = tempfile.mktemp(suffix=".srt")
    try:
        lines = text.strip().split("\n")
        with open(srt_path, "w", encoding="utf-8") as f:
            for i, line in enumerate(lines, 1):
                start = f"00:00:{(i-1)*3:02d},000"
                end = f"00:00:{i*3:02d},000"
                f.write(f"{i}\n{start} --> {end}\n{line}\n\n")

        ok, result = add_subtitles_to_video(video_path, srt_path)
        if not ok:
            return {"success": False, "error": result}
        return {"success": True, "file_path": result}
    finally:
        if os.path.exists(srt_path):
            os.unlink(srt_path)


def add_tts_narration(video_path: str, script: str, voice: str = "default") -> dict:
    """Add TTS narration to a video (placeholder for future TTS integration).

    Args:
        video_path: Source video path.
        script: Narration script text.
        voice: Voice selection.

    Returns:
        Dict indicating the feature status.
    """
    return {
        "success": False,
        "error": "TTS narration is not yet implemented. This feature will be added in a future version.",
        "hint": "You can use external TTS tools to generate audio and merge with ffmpeg.",
    }
