"""Long, complex animation test cases — full teaching-style explanations."""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from math_animation_mcp.utils.sandbox import render_manim_code

OUTPUT = os.path.join(os.path.dirname(__file__), "animation_output", "long_cases")
os.makedirs(OUTPUT, exist_ok=True)

CASES = {}

# ═══════════════════════════════════════════════════════════════════════════════
# Case 1: 高考题 — 导数压轴题完整讲解
# 2024高考风格：讨论函数单调性、极值、不等式证明
# ═══════════════════════════════════════════════════════════════════════════════
CASES["01_gaokao_derivative"] = r'''
from manim import *
import numpy as np

class GaokaoDerivative(Scene):
    def construct(self):
        # ── 题目展示 ──
        problem_title = Text("2024 高考数学压轴题", font_size=40, color=GOLD)
        problem_title.to_edge(UP)
        self.play(Write(problem_title))

        problem_box = Rectangle(width=12, height=2.5, color=WHITE, stroke_width=1)
        problem_box.next_to(problem_title, DOWN, buff=0.3)
        p1 = MathTex(r"f(x) = x - 1 - a\ln x \quad (a \in \mathbb{R})", font_size=28)
        p2 = Text("(1) 讨论 f(x) 的单调性", font_size=22)
        p3 = Text("(2) 当 a=1 时，证明 f(x) >= 0", font_size=22)
        prob_group = VGroup(p1, p2, p3).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        prob_group.move_to(problem_box.get_center())
        self.play(Create(problem_box), Write(prob_group), run_time=2)
        self.wait(2)

        # ── 第(1)题：求导 ──
        self.play(FadeOut(problem_box), FadeOut(prob_group),
                  problem_title.animate.scale(0.5).to_corner(UL))

        step1_title = Text("Step 1: Derivative", font_size=32, color=BLUE)
        step1_title.to_edge(UP)
        self.play(Write(step1_title))

        deriv_steps = VGroup(
            MathTex(r"f(x) = x - 1 - a\ln x, \quad x > 0", font_size=28),
            MathTex(r"f'(x) = 1 - \frac{a}{x} = \frac{x - a}{x}", font_size=28, color=YELLOW),
        ).arrange(DOWN, buff=0.3).next_to(step1_title, DOWN, buff=0.5)
        for s in deriv_steps:
            self.play(Write(s), run_time=1)
            self.wait(0.5)

        # ── 分类讨论 ──
        step2_title = Text("Step 2: Classification", font_size=28, color=GREEN)
        step2_title.next_to(deriv_steps, DOWN, buff=0.5)
        self.play(Write(step2_title))

        cases = VGroup(
            VGroup(
                MathTex(r"\text{Case 1: } a \le 0", font_size=24, color=RED),
                MathTex(r"f'(x) = \frac{x-a}{x} > 0 \;\forall\; x>0", font_size=22),
                Text("f(x) monotonically increasing on (0, +inf)", font_size=18, color=GRAY),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            VGroup(
                MathTex(r"\text{Case 2: } a > 0", font_size=24, color=BLUE),
                MathTex(r"f'(x) = 0 \Rightarrow x = a", font_size=22),
                MathTex(r"x \in (0, a): f'(x)<0 \;\text{decreasing}", font_size=20, color=ORANGE),
                MathTex(r"x \in (a, +\infty): f'(x)>0 \;\text{increasing}", font_size=20, color=GREEN),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).next_to(step2_title, DOWN, buff=0.3)

        for case in cases:
            for line in case:
                self.play(Write(line), run_time=0.6)
            self.wait(0.5)
        self.wait(1)

        # ── 图形验证：a>0 的情况 ──
        self.play(*[FadeOut(m) for m in self.mobjects])
        graph_title = Text("Visual Verification: a = 1", font_size=32, color=BLUE).to_edge(UP)
        self.play(Write(graph_title))

        axes = Axes(
            x_range=[0.01, 5, 1], y_range=[-2, 3, 1],
            x_length=8, y_length=5,
            axis_config={"include_tip": True},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        f_graph = axes.plot(lambda x: x - 1 - np.log(x), x_range=[0.1, 4.5], color=BLUE)
        f_label = MathTex(r"f(x) = x - 1 - \ln x", font_size=24, color=BLUE).to_corner(UR)
        self.play(Create(f_graph), Write(f_label), run_time=1.5)

        fp_graph = axes.plot(lambda x: 1 - 1/x, x_range=[0.15, 4.5], color=YELLOW)
        fp_label = MathTex(r"f'(x) = 1 - \frac{1}{x}", font_size=24, color=YELLOW)
        fp_label.next_to(f_label, DOWN, aligned_edge=RIGHT)
        self.play(Create(fp_graph), Write(fp_label), run_time=1.5)
        self.wait(0.5)

        # Mark critical point x=1
        crit_dot = Dot(axes.c2p(1, 0), color=RED, radius=0.1)
        crit_label = MathTex(r"x=1: f(1)=0", font_size=22, color=RED).next_to(crit_dot, DOWN+RIGHT)
        self.play(FadeIn(crit_dot), Write(crit_label))
        self.wait(0.5)

        # Decreasing and increasing arrows
        dec_arrow = Arrow(axes.c2p(0.4, 1.5), axes.c2p(0.8, 0.3), color=ORANGE, stroke_width=3)
        inc_arrow = Arrow(axes.c2p(1.5, 0.1), axes.c2p(3, 1.5), color=GREEN, stroke_width=3)
        dec_text = Text("Decreasing", font_size=16, color=ORANGE).next_to(dec_arrow, LEFT)
        inc_text = Text("Increasing", font_size=16, color=GREEN).next_to(inc_arrow, RIGHT)
        self.play(GrowArrow(dec_arrow), Write(dec_text))
        self.play(GrowArrow(inc_arrow), Write(inc_text))
        self.wait(1)

        # ── 第(2)题：证明 f(x) >= 0 ──
        self.play(*[FadeOut(m) for m in self.mobjects])
        proof_title = Text("Step 3: Prove f(x) >= 0 when a = 1", font_size=32, color=GOLD)
        proof_title.to_edge(UP)
        self.play(Write(proof_title))

        proof_lines = VGroup(
            MathTex(r"f(x) = x - 1 - \ln x, \quad x > 0", font_size=26),
            MathTex(r"f'(x) = \frac{x-1}{x}", font_size=26, color=YELLOW),
            MathTex(r"f'(x) = 0 \Rightarrow x = 1", font_size=26, color=GREEN),
            MathTex(r"f''(x) = \frac{1}{x^2} > 0 \;\;\text{(convex)}", font_size=26, color=TEAL),
            MathTex(r"\Rightarrow x = 1 \text{ is global minimum}", font_size=26, color=ORANGE),
            MathTex(r"f(1) = 1 - 1 - \ln 1 = 0", font_size=28, color=RED),
            MathTex(r"\therefore f(x) \ge f(1) = 0, \quad \forall x > 0", font_size=28, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(proof_title, DOWN, buff=0.5)

        for i, line in enumerate(proof_lines):
            self.play(Write(line), run_time=0.8)
            self.wait(0.3)

        # QED box
        qed = MathTex(r"\blacksquare", font_size=40, color=GOLD).next_to(proof_lines, RIGHT, buff=0.5).align_to(proof_lines[-1], DOWN)
        box = SurroundingRectangle(proof_lines[-1], color=GOLD, buff=0.15)
        self.play(Write(qed), Create(box))
        self.wait(3)
'''

# ═══════════════════════════════════════════════════════════════════════════════
# Case 2: 立体几何 — 正方体截面 + 二面角计算
# ═══════════════════════════════════════════════════════════════════════════════
CASES["02_solid_geometry"] = r'''
from manim import *
import numpy as np

class SolidGeometry(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES, theta=-40*DEGREES)

        # ── Title (fixed in frame) ──
        title = Text("Solid Geometry: Cube Cross-Section", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        # ── Build a cube ──
        a = 2
        vertices = {
            'A': np.array([0,0,0]),  'B': np.array([a,0,0]),
            'C': np.array([a,a,0]),  'D': np.array([0,a,0]),
            'E': np.array([0,0,a]),  'F': np.array([a,0,a]),
            'G': np.array([a,a,a]),  'H': np.array([0,a,a]),
        }

        edges = [
            ('A','B'), ('B','C'), ('C','D'), ('D','A'),
            ('E','F'), ('F','G'), ('G','H'), ('H','E'),
            ('A','E'), ('B','F'), ('C','G'), ('D','H'),
        ]

        cube_lines = VGroup()
        for v1, v2 in edges:
            line = Line3D(vertices[v1], vertices[v2], color=WHITE, thickness=0.02)
            cube_lines.add(line)

        vert_dots = VGroup()
        vert_labels = VGroup()
        for name, pos in vertices.items():
            dot = Dot3D(pos, color=YELLOW, radius=0.05)
            vert_dots.add(dot)
            label = Text(name, font_size=16, color=YELLOW)
            self.add_fixed_orientation_mobjects(label)
            label.next_to(dot, normalize(pos - np.array([a/2, a/2, a/2])) * 0.3)
            vert_labels.add(label)

        self.play(Create(cube_lines), run_time=2)
        self.play(FadeIn(vert_dots), FadeIn(vert_labels))
        self.wait(1)

        # ── Cross section: midpoints of AB, BC, EH ──
        M = (vertices['A'] + vertices['B']) / 2
        N = (vertices['B'] + vertices['C']) / 2
        P = (vertices['E'] + vertices['H']) / 2

        for point, name, color in [(M, "M", RED), (N, "N", GREEN), (P, "P", BLUE)]:
            dot = Dot3D(point, color=color, radius=0.08)
            label = Text(name, font_size=18, color=color)
            self.add_fixed_orientation_mobjects(label)
            label.next_to(dot, UP + RIGHT, buff=0.1)
            self.play(FadeIn(dot), FadeIn(label), run_time=0.5)

        # Draw the cross-section triangle
        triangle = Polygon(
            M, N, P,
            fill_color=ORANGE, fill_opacity=0.4,
            stroke_color=ORANGE, stroke_width=2,
        )
        self.play(Create(triangle), run_time=1.5)
        self.wait(1)

        # ── Rotate to see from different angles ──
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        # ── Area calculation (fixed in frame) ──
        calc_title = Text("Area Calculation", font_size=28, color=GOLD)
        calc_title.to_corner(DL)
        self.add_fixed_in_frame_mobjects(calc_title)
        self.play(Write(calc_title))

        MN = N - M
        MP = P - M
        cross = np.cross(MN, MP)
        area = np.linalg.norm(cross) / 2

        calc = VGroup(
            MathTex(r"\vec{MN} = (1, 1, 0)", font_size=20, color=GREEN),
            MathTex(r"\vec{MP} = (-1, 0, 2)", font_size=20, color=BLUE),
            MathTex(r"\vec{MN} \times \vec{MP} = (2, -2, 1)", font_size=20, color=ORANGE),
            MathTex(rf"S = \frac{{1}}{{2}}|\vec{{MN}} \times \vec{{MP}}| = \frac{{3}}{{2}}", font_size=20, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(calc_title, DOWN, aligned_edge=LEFT, buff=0.2)

        for c in calc:
            self.add_fixed_in_frame_mobjects(c)
            self.play(Write(c), run_time=0.6)

        self.wait(1)

        # Normal vectors for dihedral angle
        n_title = Text("Dihedral Angle", font_size=28, color=PURPLE)
        n_title.to_corner(DR)
        self.add_fixed_in_frame_mobjects(n_title)
        self.play(Write(n_title))

        n1 = np.array([0, 0, 1])  # bottom face normal
        n2 = cross / np.linalg.norm(cross)  # section normal
        cos_angle = abs(np.dot(n1, n2))
        angle_deg = np.degrees(np.arccos(cos_angle))

        angle_text = MathTex(
            rf"\theta = \arccos\left(\frac{{|n_1 \cdot n_2|}}{{|n_1||n_2|}}\right) \approx {angle_deg:.1f}^\circ",
            font_size=20, color=PURPLE,
        ).next_to(n_title, DOWN, aligned_edge=RIGHT, buff=0.2)
        self.add_fixed_in_frame_mobjects(angle_text)
        self.play(Write(angle_text))

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait(2)
'''

# ═══════════════════════════════════════════════════════════════════════════════
# Case 3: 高考函数题 — 含参数的函数讨论
# ═══════════════════════════════════════════════════════════════════════════════
CASES["03_gaokao_function"] = r'''
from manim import *
import numpy as np

class GaokaoFunction(Scene):
    def construct(self):
        # ── Problem Statement ──
        title = Text("Function with Parameter", font_size=40, color=GOLD).to_edge(UP)
        self.play(Write(title))

        problem = VGroup(
            MathTex(r"f(x) = e^x - ax - 1", font_size=32),
            Text("(1) Find the range of a such that f(x) >= 0 for all x", font_size=20),
            Text("(2) When a = e, find the minimum value of f(x)", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.4)
        for p in problem:
            self.play(Write(p), run_time=0.8)
        self.wait(1.5)

        # ── Part (1): Derivative analysis ──
        self.play(*[FadeOut(m) for m in self.mobjects])
        part1 = Text("Part (1): f(x) >= 0 for all x", font_size=32, color=BLUE).to_edge(UP)
        self.play(Write(part1))

        analysis = VGroup(
            MathTex(r"f'(x) = e^x - a", font_size=28),
            MathTex(r"f'(x) = 0 \Rightarrow x = \ln a \;\;(a > 0)", font_size=28, color=YELLOW),
            MathTex(r"f_{\min} = f(\ln a) = a - a\ln a - 1", font_size=28, color=GREEN),
            MathTex(r"f(x) \ge 0 \;\forall x \;\Leftrightarrow\; a - a\ln a - 1 \ge 0", font_size=26, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(part1, DOWN, buff=0.5)

        for a in analysis:
            self.play(Write(a), run_time=1)
            self.wait(0.4)
        self.wait(1)

        # Let g(a) = a - a*ln(a) - 1
        self.play(*[FadeOut(m) for m in self.mobjects[1:]])

        g_title = Text("Let g(a) = a - a*ln(a) - 1", font_size=26, color=TEAL)
        g_title.next_to(part1, DOWN, buff=0.3)
        self.play(Write(g_title))

        g_analysis = VGroup(
            MathTex(r"g'(a) = 1 - \ln a - 1 = -\ln a", font_size=26),
            MathTex(r"g'(a) = 0 \Rightarrow a = 1", font_size=26, color=YELLOW),
            MathTex(r"g'(a) > 0 \text{ when } a < 1,\quad g'(a) < 0 \text{ when } a > 1", font_size=22, color=ORANGE),
            MathTex(r"g_{\max} = g(1) = 1 - 0 - 1 = 0", font_size=26, color=RED),
            MathTex(r"\therefore g(a) \le 0, \text{ equality iff } a = 1", font_size=26, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(g_title, DOWN, buff=0.3)

        for g in g_analysis:
            self.play(Write(g), run_time=0.8)
            self.wait(0.3)

        conclusion1 = MathTex(
            r"\boxed{a = 1 \text{ is the only value where } f(x) \ge 0 \;\forall x}",
            font_size=26, color=GOLD,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(conclusion1))
        self.wait(2)

        # ── Part (2): a = e, graph + min value ──
        self.play(*[FadeOut(m) for m in self.mobjects])
        part2 = Text("Part (2): a = e, find minimum", font_size=32, color=BLUE).to_edge(UP)
        self.play(Write(part2))

        axes = Axes(
            x_range=[-2, 4, 1], y_range=[-4, 8, 2],
            x_length=8, y_length=5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.3)
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        e = np.e
        f_graph = axes.plot(lambda x: np.exp(x) - e*x - 1, x_range=[-1.5, 3.5], color=BLUE)
        f_label = MathTex(r"f(x) = e^x - ex - 1", font_size=24, color=BLUE).to_corner(UR)
        self.play(Create(f_graph), Write(f_label), run_time=1.5)

        # Critical point
        crit_x = 1  # ln(e) = 1
        crit_y = np.exp(1) - e*1 - 1  # = e - e - 1 = -1
        crit_dot = Dot(axes.c2p(crit_x, crit_y), color=RED, radius=0.1)
        crit_label = MathTex(r"(1, -1)", font_size=22, color=RED).next_to(crit_dot, DOWN+LEFT)
        self.play(FadeIn(crit_dot), Write(crit_label))

        # Dashed lines
        h_dash = DashedLine(axes.c2p(0, crit_y), axes.c2p(crit_x, crit_y), color=RED, stroke_opacity=0.5)
        v_dash = DashedLine(axes.c2p(crit_x, 0), axes.c2p(crit_x, crit_y), color=RED, stroke_opacity=0.5)
        self.play(Create(h_dash), Create(v_dash))

        min_calc = VGroup(
            MathTex(r"f'(x) = e^x - e = 0 \Rightarrow x = 1", font_size=22, color=YELLOW),
            MathTex(r"f''(1) = e > 0 \;\text{(minimum)}", font_size=22, color=GREEN),
            MathTex(r"f(1) = e - e - 1 = -1", font_size=24, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(LEFT, buff=0.3).shift(DOWN * 1.5)

        for m in min_calc:
            self.play(Write(m), run_time=0.8)
            self.wait(0.3)

        result = MathTex(r"\boxed{f_{\min} = -1}", font_size=36, color=GOLD)
        result.next_to(min_calc, DOWN, buff=0.3)
        box = SurroundingRectangle(result, color=GOLD, buff=0.1)
        self.play(Write(result), Create(box))
        self.wait(3)
'''

# ═══════════════════════════════════════════════════════════════════════════════
# Case 4: 高考数列题 — 递推数列 + 数学归纳法
# ═══════════════════════════════════════════════════════════════════════════════
CASES["04_gaokao_sequence"] = r'''
from manim import *
import numpy as np

class GaokaoSequence(Scene):
    def construct(self):
        title = Text("Sequence & Mathematical Induction", font_size=36, color=GOLD).to_edge(UP)
        self.play(Write(title))

        problem = VGroup(
            MathTex(r"a_1 = 1, \quad a_{n+1} = \frac{a_n}{2a_n + 1}", font_size=28),
            Text("(1) Find the general formula for a_n", font_size=22),
            Text("(2) Prove: a_1 + a_2 + ... + a_n < 1", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.3)
        for p in problem:
            self.play(Write(p), run_time=0.8)
        self.wait(1.5)

        # ── Part 1: Take reciprocal ──
        self.play(*[FadeOut(m) for m in self.mobjects])
        part1 = Text("Part (1): Find general formula", font_size=32, color=BLUE).to_edge(UP)
        self.play(Write(part1))

        steps = VGroup(
            MathTex(r"\frac{1}{a_{n+1}} = \frac{2a_n + 1}{a_n} = 2 + \frac{1}{a_n}", font_size=28, color=YELLOW),
            MathTex(r"\text{Let } b_n = \frac{1}{a_n}, \;\text{then } b_{n+1} = b_n + 2", font_size=28, color=GREEN),
            MathTex(r"b_1 = \frac{1}{a_1} = 1", font_size=28),
            MathTex(r"\Rightarrow b_n = 1 + 2(n-1) = 2n - 1", font_size=28, color=ORANGE),
            MathTex(r"\therefore a_n = \frac{1}{2n - 1}", font_size=32, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(part1, DOWN, buff=0.5)

        for s in steps:
            self.play(Write(s), run_time=1)
            self.wait(0.5)

        box1 = SurroundingRectangle(steps[-1], color=GOLD, buff=0.1)
        self.play(Create(box1))
        self.wait(1.5)

        # ── Verify with values ──
        self.play(*[FadeOut(m) for m in self.mobjects])
        verify_title = Text("Verification", font_size=32, color=TEAL).to_edge(UP)
        self.play(Write(verify_title))

        table_header = VGroup(
            MathTex("n", font_size=24, color=WHITE),
            MathTex("a_n = \\frac{1}{2n-1}", font_size=24, color=YELLOW),
            MathTex("S_n", font_size=24, color=GREEN),
        ).arrange(RIGHT, buff=1.5).next_to(verify_title, DOWN, buff=0.5)
        underline = Line(LEFT*5, RIGHT*5, color=GRAY).next_to(table_header, DOWN, buff=0.1)
        self.play(Write(table_header), Create(underline))

        cumsum = 0
        for n in range(1, 9):
            an = 1.0 / (2*n - 1)
            cumsum += an
            row = VGroup(
                MathTex(str(n), font_size=22),
                MathTex(f"\\frac{{1}}{{{2*n-1}}} \\approx {an:.4f}", font_size=20, color=YELLOW),
                MathTex(f"{cumsum:.4f}", font_size=20, color=GREEN),
            ).arrange(RIGHT, buff=1.2).shift(DOWN * (n * 0.38 - 0.3))
            self.play(FadeIn(row), run_time=0.3)

        bound = Text("S_n < 1 for all n (approaches ~1.5 slowly)", font_size=20, color=RED)
        bound.to_edge(DOWN)
        self.play(Write(bound))
        self.wait(1)

        # ── Part 2: Prove S_n < 1 ──
        self.play(*[FadeOut(m) for m in self.mobjects])
        part2 = Text("Part (2): Prove S_n < 1", font_size=32, color=BLUE).to_edge(UP)
        self.play(Write(part2))

        proof = VGroup(
            MathTex(r"S_n = \sum_{k=1}^{n} \frac{1}{2k-1}", font_size=26),
            MathTex(r"\frac{1}{2k-1} < \frac{1}{2(k-1)} \;\text{for } k \ge 2", font_size=26, color=YELLOW),
            MathTex(r"S_n < 1 + \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^{n-1}}", font_size=26, color=ORANGE),
            MathTex(r"= 1 + \frac{1 - (1/2)^{n-1}}{1 - 1/2}", font_size=26, color=GREEN),
            MathTex(r"< 1 + 1 = 2", font_size=26, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(part2, DOWN, buff=0.5)

        for p in proof:
            self.play(Write(p), run_time=0.8)
            self.wait(0.3)

        # Actually use a tighter bound
        note = Text("(Actually S_n < 1 needs the sharper bound 1/(2k-1) < 1/(2k-2) - 1/(2k))",
                     font_size=16, color=GRAY).to_edge(DOWN)
        self.play(Write(note))
        self.wait(3)
'''

# ═══════════════════════════════════════════════════════════════════════════════
# Case 5: 物理 — 抛体运动完整分析
# ═══════════════════════════════════════════════════════════════════════════════
CASES["05_physics_projectile"] = r'''
from manim import *
import numpy as np

class ProjectileMotion(Scene):
    def construct(self):
        title = Text("Projectile Motion Analysis", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # ── Setup ──
        params = VGroup(
            MathTex(r"v_0 = 20\,\text{m/s}", font_size=24),
            MathTex(r"\theta = 45^\circ", font_size=24),
            MathTex(r"g = 9.8\,\text{m/s}^2", font_size=24),
        ).arrange(RIGHT, buff=1).next_to(title, DOWN, buff=0.3)
        self.play(Write(params))
        self.wait(1)

        # ── Equations ──
        eqs = VGroup(
            MathTex(r"x(t) = v_0 \cos\theta \cdot t", font_size=24, color=YELLOW),
            MathTex(r"y(t) = v_0 \sin\theta \cdot t - \frac{1}{2}gt^2", font_size=24, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(params, DOWN, buff=0.3)
        for eq in eqs:
            self.play(Write(eq), run_time=0.8)
        self.wait(1)

        self.play(*[FadeOut(m) for m in [params, eqs]])

        # ── Trajectory ──
        v0 = 20
        theta = np.radians(45)
        g = 9.8
        T = 2 * v0 * np.sin(theta) / g
        R = v0**2 * np.sin(2*theta) / g
        H = (v0 * np.sin(theta))**2 / (2*g)

        axes = Axes(
            x_range=[0, 45, 5], y_range=[0, 12, 2],
            x_length=10, y_length=5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.5)
        x_lab = MathTex("x", font_size=20).next_to(axes.get_x_axis(), RIGHT)
        y_lab = MathTex("y", font_size=20).next_to(axes.get_y_axis(), UP)
        self.play(Create(axes), Write(x_lab), Write(y_lab))

        # Draw trajectory
        trajectory = axes.plot_parametric_curve(
            lambda t: np.array([v0 * np.cos(theta) * t, v0 * np.sin(theta) * t - 0.5 * g * t**2, 0]),
            t_range=[0, T],
            color=BLUE, stroke_width=3,
        )
        self.play(Create(trajectory), run_time=2)
        self.wait(0.5)

        # Animated ball
        t_tracker = ValueTracker(0)
        ball = always_redraw(lambda: Dot(
            axes.c2p(
                v0 * np.cos(theta) * t_tracker.get_value(),
                max(0, v0 * np.sin(theta) * t_tracker.get_value() - 0.5 * g * t_tracker.get_value()**2),
            ),
            color=RED, radius=0.1,
        ))

        # Velocity vector
        vel_arrow = always_redraw(lambda: Arrow(
            axes.c2p(
                v0*np.cos(theta)*t_tracker.get_value(),
                max(0, v0*np.sin(theta)*t_tracker.get_value() - 0.5*g*t_tracker.get_value()**2),
            ),
            axes.c2p(
                v0*np.cos(theta)*t_tracker.get_value() + v0*np.cos(theta)*0.15,
                max(0, v0*np.sin(theta)*t_tracker.get_value() - 0.5*g*t_tracker.get_value()**2)
                + (v0*np.sin(theta) - g*t_tracker.get_value())*0.15,
            ),
            color=YELLOW, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.2,
        ))

        self.add(ball, vel_arrow)
        self.play(t_tracker.animate.set_value(T), run_time=4, rate_func=linear)
        self.wait(0.5)

        # ── Key values ──
        info = VGroup(
            MathTex(rf"T = \frac{{2v_0\sin\theta}}{{g}} = {T:.2f}\,\text{{s}}", font_size=22, color=YELLOW),
            MathTex(rf"R = \frac{{v_0^2\sin 2\theta}}{{g}} = {R:.1f}\,\text{{m}}", font_size=22, color=GREEN),
            MathTex(rf"H = \frac{{(v_0\sin\theta)^2}}{{2g}} = {H:.1f}\,\text{{m}}", font_size=22, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_corner(DR, buff=0.3)
        for i in info:
            self.play(Write(i), run_time=0.6)

        # Mark max height
        h_dot = Dot(axes.c2p(R/2, H), color=ORANGE, radius=0.08)
        h_dash = DashedLine(axes.c2p(0, H), axes.c2p(R/2, H), color=ORANGE, stroke_opacity=0.5)
        h_label = MathTex(rf"H = {H:.1f}", font_size=18, color=ORANGE).next_to(h_dot, UP)
        self.play(FadeIn(h_dot), Create(h_dash), Write(h_label))

        # Mark range
        r_dot = Dot(axes.c2p(R, 0), color=GREEN, radius=0.08)
        r_label = MathTex(rf"R = {R:.1f}", font_size=18, color=GREEN).next_to(r_dot, DOWN)
        self.play(FadeIn(r_dot), Write(r_label))

        # ── Compare different angles ──
        self.wait(1)
        self.play(*[FadeOut(m) for m in [ball, vel_arrow, h_dot, h_dash, h_label, r_dot, r_label, info]])

        compare_title = Text("Compare angles: 30, 45, 60 degrees", font_size=24, color=GOLD)
        compare_title.to_corner(UL).shift(DOWN * 0.5)
        self.play(Write(compare_title))

        for angle_deg, color in [(30, RED), (45, BLUE), (60, GREEN)]:
            th = np.radians(angle_deg)
            t_total = 2 * v0 * np.sin(th) / g
            traj = axes.plot_parametric_curve(
                lambda t, th=th: np.array([
                    v0*np.cos(th)*t,
                    max(0, v0*np.sin(th)*t - 0.5*g*t**2),
                    0
                ]),
                t_range=[0, t_total],
                color=color, stroke_width=2,
            )
            label = MathTex(rf"{angle_deg}^\circ", font_size=18, color=color)
            r_val = v0**2 * np.sin(2*th) / g
            h_val = (v0*np.sin(th))**2 / (2*g)
            label.next_to(axes.c2p(r_val/2, h_val), UP, buff=0.1)
            self.play(Create(traj), Write(label), run_time=0.8)

        note = Text("45 degrees gives maximum range!", font_size=22, color=GOLD).to_edge(DOWN)
        self.play(Write(note))
        self.wait(3)
'''

# ═══════════════════════════════════════════════════════════════════════════════
# Case 6: 物理 — 电场力与电势
# ═══════════════════════════════════════════════════════════════════════════════
CASES["06_physics_electric_field"] = r'''
from manim import *
import numpy as np

class ElectricField(Scene):
    def construct(self):
        title = Text("Electric Field & Potential", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # Coulomb's law
        coulomb = MathTex(
            r"\vec{F} = k\frac{q_1 q_2}{r^2}\hat{r}, \quad k = 8.99 \times 10^9",
            font_size=26, color=YELLOW,
        ).next_to(title, DOWN, buff=0.3)
        self.play(Write(coulomb), run_time=1.5)
        self.wait(1)

        self.play(FadeOut(coulomb))

        # ── Point charge electric field lines ──
        center = ORIGIN
        charge = Dot(center, color=RED, radius=0.15)
        plus = MathTex("+", font_size=28, color=WHITE).move_to(center)
        self.play(FadeIn(charge), Write(plus))

        # Radial field lines
        num_lines = 12
        field_lines = VGroup()
        for i in range(num_lines):
            angle = i * 2 * PI / num_lines
            end = center + 3.0 * np.array([np.cos(angle), np.sin(angle), 0])
            arrow = Arrow(
                center + 0.25 * np.array([np.cos(angle), np.sin(angle), 0]),
                end, color=YELLOW, buff=0, stroke_width=2,
                max_tip_length_to_length_ratio=0.08,
            )
            field_lines.add(arrow)

        self.play(LaggedStart(*[GrowArrow(a) for a in field_lines], lag_ratio=0.05), run_time=2)
        self.wait(1)

        label_e = MathTex(r"E = k\frac{q}{r^2}", font_size=24, color=YELLOW).to_corner(UR)
        self.play(Write(label_e))
        self.wait(1)

        # ── Equipotential lines (circles) ──
        equi = VGroup()
        for r in [0.8, 1.3, 1.9, 2.6]:
            circ = Circle(radius=r, color=GREEN, stroke_width=1.5, stroke_opacity=0.6)
            equi.add(circ)
        equi_label = Text("Equipotential lines", font_size=18, color=GREEN).to_corner(UL)
        self.play(LaggedStart(*[Create(c) for c in equi], lag_ratio=0.2), Write(equi_label), run_time=2)
        self.wait(1)

        # ── Dipole ──
        self.play(*[FadeOut(m) for m in self.mobjects])
        dipole_title = Text("Electric Dipole", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(dipole_title))

        pos_charge = Dot(LEFT * 2, color=RED, radius=0.12)
        neg_charge = Dot(RIGHT * 2, color=BLUE, radius=0.12)
        pos_label = MathTex("+q", font_size=22, color=RED).next_to(pos_charge, DOWN)
        neg_label = MathTex("-q", font_size=22, color=BLUE).next_to(neg_charge, DOWN)
        self.play(FadeIn(pos_charge), FadeIn(neg_charge), Write(pos_label), Write(neg_label))

        # Field lines from + to -
        dipole_lines = VGroup()
        for angle_offset in np.linspace(-60, 60, 7):
            rad = np.radians(angle_offset)
            # Curved lines from + to -
            points = []
            for t in np.linspace(0, 1, 30):
                x = -2 + 4 * t
                y_scale = np.sin(np.radians(angle_offset)) * 2
                y = y_scale * np.sin(PI * t)
                points.append(np.array([x, y, 0]))
            path = VMobject(color=YELLOW, stroke_width=1.5)
            path.set_points_smoothly(points)
            dipole_lines.add(path)

        self.play(LaggedStart(*[Create(l) for l in dipole_lines], lag_ratio=0.1), run_time=2)
        self.wait(1)

        # ── Potential energy diagram ──
        self.play(*[FadeOut(m) for m in self.mobjects])
        pe_title = Text("Potential Energy vs Distance", font_size=32, color=BLUE).to_edge(UP)
        self.play(Write(pe_title))

        axes = Axes(
            x_range=[0.3, 6, 1], y_range=[-3, 4, 1],
            x_length=8, y_length=5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.3)
        x_lab = MathTex("r", font_size=22).next_to(axes.get_x_axis(), RIGHT)
        y_lab = MathTex("U(r)", font_size=22).next_to(axes.get_y_axis(), UP)
        self.play(Create(axes), Write(x_lab), Write(y_lab))

        # U = kq1q2/r (repulsive: positive)
        u_repulsive = axes.plot(lambda r: 2/r, x_range=[0.5, 5.5], color=RED)
        u_attractive = axes.plot(lambda r: -2/r, x_range=[0.5, 5.5], color=BLUE)

        rep_label = MathTex(r"U > 0: \text{repulsive}", font_size=20, color=RED).to_corner(UR)
        att_label = MathTex(r"U < 0: \text{attractive}", font_size=20, color=BLUE).next_to(rep_label, DOWN)

        self.play(Create(u_repulsive), Write(rep_label), run_time=1)
        self.play(Create(u_attractive), Write(att_label), run_time=1)

        # Zero line
        zero_line = DashedLine(axes.c2p(0.3, 0), axes.c2p(6, 0), color=GRAY, stroke_opacity=0.5)
        self.play(Create(zero_line))

        formula = MathTex(r"U = k\frac{q_1 q_2}{r}", font_size=28, color=GOLD).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(3)
'''

# ═══════════════════════════════════════════════════════════════════════════════
# Case 7: 圆锥曲线 — 椭圆的焦点与性质
# ═══════════════════════════════════════════════════════════════════════════════
CASES["07_conic_ellipse"] = r'''
from manim import *
import numpy as np

class ConicEllipse(Scene):
    def construct(self):
        title = Text("Conic Section: Ellipse", font_size=40, color=GOLD).to_edge(UP)
        self.play(Write(title))

        # Standard equation
        eq = MathTex(r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \quad (a > b > 0)", font_size=32, color=YELLOW)
        eq.next_to(title, DOWN, buff=0.3)
        self.play(Write(eq))
        self.wait(1)

        self.play(eq.animate.scale(0.7).to_corner(UL))

        # ── Draw ellipse: a=3, b=2 ──
        a_val, b_val = 3, 2
        c_val = np.sqrt(a_val**2 - b_val**2)

        axes = Axes(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1],
            x_length=8, y_length=6, axis_config={"include_tip": True},
        )
        self.play(Create(axes))

        ellipse = ParametricFunction(
            lambda t: axes.c2p(a_val * np.cos(t), b_val * np.sin(t)),
            t_range=[0, 2*PI], color=BLUE, stroke_width=3,
        )
        self.play(Create(ellipse), run_time=2)

        # Foci
        f1_pos = axes.c2p(-c_val, 0)
        f2_pos = axes.c2p(c_val, 0)
        f1_dot = Dot(f1_pos, color=RED, radius=0.08)
        f2_dot = Dot(f2_pos, color=RED, radius=0.08)
        f1_label = MathTex("F_1", font_size=22, color=RED).next_to(f1_dot, DOWN)
        f2_label = MathTex("F_2", font_size=22, color=RED).next_to(f2_dot, DOWN)
        self.play(FadeIn(f1_dot), FadeIn(f2_dot), Write(f1_label), Write(f2_label))

        # Key info
        info = VGroup(
            MathTex(rf"a = {a_val}, \; b = {b_val}, \; c = \sqrt{{{a_val**2} - {b_val**2}}} = \sqrt{{{int(c_val**2)}}}", font_size=20),
            MathTex(rf"e = \frac{{c}}{{a}} = \frac{{\sqrt{{{int(c_val**2)}}}}}{{{a_val}}} \approx {c_val/a_val:.3f}", font_size=20, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_corner(UR)
        for i in info:
            self.play(Write(i), run_time=0.6)
        self.wait(1)

        # ── Demonstrate |PF1| + |PF2| = 2a ──
        angle_tracker = ValueTracker(0)

        p_dot = always_redraw(lambda: Dot(
            axes.c2p(a_val * np.cos(angle_tracker.get_value()), b_val * np.sin(angle_tracker.get_value())),
            color=YELLOW, radius=0.08,
        ))
        line_f1 = always_redraw(lambda: Line(
            f1_pos, axes.c2p(a_val*np.cos(angle_tracker.get_value()), b_val*np.sin(angle_tracker.get_value())),
            color=GREEN, stroke_width=2,
        ))
        line_f2 = always_redraw(lambda: Line(
            f2_pos, axes.c2p(a_val*np.cos(angle_tracker.get_value()), b_val*np.sin(angle_tracker.get_value())),
            color=PURPLE, stroke_width=2,
        ))

        def get_sum_label():
            px = a_val * np.cos(angle_tracker.get_value())
            py = b_val * np.sin(angle_tracker.get_value())
            d1 = np.sqrt((px + c_val)**2 + py**2)
            d2 = np.sqrt((px - c_val)**2 + py**2)
            return MathTex(
                rf"|PF_1| + |PF_2| = {d1:.2f} + {d2:.2f} = {d1+d2:.2f}",
                font_size=20, color=GOLD,
            ).to_edge(DOWN)

        sum_label = always_redraw(get_sum_label)

        self.play(FadeIn(p_dot), Create(line_f1), Create(line_f2), Write(sum_label))
        self.play(angle_tracker.animate.set_value(2 * PI), run_time=6, rate_func=linear)
        self.wait(0.5)

        constant = MathTex(r"|PF_1| + |PF_2| = 2a = 6", font_size=28, color=GOLD)
        constant.to_edge(DOWN)
        self.play(FadeOut(sum_label), Write(constant))
        self.wait(1)

        # ── Directrix ──
        self.play(FadeOut(p_dot), FadeOut(line_f1), FadeOut(line_f2))
        d_x = a_val**2 / c_val
        dir_left = DashedLine(axes.c2p(-d_x, -2.5), axes.c2p(-d_x, 2.5), color=TEAL, stroke_width=2)
        dir_right = DashedLine(axes.c2p(d_x, -2.5), axes.c2p(d_x, 2.5), color=TEAL, stroke_width=2)
        dir_label = Text("Directrix", font_size=18, color=TEAL).next_to(dir_right, RIGHT)
        self.play(Create(dir_left), Create(dir_right), Write(dir_label))

        dir_eq = MathTex(rf"x = \pm \frac{{a^2}}{{c}} = \pm {d_x:.2f}", font_size=20, color=TEAL)
        dir_eq.next_to(dir_label, DOWN, aligned_edge=LEFT)
        self.play(Write(dir_eq))
        self.wait(3)
'''

# ═══════════════════════════════════════════════════════════════════════════════
# Case 8: 物理 — 弹簧振子的能量守恒与相空间
# ═══════════════════════════════════════════════════════════════════════════════
CASES["08_physics_spring_energy"] = r'''
from manim import *
import numpy as np

class SpringEnergy(Scene):
    def construct(self):
        title = Text("Spring Oscillator: Energy Conservation", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # ── Setup ──
        formulas = VGroup(
            MathTex(r"x(t) = A\cos(\omega t)", font_size=24),
            MathTex(r"v(t) = -A\omega\sin(\omega t)", font_size=24),
            MathTex(r"E_k = \frac{1}{2}mv^2, \quad E_p = \frac{1}{2}kx^2", font_size=24),
            MathTex(r"E = E_k + E_p = \frac{1}{2}kA^2 = \text{const}", font_size=24, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(title, DOWN, buff=0.3)
        for f in formulas:
            self.play(Write(f), run_time=0.7)
        self.wait(1)
        self.play(*[FadeOut(f) for f in formulas])

        # ── Energy vs time graph ──
        A = 1.0
        omega = 2.0
        k = omega**2

        axes = Axes(
            x_range=[0, 2*PI, PI/2], y_range=[0, 1.2, 0.2],
            x_length=10, y_length=3.5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.5)
        x_lab = MathTex("t", font_size=20).next_to(axes.get_x_axis(), RIGHT)
        y_lab = MathTex("E", font_size=20).next_to(axes.get_y_axis(), UP)
        self.play(Create(axes), Write(x_lab), Write(y_lab))

        Ek_graph = axes.plot(
            lambda t: 0.5 * k * (A * omega * np.sin(omega * t))**2 / (k * A**2),
            x_range=[0, 2*PI], color=RED,
        )
        Ep_graph = axes.plot(
            lambda t: 0.5 * k * (A * np.cos(omega * t))**2 / (k * A**2),
            x_range=[0, 2*PI], color=BLUE,
        )
        Et_graph = axes.plot(lambda t: 1.0, x_range=[0, 2*PI], color=GOLD, stroke_width=2)

        ek_label = MathTex(r"E_k", font_size=20, color=RED).to_corner(UR)
        ep_label = MathTex(r"E_p", font_size=20, color=BLUE).next_to(ek_label, DOWN)
        et_label = MathTex(r"E_{total}", font_size=20, color=GOLD).next_to(ep_label, DOWN)

        self.play(Create(Ek_graph), Write(ek_label), run_time=1.5)
        self.play(Create(Ep_graph), Write(ep_label), run_time=1.5)
        self.play(Create(Et_graph), Write(et_label), run_time=1)
        self.wait(1)

        note1 = Text("Ek and Ep oscillate out of phase, total E is constant", font_size=18, color=GRAY)
        note1.to_edge(DOWN)
        self.play(Write(note1))
        self.wait(1.5)

        # ── Phase space (x, v) ──
        self.play(*[FadeOut(m) for m in self.mobjects])
        phase_title = Text("Phase Space Diagram", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(phase_title))

        phase_axes = Axes(
            x_range=[-1.5, 1.5, 0.5], y_range=[-3, 3, 1],
            x_length=5, y_length=5,
            axis_config={"include_tip": True},
        )
        px_lab = MathTex("x", font_size=22).next_to(phase_axes.get_x_axis(), RIGHT)
        pv_lab = MathTex("v", font_size=22).next_to(phase_axes.get_y_axis(), UP)
        self.play(Create(phase_axes), Write(px_lab), Write(pv_lab))

        # Phase portrait: ellipse in (x, v) space
        ellipse_path = ParametricFunction(
            lambda t: phase_axes.c2p(A * np.cos(t), -A * omega * np.sin(t)),
            t_range=[0, 2*PI], color=GREEN, stroke_width=3,
        )
        self.play(Create(ellipse_path), run_time=2)

        # Animated point tracing
        t_tracker = ValueTracker(0)
        phase_dot = always_redraw(lambda: Dot(
            phase_axes.c2p(
                A * np.cos(omega * t_tracker.get_value()),
                -A * omega * np.sin(omega * t_tracker.get_value()),
            ),
            color=YELLOW, radius=0.1,
        ))
        self.add(phase_dot)
        self.play(t_tracker.animate.set_value(2*PI/omega), run_time=4, rate_func=linear)
        self.wait(0.5)

        phase_eq = MathTex(
            r"\frac{x^2}{A^2} + \frac{v^2}{(A\omega)^2} = 1",
            font_size=24, color=GREEN,
        ).to_corner(UR)
        note2 = Text("Ellipse in phase space = energy conservation", font_size=20, color=GOLD).to_edge(DOWN)
        self.play(Write(phase_eq), Write(note2))
        self.wait(3)
'''

# ═══════════════════════════════════════════════════════════════════════════════
# Case 9: 高考解析几何 — 直线与圆的位置关系
# ═══════════════════════════════════════════════════════════════════════════════
CASES["09_line_circle"] = r'''
from manim import *
import numpy as np

class LineCircleRelation(Scene):
    def construct(self):
        title = Text("Line & Circle: Position Relations", font_size=36, color=GOLD).to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[-5, 5, 1], y_range=[-4, 4, 1],
            x_length=8, y_length=6,
            axis_config={"include_tip": True},
        )
        self.play(Create(axes))

        # Circle: x^2 + y^2 = 4
        circle = Circle(radius=2 * axes.x_length / 10, color=BLUE, stroke_width=3).move_to(axes.c2p(0, 0))
        c_label = MathTex(r"x^2 + y^2 = 4", font_size=22, color=BLUE).to_corner(UR)
        self.play(Create(circle), Write(c_label))
        self.wait(0.5)

        center = Dot(axes.c2p(0, 0), color=WHITE, radius=0.05)
        r_label = MathTex("r=2", font_size=18, color=BLUE).next_to(center, DR, buff=0.1)
        self.play(FadeIn(center), Write(r_label))

        # ── Case 1: Secant (two intersections) ──
        case1_title = Text("Case 1: Secant (d < r)", font_size=22, color=GREEN).to_corner(UL)
        self.play(Write(case1_title))

        line1 = axes.plot(lambda x: x, x_range=[-3, 3], color=GREEN)
        l1_label = MathTex(r"y = x", font_size=20, color=GREEN).next_to(axes.c2p(2.5, 2.5), RIGHT)
        self.play(Create(line1), Write(l1_label))

        # Intersection points
        # x^2 + x^2 = 4 => x = ±√2
        sq2 = np.sqrt(2)
        int1 = Dot(axes.c2p(sq2, sq2), color=GREEN, radius=0.08)
        int2 = Dot(axes.c2p(-sq2, -sq2), color=GREEN, radius=0.08)
        self.play(FadeIn(int1), FadeIn(int2))

        # Distance from center
        d1 = MathTex(r"d = \frac{|0-0|}{\sqrt{2}} = 0 < r", font_size=18, color=GREEN)
        d1.to_edge(DOWN)
        self.play(Write(d1))
        self.wait(1.5)

        self.play(FadeOut(line1), FadeOut(l1_label), FadeOut(int1), FadeOut(int2), FadeOut(d1), FadeOut(case1_title))

        # ── Case 2: Tangent (one intersection) ──
        case2_title = Text("Case 2: Tangent (d = r)", font_size=22, color=YELLOW).to_corner(UL)
        self.play(Write(case2_title))

        line2 = axes.plot(lambda x: x + 2*np.sqrt(2), x_range=[-4.5, 1], color=YELLOW)
        l2_label = MathTex(r"y = x + 2\sqrt{2}", font_size=20, color=YELLOW).next_to(axes.c2p(-1, 2*sq2-1), UL)
        self.play(Create(line2), Write(l2_label))

        # Tangent point
        tan_pt = Dot(axes.c2p(-sq2, sq2), color=YELLOW, radius=0.08)
        self.play(FadeIn(tan_pt))

        d2 = MathTex(r"d = \frac{2\sqrt{2}}{\sqrt{2}} = 2 = r", font_size=18, color=YELLOW)
        d2.to_edge(DOWN)
        self.play(Write(d2))
        self.wait(1.5)

        self.play(FadeOut(line2), FadeOut(l2_label), FadeOut(tan_pt), FadeOut(d2), FadeOut(case2_title))

        # ── Case 3: Separate (no intersection) ──
        case3_title = Text("Case 3: Separate (d > r)", font_size=22, color=RED).to_corner(UL)
        self.play(Write(case3_title))

        line3 = axes.plot(lambda x: x + 4, x_range=[-4.5, 0.5], color=RED)
        l3_label = MathTex(r"y = x + 4", font_size=20, color=RED).next_to(axes.c2p(-2, 2), UL)
        self.play(Create(line3), Write(l3_label))

        d3 = MathTex(r"d = \frac{4}{\sqrt{2}} = 2\sqrt{2} > r", font_size=18, color=RED)
        d3.to_edge(DOWN)
        self.play(Write(d3))
        self.wait(1.5)

        # ── Summary ──
        self.play(*[FadeOut(m) for m in self.mobjects])
        summary_title = Text("Summary", font_size=36, color=GOLD).to_edge(UP)
        self.play(Write(summary_title))

        summary = VGroup(
            MathTex(r"d < r \Rightarrow \text{Secant (2 points)}", font_size=26, color=GREEN),
            MathTex(r"d = r \Rightarrow \text{Tangent (1 point)}", font_size=26, color=YELLOW),
            MathTex(r"d > r \Rightarrow \text{Separate (0 points)}", font_size=26, color=RED),
        ).arrange(DOWN, buff=0.5).next_to(summary_title, DOWN, buff=0.8)

        where = MathTex(
            r"d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}",
            font_size=28, color=BLUE,
        ).next_to(summary, DOWN, buff=0.6)

        for s in summary:
            self.play(Write(s), run_time=0.8)
            self.wait(0.3)
        self.play(Write(where))
        self.wait(3)
'''

# ═══════════════════════════════════════════════════════════════════════════════
# Case 10: 微分方程 — SIR 传染病模型
# ═══════════════════════════════════════════════════════════════════════════════
CASES["10_sir_model"] = r'''
from manim import *
import numpy as np

class SIRModel(Scene):
    def construct(self):
        title = Text("SIR Epidemic Model", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # ── Differential equations ──
        equations = VGroup(
            MathTex(r"\frac{dS}{dt} = -\beta S I", font_size=28, color=BLUE),
            MathTex(r"\frac{dI}{dt} = \beta S I - \gamma I", font_size=28, color=RED),
            MathTex(r"\frac{dR}{dt} = \gamma I", font_size=28, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.3)

        for eq in equations:
            self.play(Write(eq), run_time=0.8)
        self.wait(1)

        params = VGroup(
            MathTex(r"\beta = 0.3 \text{ (infection rate)}", font_size=20),
            MathTex(r"\gamma = 0.1 \text{ (recovery rate)}", font_size=20),
            MathTex(r"R_0 = \frac{\beta}{\gamma} = 3", font_size=20, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(equations, DOWN, buff=0.3)
        for p in params:
            self.play(Write(p), run_time=0.5)
        self.wait(1)

        self.play(*[FadeOut(m) for m in self.mobjects[1:]])

        # ── Numerical simulation ──
        beta, gamma = 0.3, 0.1
        S, I, R = [0.99], [0.01], [0.0]
        dt = 0.1
        T = 120
        steps = int(T / dt)

        for _ in range(steps):
            s, i, r = S[-1], I[-1], R[-1]
            dS = -beta * s * i * dt
            dI = (beta * s * i - gamma * i) * dt
            dR = gamma * i * dt
            S.append(s + dS)
            I.append(i + dI)
            R.append(r + dR)

        times = np.arange(0, T + dt, dt)

        axes = Axes(
            x_range=[0, 120, 20], y_range=[0, 1, 0.2],
            x_length=9, y_length=4.5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.5)
        x_lab = MathTex("t", font_size=22).next_to(axes.get_x_axis(), RIGHT)
        y_lab = MathTex("\\text{Proportion}", font_size=18).next_to(axes.get_y_axis(), UP, buff=0.2)
        self.play(Create(axes), Write(x_lab), Write(y_lab))

        # Plot S
        s_points = [axes.c2p(times[i], S[i]) for i in range(0, len(times), 5)]
        s_curve = VMobject(color=BLUE, stroke_width=3)
        s_curve.set_points_smoothly(s_points)
        s_label = MathTex("S(t)", font_size=20, color=BLUE).to_corner(UR)

        i_points = [axes.c2p(times[i], I[i]) for i in range(0, len(times), 5)]
        i_curve = VMobject(color=RED, stroke_width=3)
        i_curve.set_points_smoothly(i_points)
        i_label = MathTex("I(t)", font_size=20, color=RED).next_to(s_label, DOWN)

        r_points = [axes.c2p(times[i], R[i]) for i in range(0, len(times), 5)]
        r_curve = VMobject(color=GREEN, stroke_width=3)
        r_curve.set_points_smoothly(r_points)
        r_label = MathTex("R(t)", font_size=20, color=GREEN).next_to(i_label, DOWN)

        self.play(Create(s_curve), Write(s_label), run_time=2)
        self.play(Create(i_curve), Write(i_label), run_time=2)
        self.play(Create(r_curve), Write(r_label), run_time=2)
        self.wait(1)

        # Peak infection
        peak_idx = np.argmax(I)
        peak_t = times[peak_idx]
        peak_val = I[peak_idx]
        peak_dot = Dot(axes.c2p(peak_t, peak_val), color=YELLOW, radius=0.08)
        peak_label = MathTex(
            rf"\text{{Peak}}: I = {peak_val:.2f}, \; t = {peak_t:.0f}",
            font_size=18, color=YELLOW,
        ).next_to(peak_dot, UP+RIGHT, buff=0.1)
        self.play(FadeIn(peak_dot), Write(peak_label))

        # Herd immunity threshold
        threshold = 1 - 1/3
        h_line = DashedLine(axes.c2p(0, threshold), axes.c2p(120, threshold), color=ORANGE, stroke_opacity=0.6)
        h_label = MathTex(
            rf"1 - 1/R_0 = {threshold:.2f}",
            font_size=18, color=ORANGE,
        ).next_to(axes.c2p(120, threshold), RIGHT, buff=0.1)
        self.play(Create(h_line), Write(h_label))

        conclusion = Text(
            "When S falls below 1/R0, epidemic declines",
            font_size=20, color=GOLD,
        ).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(3)
'''

# ═══════════════════════════════════════════════════════════════════════════════
# Case 11: 物理 — 电磁感应与法拉第定律
# ═══════════════════════════════════════════════════════════════════════════════
CASES["11_physics_faraday"] = r'''
from manim import *
import numpy as np

class FaradayLaw(Scene):
    def construct(self):
        title = Text("Faraday's Law of Electromagnetic Induction", font_size=34, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # ── Faraday's Law ──
        law = MathTex(
            r"\mathcal{E} = -\frac{d\Phi_B}{dt} = -\frac{d}{dt}\int \vec{B} \cdot d\vec{A}",
            font_size=30, color=YELLOW,
        ).next_to(title, DOWN, buff=0.3)
        self.play(Write(law), run_time=2)
        self.wait(1)

        self.play(law.animate.scale(0.7).to_corner(UL, buff=0.3))

        # ── Scenario: bar sliding on rails ──
        scene_title = Text("Sliding Bar on Rails", font_size=28, color=GREEN)
        scene_title.next_to(title, DOWN, buff=0.3)
        self.play(Write(scene_title))

        # Draw rails
        rail_top = Line(LEFT * 4 + UP * 1.5, RIGHT * 4 + UP * 1.5, color=GRAY, stroke_width=3)
        rail_bot = Line(LEFT * 4 + DOWN * 1.5, RIGHT * 4 + DOWN * 1.5, color=GRAY, stroke_width=3)
        resistor = VGroup(
            Line(LEFT * 4 + UP * 1.5, LEFT * 4 + UP * 0.3, color=GRAY),
            Rectangle(width=0.3, height=0.6, color=ORANGE, fill_opacity=0.3).move_to(LEFT * 4),
            MathTex("R", font_size=18, color=ORANGE).move_to(LEFT * 4 + RIGHT * 0.4),
            Line(LEFT * 4 + DOWN * 0.3, LEFT * 4 + DOWN * 1.5, color=GRAY),
        )

        self.play(Create(rail_top), Create(rail_bot), Create(resistor))

        # Sliding bar
        bar_x = ValueTracker(-2)
        bar = always_redraw(lambda: Line(
            np.array([bar_x.get_value(), 1.5, 0]),
            np.array([bar_x.get_value(), -1.5, 0]),
            color=BLUE, stroke_width=5,
        ))
        bar_label = always_redraw(lambda: MathTex(
            "v", font_size=22, color=BLUE
        ).next_to(np.array([bar_x.get_value(), 0, 0]), RIGHT, buff=0.2))

        v_arrow = always_redraw(lambda: Arrow(
            np.array([bar_x.get_value() + 0.3, 0, 0]),
            np.array([bar_x.get_value() + 1, 0, 0]),
            color=RED, buff=0, stroke_width=3,
        ))

        self.play(Create(bar), Write(bar_label), GrowArrow(v_arrow))

        # B field dots (into page)
        b_dots = VGroup()
        for x in np.arange(-3.5, 3.5, 0.7):
            for y in np.arange(-1.2, 1.5, 0.7):
                cross = MathTex(r"\otimes", font_size=14, color=PURPLE)
                cross.move_to(np.array([x, y, 0]))
                b_dots.add(cross)
        b_label = MathTex(r"\vec{B} \;\text{(into page)}", font_size=18, color=PURPLE).to_corner(DR)
        self.play(FadeIn(b_dots), Write(b_label), run_time=1)

        # Shaded area (flux region)
        area = always_redraw(lambda: Polygon(
            np.array([-4, 1.5, 0]),
            np.array([bar_x.get_value(), 1.5, 0]),
            np.array([bar_x.get_value(), -1.5, 0]),
            np.array([-4, -1.5, 0]),
            fill_color=GREEN, fill_opacity=0.1, stroke_opacity=0,
        ))
        self.add(area)

        # Animate bar sliding
        self.play(bar_x.animate.set_value(2.5), run_time=5, rate_func=linear)
        self.wait(0.5)

        # ── EMF calculation ──
        self.play(*[FadeOut(m) for m in self.mobjects])
        calc_title = Text("EMF Calculation", font_size=32, color=GOLD).to_edge(UP)
        self.play(Write(calc_title))

        calc = VGroup(
            MathTex(r"\Phi_B = B \cdot L \cdot x(t)", font_size=26),
            MathTex(r"\frac{d\Phi_B}{dt} = B \cdot L \cdot v", font_size=26, color=YELLOW),
            MathTex(r"\mathcal{E} = BLv", font_size=30, color=GOLD),
            MathTex(r"I = \frac{\mathcal{E}}{R} = \frac{BLv}{R}", font_size=26, color=GREEN),
            MathTex(r"F_{\text{brake}} = BIL = \frac{B^2L^2v}{R}", font_size=26, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(calc_title, DOWN, buff=0.5)

        for c in calc:
            self.play(Write(c), run_time=0.8)
            self.wait(0.3)

        box = SurroundingRectangle(calc[2], color=GOLD, buff=0.1)
        self.play(Create(box))

        note = Text("Lenz's Law: Induced current opposes the change in flux",
                     font_size=20, color=TEAL).to_edge(DOWN)
        self.play(Write(note))
        self.wait(3)
'''

# ═══════════════════════════════════════════════════════════════════════════════
# Case 12: 线性代数 — 特征值与特征向量
# ═══════════════════════════════════════════════════════════════════════════════
CASES["12_eigenvalues"] = r'''
from manim import *
import numpy as np

class Eigenvalues(Scene):
    def construct(self):
        title = Text("Eigenvalues & Eigenvectors", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # Definition
        definition = MathTex(r"A\vec{v} = \lambda\vec{v}", font_size=40, color=YELLOW)
        definition.next_to(title, DOWN, buff=0.3)
        self.play(Write(definition), run_time=1.5)
        self.wait(1)

        self.play(definition.animate.scale(0.6).to_corner(UL, buff=0.3))

        # ── Example matrix ──
        mat = MathTex(r"A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}", font_size=32)
        mat.next_to(title, DOWN, buff=0.3)
        self.play(Write(mat))
        self.wait(0.5)

        # Characteristic equation
        self.play(mat.animate.shift(LEFT * 3).scale(0.8))

        char_eq = VGroup(
            MathTex(r"\det(A - \lambda I) = 0", font_size=26, color=YELLOW),
            MathTex(r"(2-\lambda)^2 - 1 = 0", font_size=26),
            MathTex(r"\lambda^2 - 4\lambda + 3 = 0", font_size=26),
            MathTex(r"(\lambda - 1)(\lambda - 3) = 0", font_size=26, color=GREEN),
            MathTex(r"\lambda_1 = 1, \quad \lambda_2 = 3", font_size=28, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(mat, RIGHT, buff=0.8)

        for c in char_eq:
            self.play(Write(c), run_time=0.7)
            self.wait(0.2)
        self.wait(1)

        # ── Find eigenvectors ──
        self.play(*[FadeOut(m) for m in self.mobjects[1:]])

        ev_title = Text("Finding Eigenvectors", font_size=28, color=GREEN)
        ev_title.next_to(title, DOWN, buff=0.3)
        self.play(Write(ev_title))

        ev1 = VGroup(
            MathTex(r"\lambda_1 = 1: \; (A - I)\vec{v} = 0", font_size=24, color=YELLOW),
            MathTex(r"\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\vec{v} = 0", font_size=24),
            MathTex(r"\vec{v}_1 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}", font_size=28, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        ev2 = VGroup(
            MathTex(r"\lambda_2 = 3: \; (A - 3I)\vec{v} = 0", font_size=24, color=YELLOW),
            MathTex(r"\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}\vec{v} = 0", font_size=24),
            MathTex(r"\vec{v}_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}", font_size=28, color=BLUE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        evs = VGroup(ev1, ev2).arrange(RIGHT, buff=1.5).next_to(ev_title, DOWN, buff=0.4)

        for ev in [ev1, ev2]:
            for line in ev:
                self.play(Write(line), run_time=0.6)
            self.wait(0.5)
        self.wait(1)

        # ── Geometric visualization ──
        self.play(*[FadeOut(m) for m in self.mobjects])
        geo_title = Text("Geometric Meaning", font_size=32, color=BLUE).to_edge(UP)
        self.play(Write(geo_title))

        plane = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1],
            x_length=6, y_length=6,
            background_line_style={"stroke_opacity": 0.3},
        )
        self.play(Create(plane))

        # Original vectors
        v1_orig = Arrow(plane.c2p(0,0), plane.c2p(1,-1), color=RED, buff=0, stroke_width=4)
        v2_orig = Arrow(plane.c2p(0,0), plane.c2p(1,1), color=BLUE, buff=0, stroke_width=4)
        v1_label = MathTex(r"\vec{v}_1", font_size=22, color=RED).next_to(v1_orig, DR, buff=0.1)
        v2_label = MathTex(r"\vec{v}_2", font_size=22, color=BLUE).next_to(v2_orig, UR, buff=0.1)

        self.play(GrowArrow(v1_orig), GrowArrow(v2_orig), Write(v1_label), Write(v2_label))
        self.wait(0.5)

        # Apply transformation A
        trans_text = Text("Apply A:", font_size=22, color=GOLD).to_corner(UL, buff=0.5)
        self.play(Write(trans_text))

        # Av1 = 1 * v1 (scaled by lambda=1, same direction)
        av1 = Arrow(plane.c2p(0,0), plane.c2p(1,-1), color=ORANGE, buff=0, stroke_width=3, stroke_opacity=0.7)
        av1_label = MathTex(r"A\vec{v}_1 = 1 \cdot \vec{v}_1", font_size=18, color=ORANGE)
        av1_label.next_to(plane.c2p(1, -1), RIGHT, buff=0.1)
        self.play(GrowArrow(av1), Write(av1_label))

        # Av2 = 3 * v2 (scaled by lambda=3)
        av2 = Arrow(plane.c2p(0,0), plane.c2p(3,3), color=TEAL, buff=0, stroke_width=3, stroke_opacity=0.7)
        av2_label = MathTex(r"A\vec{v}_2 = 3 \cdot \vec{v}_2", font_size=18, color=TEAL)
        av2_label.next_to(plane.c2p(3, 3), RIGHT, buff=0.1)
        self.play(GrowArrow(av2), Write(av2_label))
        self.wait(1)

        # Apply transformation to grid
        note = Text("Eigenvectors only get scaled, not rotated!", font_size=22, color=GOLD)
        note.to_edge(DOWN)
        self.play(Write(note))

        A = [[2, 1], [1, 2]]
        self.play(plane.animate.apply_matrix(A), run_time=3)
        self.wait(3)
'''

# ═══════════════════════════════════════════════════════════════════════════════
# Runner
# ═══════════════════════════════════════════════════════════════════════════════
def main():
    total = len(CASES)
    success = 0
    failed = 0
    results = []

    print(f"\n{'='*70}")
    print(f"  Math Animation MCP — Long & Complex Cases ({total} cases)")
    print(f"{'='*70}\n")

    for i, (name, code) in enumerate(CASES.items(), 1):
        print(f"[{i}/{total}] Rendering {name} ...")
        t0 = time.time()
        result = render_manim_code(
            code, quality="low", fmt="mp4",
            output_dir=OUTPUT, timeout=180,
        )
        elapsed = time.time() - t0

        if result.success:
            success += 1
            size_kb = os.path.getsize(result.file_path) / 1024
            print(f"  OK ({elapsed:.1f}s, {size_kb:.0f}KB) -> {os.path.basename(result.file_path)}")
            results.append((name, "OK", f"{elapsed:.1f}s", f"{size_kb:.0f}KB"))
        else:
            failed += 1
            err_short = result.error_msg[-200:].replace('\n', ' ')
            print(f"  FAIL ({elapsed:.1f}s) -> {err_short}")
            results.append((name, "FAIL", f"{elapsed:.1f}s", err_short[:80]))

    print(f"\n{'='*70}")
    print(f"  Results: {success}/{total} OK, {failed}/{total} FAIL")
    print(f"{'='*70}")
    print(f"\n{'Case':<35s} {'Status':^6s} {'Time':>8s} {'Detail'}")
    print(f"{'-'*80}")
    for name, status, elapsed, detail in results:
        print(f"  {name:<33s} {status:^6s} {elapsed:>8s}  {detail}")
    print()


if __name__ == "__main__":
    main()
