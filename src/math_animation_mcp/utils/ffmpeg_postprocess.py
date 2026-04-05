"""FFmpeg post-processing: watermark, subtitles, format conversion, compression."""

from __future__ import annotations

import os
import subprocess
import shutil


def _run_ffmpeg(args: list[str], timeout: int = 120) -> tuple[bool, str]:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        return False, "ffmpeg not found in PATH"
    try:
        result = subprocess.run(
            [ffmpeg] + args,
            capture_output=True, text=True, timeout=timeout,
        )
        if result.returncode != 0:
            return False, result.stderr[-1000:]
        return True, ""
    except subprocess.TimeoutExpired:
        return False, f"ffmpeg timed out after {timeout}s"
    except Exception as e:
        return False, str(e)


def add_watermark(video_path: str, text: str, output_path: str | None = None) -> tuple[bool, str]:
    """Burn a text watermark into the bottom-right corner."""
    if not output_path:
        base, ext = os.path.splitext(video_path)
        output_path = f"{base}_watermarked{ext}"
    ok, err = _run_ffmpeg([
        "-i", video_path,
        "-vf", f"drawtext=text='{text}':fontsize=20:fontcolor=white@0.5:x=w-tw-20:y=h-th-20",
        "-codec:a", "copy", "-y", output_path,
    ])
    return (True, output_path) if ok else (False, err)


def convert_format(video_path: str, target_format: str, output_path: str | None = None) -> tuple[bool, str]:
    """Convert video to a different format (mp4, webm, gif)."""
    if not output_path:
        base = os.path.splitext(video_path)[0]
        output_path = f"{base}.{target_format}"

    if target_format == "gif":
        ok, err = _run_ffmpeg([
            "-i", video_path,
            "-vf", "fps=15,scale=640:-1:flags=lanczos",
            "-y", output_path,
        ])
    else:
        ok, err = _run_ffmpeg([
            "-i", video_path, "-y", output_path,
        ])
    return (True, output_path) if ok else (False, err)


def change_aspect_ratio(
    video_path: str,
    aspect: str = "16:9",
    output_path: str | None = None,
) -> tuple[bool, str]:
    """Pad/crop video to a target aspect ratio."""
    if not output_path:
        base, ext = os.path.splitext(video_path)
        output_path = f"{base}_{aspect.replace(':', 'x')}{ext}"

    aspect_map = {
        "16:9": "1920:1080",
        "9:16": "1080:1920",
        "1:1": "1080:1080",
        "4:3": "1440:1080",
    }
    size = aspect_map.get(aspect, "1920:1080")
    w, h = size.split(":")
    vf = f"scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:black"

    ok, err = _run_ffmpeg(["-i", video_path, "-vf", vf, "-y", output_path])
    return (True, output_path) if ok else (False, err)


def add_subtitles_to_video(video_path: str, srt_path: str, output_path: str | None = None) -> tuple[bool, str]:
    """Burn SRT subtitles into video."""
    if not output_path:
        base, ext = os.path.splitext(video_path)
        output_path = f"{base}_subtitled{ext}"
    ok, err = _run_ffmpeg([
        "-i", video_path,
        "-vf", f"subtitles={srt_path}",
        "-y", output_path,
    ])
    return (True, output_path) if ok else (False, err)
