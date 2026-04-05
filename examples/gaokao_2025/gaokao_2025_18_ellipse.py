# 2025 Gaokao I - Problem 18: Ellipse (Conic Section)
from manim import *
import numpy as np

class Gaokao2025_18_Ellipse(Scene):
    def construct(self):
        # ══════════════════════════════════════════════════════════
        # Scene 1: Title & Problem
        # ══════════════════════════════════════════════════════════
        title = Text("2025 New Gaokao I — Problem 18", font_size=36, color=GOLD)
        sub = Text("Conic Section: Ellipse", font_size=24, color=GRAY)
        sub.next_to(title, DOWN, buff=0.2)
        self.play(Write(title), FadeIn(sub))
        self.wait(1.5)

        problem = VGroup(
            MathTex(r"C: \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \;\;(a>b>0)", font_size=24),
            Text("A = lower vertex, B = right vertex", font_size=18),
            MathTex(r"|AB| = \sqrt{10}, \quad e = \frac{2\sqrt{2}}{3}", font_size=24, color=YELLOW),
        ).arrange(DOWN, buff=0.15).next_to(sub, DOWN, buff=0.3)
        for p in problem:
            self.play(Write(p), run_time=0.7)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ══════════════════════════════════════════════════════════
        # Scene 2: Part (1) — Find the equation
        # ══════════════════════════════════════════════════════════
        part1 = Text("Part (1): Find the equation of ellipse C", font_size=30, color=BLUE)
        part1.to_edge(UP)
        self.play(Write(part1))

        steps = VGroup(
            MathTex(r"A = (0, -b), \quad B = (a, 0)", font_size=26),
            MathTex(r"|AB| = \sqrt{a^2 + b^2} = \sqrt{10}", font_size=26, color=YELLOW),
            MathTex(r"\Rightarrow a^2 + b^2 = 10 \quad \cdots (1)", font_size=26),
            MathTex(r"e = \frac{c}{a} = \frac{2\sqrt{2}}{3} \Rightarrow c = \frac{2\sqrt{2}}{3}a", font_size=26, color=GREEN),
            MathTex(r"c^2 = a^2 - b^2 = \frac{8}{9}a^2 \Rightarrow b^2 = \frac{a^2}{9} \quad \cdots (2)", font_size=24, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(part1, DOWN, buff=0.5)

        for s in steps:
            self.play(Write(s), run_time=0.8)
            self.wait(0.3)
        self.wait(0.5)

        # Solve
        solve = VGroup(
            MathTex(r"\text{Substituting (2) into (1):}", font_size=22, color=GRAY),
            MathTex(r"a^2 + \frac{a^2}{9} = 10 \Rightarrow \frac{10a^2}{9} = 10 \Rightarrow a^2 = 9", font_size=26, color=YELLOW),
            MathTex(r"b^2 = 10 - 9 = 1", font_size=26, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(steps, DOWN, buff=0.3)

        for s in solve:
            self.play(Write(s), run_time=0.7)

        answer1 = MathTex(
            r"\boxed{\frac{x^2}{9} + y^2 = 1}",
            font_size=36, color=GOLD,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(answer1))
        self.wait(2)

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ══════════════════════════════════════════════════════════
        # Scene 3: Draw the ellipse
        # ══════════════════════════════════════════════════════════
        draw_title = Text("Visualizing the Ellipse", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(draw_title))

        a_val, b_val = 3.0, 1.0
        c_val = np.sqrt(a_val**2 - b_val**2)

        axes = Axes(
            x_range=[-5, 5, 1], y_range=[-2.5, 2.5, 1],
            x_length=10, y_length=5,
            axis_config={"include_tip": True},
        )
        self.play(Create(axes))

        ellipse = ParametricFunction(
            lambda t: axes.c2p(a_val * np.cos(t), b_val * np.sin(t)),
            t_range=[0, 2*PI], color=BLUE, stroke_width=3,
        )
        self.play(Create(ellipse), run_time=2)

        eq_label = MathTex(r"\frac{x^2}{9} + y^2 = 1", font_size=22, color=BLUE).to_corner(UR)
        self.play(Write(eq_label))

        # Mark key points
        A_pt = axes.c2p(0, -1)
        B_pt = axes.c2p(3, 0)
        F1_pt = axes.c2p(-c_val, 0)
        F2_pt = axes.c2p(c_val, 0)
        O_pt = axes.c2p(0, 0)

        for pt, name, color in [
            (A_pt, "A(0,-1)", RED), (B_pt, "B(3,0)", GREEN),
            (F1_pt, "F_1", ORANGE), (F2_pt, "F_2", ORANGE),
        ]:
            dot = Dot(pt, color=color, radius=0.06)
            label = MathTex(name, font_size=16, color=color)
            if "A" in name:
                label.next_to(dot, DOWN+LEFT, buff=0.1)
            elif "B" in name:
                label.next_to(dot, UP+RIGHT, buff=0.1)
            else:
                label.next_to(dot, DOWN, buff=0.1)
            self.play(FadeIn(dot), Write(label), run_time=0.4)

        # |AB| line
        ab_line = DashedLine(A_pt, B_pt, color=YELLOW, stroke_width=2)
        ab_label = MathTex(r"|AB|=\sqrt{10}", font_size=18, color=YELLOW).move_to((np.array(A_pt)+np.array(B_pt))/2 + RIGHT*0.8)
        self.play(Create(ab_line), Write(ab_label))
        self.wait(1)

        # Eccentricity info
        ecc_info = VGroup(
            MathTex(r"a=3,\; b=1,\; c=2\sqrt{2}", font_size=20),
            MathTex(r"e = \frac{2\sqrt{2}}{3} \approx 0.943", font_size=20, color=ORANGE),
        ).arrange(DOWN, buff=0.1).to_corner(UL)
        for e in ecc_info:
            self.play(Write(e), run_time=0.5)
        self.wait(1.5)

        # ══════════════════════════════════════════════════════════
        # Scene 4: Part (2)(i) — Point R on ray AP
        # ══════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])
        part2i = Text("Part (2)(i): Point R on ray AP with |AR|*|AP| = 3", font_size=26, color=BLUE)
        part2i.to_edge(UP)
        self.play(Write(part2i))

        derivation = VGroup(
            MathTex(r"A = (0, -1), \;\; P = (m, n)", font_size=24),
            MathTex(r"\vec{AP} = (m, n+1)", font_size=24, color=YELLOW),
            MathTex(r"|AP| = \sqrt{m^2 + (n+1)^2}", font_size=24),
            MathTex(r"R \text{ on ray } AP: \; R = A + t \cdot \vec{AP}, \; t > 0", font_size=22),
            MathTex(r"|AR| = t \cdot |AP|", font_size=24, color=GREEN),
            MathTex(r"|AR| \cdot |AP| = 3 \Rightarrow t \cdot |AP|^2 = 3", font_size=24, color=ORANGE),
            MathTex(r"t = \frac{3}{m^2 + (n+1)^2}", font_size=24, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(part2i, DOWN, buff=0.4)

        for d in derivation:
            self.play(Write(d), run_time=0.7)
            self.wait(0.2)

        self.wait(0.5)

        result_r = VGroup(
            MathTex(r"R = \left(\frac{3m}{m^2+(n+1)^2}, \;\; \frac{3(n+1)}{m^2+(n+1)^2} - 1\right)", font_size=22, color=GOLD),
        ).next_to(derivation, DOWN, buff=0.3)
        box_r = SurroundingRectangle(result_r, color=GOLD, buff=0.1)
        self.play(Write(result_r[0]), Create(box_r))
        self.wait(2)

        # ══════════════════════════════════════════════════════════
        # Scene 5: Geometric illustration of Part (2)(i)
        # ══════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])
        vis_title = Text("Geometric View: Ray AP and Point R", font_size=28, color=BLUE).to_edge(UP)
        self.play(Write(vis_title))

        axes2 = Axes(
            x_range=[-5, 5, 1], y_range=[-2.5, 2.5, 1],
            x_length=10, y_length=5,
            axis_config={"include_tip": True},
        )
        ellipse2 = ParametricFunction(
            lambda t: axes2.c2p(3*np.cos(t), np.sin(t)),
            t_range=[0, 2*PI], color=BLUE, stroke_width=2,
        )
        self.play(Create(axes2), Create(ellipse2))

        # Example: P = (2, 1)
        m_val, n_val = 2.0, 1.0
        A_pos = axes2.c2p(0, -1)
        P_pos = axes2.c2p(m_val, n_val)

        t_val = 3.0 / (m_val**2 + (n_val+1)**2)
        R_x = t_val * m_val
        R_y = t_val * (n_val + 1) - 1
        R_pos = axes2.c2p(R_x, R_y)

        A_dot = Dot(A_pos, color=RED, radius=0.08)
        P_dot = Dot(P_pos, color=GREEN, radius=0.08)
        R_dot = Dot(R_pos, color=GOLD, radius=0.08)

        # Ray AP extended
        ray_dir = np.array(P_pos) - np.array(A_pos)
        ray_end = np.array(A_pos) + 2 * ray_dir
        ray = Arrow(A_pos, ray_end, color=GRAY, stroke_width=2, buff=0)

        self.play(FadeIn(A_dot), FadeIn(P_dot))
        self.play(Create(ray))
        self.play(FadeIn(R_dot))

        # Labels
        a_lab = MathTex("A(0,-1)", font_size=16, color=RED).next_to(A_dot, DL, buff=0.1)
        p_lab = MathTex("P(2,1)", font_size=16, color=GREEN).next_to(P_dot, UR, buff=0.1)
        r_lab = MathTex(f"R({R_x:.2f},{R_y:.2f})", font_size=16, color=GOLD).next_to(R_dot, DOWN, buff=0.1)
        self.play(Write(a_lab), Write(p_lab), Write(r_lab))

        # Show |AR| and |AP|
        ar_brace = BraceBetweenPoints(A_pos, R_pos, direction=normalize(np.array([ray_dir[1], -ray_dir[0], 0])))
        ar_val = np.linalg.norm(np.array(R_pos) - np.array(A_pos))
        ap_val = np.linalg.norm(np.array(P_pos) - np.array(A_pos))
        check = MathTex(
            rf"|AR| \times |AP| = {ar_val:.2f} \times {ap_val:.2f} = {ar_val*ap_val:.2f} \approx 3",
            font_size=18, color=GOLD,
        ).to_edge(DOWN)
        self.play(Write(check))
        self.wait(2)

        # ══════════════════════════════════════════════════════════
        # Scene 6: Part (2)(ii) — |PM| maximum
        # ══════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])
        part2ii = Text("Part (2)(ii): k1 = 3*k2, find max |PM|", font_size=26, color=BLUE)
        part2ii.to_edge(UP)
        self.play(Write(part2ii))

        explanation = VGroup(
            MathTex(r"\text{Q on ellipse C, O = origin}", font_size=22),
            MathTex(r"k_{OQ} = k_1, \quad k_{OP} = k_2, \quad k_1 = 3k_2", font_size=22, color=YELLOW),
            MathTex(r"\text{Let } Q = (3\cos\theta, \sin\theta) \text{ on ellipse}", font_size=22),
            MathTex(r"k_1 = \frac{\sin\theta}{3\cos\theta}, \quad k_2 = \frac{k_1}{3} = \frac{\sin\theta}{9\cos\theta}", font_size=22, color=GREEN),
            MathTex(r"\text{P is on line } y = \frac{\sin\theta}{9\cos\theta} x", font_size=22),
            MathTex(r"\text{M on ellipse, maximize } |PM|", font_size=22, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(part2ii, DOWN, buff=0.3)

        for e in explanation:
            self.play(Write(e), run_time=0.7)
            self.wait(0.2)

        self.wait(1)

        # Key insight
        insight = VGroup(
            MathTex(r"|PM|_{\max} = \sqrt{m^2 + (n+1)^2} + 1", font_size=24, color=GOLD),
            Text("(distance from P to center of ellipse-related circle + semi-axis)", font_size=16, color=GRAY),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN, buff=0.5)
        box2 = SurroundingRectangle(insight[0], color=GOLD, buff=0.1)
        self.play(Write(insight[0]), Write(insight[1]), Create(box2))
        self.wait(2)

        # ══════════════════════════════════════════════════════════
        # Scene 7: Animated demonstration
        # ══════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])
        demo_title = Text("Animation: Point M traverses ellipse", font_size=28, color=BLUE).to_edge(UP)
        self.play(Write(demo_title))

        axes3 = Axes(
            x_range=[-5, 5, 1], y_range=[-2.5, 2.5, 1],
            x_length=10, y_length=5, axis_config={"include_tip": True},
        )
        ellipse3 = ParametricFunction(
            lambda t: axes3.c2p(3*np.cos(t), np.sin(t)),
            t_range=[0, 2*PI], color=BLUE, stroke_width=2,
        )
        self.play(Create(axes3), Create(ellipse3))

        # Fix P = (1, 1/3) as an example satisfying k1=3k2
        P_ex = axes3.c2p(1, 1/3)
        p_dot_ex = Dot(P_ex, color=GREEN, radius=0.08)
        p_lab_ex = MathTex("P", font_size=20, color=GREEN).next_to(p_dot_ex, UR, buff=0.1)
        self.play(FadeIn(p_dot_ex), Write(p_lab_ex))

        # M moves on ellipse, track |PM|
        theta_tracker = ValueTracker(0)

        m_dot = always_redraw(lambda: Dot(
            axes3.c2p(3*np.cos(theta_tracker.get_value()), np.sin(theta_tracker.get_value())),
            color=RED, radius=0.07,
        ))
        pm_line = always_redraw(lambda: DashedLine(
            P_ex,
            axes3.c2p(3*np.cos(theta_tracker.get_value()), np.sin(theta_tracker.get_value())),
            color=YELLOW, stroke_width=2,
        ))

        def get_dist_label():
            mx = 3*np.cos(theta_tracker.get_value())
            my = np.sin(theta_tracker.get_value())
            dist = np.sqrt((mx - 1)**2 + (my - 1/3)**2)
            return MathTex(
                rf"|PM| = {dist:.2f}", font_size=20, color=YELLOW,
            ).to_edge(DOWN)

        dist_label = always_redraw(get_dist_label)

        self.add(m_dot, pm_line, dist_label)
        self.play(theta_tracker.animate.set_value(2*PI), run_time=8, rate_func=linear)
        self.wait(1)

        # Mark the farthest point
        # Max distance occurs approximately when M is diametrically opposite to P
        max_theta = PI + np.arctan2(1/3, 1/3)  # approximate
        dists = [(3*np.cos(t) - 1)**2 + (np.sin(t) - 1/3)**2 for t in np.linspace(0, 2*PI, 1000)]
        max_idx = np.argmax(dists)
        max_t = np.linspace(0, 2*PI, 1000)[max_idx]
        max_mx, max_my = 3*np.cos(max_t), np.sin(max_t)
        max_dist = np.sqrt(dists[max_idx])

        max_dot = Dot(axes3.c2p(max_mx, max_my), color=GOLD, radius=0.1)
        max_label = MathTex(
            rf"|PM|_{{\max}} \approx {max_dist:.2f}",
            font_size=22, color=GOLD,
        ).next_to(max_dot, DL, buff=0.2)
        max_line = Line(P_ex, axes3.c2p(max_mx, max_my), color=GOLD, stroke_width=3)

        self.play(FadeIn(max_dot), Write(max_label), Create(max_line))
        self.wait(3)

