"""一元二次方程求解过程
Step-by-step solution of quadratic equations with visual graph.
Keywords: 一元二次方程, quadratic, 求根公式, 二次函数, 抛物线, parabola
Difficulty: 2
"""
from manim import *
import numpy as np


class QuadraticEquation(Scene):
    def construct(self):
        title = Text("一元二次方程", font_size=48)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        # Show general form
        general = MathTex(r"ax^2 + bx + c = 0", font_size=40)
        self.play(Write(general))
        self.wait(1)

        # Show quadratic formula
        formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            font_size=40, color=YELLOW,
        )
        self.play(Transform(general, formula))
        self.wait(1)
        self.play(general.animate.to_edge(UP, buff=1.2).scale(0.7))

        # Concrete example
        example = MathTex(r"x^2 - 5x + 6 = 0", font_size=36)
        example.next_to(general, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(0.5)

        step1 = MathTex(r"a=1,\ b=-5,\ c=6", font_size=30, color=BLUE)
        step1.next_to(example, DOWN, buff=0.3)
        self.play(Write(step1))
        self.wait(0.5)

        step2 = MathTex(r"\Delta = 25 - 24 = 1", font_size=30, color=GREEN)
        step2.next_to(step1, DOWN, buff=0.3)
        self.play(Write(step2))
        self.wait(0.5)

        step3 = MathTex(r"x_1 = 2,\quad x_2 = 3", font_size=36, color=RED)
        step3.next_to(step2, DOWN, buff=0.3)
        self.play(Write(step3))
        self.wait(0.5)

        # Shift text up and show graph
        text_group = VGroup(general, example, step1, step2, step3)
        self.play(text_group.animate.scale(0.6).to_edge(LEFT, buff=0.3))

        axes = Axes(
            x_range=[-1, 6, 1], y_range=[-2, 5, 1],
            x_length=5, y_length=4,
            axis_config={"include_tip": True},
        ).to_edge(RIGHT, buff=0.5)
        graph = axes.plot(lambda x: x**2 - 5*x + 6, x_range=[-0.5, 5.5], color=BLUE)

        root1 = Dot(axes.c2p(2, 0), color=RED)
        root2 = Dot(axes.c2p(3, 0), color=RED)
        r1_label = MathTex("x_1=2", font_size=20, color=RED).next_to(root1, DOWN)
        r2_label = MathTex("x_2=3", font_size=20, color=RED).next_to(root2, DOWN)

        self.play(Create(axes))
        self.play(Create(graph))
        self.play(FadeIn(root1), FadeIn(root2), Write(r1_label), Write(r2_label))
        self.wait(2)
