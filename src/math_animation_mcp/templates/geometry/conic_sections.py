"""圆锥曲线（椭圆、双曲线、抛物线）
Visualization of conic sections: ellipse, hyperbola, parabola.
Keywords: 圆锥曲线, conic sections, 椭圆, ellipse, 双曲线, hyperbola, 抛物线, parabola, 高考
Difficulty: 3
"""
from manim import *
import numpy as np


class ConicSections(Scene):
    def construct(self):
        title = Text("圆锥曲线", font_size=48)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        axes = Axes(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1],
            x_length=7, y_length=5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.3)
        self.play(Create(axes))

        # Ellipse
        ellipse_label = Text("椭圆", font_size=28, color=BLUE).to_corner(UR)
        eq1 = MathTex(r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1", font_size=28, color=BLUE)
        eq1.next_to(ellipse_label, DOWN)

        ellipse = axes.plot_parametric_curve(
            lambda t: np.array([2 * np.cos(t), 1.2 * np.sin(t), 0]),
            t_range=[0, 2 * PI],
            color=BLUE,
        )
        f1 = Dot(axes.c2p(-1.6, 0), color=YELLOW)
        f2 = Dot(axes.c2p(1.6, 0), color=YELLOW)
        f1_label = MathTex("F_1", font_size=20).next_to(f1, DOWN, buff=0.1)
        f2_label = MathTex("F_2", font_size=20).next_to(f2, DOWN, buff=0.1)

        self.play(Write(ellipse_label), Write(eq1))
        self.play(Create(ellipse), FadeIn(f1), FadeIn(f2), Write(f1_label), Write(f2_label))
        self.wait(1.5)
        self.play(FadeOut(ellipse), FadeOut(f1), FadeOut(f2),
                  FadeOut(f1_label), FadeOut(f2_label),
                  FadeOut(ellipse_label), FadeOut(eq1))

        # Parabola
        para_label = Text("抛物线", font_size=28, color=GREEN).to_corner(UR)
        eq2 = MathTex(r"y^2 = 2px", font_size=28, color=GREEN)
        eq2.next_to(para_label, DOWN)

        parabola = axes.plot(lambda x: np.sqrt(2 * x) if x >= 0 else 0,
                             x_range=[0, 3.5], color=GREEN)
        parabola2 = axes.plot(lambda x: -np.sqrt(2 * x) if x >= 0 else 0,
                              x_range=[0, 3.5], color=GREEN)

        self.play(Write(para_label), Write(eq2))
        self.play(Create(parabola), Create(parabola2))
        self.wait(1.5)
        self.play(FadeOut(parabola), FadeOut(parabola2),
                  FadeOut(para_label), FadeOut(eq2))

        # Hyperbola
        hyp_label = Text("双曲线", font_size=28, color=RED).to_corner(UR)
        eq3 = MathTex(r"\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1", font_size=28, color=RED)
        eq3.next_to(hyp_label, DOWN)

        hyp_right = axes.plot_parametric_curve(
            lambda t: np.array([1.5 * np.cosh(t), 1.0 * np.sinh(t), 0]),
            t_range=[-1.5, 1.5], color=RED,
        )
        hyp_left = axes.plot_parametric_curve(
            lambda t: np.array([-1.5 * np.cosh(t), 1.0 * np.sinh(t), 0]),
            t_range=[-1.5, 1.5], color=RED,
        )

        self.play(Write(hyp_label), Write(eq3))
        self.play(Create(hyp_right), Create(hyp_left))
        self.wait(2)
