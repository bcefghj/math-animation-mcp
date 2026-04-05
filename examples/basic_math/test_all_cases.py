"""Comprehensive test: render 15 different animation cases."""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from math_animation_mcp.utils.sandbox import render_manim_code

OUTPUT = os.path.join(os.path.dirname(__file__), "animation_output", "test_cases")
os.makedirs(OUTPUT, exist_ok=True)

CASES = {}

# ═══════════════════════════════════════════════════════════════
# Case 1: 欧拉公式 — 数学中最美的公式
# ═══════════════════════════════════════════════════════════════
CASES["01_euler_formula"] = r'''
from manim import *
import numpy as np

class EulerFormula(Scene):
    def construct(self):
        # Title
        title = Text("欧拉公式", font_size=56, color=BLUE)
        subtitle = Text("数学中最美丽的公式", font_size=28, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # The formula
        euler = MathTex(r"e^{i\pi} + 1 = 0", font_size=72)
        self.play(Write(euler), run_time=2)
        self.wait(1)

        # Highlight each part
        parts = [
            (MathTex(r"e", font_size=48, color=RED), "自然常数 e ≈ 2.718", RED),
            (MathTex(r"i", font_size=48, color=GREEN), "虚数单位 i² = -1", GREEN),
            (MathTex(r"\pi", font_size=48, color=YELLOW), "圆周率 π ≈ 3.14159", YELLOW),
            (MathTex(r"1", font_size=48, color=BLUE), "乘法单位元", BLUE),
            (MathTex(r"0", font_size=48, color=PURPLE), "加法单位元", PURPLE),
        ]

        euler_small = euler.copy().scale(0.6).to_edge(UP)
        self.play(Transform(euler, euler_small))

        for i, (sym, desc, color) in enumerate(parts):
            row = VGroup(sym, Text(desc, font_size=24, color=color))
            row.arrange(RIGHT, buff=0.5)
            row.move_to(DOWN * (i * 0.7 - 1))
            self.play(FadeIn(row), run_time=0.6)

        self.wait(1)

        # Unit circle connection
        self.play(*[FadeOut(m) for m in self.mobjects])

        axes = Axes(x_range=[-1.8, 1.8, 0.5], y_range=[-1.8, 1.8, 0.5],
                    x_length=5, y_length=5, axis_config={"include_tip": True})
        circle = Circle(radius=1.5, color=BLUE).move_to(axes.c2p(0, 0))
        self.play(Create(axes), Create(circle))

        # Trace e^(it) path
        angle = ValueTracker(0)
        dot = always_redraw(lambda: Dot(
            axes.c2p(np.cos(angle.get_value()), np.sin(angle.get_value())),
            color=YELLOW, radius=0.08))
        line = always_redraw(lambda: Line(
            axes.c2p(0, 0),
            axes.c2p(np.cos(angle.get_value()), np.sin(angle.get_value())),
            color=YELLOW))
        label = always_redraw(lambda: MathTex(
            rf"e^{{i \cdot {angle.get_value():.1f}}}",
            font_size=28, color=YELLOW
        ).next_to(dot, UR, buff=0.1))

        self.play(FadeIn(dot), Create(line), Write(label))
        self.play(angle.animate.set_value(PI), run_time=3, rate_func=smooth)
        self.wait(0.5)

        # At pi: e^(i*pi) = -1
        result = MathTex(r"e^{i\pi} = -1", font_size=40, color=RED).to_edge(DOWN)
        arrow = Arrow(dot.get_center(), axes.c2p(-1, 0), color=RED, buff=0.1)
        minus_one = MathTex("-1", font_size=28, color=RED).next_to(axes.c2p(-1, 0), DOWN)
        self.play(Write(result), Create(arrow), Write(minus_one))
        self.wait(1)

        final = MathTex(r"e^{i\pi} + 1 = 0", font_size=56, color=GOLD).move_to(ORIGIN)
        box = SurroundingRectangle(final, color=GOLD, buff=0.3)
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.play(Write(final), Create(box))
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 2: 二次函数完全平方配方
# ═══════════════════════════════════════════════════════════════
CASES["02_completing_square"] = r'''
from manim import *
import numpy as np

class CompletingSquare(Scene):
    def construct(self):
        title = Text("配方法解一元二次方程", font_size=44, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        # Original equation
        steps = [
            (r"x^2 + 6x + 5 = 0", WHITE, "原方程"),
            (r"x^2 + 6x = -5", YELLOW, "移项"),
            (r"x^2 + 6x + 9 = -5 + 9", GREEN, "两边加 (6/2)² = 9"),
            (r"(x + 3)^2 = 4", BLUE, "左边配成完全平方"),
            (r"x + 3 = \pm 2", ORANGE, "开方"),
            (r"x_1 = -1, \quad x_2 = -5", RED, "求解"),
        ]

        prev = None
        all_objs = VGroup()
        for i, (latex, color, note) in enumerate(steps):
            eq = MathTex(latex, font_size=36, color=color)
            note_text = Text(note, font_size=20, color=GRAY)
            note_text.next_to(eq, RIGHT, buff=0.5)
            row = VGroup(eq, note_text)
            row.move_to(UP * (1.5 - i * 0.7))

            if prev is None:
                self.play(Write(eq), FadeIn(note_text))
            else:
                self.play(Write(eq), FadeIn(note_text), run_time=0.8)
            self.wait(0.5)
            prev = eq
            all_objs.add(row)

        self.wait(0.5)
        # Show graph
        self.play(all_objs.animate.scale(0.5).to_edge(LEFT, buff=0.3))

        axes = Axes(x_range=[-7, 2, 1], y_range=[-5, 10, 2],
                    x_length=5, y_length=4).to_edge(RIGHT, buff=0.5)
        graph = axes.plot(lambda x: x**2 + 6*x + 5, x_range=[-6.5, 0.5], color=BLUE)
        r1 = Dot(axes.c2p(-1, 0), color=RED, radius=0.08)
        r2 = Dot(axes.c2p(-5, 0), color=RED, radius=0.08)
        l1 = MathTex("x_1=-1", font_size=18, color=RED).next_to(r1, UP)
        l2 = MathTex("x_2=-5", font_size=18, color=RED).next_to(r2, UP)
        vertex = Dot(axes.c2p(-3, -4), color=YELLOW, radius=0.08)
        vl = MathTex("(-3,-4)", font_size=18, color=YELLOW).next_to(vertex, DOWN)

        self.play(Create(axes), Create(graph))
        self.play(FadeIn(r1), FadeIn(r2), Write(l1), Write(l2))
        self.play(FadeIn(vertex), Write(vl))
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 3: 三角函数图像变换
# ═══════════════════════════════════════════════════════════════
CASES["03_trig_transform"] = r'''
from manim import *
import numpy as np

class TrigTransform(Scene):
    def construct(self):
        title = Text("三角函数图像变换", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))

        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/2], y_range=[-2.5, 2.5, 1],
            x_length=10, y_length=5,
            axis_config={"include_tip": True},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        # Base sin(x)
        sin_base = axes.plot(lambda x: np.sin(x), color=WHITE)
        sin_label = MathTex(r"y = \sin x", font_size=24, color=WHITE).to_corner(UR)
        self.play(Create(sin_base), Write(sin_label), run_time=1.5)
        self.wait(1)

        # Amplitude: 2sin(x)
        sin_amp = axes.plot(lambda x: 2*np.sin(x), color=YELLOW)
        amp_label = MathTex(r"y = 2\sin x", font_size=24, color=YELLOW)
        amp_label.next_to(sin_label, DOWN, aligned_edge=RIGHT)
        note1 = Text("振幅变为 2", font_size=20, color=YELLOW).to_edge(DOWN)
        self.play(Create(sin_amp), Write(amp_label), Write(note1))
        self.wait(1)
        self.play(FadeOut(sin_amp), FadeOut(amp_label), FadeOut(note1))

        # Frequency: sin(2x)
        sin_freq = axes.plot(lambda x: np.sin(2*x), color=GREEN)
        freq_label = MathTex(r"y = \sin 2x", font_size=24, color=GREEN)
        freq_label.next_to(sin_label, DOWN, aligned_edge=RIGHT)
        note2 = Text("周期变为 π", font_size=20, color=GREEN).to_edge(DOWN)
        self.play(Create(sin_freq), Write(freq_label), Write(note2))
        self.wait(1)
        self.play(FadeOut(sin_freq), FadeOut(freq_label), FadeOut(note2))

        # Phase: sin(x + pi/3)
        sin_phase = axes.plot(lambda x: np.sin(x + PI/3), color=RED)
        phase_label = MathTex(r"y = \sin(x + \frac{\pi}{3})", font_size=24, color=RED)
        phase_label.next_to(sin_label, DOWN, aligned_edge=RIGHT)
        note3 = Text("向左平移 π/3", font_size=20, color=RED).to_edge(DOWN)
        self.play(Create(sin_phase), Write(phase_label), Write(note3))
        self.wait(1)
        self.play(FadeOut(sin_phase), FadeOut(phase_label), FadeOut(note3))

        # Vertical shift: sin(x) + 1
        sin_shift = axes.plot(lambda x: np.sin(x) + 1, color=PURPLE)
        shift_label = MathTex(r"y = \sin x + 1", font_size=24, color=PURPLE)
        shift_label.next_to(sin_label, DOWN, aligned_edge=RIGHT)
        note4 = Text("向上平移 1", font_size=20, color=PURPLE).to_edge(DOWN)
        self.play(Create(sin_shift), Write(shift_label), Write(note4))
        self.wait(1)
        self.play(FadeOut(sin_shift), FadeOut(shift_label), FadeOut(note4))

        # Combined: 2sin(2x + pi/3) + 1
        sin_all = axes.plot(lambda x: 2*np.sin(2*x + PI/3) + 1, color=GOLD)
        all_label = MathTex(r"y = 2\sin(2x + \frac{\pi}{3}) + 1", font_size=24, color=GOLD)
        all_label.next_to(sin_label, DOWN, aligned_edge=RIGHT)
        note5 = Text("综合变换", font_size=20, color=GOLD).to_edge(DOWN)
        self.play(Create(sin_all), Write(all_label), Write(note5))
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 4: 向量加法的平行四边形法则
# ═══════════════════════════════════════════════════════════════
CASES["04_vector_addition"] = r'''
from manim import *
import numpy as np

class VectorAddition(Scene):
    def construct(self):
        title = Text("向量加法：平行四边形法则", font_size=44, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        plane = NumberPlane(
            x_range=[-1, 7, 1], y_range=[-1, 5, 1],
            x_length=8, y_length=5,
            background_line_style={"stroke_opacity": 0.3},
        ).shift(DOWN*0.3)
        self.play(Create(plane), run_time=1)

        origin = plane.c2p(0, 0)
        a_end = plane.c2p(4, 1)
        b_end = plane.c2p(2, 3)
        sum_end = plane.c2p(6, 4)

        # Vector a
        vec_a = Arrow(origin, a_end, color=RED, buff=0, stroke_width=4)
        label_a = MathTex(r"\vec{a}", font_size=32, color=RED).next_to(vec_a, DOWN, buff=0.1)
        self.play(GrowArrow(vec_a), Write(label_a))
        self.wait(0.5)

        # Vector b
        vec_b = Arrow(origin, b_end, color=BLUE, buff=0, stroke_width=4)
        label_b = MathTex(r"\vec{b}", font_size=32, color=BLUE).next_to(vec_b, LEFT, buff=0.1)
        self.play(GrowArrow(vec_b), Write(label_b))
        self.wait(0.5)

        # Parallelogram
        b_shifted = Arrow(a_end, sum_end, color=BLUE, buff=0, stroke_width=3, stroke_opacity=0.6)
        a_shifted = Arrow(b_end, sum_end, color=RED, buff=0, stroke_width=3, stroke_opacity=0.6)
        dash_b = DashedLine(a_end, sum_end, color=BLUE, stroke_opacity=0.5)
        dash_a = DashedLine(b_end, sum_end, color=RED, stroke_opacity=0.5)

        self.play(Create(dash_b), Create(dash_a))
        self.play(GrowArrow(b_shifted), GrowArrow(a_shifted))
        self.wait(0.5)

        # Fill parallelogram
        parallelogram = Polygon(
            origin, a_end, sum_end, b_end,
            fill_color=YELLOW, fill_opacity=0.15, stroke_opacity=0,
        )
        self.play(FadeIn(parallelogram))

        # Sum vector
        vec_sum = Arrow(origin, sum_end, color=YELLOW, buff=0, stroke_width=5)
        label_sum = MathTex(r"\vec{a} + \vec{b}", font_size=32, color=YELLOW)
        label_sum.next_to(vec_sum.get_center(), UL, buff=0.1)
        self.play(GrowArrow(vec_sum), Write(label_sum))
        self.wait(0.5)

        # Equation
        eq = MathTex(r"\vec{a} + \vec{b} = (4,1) + (2,3) = (6,4)", font_size=28, color=WHITE)
        eq.to_edge(DOWN)
        self.play(Write(eq))
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 5: 极限的 ε-δ 定义
# ═══════════════════════════════════════════════════════════════
CASES["05_epsilon_delta"] = r'''
from manim import *
import numpy as np

class EpsilonDelta(Scene):
    def construct(self):
        title = Text("极限的 ε-δ 定义", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        definition = MathTex(
            r"\forall \varepsilon > 0, \exists \delta > 0 : "
            r"0 < |x - a| < \delta \Rightarrow |f(x) - L| < \varepsilon",
            font_size=26, color=YELLOW,
        ).next_to(title, DOWN, buff=0.3)
        self.play(Write(definition), run_time=2)
        self.wait(1)

        # Graph
        axes = Axes(
            x_range=[-1, 5, 1], y_range=[-1, 5, 1],
            x_length=7, y_length=4.5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(labels))

        func = lambda x: 0.5 * x**2 - 0.5*x + 1
        curve = axes.plot(func, x_range=[0, 4.2], color=BLUE)
        self.play(Create(curve))

        a_val = 2
        L_val = func(a_val)

        # Point (a, L)
        a_dot = Dot(axes.c2p(a_val, L_val), color=YELLOW)
        a_label = MathTex("a", font_size=22).next_to(axes.c2p(a_val, 0), DOWN)
        L_label = MathTex("L", font_size=22).next_to(axes.c2p(0, L_val), LEFT)
        self.play(FadeIn(a_dot), Write(a_label), Write(L_label))

        # Dashed lines to axes
        h_dash = DashedLine(axes.c2p(a_val, 0), axes.c2p(a_val, L_val), color=GRAY, stroke_opacity=0.5)
        v_dash = DashedLine(axes.c2p(0, L_val), axes.c2p(a_val, L_val), color=GRAY, stroke_opacity=0.5)
        self.play(Create(h_dash), Create(v_dash))

        # Epsilon band
        eps = 0.8
        eps_rect = Rectangle(
            width=axes.x_length, height=eps * axes.y_length / 6,
            fill_color=GREEN, fill_opacity=0.15, stroke_color=GREEN, stroke_width=1,
        ).move_to(axes.c2p(2.5, L_val))
        eps_label_top = MathTex(r"L + \varepsilon", font_size=18, color=GREEN)
        eps_label_top.next_to(axes.c2p(0, L_val + eps), LEFT, buff=0.1)
        eps_label_bot = MathTex(r"L - \varepsilon", font_size=18, color=GREEN)
        eps_label_bot.next_to(axes.c2p(0, L_val - eps), LEFT, buff=0.1)
        self.play(FadeIn(eps_rect), Write(eps_label_top), Write(eps_label_bot))
        self.wait(0.5)

        # Delta band
        delta = 0.6
        delta_rect = Rectangle(
            width=delta * 2 * axes.x_length / 6, height=axes.y_length,
            fill_color=RED, fill_opacity=0.1, stroke_color=RED, stroke_width=1,
        ).move_to(axes.c2p(a_val, 2.5))
        d_label_l = MathTex(r"a-\delta", font_size=18, color=RED)
        d_label_l.next_to(axes.c2p(a_val - delta, 0), DOWN, buff=0.1)
        d_label_r = MathTex(r"a+\delta", font_size=18, color=RED)
        d_label_r.next_to(axes.c2p(a_val + delta, 0), DOWN, buff=0.1)
        self.play(FadeIn(delta_rect), Write(d_label_l), Write(d_label_r))
        self.wait(0.5)

        conclusion = Text(
            "当 x 在 δ 范围内时，f(x) 必然在 ε 范围内",
            font_size=22, color=GOLD,
        ).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 6: 矩阵乘法可视化
# ═══════════════════════════════════════════════════════════════
CASES["06_matrix_multiply"] = r'''
from manim import *

class MatrixMultiply(Scene):
    def construct(self):
        title = Text("矩阵乘法", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        # Matrices
        A = MathTex(r"\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}", font_size=36, color=RED)
        times = MathTex(r"\times", font_size=36)
        B = MathTex(r"\begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}", font_size=36, color=BLUE)
        eq = MathTex(r"=", font_size=36)
        C = MathTex(r"\begin{pmatrix} ? & ? \\ ? & ? \end{pmatrix}", font_size=36, color=GREEN)

        expr = VGroup(A, times, B, eq, C).arrange(RIGHT, buff=0.3)
        self.play(Write(A), Write(times), Write(B), Write(eq), Write(C))
        self.wait(1)

        # Move up
        self.play(expr.animate.shift(UP * 1.5).scale(0.8))

        # Step by step
        computations = [
            (r"c_{11} = 1 \times 5 + 2 \times 7 = 5 + 14 = 19", YELLOW),
            (r"c_{12} = 1 \times 6 + 2 \times 8 = 6 + 16 = 22", ORANGE),
            (r"c_{21} = 3 \times 5 + 4 \times 7 = 15 + 28 = 43", TEAL),
            (r"c_{22} = 3 \times 6 + 4 \times 8 = 18 + 32 = 50", PURPLE),
        ]

        for i, (latex, color) in enumerate(computations):
            step = MathTex(latex, font_size=28, color=color)
            step.move_to(DOWN * (i * 0.6 - 0.5))
            self.play(Write(step), run_time=1)
            self.wait(0.3)

        # Final result
        result = MathTex(
            r"\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}"
            r"\begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}"
            r"= \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}",
            font_size=32, color=GOLD,
        ).to_edge(DOWN)
        box = SurroundingRectangle(result, color=GOLD, buff=0.15)
        self.play(Write(result), Create(box))
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 7: 泰勒展开逼近 sin(x)
# ═══════════════════════════════════════════════════════════════
CASES["07_taylor_series"] = r'''
from manim import *
import numpy as np
import math

class TaylorSeries(Scene):
    def construct(self):
        title = Text("Taylor 展开逼近 sin(x)", font_size=44, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/2], y_range=[-2, 2, 1],
            x_length=10, y_length=4.5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.3)
        self.play(Create(axes))

        sin_graph = axes.plot(lambda x: np.sin(x), color=WHITE, stroke_width=3)
        sin_label = MathTex(r"\sin(x)", font_size=24, color=WHITE).to_corner(UL)
        self.play(Create(sin_graph), Write(sin_label))
        self.wait(0.5)

        def taylor_sin(x, n_terms):
            result = 0.0
            for k in range(n_terms):
                result += ((-1)**k * x**(2*k+1)) / math.factorial(2*k+1)
            return float(result)

        colors = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE]
        labels_list = [
            r"T_1: x",
            r"T_3: x - \frac{x^3}{3!}",
            r"T_5: + \frac{x^5}{5!}",
            r"T_7: + \frac{x^7}{7!}",
            r"T_9: + \frac{x^9}{9!}",
            r"T_{11}: + \frac{x^{11}}{11!}",
            r"T_{13}: + \frac{x^{13}}{13!}",
        ]

        prev_graph = None
        for i in range(7):
            n = i + 1
            color = colors[i % len(colors)]
            approx = axes.plot(
                lambda x, n=n: taylor_sin(x, n),
                x_range=[-2*PI, 2*PI],
                color=color, stroke_width=2,
            )
            label = MathTex(labels_list[i], font_size=20, color=color)
            label.to_corner(UR).shift(DOWN * i * 0.35)

            if prev_graph:
                self.play(
                    Transform(prev_graph, approx),
                    FadeIn(label),
                    run_time=0.8,
                )
            else:
                prev_graph = approx
                self.play(Create(approx), FadeIn(label), run_time=1)

            self.wait(0.3)

        conclusion = Text("More terms = better approximation!", font_size=24, color=GOLD).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 8: 概率 — 条件概率贝叶斯公式
# ═══════════════════════════════════════════════════════════════
CASES["08_bayes_theorem"] = r'''
from manim import *

class BayesTheorem(Scene):
    def construct(self):
        title = Text("Bayes Theorem", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        formula = MathTex(
            r"P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}",
            font_size=40, color=YELLOW,
        )
        self.play(Write(formula), run_time=2)
        self.wait(1)
        self.play(formula.animate.shift(UP * 1.5).scale(0.8))

        set_a = Circle(radius=1.2, color=RED, fill_opacity=0.2, fill_color=RED).shift(LEFT * 0.6)
        set_b = Circle(radius=1.2, color=BLUE, fill_opacity=0.2, fill_color=BLUE).shift(RIGHT * 0.6)
        label_a = MathTex("A", font_size=28, color=RED).move_to(LEFT * 1.5)
        label_b = MathTex("B", font_size=28, color=BLUE).move_to(RIGHT * 1.5)

        self.play(Create(set_a), Create(set_b), Write(label_a), Write(label_b))
        self.wait(0.5)

        intersection = Intersection(set_a, set_b, fill_opacity=0.5, fill_color=PURPLE, color=PURPLE)
        ab_label = MathTex(r"A \cap B", font_size=22, color=PURPLE).move_to(intersection.get_center())
        self.play(FadeIn(intersection), Write(ab_label))
        self.wait(1)

        self.play(*[FadeOut(m) for m in [set_a, set_b, label_a, label_b, intersection, ab_label]])

        example_title = Text("Medical Test Example", font_size=28, color=GREEN).shift(UP * 0.3)
        self.play(Write(example_title))

        row1 = VGroup(
            Text("Disease rate:", font_size=18, color=WHITE),
            MathTex(r"P(D) = 0.01", font_size=24),
        ).arrange(RIGHT, buff=0.3)
        row2 = VGroup(
            Text("Sensitivity:", font_size=18, color=WHITE),
            MathTex(r"P(+|D) = 0.95", font_size=24),
        ).arrange(RIGHT, buff=0.3)
        row3 = VGroup(
            Text("False positive:", font_size=18, color=WHITE),
            MathTex(r"P(+|D^c) = 0.05", font_size=24),
        ).arrange(RIGHT, buff=0.3)
        data = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT).next_to(example_title, DOWN, buff=0.3)

        for d in data:
            self.play(FadeIn(d), run_time=0.6)
        self.wait(0.5)

        question = Text("If positive, what is P(Disease)?", font_size=24, color=ORANGE)
        question.next_to(data, DOWN, buff=0.4)
        self.play(Write(question))
        self.wait(0.5)

        answer = MathTex(
            r"P(D|+) = \frac{0.95 \times 0.01}{0.95 \times 0.01 + 0.05 \times 0.99}"
            r"\approx 16.1\%",
            font_size=24, color=GOLD,
        ).next_to(question, DOWN, buff=0.3)
        box = SurroundingRectangle(answer, color=GOLD, buff=0.1)
        self.play(Write(answer), Create(box))
        self.wait(0.5)

        surprise = Text("Only 16% chance of disease even with positive test!", font_size=20, color=RED)
        surprise.to_edge(DOWN)
        self.play(Write(surprise))
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 9: 斐波那契数列与黄金比例
# ═══════════════════════════════════════════════════════════════
CASES["09_fibonacci_golden"] = r'''
from manim import *
import numpy as np

class FibonacciGolden(Scene):
    def construct(self):
        title = Text("Fibonacci & Golden Ratio", font_size=44, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        fib = [1, 1, 2, 3, 5, 8, 13, 21]
        fib_tex = MathTex(
            r"1,\ 1,\ 2,\ 3,\ 5,\ 8,\ 13,\ 21,\ \ldots",
            font_size=36, color=YELLOW,
        )
        self.play(Write(fib_tex))
        self.wait(0.5)

        rule = MathTex(r"F_n = F_{n-1} + F_{n-2}", font_size=30, color=GREEN)
        rule.next_to(fib_tex, DOWN, buff=0.3)
        self.play(Write(rule))
        self.wait(1)

        self.play(fib_tex.animate.shift(UP * 1.5).scale(0.7), rule.animate.shift(UP * 1.5).scale(0.7))

        ratios = []
        for i in range(1, len(fib)):
            ratios.append(fib[i] / fib[i-1])

        axes = Axes(
            x_range=[1, 8, 1], y_range=[1, 2.2, 0.2],
            x_length=7, y_length=3,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.5)
        x_label = MathTex("n", font_size=22).next_to(axes.get_x_axis(), RIGHT, buff=0.1)
        y_label = MathTex(r"\frac{F_n}{F_{n-1}}", font_size=22).next_to(axes.get_y_axis(), UP, buff=0.2)
        self.play(Create(axes), Write(x_label), Write(y_label))

        phi = (1 + np.sqrt(5)) / 2
        golden_line = axes.plot(lambda x: phi, x_range=[1, 8], color=GOLD, stroke_width=2)
        golden_label = MathTex(r"\varphi \approx 1.618", font_size=22, color=GOLD)
        golden_label.next_to(axes.c2p(8, phi), RIGHT, buff=0.1)
        self.play(Create(golden_line), Write(golden_label))

        dots = VGroup()
        for i, r in enumerate(ratios):
            dot = Dot(axes.c2p(i + 2, r), color=RED, radius=0.06)
            dots.add(dot)
            self.play(FadeIn(dot), run_time=0.3)

        points = [axes.c2p(i + 2, r) for i, r in enumerate(ratios)]
        path = VMobject(color=RED, stroke_width=2)
        path.set_points_as_corners(points)
        self.play(Create(path))
        self.wait(0.5)

        conclusion = MathTex(
            r"\lim_{n \to \infty} \frac{F_n}{F_{n-1}} = \varphi = \frac{1+\sqrt{5}}{2}",
            font_size=28, color=GOLD,
        ).to_edge(DOWN)
        box = SurroundingRectangle(conclusion, color=GOLD, buff=0.15)
        self.play(Write(conclusion), Create(box))
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 10: 复数与复平面
# ═══════════════════════════════════════════════════════════════
CASES["10_complex_plane"] = r'''
from manim import *
import numpy as np

class ComplexPlane_Demo(Scene):
    def construct(self):
        title = Text("复数与复平面", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))

        plane = ComplexPlane(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1],
            x_length=8, y_length=6,
        ).add_coordinates()
        self.play(Create(plane), run_time=1.5)

        # Plot z = 3 + 2i
        z1 = 3 + 2j
        dot1 = Dot(plane.n2p(z1), color=RED, radius=0.08)
        label1 = MathTex("z = 3 + 2i", font_size=24, color=RED).next_to(dot1, UR, buff=0.1)
        line1 = Line(plane.n2p(0), plane.n2p(z1), color=RED, stroke_width=2)
        self.play(Create(line1), FadeIn(dot1), Write(label1))
        self.wait(0.5)

        # Modulus
        mod_label = MathTex(r"|z| = \sqrt{3^2 + 2^2} = \sqrt{13}", font_size=22, color=YELLOW)
        mod_label.to_corner(UL)
        self.play(Write(mod_label))

        # Conjugate
        z1_conj = 3 - 2j
        dot_conj = Dot(plane.n2p(z1_conj), color=GREEN, radius=0.08)
        label_conj = MathTex(r"\bar{z} = 3 - 2i", font_size=24, color=GREEN).next_to(dot_conj, DR, buff=0.1)
        line_conj = Line(plane.n2p(0), plane.n2p(z1_conj), color=GREEN, stroke_width=2)
        self.play(Create(line_conj), FadeIn(dot_conj), Write(label_conj))
        self.wait(0.5)

        # Multiplication as rotation: z * i
        z2 = z1 * 1j  # = -2 + 3i
        dot2 = Dot(plane.n2p(z2), color=PURPLE, radius=0.08)
        label2 = MathTex(r"z \cdot i = -2 + 3i", font_size=24, color=PURPLE).next_to(dot2, UL, buff=0.1)
        line2 = Line(plane.n2p(0), plane.n2p(z2), color=PURPLE, stroke_width=2)

        rotate_note = Text("乘以 i = 逆时针旋转 90°", font_size=22, color=PURPLE).to_edge(DOWN)
        arc = Arc(radius=0.8, start_angle=np.angle(z1), angle=PI/2, color=PURPLE).move_to(plane.n2p(0))
        self.play(Create(arc), Create(line2), FadeIn(dot2), Write(label2), Write(rotate_note))
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 11: 二项式定理（杨辉三角）
# ═══════════════════════════════════════════════════════════════
CASES["11_pascal_triangle"] = r'''
from manim import *

class PascalTriangle(Scene):
    def construct(self):
        title = Text("杨辉三角与二项式定理", font_size=44, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        # Build Pascal's triangle
        rows = 7
        triangle_data = [[1]]
        for i in range(1, rows):
            prev = triangle_data[-1]
            new_row = [1]
            for j in range(len(prev) - 1):
                new_row.append(prev[j] + prev[j+1])
            new_row.append(1)
            triangle_data.append(new_row)

        all_entries = VGroup()
        for i, row in enumerate(triangle_data):
            for j, val in enumerate(row):
                entry = Text(str(val), font_size=22, color=YELLOW if val > 1 else WHITE)
                x = (j - len(row) / 2 + 0.5) * 0.7
                y = 1.2 - i * 0.55
                entry.move_to(RIGHT * x + UP * y)
                all_entries.add(entry)

        # Animate row by row
        idx = 0
        for i, row in enumerate(triangle_data):
            row_entries = all_entries[idx:idx+len(row)]
            self.play(*[FadeIn(e) for e in row_entries], run_time=0.5)
            idx += len(row)
            self.wait(0.2)

        self.wait(0.5)

        # Binomial theorem
        theorem = MathTex(
            r"(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k",
            font_size=32, color=GOLD,
        ).to_edge(DOWN, buff=0.8)
        self.play(Write(theorem))
        self.wait(0.5)

        # Example
        example = MathTex(
            r"(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3",
            font_size=28, color=GREEN,
        ).next_to(theorem, DOWN, buff=0.3)
        self.play(Write(example))
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 12: 排序算法对比
# ═══════════════════════════════════════════════════════════════
CASES["12_sort_comparison"] = r'''
from manim import *

class SortComparison(Scene):
    def construct(self):
        title = Text("排序算法时间复杂度", font_size=44, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        # Table of complexities
        data = [
            ("冒泡排序", r"O(n^2)", r"O(n^2)", r"O(1)", RED),
            ("选择排序", r"O(n^2)", r"O(n^2)", r"O(1)", ORANGE),
            ("插入排序", r"O(n)", r"O(n^2)", r"O(1)", YELLOW),
            ("归并排序", r"O(n\log n)", r"O(n\log n)", r"O(n)", GREEN),
            ("快速排序", r"O(n\log n)", r"O(n^2)", r"O(\log n)", TEAL),
            ("堆排序", r"O(n\log n)", r"O(n\log n)", r"O(1)", BLUE),
        ]

        # Headers
        headers = VGroup(
            Text("算法", font_size=20, color=WHITE),
            Text("最好", font_size=20, color=WHITE),
            Text("最坏", font_size=20, color=WHITE),
            Text("空间", font_size=20, color=WHITE),
        ).arrange(RIGHT, buff=1.2).shift(UP * 1.5)
        underline = Line(LEFT * 5, RIGHT * 5, color=GRAY, stroke_width=1).next_to(headers, DOWN, buff=0.1)
        self.play(Write(headers), Create(underline))

        for i, (name, best, worst, space, color) in enumerate(data):
            row = VGroup(
                Text(name, font_size=18, color=color),
                MathTex(best, font_size=22, color=color),
                MathTex(worst, font_size=22, color=color),
                MathTex(space, font_size=22, color=color),
            ).arrange(RIGHT, buff=1.0)
            row.move_to(UP * (0.8 - i * 0.5))
            self.play(FadeIn(row), run_time=0.5)

        self.wait(0.5)

        # Highlight O(n log n) algorithms
        highlight = Text(
            "归并/快排/堆排 是最优的通用排序算法 O(n log n)",
            font_size=22, color=GOLD,
        ).to_edge(DOWN)
        self.play(Write(highlight))
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 13: 微积分基本定理
# ═══════════════════════════════════════════════════════════════
CASES["13_ftc"] = r'''
from manim import *
import numpy as np

class FundamentalTheoremCalculus(Scene):
    def construct(self):
        title = Text("Fundamental Theorem of Calculus", font_size=40, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        theorem = MathTex(
            r"\int_a^b f(x)\,dx = F(b) - F(a)",
            font_size=40, color=YELLOW,
        )
        where = MathTex(r"F'(x) = f(x)", font_size=28, color=GRAY)
        where.next_to(theorem, DOWN, buff=0.2)
        self.play(Write(theorem), run_time=1.5)
        self.play(Write(where))
        self.wait(1)
        self.play(theorem.animate.shift(UP*1.2).scale(0.7), FadeOut(where))

        axes = Axes(
            x_range=[-0.5, 4, 1], y_range=[-0.5, 4, 1],
            x_length=7, y_length=4,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(labels))

        func = lambda x: 0.3*x**2 + 0.5
        curve = axes.plot(func, x_range=[0, 3.5], color=BLUE)
        self.play(Create(curve))

        a, b = 0.5, 3.0

        area = axes.get_area(curve, x_range=[a, b], color=GREEN, opacity=0.4)
        a_line = DashedLine(axes.c2p(a, 0), axes.c2p(a, func(a)), color=RED)
        b_line = DashedLine(axes.c2p(b, 0), axes.c2p(b, func(b)), color=RED)
        a_label = MathTex("a", font_size=22, color=RED).next_to(axes.c2p(a, 0), DOWN)
        b_label = MathTex("b", font_size=22, color=RED).next_to(axes.c2p(b, 0), DOWN)

        self.play(Create(a_line), Create(b_line), Write(a_label), Write(b_label))
        self.play(FadeIn(area))
        self.wait(0.5)

        area_label = MathTex(
            r"\int_a^b f(x)\,dx",
            font_size=24, color=GREEN,
        ).move_to(axes.c2p(1.75, 1.5))
        self.play(Write(area_label))
        self.wait(0.5)

        example = VGroup(
            MathTex(r"f(x) = 0.3x^2 + 0.5", font_size=22, color=BLUE),
            MathTex(r"F(x) = 0.1x^3 + 0.5x + C", font_size=22, color=TEAL),
            MathTex(r"\int_{0.5}^{3} f(x)\,dx = F(3) - F(0.5)", font_size=22, color=YELLOW),
            MathTex(r"= 4.2 - 0.2625 = 3.9375", font_size=22, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.5)

        for line in example:
            self.play(Write(line), run_time=0.6)

        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 14: 物理 — 简谐运动
# ═══════════════════════════════════════════════════════════════
CASES["14_simple_harmonic"] = r'''
from manim import *
import numpy as np

class SimpleHarmonicMotion(Scene):
    def construct(self):
        title = Text("Simple Harmonic Motion", font_size=44, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        pivot = Dot(LEFT * 4 + UP * 1.5, color=WHITE, radius=0.05)
        self.play(FadeIn(pivot))

        eq = MathTex(r"x(t) = A\cos(\omega t + \varphi)", font_size=28, color=YELLOW)
        eq.next_to(title, DOWN, buff=0.2)
        self.play(Write(eq))

        axes = Axes(
            x_range=[0, 4*PI, PI], y_range=[-1.5, 1.5, 0.5],
            x_length=7, y_length=3,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.8)
        t_label = MathTex("t", font_size=22).next_to(axes.get_x_axis(), RIGHT, buff=0.1)
        x_label = MathTex("x(t)", font_size=22).next_to(axes.get_y_axis(), UP, buff=0.1)
        self.play(Create(axes), Write(t_label), Write(x_label))

        t_tracker = ValueTracker(0.01)
        A, omega = 1.0, 1.0

        trace = always_redraw(lambda: axes.plot(
            lambda t: A * np.cos(omega * t),
            x_range=[0, max(0.01, t_tracker.get_value())],
            color=GREEN, stroke_width=3,
        ))

        dot = always_redraw(lambda: Dot(
            axes.c2p(t_tracker.get_value(), A * np.cos(omega * t_tracker.get_value())),
            color=RED, radius=0.08,
        ))

        mass_y = always_redraw(lambda: Dot(
            LEFT * 4 + UP * (A * np.cos(omega * t_tracker.get_value())),
            color=RED, radius=0.12,
        ))
        spring_line = always_redraw(lambda: Line(
            pivot.get_center(),
            LEFT * 4 + UP * (A * np.cos(omega * t_tracker.get_value())),
            color=GRAY, stroke_width=2,
        ))

        self.add(trace, dot, mass_y, spring_line)
        self.play(t_tracker.animate.set_value(4 * PI), run_time=6, rate_func=linear)
        self.wait(0.5)

        energy = VGroup(
            MathTex(r"E_k = \frac{1}{2}mv^2", font_size=22, color=ORANGE),
            MathTex(r"E_p = \frac{1}{2}kx^2", font_size=22, color=TEAL),
            MathTex(r"E = E_k + E_p = C", font_size=22, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(DR, buff=0.3)
        for e in energy:
            self.play(Write(e), run_time=0.5)
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════
# Case 15: 3D — 空间向量与平面方程
# ═══════════════════════════════════════════════════════════════
CASES["15_3d_plane"] = r'''
from manim import *
import numpy as np

class PlaneEquation3D(ThreeDScene):
    def construct(self):
        # 3D axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
            x_length=6, y_length=6, z_length=6,
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(axes), Write(labels))

        # Plane: 2x + 3y + z = 6
        plane_surface = Surface(
            lambda u, v: axes.c2p(u, v, 6 - 2*u - 3*v),
            u_range=[-1, 3], v_range=[-1, 2.5],
            fill_opacity=0.3, fill_color=BLUE,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        self.play(Create(plane_surface), run_time=2)

        # Normal vector
        center = axes.c2p(1, 1, 1)
        normal = Arrow3D(
            start=center,
            end=center + np.array([2, 3, 1]) * 0.5,
            color=RED,
        )
        self.play(Create(normal))

        # Equation label
        eq = MathTex(r"2x + 3y + z = 6", font_size=36, color=YELLOW)
        eq.to_corner(UL)
        self.add_fixed_in_frame_mobjects(eq)
        self.play(Write(eq))

        normal_label = MathTex(r"\vec{n} = (2, 3, 1)", font_size=28, color=RED)
        normal_label.next_to(eq, DOWN, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(normal_label)
        self.play(Write(normal_label))

        # Rotate camera
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.wait(1)
'''


# ═══════════════════════════════════════════════════════════════
# Runner
# ═══════════════════════════════════════════════════════════════
def main():
    total = len(CASES)
    success = 0
    failed = 0
    results = []

    print(f"\n{'='*60}")
    print(f"  Math Animation MCP — 综合渲染测试 ({total} 个案例)")
    print(f"{'='*60}\n")

    for i, (name, code) in enumerate(CASES.items(), 1):
        print(f"[{i}/{total}] 渲染 {name} ...")
        t0 = time.time()
        result = render_manim_code(
            code, quality="low", fmt="mp4",
            output_dir=OUTPUT, timeout=90,
        )
        elapsed = time.time() - t0

        if result.success:
            success += 1
            size_kb = os.path.getsize(result.file_path) / 1024
            print(f"  ✅ 成功 ({elapsed:.1f}s, {size_kb:.0f}KB) → {os.path.basename(result.file_path)}")
            results.append((name, "✅", f"{elapsed:.1f}s", f"{size_kb:.0f}KB"))
        else:
            failed += 1
            err_short = result.error_msg[:120].replace('\n', ' ')
            print(f"  ❌ 失败 ({elapsed:.1f}s) — {err_short}")
            results.append((name, "❌", f"{elapsed:.1f}s", err_short[:60]))

    print(f"\n{'='*60}")
    print(f"  测试结果: {success}/{total} 成功, {failed}/{total} 失败")
    print(f"{'='*60}")
    print(f"\n{'案例':<30s} {'状态':^4s} {'耗时':>8s} {'详情'}")
    print(f"{'-'*70}")
    for name, status, elapsed, detail in results:
        print(f"  {name:<28s} {status:^4s} {elapsed:>8s}  {detail}")
    print()


if __name__ == "__main__":
    main()
