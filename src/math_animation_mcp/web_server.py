"""Gradio web interface for math animation generation."""

from __future__ import annotations

import json
import os

import gradio as gr

from math_animation_mcp.tools.render_tools import render_animation, preview_scene
from math_animation_mcp.tools.template_tools import list_templates, get_template, search_templates
from math_animation_mcp.tools.input_tools import detect_input_type, normalize_content, fix_ocr_errors
from math_animation_mcp.tools.personalization_tools import get_preferences, set_style
from math_animation_mcp.styles.presets import PRESETS, AUDIENCE_LEVELS

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "./animation_output")

EXAMPLE_CODE = '''from manim import *
import numpy as np

class Example(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-PI, PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8, y_length=4,
        )
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)
        sin_label = MathTex(r"\\sin(x)", color=BLUE).to_corner(UR)
        cos_label = MathTex(r"\\cos(x)", color=RED).next_to(sin_label, DOWN)

        self.play(Create(axes))
        self.play(Create(sin_graph), Write(sin_label))
        self.play(Create(cos_graph), Write(cos_label))
        self.wait(2)
'''


def render_from_code(
    code: str,
    quality: str,
    fmt: str,
    style: str,
) -> tuple[str | None, str]:
    """Render Manim code and return (video_path, status_message)."""
    if not code.strip():
        return None, "请输入 Manim 代码"

    style_key = None
    for key, preset in PRESETS.items():
        if preset.display_name == style:
            style_key = key
            break

    result = render_animation(
        code,
        quality=quality.lower(),
        fmt=fmt.lower(),
        style=style_key,
        output_dir=OUTPUT_DIR,
    )

    if result["success"]:
        return result["file_path"], f"渲染成功！文件: {result['file_path']}"
    else:
        return None, f"渲染失败: {result['error_msg']}"


def quick_preview(code: str, style: str) -> tuple[str | None, str]:
    """Quick 480p preview."""
    if not code.strip():
        return None, "请输入 Manim 代码"

    style_key = None
    for key, preset in PRESETS.items():
        if preset.display_name == style:
            style_key = key
            break

    result = preview_scene(code, style=style_key, output_dir=OUTPUT_DIR)
    if result["success"]:
        return result["file_path"], "预览成功！"
    else:
        return None, f"预览失败: {result['error_msg']}"


def browse_templates(category: str | None) -> str:
    """List templates in a category."""
    cat = category if category != "全部" else None
    templates = list_templates(category=cat)
    if not templates:
        return "没有找到模板"
    lines = []
    for t in templates:
        lines.append(f"**{t['title']}** (`{t['id']}`)\n  {t['description']}\n  难度: {'⭐' * t['difficulty']}")
    return "\n\n".join(lines)


def load_template(template_id: str) -> str:
    """Load a template's source code."""
    result = get_template(template_id.strip())
    if "error" in result:
        return f"# 错误: {result['error']}"
    return result.get("code", "# No code found")


def search_for_templates(keyword: str) -> str:
    """Search templates by keyword."""
    results = search_templates(keyword)
    if not results:
        return "没有找到匹配的模板"
    lines = []
    for t in results:
        lines.append(f"- **{t['title']}** (`{t['id']}`) — {t['description']}")
    return "\n".join(lines)


def build_interface() -> gr.Blocks:
    """Build the Gradio interface."""
    style_choices = [p.display_name for p in PRESETS.values()]
    category_choices = ["全部", "geometry", "algebra", "calculus", "trigonometry", "statistics", "physics", "cs"]

    with gr.Blocks(
        title="Math Animation Studio",
    ) as demo:
        gr.Markdown(
            "# 🎬 数学动画工作室\n"
            "生成 3Blue1Brown 风格的数学教学动画。输入 Manim 代码或选择模板，一键渲染。"
        )

        with gr.Tabs():
            # Tab 1: Code Editor
            with gr.Tab("代码编辑器"):
                with gr.Row():
                    with gr.Column(scale=3):
                        code_input = gr.Code(
                            value=EXAMPLE_CODE,
                            language="python",
                            label="Manim 代码",
                            lines=25,
                        )
                    with gr.Column(scale=1):
                        style_select = gr.Dropdown(
                            choices=style_choices,
                            value="3Blue1Brown",
                            label="视觉风格",
                        )
                        quality_select = gr.Dropdown(
                            choices=["Low", "Medium", "High"],
                            value="Medium",
                            label="渲染质量",
                        )
                        format_select = gr.Dropdown(
                            choices=["mp4", "gif", "webm"],
                            value="mp4",
                            label="输出格式",
                        )
                        preview_btn = gr.Button("⚡ 快速预览 (480p)", variant="secondary")
                        render_btn = gr.Button("🎬 渲染", variant="primary")

                with gr.Row():
                    video_output = gr.Video(label="渲染结果")
                    status_output = gr.Textbox(label="状态", lines=3)

                preview_btn.click(
                    fn=quick_preview,
                    inputs=[code_input, style_select],
                    outputs=[video_output, status_output],
                )
                render_btn.click(
                    fn=render_from_code,
                    inputs=[code_input, quality_select, format_select, style_select],
                    outputs=[video_output, status_output],
                )

            # Tab 2: Template Browser
            with gr.Tab("模板库"):
                with gr.Row():
                    cat_select = gr.Dropdown(
                        choices=category_choices,
                        value="全部",
                        label="分类",
                    )
                    search_input = gr.Textbox(label="搜索关键词", placeholder="例: 勾股, derivative, 正弦")
                    search_btn = gr.Button("搜索")

                template_list = gr.Markdown(label="模板列表")
                cat_select.change(fn=browse_templates, inputs=[cat_select], outputs=[template_list])

                search_btn.click(fn=search_for_templates, inputs=[search_input], outputs=[template_list])

                with gr.Row():
                    template_id_input = gr.Textbox(label="模板 ID", placeholder="例: geometry/pythagorean")
                    load_btn = gr.Button("加载模板代码")

                template_code_output = gr.Code(language="python", label="模板代码", lines=20)
                load_btn.click(fn=load_template, inputs=[template_id_input], outputs=[template_code_output])

            # Tab 3: Settings
            with gr.Tab("设置"):
                gr.Markdown("## 个性化设置")
                with gr.Row():
                    with gr.Column():
                        gr.Markdown("### 视觉风格")
                        for name, preset in PRESETS.items():
                            gr.Markdown(
                                f"**{preset.display_name}** — {preset.description}\n"
                                f"背景: `{preset.background_color}` | 适合: {preset.suitable_for}"
                            )
                    with gr.Column():
                        gr.Markdown("### 受众级别")
                        for level, info in AUDIENCE_LEVELS.items():
                            gr.Markdown(
                                f"**L{level} - {info['name']}** — "
                                f"速度 {info['speed']}x | {info['detail']} | {info['terms']}"
                            )

        gr.Markdown(
            "---\n"
            "**Math Animation MCP** v0.1.0 | "
            "[GitHub](https://github.com/your-name/math-animation-mcp) | "
            "Powered by ManimCE + MCP"
        )

    return demo


def launch(port: int = 7860, share: bool = False):
    """Launch the Gradio web interface."""
    demo = build_interface()
    demo.launch(server_port=port, share=share)


if __name__ == "__main__":
    launch()
