"""定积分与面积
Definite integral as area under a curve, with Riemann sum visualization.
Keywords: 积分, integral, 面积, area, 黎曼和, Riemann sum, 定积分
Difficulty: 3
"""
from manim import *
import numpy as np


class IntegralArea(Scene):
    def construct(self):
        title = Text("定积分与面积", font_size=48)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        axes = Axes(
            x_range=[-0.5, 4, 1], y_range=[-0.5, 5, 1],
            x_length=7, y_length=5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.3)
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        func = lambda x: 0.5 * x**2 + 0.5
        curve = axes.plot(func, x_range=[0, 3.5], color=BLUE)
        self.play(Create(curve))

        # Riemann sum with increasing rectangles
        n_tracker = ValueTracker(4)

        def get_riemann_rects():
            n = int(n_tracker.get_value())
            return axes.get_riemann_rectangles(
                curve, x_range=[0.5, 3], dx=2.5 / n,
                color=[BLUE, GREEN], fill_opacity=0.5,
            )

        rects = always_redraw(get_riemann_rects)
        n_label = always_redraw(lambda: MathTex(
            f"n = {int(n_tracker.get_value())}",
            font_size=28, color=YELLOW,
        ).to_corner(UR))

        self.play(Create(rects), Write(n_label))
        self.wait(1)

        # Increase number of rectangles
        for target_n in [8, 16, 32]:
            self.play(n_tracker.animate.set_value(target_n), run_time=1.5)
            self.wait(0.5)

        # Show the integral
        area = axes.get_area(curve, x_range=[0.5, 3], color=GREEN, opacity=0.4)
        self.play(FadeOut(rects), FadeIn(area))

        integral = MathTex(
            r"\int_{0.5}^{3} (0.5x^2 + 0.5)\, dx",
            font_size=32, color=YELLOW,
        ).to_edge(DOWN)
        self.play(Write(integral))
        self.wait(2)
