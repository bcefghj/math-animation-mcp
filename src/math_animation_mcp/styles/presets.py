"""Six visual style presets for math animations."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class StylePreset:
    name: str
    display_name: str
    background_color: str
    text_color: str
    primary_color: str
    secondary_color: str
    accent_color: str
    highlight_color: str
    description: str
    suitable_for: str

    def to_manim_config_code(self) -> str:
        """Return Manim config lines to apply this style."""
        return (
            f'config.background_color = "{self.background_color}"\n'
        )

    def get_color_constants(self) -> str:
        """Return Python code defining color constants for this style."""
        return (
            f'STYLE_BG = "{self.background_color}"\n'
            f'STYLE_TEXT = "{self.text_color}"\n'
            f'STYLE_PRIMARY = "{self.primary_color}"\n'
            f'STYLE_SECONDARY = "{self.secondary_color}"\n'
            f'STYLE_ACCENT = "{self.accent_color}"\n'
            f'STYLE_HIGHLIGHT = "{self.highlight_color}"\n'
        )


PRESETS: dict[str, StylePreset] = {
    "three_blue_one_brown": StylePreset(
        name="three_blue_one_brown",
        display_name="3Blue1Brown",
        background_color="#1C1C1C",
        text_color="#FFFFFF",
        primary_color="#58C4DD",
        secondary_color="#FFFF00",
        accent_color="#83C167",
        highlight_color="#FF8080",
        description="经典 3Blue1Brown 深色风格，蓝+黄+绿配色",
        suitable_for="科普/大学教学",
    ),
    "khan_academy": StylePreset(
        name="khan_academy",
        display_name="可汗学院",
        background_color="#FFFFFF",
        text_color="#21242C",
        primary_color="#1865F2",
        secondary_color="#14BF96",
        accent_color="#FF914D",
        highlight_color="#D92916",
        description="明亮白色背景，柔和色彩，高对比度",
        suitable_for="中小学教学",
    ),
    "textbook": StylePreset(
        name="textbook",
        display_name="教科书",
        background_color="#F5F5F5",
        text_color="#1A1A1A",
        primary_color="#2C3E50",
        secondary_color="#7F8C8D",
        accent_color="#E74C3C",
        highlight_color="#3498DB",
        description="正式极简风格，黑+灰+少量强调色",
        suitable_for="正式/论文",
    ),
    "playful": StylePreset(
        name="playful",
        display_name="趣味多彩",
        background_color="#FFF8E1",
        text_color="#33312E",
        primary_color="#FF6B6B",
        secondary_color="#4ECDC4",
        accent_color="#FFE66D",
        highlight_color="#A8E6CF",
        description="彩虹色系，温暖背景，活泼有趣",
        suitable_for="小学/低龄",
    ),
    "dark_tech": StylePreset(
        name="dark_tech",
        display_name="暗色科技",
        background_color="#000000",
        text_color="#E0E0E0",
        primary_color="#00D4FF",
        secondary_color="#BD00FF",
        accent_color="#39FF14",
        highlight_color="#FF006E",
        description="纯黑背景，霓虹蓝+紫+绿",
        suitable_for="大学/竞赛/CS",
    ),
    "blackboard": StylePreset(
        name="blackboard",
        display_name="黑板风",
        background_color="#2D5016",
        text_color="#F5F5DC",
        primary_color="#FFFFFF",
        secondary_color="#FFE4B5",
        accent_color="#FFD700",
        highlight_color="#FF6347",
        description="深绿黑板背景，白色粉笔感文字",
        suitable_for="课堂模拟",
    ),
}

AUDIENCE_LEVELS = {
    1: {"name": "小学", "speed": 0.5, "font_scale": 1.5, "detail": "极详细", "terms": "生活用语"},
    2: {"name": "初中", "speed": 0.7, "font_scale": 1.3, "detail": "详细", "terms": "基础术语"},
    3: {"name": "高中", "speed": 1.0, "font_scale": 1.0, "detail": "适中", "terms": "标准术语"},
    4: {"name": "大学", "speed": 1.2, "font_scale": 0.9, "detail": "精简", "terms": "专业术语"},
    5: {"name": "竞赛/研究", "speed": 1.5, "font_scale": 0.85, "detail": "最精简", "terms": "高级术语"},
}


def get_preset(name: str) -> StylePreset | None:
    return PRESETS.get(name)


def list_presets() -> list[dict]:
    return [
        {
            "name": p.name,
            "display_name": p.display_name,
            "description": p.description,
            "suitable_for": p.suitable_for,
            "background_color": p.background_color,
        }
        for p in PRESETS.values()
    ]
