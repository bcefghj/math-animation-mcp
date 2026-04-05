# 2024 Gaokao Analytic Geometry — GRAPHICS-FIRST, long (~3min)
# Ellipse x²/4 + y²/3 = 1 (a=2, b=√3, c=1)
# Chord through focus, triangle area with origin, |PF1|+|PF2|=2a
from manim import *
import numpy as np

class Gaokao2024_Conic_Long(Scene):
    def construct(self):
        tag = Text("2024 Gaokao · Conic Section (Ellipse)", font_size=22, color=GOLD).to_edge(UP, buff=0.2)
        self.play(Write(tag), run_time=0.6)

        a_val, b_val = 2.0, np.sqrt(3)
        c_val = 1.0

        # ── Full-screen axes ──
        axes = Axes(
            x_range=[-3.5, 3.5, 1], y_range=[-2.8, 2.8, 1],
            x_length=10, y_length=6.5,
            axis_config={"include_tip": True, "stroke_width": 1, "tick_size": 0.05},
        ).shift(DOWN * 0.1)
        self.play(Create(axes), run_time=1)

        # ── Step 1: Draw the ellipse gradually ──
        step = Text("Drawing the ellipse", font_size=13, color=TEAL).to_corner(UR, buff=0.2)
        self.play(Write(step), run_time=0.2)

        ellipse = ParametricFunction(
            lambda t: axes.c2p(a_val * np.cos(t), b_val * np.sin(t)),
            t_range=[0, 2 * PI], color=BLUE, stroke_width=3,
        )
        # Trace a dot along the ellipse
        trace_dot = Dot(axes.c2p(a_val, 0), color=YELLOW, radius=0.05)
        self.play(Create(ellipse), MoveAlongPath(trace_dot, ellipse), run_time=3)
        self.play(FadeOut(trace_dot))

        eq = MathTex(r"\frac{x^2}{4}+\frac{y^2}{3}=1", font_size=16, color=BLUE).to_corner(UL, buff=0.3).shift(DOWN*0.5)
        self.play(Write(eq))
        self.play(FadeOut(step))

        # ── Step 2: Mark key points ──
        step2 = Text("Key points", font_size=13, color=TEAL).to_corner(UR, buff=0.2)
        self.play(Write(step2), run_time=0.2)

        F1, F2 = axes.c2p(-c_val, 0), axes.c2p(c_val, 0)
        f1d, f2d = Dot(F1, color=RED, radius=0.06), Dot(F2, color=RED, radius=0.06)
        f1l = MathTex("F_1(-1,0)", font_size=11, color=RED).next_to(f1d, DL, buff=0.05)
        f2l = MathTex("F_2(1,0)", font_size=11, color=RED).next_to(f2d, DR, buff=0.05)
        self.play(FadeIn(f1d), FadeIn(f2d), Write(f1l), Write(f2l), run_time=0.6)

        O_dot = Dot(axes.c2p(0, 0), color=WHITE, radius=0.04)
        O_lab = MathTex("O", font_size=11, color=WHITE).next_to(O_dot, DL, buff=0.04)
        self.play(FadeIn(O_dot), Write(O_lab), run_time=0.3)

        # Vertices
        verts_pts = [(a_val, 0), (-a_val, 0), (0, b_val), (0, -b_val)]
        for x, y in verts_pts:
            vd = Dot(axes.c2p(x, y), color=WHITE, radius=0.04)
            self.play(FadeIn(vd), run_time=0.1)

        # Semi-major/minor axes
        a_brace = BraceBetweenPoints(axes.c2p(0, 0), axes.c2p(a_val, 0), direction=DOWN, color=GREEN)
        a_txt = MathTex("a=2", font_size=12, color=GREEN).next_to(a_brace, DOWN, buff=0.05)
        b_brace = BraceBetweenPoints(axes.c2p(0, 0), axes.c2p(0, b_val), direction=LEFT, color=PURPLE)
        b_txt = MathTex(r"b=\sqrt{3}", font_size=12, color=PURPLE).next_to(b_brace, LEFT, buff=0.05)
        self.play(Create(a_brace), Write(a_txt), Create(b_brace), Write(b_txt), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(a_brace), FadeOut(a_txt), FadeOut(b_brace), FadeOut(b_txt), FadeOut(step2))

        # ── Step 3: Focal chord sweeping ──
        step3 = Text("Chord through F1 sweeps", font_size=13, color=TEAL).to_corner(UR, buff=0.2)
        self.play(Write(step3), run_time=0.2)

        slope_tr = ValueTracker(0.5)

        def chord_pts(k):
            A_c = 3 + 4*k**2
            B_c = 8*k**2
            C_c = 4*k**2 - 12
            disc = B_c**2 - 4*A_c*C_c
            if disc < 0:
                return None
            x1 = (-B_c + np.sqrt(disc)) / (2*A_c)
            x2 = (-B_c - np.sqrt(disc)) / (2*A_c)
            return (x1, k*(x1+1)), (x2, k*(x2+1))

        chord_line = always_redraw(lambda: self._mk_chord(axes, slope_tr.get_value()))
        tri_fill = always_redraw(lambda: self._mk_tri(axes, slope_tr.get_value()))
        area_lbl = always_redraw(lambda: self._mk_area(axes, slope_tr.get_value()))
        dot_A = always_redraw(lambda: self._mk_dot(axes, slope_tr.get_value(), 0))
        dot_B = always_redraw(lambda: self._mk_dot(axes, slope_tr.get_value(), 1))

        self.add(tri_fill, chord_line, dot_A, dot_B, area_lbl)

        # Slow sweep
        self.play(slope_tr.animate.set_value(5), run_time=4, rate_func=smooth)
        self.play(slope_tr.animate.set_value(-5), run_time=4, rate_func=smooth)
        self.play(slope_tr.animate.set_value(1), run_time=2, rate_func=smooth)
        self.wait(1)
        self.play(FadeOut(step3))

        # ── Step 4: Special case — vertical chord x=-1 ──
        step4 = Text("Special case: x = -1 (vertical)", font_size=13, color=TEAL).to_corner(UR, buff=0.2)
        self.play(Write(step4), run_time=0.2)

        self.play(FadeOut(chord_line), FadeOut(tri_fill), FadeOut(area_lbl), FadeOut(dot_A), FadeOut(dot_B))

        y_at_neg1 = b_val * np.sqrt(1 - (1/a_val)**2)  # sqrt(3) * sqrt(3/4) = 3/2
        P_top = axes.c2p(-1, y_at_neg1)
        P_bot = axes.c2p(-1, -y_at_neg1)
        vert_chord = Line(P_top, P_bot, color=YELLOW, stroke_width=3)
        pd_top = Dot(P_top, color=YELLOW, radius=0.06)
        pd_bot = Dot(P_bot, color=YELLOW, radius=0.06)
        self.play(Create(vert_chord), FadeIn(pd_top), FadeIn(pd_bot))

        # Triangle OAB
        O_pos = axes.c2p(0, 0)
        tri_vert = Polygon(O_pos, P_top, P_bot, fill_color=GREEN, fill_opacity=0.25, stroke_color=GREEN, stroke_width=1.5)
        self.play(FadeIn(tri_vert))

        # Distance from O to chord = 1, chord length = 2*y_at_neg1 = 3
        base_brace = BraceBetweenPoints(P_bot, P_top, direction=LEFT, color=YELLOW)
        base_txt = MathTex(rf"|AB|={2*y_at_neg1:.1f}", font_size=12, color=YELLOW).next_to(base_brace, LEFT, buff=0.05)
        h_line = DashedLine(O_pos, axes.c2p(-1, 0), color=GREEN, stroke_width=1.5)
        h_txt = MathTex("d=1", font_size=12, color=GREEN).next_to(h_line, UP, buff=0.05)
        self.play(Create(base_brace), Write(base_txt), Create(h_line), Write(h_txt), run_time=0.8)

        area_val = 0.5 * 2 * y_at_neg1 * 1
        area_eq = MathTex(rf"S = \frac{{1}}{{2}} \times {2*y_at_neg1:.1f} \times 1 = {area_val:.2f}",
                          font_size=16, color=GOLD).to_edge(DOWN, buff=0.3)
        abox = SurroundingRectangle(area_eq, color=GOLD, buff=0.08)
        self.play(Write(area_eq), Create(abox))
        self.wait(2)

        self.play(*[FadeOut(m) for m in [vert_chord, pd_top, pd_bot, tri_vert, base_brace, base_txt,
                                          h_line, h_txt, area_eq, abox, step4]])

        # ── Step 5: |PF1| + |PF2| = 2a animation ──
        step5 = Text("|PF1|+|PF2| = 2a property", font_size=13, color=TEAL).to_corner(UR, buff=0.2)
        self.play(Write(step5), run_time=0.2)

        theta_tr = ValueTracker(0)

        def p_pos(t):
            return axes.c2p(a_val * np.cos(t), b_val * np.sin(t))

        p_dot = always_redraw(lambda: Dot(p_pos(theta_tr.get_value()), color=YELLOW, radius=0.06))
        pf1 = always_redraw(lambda: Line(F1, p_pos(theta_tr.get_value()), color=GREEN, stroke_width=2))
        pf2 = always_redraw(lambda: Line(F2, p_pos(theta_tr.get_value()), color=PURPLE, stroke_width=2))

        def dist_sum():
            t = theta_tr.get_value()
            px, py = a_val*np.cos(t), b_val*np.sin(t)
            d1 = np.sqrt((px+c_val)**2 + py**2)
            d2 = np.sqrt((px-c_val)**2 + py**2)
            return d1, d2

        sum_lbl = always_redraw(lambda: MathTex(
            rf"|PF_1|={dist_sum()[0]:.2f},\;|PF_2|={dist_sum()[1]:.2f},\;\Sigma={dist_sum()[0]+dist_sum()[1]:.2f}",
            font_size=13, color=GOLD,
        ).to_edge(DOWN, buff=0.3))

        # P trace path
        trace = TracedPath(lambda: p_pos(theta_tr.get_value()), stroke_color=YELLOW, stroke_width=1, stroke_opacity=0.5)

        self.add(p_dot, pf1, pf2, sum_lbl, trace)
        self.play(theta_tr.animate.set_value(2 * PI), run_time=8, rate_func=linear)

        const_box = MathTex(r"|PF_1|+|PF_2| = 2a = 4 \;\forall P", font_size=18, color=GOLD)
        const_box.to_edge(DOWN, buff=0.3)
        cbox = SurroundingRectangle(const_box, color=GOLD, buff=0.08)
        self.play(FadeOut(sum_lbl), Write(const_box), Create(cbox))
        self.wait(1)

        self.play(FadeOut(step5))

        # ── Step 6: Eccentricity visualization ──
        step6 = Text("Eccentricity e = c/a", font_size=13, color=TEAL).to_corner(UR, buff=0.2)
        self.play(Write(step6), run_time=0.2)

        e_val = c_val / a_val
        # Draw a-line, c-line from center
        a_line = Line(axes.c2p(0, 0), axes.c2p(a_val, 0), color=GREEN, stroke_width=2.5)
        c_line = Line(axes.c2p(0, 0), axes.c2p(c_val, 0), color=RED, stroke_width=2.5)
        a_lab = MathTex("a=2", font_size=12, color=GREEN).next_to(a_line, UP, buff=0.05)
        c_lab = MathTex("c=1", font_size=12, color=RED).next_to(c_line, DOWN, buff=0.05)
        self.play(Create(a_line), Write(a_lab), Create(c_line), Write(c_lab), run_time=0.8)

        e_eq = MathTex(rf"e = \frac{{c}}{{a}} = \frac{{1}}{{2}} = {e_val:.1f}", font_size=18, color=GOLD)
        e_eq.to_edge(DOWN, buff=0.5)
        self.play(Write(e_eq))
        self.wait(3)

    def _mk_chord(self, axes, k):
        if abs(k) < 0.05:
            return VMobject()
        A_c = 3 + 4*k**2
        B_c = 8*k**2
        C_c = 4*k**2 - 12
        disc = B_c**2 - 4*A_c*C_c
        if disc < 0:
            return VMobject()
        x1 = (-B_c + np.sqrt(disc)) / (2*A_c)
        x2 = (-B_c - np.sqrt(disc)) / (2*A_c)
        return Line(axes.c2p(x1, k*(x1+1)), axes.c2p(x2, k*(x2+1)), color=YELLOW, stroke_width=2)

    def _mk_tri(self, axes, k):
        if abs(k) < 0.05:
            return VMobject()
        A_c = 3 + 4*k**2
        B_c = 8*k**2
        C_c = 4*k**2 - 12
        disc = B_c**2 - 4*A_c*C_c
        if disc < 0:
            return VMobject()
        x1 = (-B_c + np.sqrt(disc)) / (2*A_c)
        x2 = (-B_c - np.sqrt(disc)) / (2*A_c)
        return Polygon(
            axes.c2p(0, 0), axes.c2p(x1, k*(x1+1)), axes.c2p(x2, k*(x2+1)),
            fill_color=GREEN, fill_opacity=0.15, stroke_color=GREEN, stroke_width=1,
        )

    def _mk_area(self, axes, k):
        if abs(k) < 0.05:
            return VMobject()
        A_c = 3 + 4*k**2
        B_c = 8*k**2
        C_c = 4*k**2 - 12
        disc = B_c**2 - 4*A_c*C_c
        if disc < 0:
            return VMobject()
        x1 = (-B_c + np.sqrt(disc)) / (2*A_c)
        x2 = (-B_c - np.sqrt(disc)) / (2*A_c)
        y1, y2 = k*(x1+1), k*(x2+1)
        area = abs(x1*y2 - x2*y1) / 2
        return MathTex(rf"S = {area:.2f}", font_size=14, color=GOLD).to_edge(DOWN, buff=0.3)

    def _mk_dot(self, axes, k, idx):
        if abs(k) < 0.05:
            return VMobject()
        A_c = 3 + 4*k**2
        B_c = 8*k**2
        C_c = 4*k**2 - 12
        disc = B_c**2 - 4*A_c*C_c
        if disc < 0:
            return VMobject()
        x1 = (-B_c + np.sqrt(disc)) / (2*A_c)
        x2 = (-B_c - np.sqrt(disc)) / (2*A_c)
        xs = [x1, x2]
        ys = [k*(x1+1), k*(x2+1)]
        return Dot(axes.c2p(xs[idx], ys[idx]), color=YELLOW, radius=0.05)
