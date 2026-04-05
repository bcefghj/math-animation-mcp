"""函数图像变换
Function graph transformations: shift, stretch, reflect.
Keywords: 函数, function, 图像变换, transformation, 平移, 伸缩, 翻转
Difficulty: 3
"""
from manim import *
import numpy as np


class FunctionTransformations(Scene):
    def construct(self):
        title = Text("函数图像变换", font_size=48)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))

        axes = Axes(
            x_range=[-5, 5, 1], y_range=[-4, 4, 1],
            x_length=8, y_length=6,
            axis_config={"include_tip": True},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        # Base function
        base = axes.plot(lambda x: x**2, x_range=[-2, 2], color=WHITE)
        base_label = MathTex(r"y = x^2", font_size=28, color=WHITE).to_corner(UR)
        self.play(Create(base), Write(base_label))
        self.wait(1)

        # Vertical shift
        shifted = axes.plot(lambda x: x**2 + 2, x_range=[-2, 2], color=YELLOW)
        shift_label = MathTex(r"y = x^2 + 2", font_size=28, color=YELLOW)
        shift_label.next_to(base_label, DOWN, aligned_edge=RIGHT)
        note = Text("向上平移 2", font_size=24, color=YELLOW).to_edge(DOWN)
        self.play(Create(shifted), Write(shift_label), Write(note))
        self.wait(1)
        self.play(FadeOut(shifted), FadeOut(shift_label), FadeOut(note))

        # Horizontal shift
        h_shifted = axes.plot(lambda x: (x - 1)**2, x_range=[-1, 3], color=GREEN)
        h_label = MathTex(r"y = (x-1)^2", font_size=28, color=GREEN)
        h_label.next_to(base_label, DOWN, aligned_edge=RIGHT)
        h_note = Text("向右平移 1", font_size=24, color=GREEN).to_edge(DOWN)
        self.play(Create(h_shifted), Write(h_label), Write(h_note))
        self.wait(1)
        self.play(FadeOut(h_shifted), FadeOut(h_label), FadeOut(h_note))

        # Vertical stretch
        stretched = axes.plot(lambda x: 2 * x**2, x_range=[-1.5, 1.5], color=RED)
        s_label = MathTex(r"y = 2x^2", font_size=28, color=RED)
        s_label.next_to(base_label, DOWN, aligned_edge=RIGHT)
        s_note = Text("纵向拉伸 2 倍", font_size=24, color=RED).to_edge(DOWN)
        self.play(Create(stretched), Write(s_label), Write(s_note))
        self.wait(1)
        self.play(FadeOut(stretched), FadeOut(s_label), FadeOut(s_note))

        # Reflection
        reflected = axes.plot(lambda x: -(x**2), x_range=[-2, 2], color=BLUE)
        r_label = MathTex(r"y = -x^2", font_size=28, color=BLUE)
        r_label.next_to(base_label, DOWN, aligned_edge=RIGHT)
        r_note = Text("关于 x 轴翻转", font_size=24, color=BLUE).to_edge(DOWN)
        self.play(Create(reflected), Write(r_label), Write(r_note))
        self.wait(2)
