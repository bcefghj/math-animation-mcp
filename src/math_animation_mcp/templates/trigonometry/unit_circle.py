"""单位圆与三角函数
Unit circle showing sin, cos values as angle rotates.
Keywords: 单位圆, unit circle, 三角函数, trigonometry, sin, cos, 正弦, 余弦, 高考
Difficulty: 3
"""
from manim import *
import numpy as np


class UnitCircle(Scene):
    def construct(self):
        title = Text("单位圆与三角函数", font_size=48)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))

        # Unit circle on the left
        circle_center = LEFT * 3
        axes_circle = Axes(
            x_range=[-1.5, 1.5, 0.5], y_range=[-1.5, 1.5, 0.5],
            x_length=4, y_length=4,
            axis_config={"include_tip": False, "stroke_width": 1},
        ).move_to(circle_center)

        circle = Circle(radius=1.5, color=WHITE, stroke_width=2).move_to(circle_center)

        # Sine graph on the right
        axes_sin = Axes(
            x_range=[0, 2 * PI + 0.5, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5, y_length=3,
            axis_config={"include_tip": True},
        ).shift(RIGHT * 2.5)

        self.play(Create(axes_circle), Create(circle), Create(axes_sin))

        # Animated angle
        angle_tracker = ValueTracker(0)

        radius_line = always_redraw(lambda: Line(
            circle_center,
            circle_center + 1.5 * np.array([
                np.cos(angle_tracker.get_value()),
                np.sin(angle_tracker.get_value()), 0
            ]),
            color=YELLOW,
        ))

        point = always_redraw(lambda: Dot(
            circle_center + 1.5 * np.array([
                np.cos(angle_tracker.get_value()),
                np.sin(angle_tracker.get_value()), 0
            ]),
            color=RED,
        ))

        # sin projection line
        sin_line = always_redraw(lambda: DashedLine(
            circle_center + 1.5 * np.array([
                np.cos(angle_tracker.get_value()),
                np.sin(angle_tracker.get_value()), 0
            ]),
            circle_center + 1.5 * np.array([
                np.cos(angle_tracker.get_value()), 0, 0
            ]),
            color=GREEN,
        ))

        sin_label = always_redraw(lambda: MathTex(
            rf"\sin\theta = {np.sin(angle_tracker.get_value()):.2f}",
            font_size=24, color=GREEN,
        ).to_corner(UL))

        cos_label = always_redraw(lambda: MathTex(
            rf"\cos\theta = {np.cos(angle_tracker.get_value()):.2f}",
            font_size=24, color=BLUE,
        ).next_to(sin_label, DOWN, aligned_edge=LEFT))

        self.play(Create(radius_line), FadeIn(point), Create(sin_line),
                  Write(sin_label), Write(cos_label))

        # Trace sine curve
        sin_curve = always_redraw(lambda: axes_sin.plot(
            lambda x: np.sin(x),
            x_range=[0, min(angle_tracker.get_value(), 2 * PI)],
            color=GREEN,
        ))
        self.add(sin_curve)

        self.play(angle_tracker.animate.set_value(2 * PI), run_time=6, rate_func=linear)
        self.wait(1)
