"""正态分布
Normal distribution curve with mean, standard deviation visualization.
Keywords: 正态分布, normal distribution, 高斯, gaussian, 概率, probability, 标准差
Difficulty: 3
"""
from manim import *
import numpy as np


class NormalDistribution(Scene):
    def construct(self):
        title = Text("正态分布", font_size=48)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        axes = Axes(
            x_range=[-4, 4, 1], y_range=[0, 0.5, 0.1],
            x_length=8, y_length=4,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(labels))

        def normal_pdf(x, mu=0, sigma=1):
            return (1 / (sigma * np.sqrt(2 * PI))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

        curve = axes.plot(lambda x: normal_pdf(x), x_range=[-3.5, 3.5], color=BLUE)
        eq = MathTex(
            r"f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}",
            font_size=28, color=BLUE,
        ).to_corner(UR)

        self.play(Create(curve), Write(eq))
        self.wait(1)

        # Show 68-95-99.7 rule
        area_1 = axes.get_area(curve, x_range=[-1, 1], color=GREEN, opacity=0.4)
        label_1 = MathTex(r"68.3\%", font_size=24, color=GREEN).move_to(axes.c2p(0, 0.15))
        self.play(FadeIn(area_1), Write(label_1))
        self.wait(1)

        area_2 = axes.get_area(curve, x_range=[-2, 2], color=YELLOW, opacity=0.25)
        label_2 = MathTex(r"95.4\%", font_size=24, color=YELLOW).move_to(axes.c2p(0, 0.08))
        self.play(FadeIn(area_2), Write(label_2))
        self.wait(1)

        area_3 = axes.get_area(curve, x_range=[-3, 3], color=RED, opacity=0.15)
        label_3 = MathTex(r"99.7\%", font_size=24, color=RED).move_to(axes.c2p(0, 0.03))
        self.play(FadeIn(area_3), Write(label_3))
        self.wait(1)

        # Sigma labels
        for i in range(1, 4):
            for sign in [1, -1]:
                mark = MathTex(rf"{'+' if sign > 0 else '-'}{i}\sigma", font_size=18)
                mark.next_to(axes.c2p(sign * i, 0), DOWN, buff=0.15)
                self.play(Write(mark), run_time=0.3)

        self.wait(2)
