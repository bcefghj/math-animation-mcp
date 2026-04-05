"""导数的几何意义——切线
Geometric meaning of derivative: tangent line sliding along a curve.
Keywords: 导数, derivative, 切线, tangent, 斜率, slope, 几何意义, 高考
Difficulty: 3
"""
from manim import *
import numpy as np


class DerivativeTangent(Scene):
    def construct(self):
        title = Text("导数的几何意义", font_size=48)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        axes = Axes(
            x_range=[-1, 5, 1], y_range=[-1, 8, 1],
            x_length=7, y_length=5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        func = lambda x: 0.3 * x**2
        curve = axes.plot(func, x_range=[0, 4.5], color=BLUE)
        curve_label = MathTex(r"f(x) = 0.3x^2", font_size=28, color=BLUE).to_corner(UR)
        self.play(Create(curve), Write(curve_label))
        self.wait(0.5)

        # Animated tangent line
        x_tracker = ValueTracker(1)

        dot = always_redraw(lambda: Dot(
            axes.c2p(x_tracker.get_value(), func(x_tracker.get_value())),
            color=YELLOW,
        ))

        tangent = always_redraw(lambda: axes.plot(
            lambda x: (0.6 * x_tracker.get_value()) * (x - x_tracker.get_value()) + func(x_tracker.get_value()),
            x_range=[max(-0.5, x_tracker.get_value() - 2), min(5, x_tracker.get_value() + 2)],
            color=RED,
        ))

        slope_text = always_redraw(lambda: MathTex(
            rf"f'({x_tracker.get_value():.1f}) = {0.6 * x_tracker.get_value():.2f}",
            font_size=28, color=RED,
        ).to_corner(DR))

        self.play(FadeIn(dot), Create(tangent), Write(slope_text))
        self.wait(0.5)

        self.play(x_tracker.animate.set_value(4), run_time=4, rate_func=smooth)
        self.wait(0.5)
        self.play(x_tracker.animate.set_value(0.5), run_time=3, rate_func=smooth)
        self.wait(1)

        conclusion = MathTex(
            r"f'(x_0) = \lim_{h \to 0} \frac{f(x_0+h) - f(x_0)}{h}",
            font_size=32, color=YELLOW,
        ).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)
