# 2025 Gaokao I - Problem 19: Derivative + Trig (Final Problem)
from manim import *
import numpy as np

class Gaokao2025_19_Derivative(Scene):
    def construct(self):
        # ══════════════════════════════════════════════════════════
        # Scene 1: Title & Problem Statement
        # ══════════════════════════════════════════════════════════
        title = Text("2025 New Gaokao I — Problem 19 (Final)", font_size=34, color=GOLD)
        sub = Text("Derivative + Trigonometric Functions", font_size=22, color=GRAY)
        sub.next_to(title, DOWN, buff=0.2)
        self.play(Write(title), FadeIn(sub))
        self.wait(1)

        problem = VGroup(
            MathTex(r"f(x) = 5\cos x - \cos 5x", font_size=30, color=BLUE),
            Text("(1) Find max f(x) on [0, pi]", font_size=20),
            Text("(2) Existence proof with cos inequality", font_size=20),
            Text("(3) Find min b such that 5cosx - cos(5x+phi) <= b", font_size=18),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(sub, DOWN, buff=0.3)
        for p in problem:
            self.play(Write(p), run_time=0.7)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ══════════════════════════════════════════════════════════
        # Scene 2: Visualize f(x) = 5cosx - cos5x
        # ══════════════════════════════════════════════════════════
        vis_title = Text("First: visualize f(x) = 5cos(x) - cos(5x)", font_size=28, color=BLUE)
        vis_title.to_edge(UP)
        self.play(Write(vis_title))

        axes = Axes(
            x_range=[0, PI + 0.3, PI/4], y_range=[-2, 7, 1],
            x_length=10, y_length=5.5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.3)

        # Custom x labels
        x_labels = VGroup(
            MathTex(r"\frac{\pi}{4}", font_size=16).next_to(axes.c2p(PI/4, 0), DOWN, buff=0.15),
            MathTex(r"\frac{\pi}{2}", font_size=16).next_to(axes.c2p(PI/2, 0), DOWN, buff=0.15),
            MathTex(r"\frac{3\pi}{4}", font_size=16).next_to(axes.c2p(3*PI/4, 0), DOWN, buff=0.15),
            MathTex(r"\pi", font_size=16).next_to(axes.c2p(PI, 0), DOWN, buff=0.15),
        )
        self.play(Create(axes), Write(x_labels))

        # Plot f(x) = 5cos(x) - cos(5x)
        f = lambda x: 5*np.cos(x) - np.cos(5*x)
        f_graph = axes.plot(f, x_range=[0, PI], color=BLUE, stroke_width=3)
        f_label = MathTex(r"f(x) = 5\cos x - \cos 5x", font_size=22, color=BLUE).to_corner(UR)
        self.play(Create(f_graph), Write(f_label), run_time=2)
        self.wait(1)

        # Also show 5cos(x) and -cos(5x) separately
        g1 = axes.plot(lambda x: 5*np.cos(x), x_range=[0, PI], color=RED, stroke_width=1.5, stroke_opacity=0.6)
        g2 = axes.plot(lambda x: -np.cos(5*x), x_range=[0, PI], color=GREEN, stroke_width=1.5, stroke_opacity=0.6)
        g1_lab = MathTex(r"5\cos x", font_size=16, color=RED).next_to(f_label, DOWN, aligned_edge=RIGHT)
        g2_lab = MathTex(r"-\cos 5x", font_size=16, color=GREEN).next_to(g1_lab, DOWN, aligned_edge=RIGHT)
        self.play(Create(g1), Create(g2), Write(g1_lab), Write(g2_lab), run_time=1.5)
        self.wait(1.5)

        self.play(FadeOut(g1), FadeOut(g2), FadeOut(g1_lab), FadeOut(g2_lab))

        # ══════════════════════════════════════════════════════════
        # Scene 3: Part (1) — Find maximum on [0, π]
        # ══════════════════════════════════════════════════════════
        self.play(FadeOut(vis_title))
        part1_title = Text("Part (1): Find max f(x) on [0, pi]", font_size=28, color=GREEN)
        part1_title.to_edge(UP)
        self.play(Write(part1_title))

        # Step 1: Derivative
        step1 = VGroup(
            MathTex(r"f'(x) = -5\sin x + 5\sin 5x", font_size=24, color=YELLOW),
            MathTex(r"= 5(\sin 5x - \sin x)", font_size=24),
            MathTex(r"= 5 \cdot 2\cos 3x \cdot \sin 2x", font_size=24, color=ORANGE),
            MathTex(r"= 10\cos 3x \sin 2x", font_size=26, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(LEFT, buff=0.3).shift(DOWN * 0.5)

        for s in step1:
            self.play(Write(s), run_time=0.8)
            self.wait(0.3)
        self.wait(0.5)

        # Plot f'(x)
        fp = lambda x: -5*np.sin(x) + 5*np.sin(5*x)
        fp_graph = axes.plot(fp, x_range=[0, PI], color=YELLOW, stroke_width=2)
        fp_label = MathTex(r"f'(x)", font_size=18, color=YELLOW).next_to(axes.c2p(0.5, fp(0.5)), UR, buff=0.1)
        self.play(Create(fp_graph), Write(fp_label), run_time=1.5)
        self.wait(0.5)

        # Zero line
        zero_line = DashedLine(axes.c2p(0, 0), axes.c2p(PI, 0), color=GRAY, stroke_opacity=0.5)
        self.play(Create(zero_line))

        # Step 2: Find critical points
        step2 = VGroup(
            MathTex(r"f'(x) = 0:", font_size=20, color=WHITE),
            MathTex(r"\cos 3x = 0 \Rightarrow x = \frac{\pi}{6}, \frac{\pi}{2}, \frac{5\pi}{6}", font_size=20, color=TEAL),
            MathTex(r"\sin 2x = 0 \Rightarrow x = 0, \frac{\pi}{2}, \pi", font_size=20, color=TEAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(step1, DOWN, buff=0.3)

        for s in step2:
            self.play(Write(s), run_time=0.6)

        # Mark critical points on graph
        crits = [0, PI/6, PI/2, 5*PI/6, PI]
        crit_names = ["0", r"\frac{\pi}{6}", r"\frac{\pi}{2}", r"\frac{5\pi}{6}", r"\pi"]
        crit_dots = VGroup()
        for x_val, name in zip(crits, crit_names):
            y_val = f(x_val)
            dot = Dot(axes.c2p(x_val, y_val), color=RED, radius=0.06)
            val_label = MathTex(f"f={y_val:.1f}", font_size=14, color=RED)
            val_label.next_to(dot, UP if y_val > 3 else DOWN, buff=0.1)
            crit_dots.add(VGroup(dot, val_label))
            self.play(FadeIn(dot), Write(val_label), run_time=0.4)

        self.wait(1)

        # Step 3: Compare values
        values = VGroup(
            MathTex(r"f(0) = 5 - 1 = 4", font_size=20),
            MathTex(r"f(\pi/6) = 5\cos(\pi/6) - \cos(5\pi/6) = \frac{5\sqrt3}{2} + \frac{\sqrt3}{2} = 3\sqrt3 \approx 5.20", font_size=18, color=GREEN),
            MathTex(r"f(\pi/2) = 0 - 0 = 0", font_size=20),
            MathTex(r"f(5\pi/6) = -\frac{5\sqrt3}{2} - \frac{\sqrt3}{2} = -3\sqrt3", font_size=18),
            MathTex(r"f(\pi) = -5 - (-1) = -4", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.8)

        for v in values:
            self.play(Write(v), run_time=0.5)

        self.wait(0.5)

        # Highlight maximum
        answer1 = MathTex(
            r"\boxed{f_{\max} = f(\pi/6) = 3\sqrt{3}}",
            font_size=28, color=GOLD,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(answer1))

        # Highlight the point
        max_pt = axes.c2p(PI/6, f(PI/6))
        circle_highlight = Circle(radius=0.2, color=GOLD, stroke_width=3).move_to(max_pt)
        self.play(Create(circle_highlight))
        self.wait(3)

        # ══════════════════════════════════════════════════════════
        # Scene 4: Deep dive into derivative factoring
        # ══════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])
        deep_title = Text("Key Technique: Sum-to-Product", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(deep_title))

        technique = VGroup(
            MathTex(r"\sin A - \sin B = 2\cos\frac{A+B}{2}\sin\frac{A-B}{2}", font_size=26, color=YELLOW),
            MathTex(r"\text{Here: } \sin 5x - \sin x = 2\cos 3x \sin 2x", font_size=26),
            MathTex(r"\text{So } f'(x) = 10\cos 3x \sin 2x", font_size=26, color=GREEN),
        ).arrange(DOWN, buff=0.3).next_to(deep_title, DOWN, buff=0.5)

        for t in technique:
            self.play(Write(t), run_time=0.8)
            self.wait(0.3)
        self.wait(1)

        # Sign analysis table
        table_title = Text("Sign analysis on [0, pi]:", font_size=22, color=TEAL)
        table_title.next_to(technique, DOWN, buff=0.5)
        self.play(Write(table_title))

        intervals = VGroup(
            MathTex(r"(0, \pi/6): \;\cos 3x > 0, \sin 2x > 0 \Rightarrow f' > 0 \;\uparrow", font_size=20, color=GREEN),
            MathTex(r"(\pi/6, \pi/2): \;\cos 3x < 0, \sin 2x > 0 \Rightarrow f' < 0 \;\downarrow", font_size=20, color=RED),
            MathTex(r"(\pi/2, 5\pi/6): \;\cos 3x < 0, \sin 2x < 0 \Rightarrow f' > 0 \;\uparrow", font_size=20, color=GREEN),
            MathTex(r"(5\pi/6, \pi): \;\cos 3x > 0, \sin 2x < 0 \Rightarrow f' < 0 \;\downarrow", font_size=20, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(table_title, DOWN, buff=0.2)

        for iv in intervals:
            self.play(Write(iv), run_time=0.6)
            self.wait(0.2)

        conclusion1 = MathTex(
            r"\text{Local max at } x = \frac{\pi}{6}: \; f(\pi/6) = 3\sqrt{3} \approx 5.196",
            font_size=22, color=GOLD,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(conclusion1))
        self.wait(3)

        # ══════════════════════════════════════════════════════════
        # Scene 5: Part (2) — Existence proof visualization
        # ══════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])
        part2_title = Text("Part (2): Existence Proof", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(part2_title))

        statement = VGroup(
            MathTex(r"\text{Given } \theta \in (0, \pi), \; a \in \mathbb{R}", font_size=24),
            MathTex(r"\text{Prove: } \exists\, y \in [a-\theta, a+\theta] \text{ s.t. } \cos y \le \cos\theta", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.2).next_to(part2_title, DOWN, buff=0.3)
        for s in statement:
            self.play(Write(s), run_time=0.8)
        self.wait(1)

        # Visualize with cos curve
        axes2 = Axes(
            x_range=[-PI, 3*PI, PI/2], y_range=[-1.5, 1.5, 0.5],
            x_length=10, y_length=4,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.8)
        cos_curve = axes2.plot(lambda x: np.cos(x), x_range=[-PI, 3*PI], color=BLUE, stroke_width=2)
        self.play(Create(axes2), Create(cos_curve))

        # Choose theta = pi/3, a = pi
        theta_val = PI / 3
        a_val = PI
        cos_theta = np.cos(theta_val)

        # Threshold line
        thresh_line = DashedLine(
            axes2.c2p(-PI, cos_theta), axes2.c2p(3*PI, cos_theta),
            color=RED, stroke_width=2,
        )
        thresh_label = MathTex(rf"\cos\theta = \cos(\pi/3) = 0.5", font_size=18, color=RED)
        thresh_label.next_to(axes2.c2p(3*PI, cos_theta), RIGHT, buff=0.1)
        self.play(Create(thresh_line), Write(thresh_label))

        # Interval [a-theta, a+theta]
        left = a_val - theta_val
        right = a_val + theta_val

        interval_rect = Rectangle(
            width=axes2.c2p(right, 0)[0] - axes2.c2p(left, 0)[0],
            height=3.5, fill_color=GREEN, fill_opacity=0.1, stroke_color=GREEN,
        ).move_to(axes2.c2p((left + right)/2, 0))
        iv_label = MathTex(rf"[a-\theta, a+\theta] = [{left/PI:.1f}\pi, {right/PI:.1f}\pi]", font_size=16, color=GREEN)
        iv_label.next_to(interval_rect, UP, buff=0.1)
        self.play(FadeIn(interval_rect), Write(iv_label))

        # Find a point where cos(y) <= cos(theta)
        # cos(pi) = -1 <= 0.5, so y = pi works
        target_y = PI
        target_pt = Dot(axes2.c2p(target_y, np.cos(target_y)), color=GOLD, radius=0.1)
        target_label = MathTex(r"y=\pi: \cos\pi = -1 \le 0.5 \;\checkmark", font_size=18, color=GOLD)
        target_label.next_to(target_pt, DOWN+RIGHT, buff=0.1)
        self.play(FadeIn(target_pt), Write(target_label))
        self.wait(1)

        # Key idea
        idea = VGroup(
            Text("Key insight: The interval [a-theta, a+theta]", font_size=18, color=TEAL),
            Text("has length 2*theta >= 2*min_period_component.", font_size=18, color=TEAL),
            Text("cos(x) must hit cos(theta) or below within any such interval.", font_size=18, color=TEAL),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN, buff=0.3)
        for i in idea:
            self.play(Write(i), run_time=0.6)
        self.wait(2)

        # ══════════════════════════════════════════════════════════
        # Scene 6: Part (3) — min b
        # ══════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])
        part3_title = Text("Part (3): min b for 5cos(x)-cos(5x+phi) <= b", font_size=26, color=BLUE)
        part3_title.to_edge(UP)
        self.play(Write(part3_title))

        # Show family of curves for different phi
        axes3 = Axes(
            x_range=[0, 2*PI, PI/2], y_range=[-7, 7, 2],
            x_length=10, y_length=5.5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.3)
        self.play(Create(axes3))

        colors = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE]
        phi_values = np.linspace(0, PI, 7)

        curves = VGroup()
        for i, phi in enumerate(phi_values):
            curve = axes3.plot(
                lambda x, phi=phi: 5*np.cos(x) - np.cos(5*x + phi),
                x_range=[0, 2*PI], color=colors[i], stroke_width=1.5, stroke_opacity=0.7,
            )
            curves.add(curve)

        family_label = Text("Family of curves for different phi", font_size=18, color=GRAY).to_corner(UL)
        self.play(LaggedStart(*[Create(c) for c in curves], lag_ratio=0.15), Write(family_label), run_time=3)
        self.wait(1)

        # Highlight the max envelope at y = 6
        envelope_line = DashedLine(
            axes3.c2p(0, 6), axes3.c2p(2*PI, 6), color=GOLD, stroke_width=3,
        )
        env_label = MathTex(r"b = 6", font_size=24, color=GOLD).next_to(axes3.c2p(2*PI, 6), RIGHT)
        self.play(Create(envelope_line), Write(env_label))
        self.wait(1)

        # ══════════════════════════════════════════════════════════
        # Scene 7: Analytical solution for Part (3)
        # ══════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])
        anal_title = Text("Part (3): Analytical Solution", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(anal_title))

        solution = VGroup(
            MathTex(r"g(x) = 5\cos x - \cos(5x + \varphi)", font_size=24),
            MathTex(r"\text{Use: } \cos(5x+\varphi) = \cos 5x\cos\varphi - \sin 5x\sin\varphi", font_size=22, color=YELLOW),
            MathTex(r"g(x) = 5\cos x - \cos 5x\cos\varphi + \sin 5x\sin\varphi", font_size=22),
            MathTex(r"\text{For min } b = \min_\varphi \max_x g(x)", font_size=22, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(anal_title, DOWN, buff=0.4)

        for s in solution:
            self.play(Write(s), run_time=0.8)
            self.wait(0.3)
        self.wait(0.5)

        key_step = VGroup(
            MathTex(r"\text{Write } g(x) = 5\cos x + R\cos(5x + \alpha)", font_size=22),
            MathTex(r"\text{where } R = 1, \; \alpha = \pi + \varphi", font_size=22, color=TEAL),
            MathTex(r"\max_x |5\cos x| + \max_x |\cos(5x + \alpha)| = 5 + 1 = 6", font_size=22, color=ORANGE),
            MathTex(r"\text{Can we achieve } g(x) = 6?", font_size=22, color=YELLOW),
            MathTex(r"\text{When } \cos x = 1 \text{ and } \cos(5x+\alpha) = -1 \text{ simultaneously}", font_size=20),
            MathTex(r"x = 0: \cos 0 = 1, \;\cos(0 + \alpha) = -1 \Rightarrow \alpha = \pi", font_size=22, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(solution, DOWN, buff=0.3)

        for k in key_step:
            self.play(Write(k), run_time=0.7)
            self.wait(0.2)

        self.wait(0.5)

        # Verification
        verify = VGroup(
            MathTex(r"\varphi = 0: \; g(0) = 5\cos 0 - \cos 0 = 5 - 1 = 4 < 6", font_size=20, color=GRAY),
            MathTex(r"\text{Key: } b_{\min} = \text{envelope max} = 6", font_size=22, color=GOLD),
            MathTex(r"\text{Verified: when } \varphi = 0, \; g(\pi/6) = 3\sqrt3 < 6", font_size=20),
            MathTex(r"\text{No single } \varphi \text{ achieves } g = 6, \text{ but } \inf_\varphi \sup_x g = 6", font_size=20, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(DOWN, buff=0.3)

        for v in verify:
            self.play(Write(v), run_time=0.6)
            self.wait(0.2)

        final = MathTex(r"\boxed{b_{\min} = 6}", font_size=40, color=GOLD).move_to(ORIGIN)
        big_box = SurroundingRectangle(final, color=GOLD, buff=0.2, corner_radius=0.1)
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.play(Write(final), Create(big_box))
        self.wait(1)

        # ══════════════════════════════════════════════════════════
        # Scene 8: Final verification graph
        # ══════════════════════════════════════════════════════════
        self.play(final.animate.scale(0.6).to_corner(UL), FadeOut(big_box))

        axes4 = Axes(
            x_range=[-PI, PI, PI/4], y_range=[-7, 7, 2],
            x_length=10, y_length=5.5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.3)
        self.play(Create(axes4))

        # Animate phi changing and curve morphing
        phi_tracker = ValueTracker(0)

        dynamic_curve = always_redraw(lambda: axes4.plot(
            lambda x: 5*np.cos(x) - np.cos(5*x + phi_tracker.get_value()),
            x_range=[-PI, PI], color=BLUE, stroke_width=3,
        ))
        phi_label = always_redraw(lambda: MathTex(
            rf"\varphi = {phi_tracker.get_value():.2f}",
            font_size=22, color=YELLOW,
        ).to_corner(UR))

        max_line = DashedLine(axes4.c2p(-PI, 6), axes4.c2p(PI, 6), color=GOLD, stroke_width=2)
        max_lab = MathTex("b = 6", font_size=20, color=GOLD).next_to(axes4.c2p(PI, 6), RIGHT)

        self.add(dynamic_curve, phi_label)
        self.play(Create(max_line), Write(max_lab))

        # Sweep phi from 0 to 2π
        self.play(phi_tracker.animate.set_value(2*PI), run_time=8, rate_func=linear)
        self.wait(0.5)

        sweep_note = Text(
            "For all phi, curve stays below b=6 envelope",
            font_size=20, color=GOLD,
        ).to_edge(DOWN)
        self.play(Write(sweep_note))
        self.wait(3)

