"""勾股定理可视化证明
Animated proof of the Pythagorean theorem using area rearrangement.
Keywords: 勾股定理, pythagorean, 直角三角形, right triangle, 证明, proof
Difficulty: 2
"""
from manim import *


class PythagoreanTheorem(Scene):
    def construct(self):
        title = Text("勾股定理", font_size=48)
        subtitle = MathTex(r"a^2 + b^2 = c^2", font_size=36)
        subtitle.next_to(title, DOWN)
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        a, b = 3, 4
        triangle = Polygon(
            ORIGIN, RIGHT * a, RIGHT * a + UP * b,
            color=WHITE, fill_opacity=0.3, fill_color=BLUE,
        )
        label_a = MathTex("a", color=YELLOW).next_to(triangle, DOWN)
        label_b = MathTex("b", color=GREEN).next_to(triangle, RIGHT)
        label_c = MathTex("c", color=RED).move_to(
            (ORIGIN + RIGHT * a + UP * b) / 2 + LEFT * 0.3 + UP * 0.3
        )

        self.play(Create(triangle))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)

        sq_a = Square(side_length=a * 0.4, color=YELLOW, fill_opacity=0.3, fill_color=YELLOW)
        sq_a.next_to(triangle, DOWN, buff=0.1).align_to(triangle, LEFT)
        sq_a_label = MathTex("a^2", color=YELLOW, font_size=30).move_to(sq_a)

        sq_b = Square(side_length=b * 0.4, color=GREEN, fill_opacity=0.3, fill_color=GREEN)
        sq_b.next_to(triangle, RIGHT, buff=0.1).align_to(triangle, DOWN)
        sq_b_label = MathTex("b^2", color=GREEN, font_size=30).move_to(sq_b)

        self.play(Create(sq_a), Write(sq_a_label))
        self.play(Create(sq_b), Write(sq_b_label))
        self.wait(1)

        c_len = (a**2 + b**2) ** 0.5
        sq_c = Square(side_length=c_len * 0.4, color=RED, fill_opacity=0.3, fill_color=RED)
        sq_c.move_to(UP * 2)
        sq_c_label = MathTex("c^2", color=RED, font_size=30).move_to(sq_c)

        equation = MathTex(r"a^2", "+", r"b^2", "=", r"c^2", font_size=48)
        equation[0].set_color(YELLOW)
        equation[2].set_color(GREEN)
        equation[4].set_color(RED)
        equation.to_edge(DOWN)

        self.play(Create(sq_c), Write(sq_c_label))
        self.play(Write(equation))
        self.wait(2)
