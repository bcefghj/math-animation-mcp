"""User preferences schema and persistence."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class StyleConfig(BaseModel):
    preset: str = "three_blue_one_brown"
    custom_colors: dict[str, str] = Field(default_factory=lambda: {
        "primary": "#3B82F6",
        "secondary": "#F59E0B",
        "accent": "#10B981",
    })


class AudienceConfig(BaseModel):
    level: int = Field(default=3, ge=1, le=5)
    language: str = "zh-CN"


class OutputConfig(BaseModel):
    default_quality: str = "medium"
    default_format: str = "mp4"
    aspect_ratio: str = "16:9"
    max_duration: int = 120


class AnimationConfig(BaseModel):
    speed_multiplier: float = 1.0
    pause_between_steps: float = 1.0
    font_scale: float = 1.0


class BrandingConfig(BaseModel):
    watermark: str = ""
    logo_path: str = ""
    intro_text: str = ""
    outro_text: str = ""


class UserPreferences(BaseModel):
    style: StyleConfig = Field(default_factory=StyleConfig)
    audience: AudienceConfig = Field(default_factory=AudienceConfig)
    output: OutputConfig = Field(default_factory=OutputConfig)
    animation: AnimationConfig = Field(default_factory=AnimationConfig)
    branding: BrandingConfig = Field(default_factory=BrandingConfig)


_PREFS_PATH = os.environ.get(
    "MANIM_PREFS_PATH",
    os.path.join(os.getcwd(), "manim_prefs.yaml"),
)


def _get_default_prefs_path() -> str:
    return os.environ.get("MANIM_PREFS_PATH", os.path.join(os.getcwd(), "manim_prefs.yaml"))


def load_preferences(path: str | None = None) -> UserPreferences:
    path = path or _get_default_prefs_path()
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        return UserPreferences(**data)

    default_path = Path(__file__).parent / "default_prefs.yaml"
    if default_path.exists():
        with open(default_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        return UserPreferences(**data)

    return UserPreferences()


def save_preferences(prefs: UserPreferences, path: str | None = None) -> str:
    path = path or _get_default_prefs_path()
    data = prefs.model_dump()
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
    return path


def update_preferences(updates: dict[str, Any], path: str | None = None) -> UserPreferences:
    """Merge partial updates into existing preferences."""
    prefs = load_preferences(path)
    data = prefs.model_dump()
    for key, value in updates.items():
        if key in data and isinstance(data[key], dict) and isinstance(value, dict):
            data[key].update(value)
        else:
            data[key] = value
    new_prefs = UserPreferences(**data)
    save_preferences(new_prefs, path)
    return new_prefs
