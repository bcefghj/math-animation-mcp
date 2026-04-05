"""Personalization MCP tools: style, preferences, branding."""

from __future__ import annotations

from typing import Any

from math_animation_mcp.config.schema import (
    load_preferences,
    save_preferences,
    update_preferences,
    UserPreferences,
)
from math_animation_mcp.styles.presets import (
    get_preset,
    list_presets,
    AUDIENCE_LEVELS,
)


def set_style(style_name: str) -> dict:
    """Switch visual style preset.

    Args:
        style_name: three_blue_one_brown | khan_academy | textbook | playful | dark_tech | blackboard

    Returns:
        Updated style info or error.
    """
    preset = get_preset(style_name)
    if not preset:
        return {
            "error": f"Unknown style '{style_name}'",
            "available": [p["name"] for p in list_presets()],
        }
    prefs = update_preferences({"style": {"preset": style_name}})
    return {
        "success": True,
        "style": preset.display_name,
        "description": preset.description,
        "background_color": preset.background_color,
    }


def set_preferences(updates: dict[str, Any]) -> dict:
    """Update user preferences (partial merge).

    Args:
        updates: Partial dict matching UserPreferences structure.

    Returns:
        Full updated preferences.
    """
    try:
        prefs = update_preferences(updates)
        return {"success": True, "preferences": prefs.model_dump()}
    except Exception as e:
        return {"success": False, "error": str(e)}


def get_preferences() -> dict:
    """Read current user preferences."""
    prefs = load_preferences()
    level_info = AUDIENCE_LEVELS.get(prefs.audience.level, {})
    return {
        "preferences": prefs.model_dump(),
        "audience_info": level_info,
        "style_info": get_preset(prefs.style.preset).__dict__ if get_preset(prefs.style.preset) else {},
    }


def set_branding(
    watermark: str | None = None,
    logo_path: str | None = None,
    intro_text: str | None = None,
    outro_text: str | None = None,
) -> dict:
    """Set branding options (watermark, logo, intro/outro text).

    Args:
        watermark: Text to overlay as watermark.
        logo_path: Path to logo image file.
        intro_text: Text for intro slide.
        outro_text: Text for outro slide.
    """
    branding_updates: dict[str, str] = {}
    if watermark is not None:
        branding_updates["watermark"] = watermark
    if logo_path is not None:
        branding_updates["logo_path"] = logo_path
    if intro_text is not None:
        branding_updates["intro_text"] = intro_text
    if outro_text is not None:
        branding_updates["outro_text"] = outro_text

    prefs = update_preferences({"branding": branding_updates})
    return {"success": True, "branding": prefs.branding.model_dump()}
