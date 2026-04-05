# 2024 Gaokao Derivative — GRAPHICS-FIRST, long (~3min)
# f(x) = e^x - ax - 1, study monotonicity, extrema, f(x)>=0 proof
# Focus: curves always visible, tangent line sweeping, parameter a scanning
from manim import *
import numpy as np

class Gaokao2024_Deriv_Long(Scene):
    def construct(self):
        tag = Text("2024 Gaokao · Derivative & Function", font_size=22, color=GOLD).to_edge(UP, buff=0.2)
        self.play(Write(tag), run_time=0.6)

        # ── Full-screen coordinate system ──
        axes = Axes(
            x_range=[-3.5, 3.5, 1], y_range=[-2, 7, 1],
            x_length=10.5, y_length=6.5,
            axis_config={"include_tip": True, "stroke_width": 1, "tick_size": 0.05},
        ).shift(DOWN * 0.1)
        self.play(Create(axes), run_time=0.8)

        # ══════════════════════════════════════════
        # Part A: f(x) = e^x - x - 1  (a = 1)
        # ══════════════════════════════════════════
        step_a = Text("f(x) = e^x - x - 1", font_size=14, color=TEAL).to_corner(UR, buff=0.2)
        self.play(Write(step_a), run_time=0.3)

        f1 = lambda x: np.exp(x) - x - 1
        f1p = lambda x: np.exp(x) - 1

        curve1 = axes.plot(f1, x_range=[-3, 2.5], color=BLUE, stroke_width=3)
        trace_d = Dot(axes.c2p(-3, f1(-3)), color=BLUE, radius=0.04)
        self.play(Create(curve1), MoveAlongPath(trace_d, curve1), run_time=3)
        self.play(FadeOut(trace_d))

        eq_label = MathTex(r"f(x)=e^x - x - 1", font_size=16, color=BLUE).to_corner(UL, buff=0.3).shift(DOWN*0.5)
        self.play(Write(eq_label))

        # ── f'(x) = e^x - 1 ──
        fp_curve = axes.plot(f1p, x_range=[-3, 2.2], color=YELLOW, stroke_width=2, stroke_opacity=0.7)
        fp_label = MathTex(r"f'(x)=e^x-1", font_size=13, color=YELLOW).next_to(eq_label, DOWN, buff=0.1)
        self.play(Create(fp_curve), Write(fp_label), run_time=1.5)

        # Zero of f' at x=0
        zero_dot = Dot(axes.c2p(0, 0), color=RED, radius=0.07)
        zero_lab = MathTex(r"f'(0)=0", font_size=11, color=RED).next_to(zero_dot, DR, buff=0.05)
        self.play(FadeIn(zero_dot), Write(zero_lab), run_time=0.4)
        self.wait(0.5)

        # ── Tangent line sweeping along the curve ──
        step_tang = Text("Tangent line sweeps", font_size=13, color=TEAL).to_corner(UR, buff=0.2)
        self.play(FadeOut(step_a), Write(step_tang), run_time=0.3)

        x_tr = ValueTracker(-2.5)
        tang_line = always_redraw(lambda: self._tangent(axes, f1, f1p, x_tr.get_value()))
        tang_dot = always_redraw(lambda: Dot(
            axes.c2p(x_tr.get_value(), f1(x_tr.get_value())), color=ORANGE, radius=0.05
        ))
        slope_lbl = always_redraw(lambda: MathTex(
            rf"k={f1p(x_tr.get_value()):.2f}", font_size=12, color=ORANGE,
        ).next_to(axes.c2p(x_tr.get_value(), f1(x_tr.get_value())), UR, buff=0.15))

        self.add(tang_line, tang_dot, slope_lbl)
        self.play(x_tr.animate.set_value(2.2), run_time=6, rate_func=smooth)
        self.wait(0.5)
        self.play(FadeOut(tang_line), FadeOut(tang_dot), FadeOut(slope_lbl))
        self.play(FadeOut(step_tang))

        # ── Monotonicity regions ──
        step_mono = Text("Monotonicity analysis", font_size=13, color=TEAL).to_corner(UR, buff=0.2)
        self.play(Write(step_mono), run_time=0.2)

        # f' < 0 region: x < 0, shade under f' curve
        zero_line = axes.plot(lambda x: 0, x_range=[-3, 2.5], color=GRAY, stroke_width=0.5)
        dec_shade = axes.get_area(fp_curve, x_range=[-2.8, 0], bounded_graph=zero_line, color=RED, opacity=0.12)
        inc_shade = axes.get_area(fp_curve, x_range=[0, 2.0], bounded_graph=zero_line, color=GREEN, opacity=0.12)

        dec_arr = Arrow(axes.c2p(-1.5, 2), axes.c2p(-0.5, 0.5), color=RED, stroke_width=2, buff=0,
                        max_tip_length_to_length_ratio=0.15)
        inc_arr = Arrow(axes.c2p(0.5, 0.5), axes.c2p(1.5, 3), color=GREEN, stroke_width=2, buff=0,
                        max_tip_length_to_length_ratio=0.15)
        dec_txt = MathTex(r"f'\!<\!0,\;\downarrow", font_size=13, color=RED).next_to(dec_arr, UP, buff=0.05)
        inc_txt = MathTex(r"f'\!>\!0,\;\uparrow", font_size=13, color=GREEN).next_to(inc_arr, UP, buff=0.05)

        self.play(FadeIn(dec_shade), FadeIn(inc_shade), run_time=0.6)
        self.play(GrowArrow(dec_arr), Write(dec_txt), run_time=0.5)
        self.play(GrowArrow(inc_arr), Write(inc_txt), run_time=0.5)

        # Minimum at x=0
        min_dot = Dot(axes.c2p(0, 0), color=GOLD, radius=0.08)
        min_lab = MathTex(r"f_{\min}=f(0)=0", font_size=13, color=GOLD).next_to(min_dot, DOWN, buff=0.15)
        self.play(FadeIn(min_dot), Write(min_lab), Flash(min_dot, color=GOLD))
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in [dec_shade, inc_shade, dec_arr, inc_arr, dec_txt, inc_txt, step_mono]])

        # ── f(x) >= 0 proof: shade area ──
        step_proof = Text("f(x) >= 0 for all x", font_size=13, color=TEAL).to_corner(UR, buff=0.2)
        self.play(Write(step_proof), run_time=0.2)

        x_axis_line = DashedLine(axes.c2p(-3.5, 0), axes.c2p(3.5, 0), color=GRAY, stroke_width=1)
        above_shade = axes.get_area(curve1, x_range=[-2.8, 2.3], bounded_graph=zero_line, color=BLUE, opacity=0.12)
        self.play(Create(x_axis_line), FadeIn(above_shade), run_time=0.8)

        ineq = MathTex(r"e^x \ge x + 1, \;\forall x \in \mathbb{R}", font_size=18, color=GOLD)
        ineq.to_edge(DOWN, buff=0.3)
        ibox = SurroundingRectangle(ineq, color=GOLD, buff=0.08)
        self.play(Write(ineq), Create(ibox))
        self.wait(2)

        self.play(*[FadeOut(m) for m in [above_shade, x_axis_line, ineq, ibox, step_proof,
                                          fp_curve, fp_label, zero_dot, zero_lab, min_dot, min_lab]])

        # ══════════════════════════════════════════
        # Part B: Parameter scanning f(x) = e^x - ax - 1
        # ══════════════════════════════════════════
        step_b = Text("Parameter a scanning", font_size=14, color=TEAL).to_corner(UR, buff=0.2)
        self.play(FadeOut(curve1), FadeOut(eq_label), Write(step_b), run_time=0.3)

        a_tr = ValueTracker(1.0)
        param_curve = always_redraw(lambda: axes.plot(
            lambda x: np.exp(x) - a_tr.get_value() * x - 1,
            x_range=[-3, 2.5], color=BLUE, stroke_width=3,
        ))
        param_label = always_redraw(lambda: MathTex(
            rf"f(x)=e^x - {a_tr.get_value():.1f}x - 1", font_size=16, color=BLUE,
        ).to_corner(UL, buff=0.3).shift(DOWN*0.5))

        # Minimum point marker (x0 = ln(a))
        def get_min_pt():
            a = max(0.01, a_tr.get_value())
            x0 = np.log(a)
            return axes.c2p(x0, np.exp(x0) - a * x0 - 1)

        min_mk = always_redraw(lambda: Dot(get_min_pt(), color=RED, radius=0.07))
        min_mkl = always_redraw(lambda: MathTex(
            rf"x_0=\ln({a_tr.get_value():.1f})", font_size=11, color=RED,
        ).next_to(get_min_pt(), DR, buff=0.08))

        # a value display
        a_disp = always_redraw(lambda: MathTex(
            rf"a = {a_tr.get_value():.2f}", font_size=22, color=ORANGE,
        ).to_edge(DOWN, buff=0.3))

        self.add(param_curve, param_label, min_mk, min_mkl, a_disp)

        # Draw x-axis reference
        x_ref = DashedLine(axes.c2p(-3.5, 0), axes.c2p(3.5, 0), color=GRAY, stroke_width=0.8)
        self.play(Create(x_ref), run_time=0.3)

        # Scan a from 0.1 to 4 slowly
        self.play(a_tr.animate.set_value(0.1), run_time=2, rate_func=smooth)
        self.wait(0.5)
        self.play(a_tr.animate.set_value(4.0), run_time=5, rate_func=smooth)
        self.wait(0.5)

        # a = 1: tangent to x-axis
        self.play(a_tr.animate.set_value(1.0), run_time=2, rate_func=smooth)
        self.wait(0.5)

        tangent_note = MathTex(r"a=1:\;f_{\min}=0\;\text{(tangent to x-axis)}", font_size=16, color=GOLD)
        tangent_note.to_edge(DOWN, buff=0.5)
        tbox = SurroundingRectangle(tangent_note, color=GOLD, buff=0.08)
        self.play(FadeOut(a_disp), Write(tangent_note), Create(tbox))
        self.wait(1.5)

        # a > 1: curve dips below x-axis
        self.play(FadeOut(tangent_note), FadeOut(tbox))
        self.add(a_disp)
        self.play(a_tr.animate.set_value(2.0), run_time=2)

        below_label = MathTex(r"a>1:\;f\text{ crosses below }0", font_size=14, color=RED).to_edge(DOWN, buff=0.5)
        self.play(Write(below_label))
        self.wait(1)

        # a < 1: curve always above
        self.play(FadeOut(below_label))
        self.play(a_tr.animate.set_value(0.5), run_time=2)

        above_label = MathTex(r"a<1:\;f(x) > 0 \;\forall x", font_size=14, color=GREEN).to_edge(DOWN, buff=0.5)
        self.play(Write(above_label))
        self.wait(1)
        self.play(FadeOut(above_label), FadeOut(step_b))

        # ══════════════════════════════════════════
        # Part C: Symmetry center proof (bonus visual)
        # g(x) = f(x+1) shifted, check symmetry
        # ══════════════════════════════════════════
        step_c = Text("Bonus: symmetry of shifted f", font_size=13, color=TEAL).to_corner(UR, buff=0.2)
        self.play(Write(step_c), run_time=0.2)

        self.play(a_tr.animate.set_value(1.0), run_time=1)
        self.play(FadeOut(min_mk), FadeOut(min_mkl), FadeOut(a_disp))

        # Draw the curve and its reflection about (1, f(1))
        sym_pt = axes.c2p(0, 0)  # f(0) = 0 is the min
        sym_dot = Dot(sym_pt, color=GOLD, radius=0.08)
        sym_lab = MathTex(r"(0,0)", font_size=12, color=GOLD).next_to(sym_dot, DL, buff=0.05)
        self.play(FadeIn(sym_dot), Write(sym_lab))

        # Reflect curve about (0, 0): g(x) = -f(-x)
        reflect_curve = axes.plot(lambda x: -(np.exp(-x) + x - 1), x_range=[-2.5, 3], color=RED, stroke_width=2, stroke_opacity=0.6)
        reflect_lab = MathTex(r"-f(-x)", font_size=12, color=RED).next_to(reflect_curve, LEFT, buff=0.2)
        self.play(Create(reflect_curve), Write(reflect_lab), run_time=1.5)

        no_sym = MathTex(r"f(x) \neq -f(-x) \;\Rightarrow\; \text{not point-symmetric at }O",
                         font_size=14, color=RED).to_edge(DOWN, buff=0.3)
        self.play(Write(no_sym))
        self.wait(2)

        # Final conclusion
        self.play(FadeOut(no_sym), FadeOut(reflect_curve), FadeOut(reflect_lab), FadeOut(step_c))

        final = MathTex(r"e^x \ge x + 1,\; \text{equality at } x=0", font_size=20, color=GOLD)
        final.to_edge(DOWN, buff=0.3)
        fbox = SurroundingRectangle(final, color=GOLD, buff=0.08)
        self.play(Write(final), Create(fbox))
        self.wait(4)

    def _tangent(self, axes, f, fp, x0):
        y0 = f(x0)
        k = fp(x0)
        dx = 1.5
        return Line(
            axes.c2p(x0 - dx, y0 + k*(-dx)),
            axes.c2p(x0 + dx, y0 + k*(dx)),
            color=ORANGE, stroke_width=2, stroke_opacity=0.7,
        )
