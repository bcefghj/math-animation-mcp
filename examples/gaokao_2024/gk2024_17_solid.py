# 2024 Gaokao Solid Geometry — GRAPHICS-FIRST, long (~3min)
# Regular triangular prism ABC-A1B1C1, side=2, height=2
# D on circle with diameter AC on plane ABC
# (1) Prove BD ⊥ plane AA1C1C
# (2) Dihedral angle A-A1B1-C when D sweeps the semicircle
from manim import *
import numpy as np

def normalize(v):
    n = np.linalg.norm(v)
    return v / n if n > 1e-9 else v

class Gaokao2024_Solid_Long(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65*DEGREES, theta=-45*DEGREES)

        # ── Small title fixed in frame ──
        tag = Text("2024 Gaokao · Solid Geometry", font_size=22, color=GOLD)
        tag.to_corner(UL, buff=0.2)
        self.add_fixed_in_frame_mobjects(tag)
        self.play(Write(tag), run_time=0.6)

        # ── Prism vertices ──
        s = 2.0
        h = 2.0
        A = np.array([-1, -np.sqrt(3)/3, 0]) * s
        B = np.array([1, -np.sqrt(3)/3, 0]) * s
        C = np.array([0, 2*np.sqrt(3)/3, 0]) * s
        A1 = A + np.array([0, 0, h])
        B1 = B + np.array([0, 0, h])
        C1 = C + np.array([0, 0, h])

        verts = {'A': A, 'B': B, 'C': C, "A'": A1, "B'": B1, "C'": C1}

        bottom = [(A, B), (B, C), (C, A)]
        top = [(A1, B1), (B1, C1), (C1, A1)]
        sides = [(A, A1), (B, B1), (C, C1)]

        # Step 1: Build the prism with animation
        step1 = Text("Step 1: Build the prism", font_size=14, color=TEAL)
        step1.to_corner(UR, buff=0.2)
        self.add_fixed_in_frame_mobjects(step1)
        self.play(Write(step1), run_time=0.3)

        all_edges = VGroup()
        for v1, v2 in bottom:
            l = Line3D(v1, v2, color=BLUE_C, thickness=0.02)
            all_edges.add(l)
        self.play(LaggedStart(*[Create(l) for l in all_edges], lag_ratio=0.1), run_time=1)

        for v1, v2 in sides:
            l = Line3D(v1, v2, color=BLUE_C, thickness=0.015)
            all_edges.add(l)
            self.play(Create(l), run_time=0.3)

        for v1, v2 in top:
            l = Line3D(v1, v2, color=BLUE_C, thickness=0.02)
            all_edges.add(l)
        self.play(LaggedStart(*[Create(l) for l in all_edges[-3:]], lag_ratio=0.1), run_time=0.6)

        # Bottom face fill
        bottom_face = Polygon(A, B, C, fill_color=BLUE, fill_opacity=0.1, stroke_width=0)
        self.play(FadeIn(bottom_face), run_time=0.5)

        # Labels
        for name, pos in verts.items():
            dot = Dot3D(pos, color=YELLOW, radius=0.04)
            lab = Text(name, font_size=13, color=YELLOW)
            self.add_fixed_orientation_mobjects(lab)
            offset = normalize(pos - np.mean([A, B, C, A1, B1, C1], axis=0)) * 0.25
            lab.move_to(pos + offset)
            self.play(FadeIn(dot), FadeIn(lab), run_time=0.1)

        self.wait(0.5)
        self.play(FadeOut(step1))

        # ── Step 2: D on semicircle with diameter AC ──
        step2 = Text("Step 2: D on circle (diameter AC)", font_size=14, color=TEAL)
        step2.to_corner(UR, buff=0.2)
        self.add_fixed_in_frame_mobjects(step2)
        self.play(Write(step2), run_time=0.3)

        # Center and radius of circle with diameter AC
        M = (A + C) / 2
        radius = np.linalg.norm(C - A) / 2

        # Draw the semicircle on the bottom plane (z=0)
        ac_dir = normalize(C - A)
        perp_dir = np.cross(ac_dir, np.array([0, 0, 1]))
        perp_dir = normalize(perp_dir)

        semicircle = ParametricFunction(
            lambda t: M + radius * (np.cos(t) * ac_dir + np.sin(t) * perp_dir),
            t_range=[0, PI], color=ORANGE, stroke_width=2,
        )
        self.play(Create(semicircle), run_time=1.5)

        # Place D at angle pi/3 initially
        theta0 = PI / 3
        D0 = M + radius * (np.cos(theta0) * ac_dir + np.sin(theta0) * perp_dir)
        d_dot = Dot3D(D0, color=RED, radius=0.06)
        d_label = Text("D", font_size=14, color=RED)
        self.add_fixed_orientation_mobjects(d_label)
        d_label.move_to(D0 + DOWN * 0.3)
        self.play(FadeIn(d_dot), FadeIn(d_label), run_time=0.5)

        # Draw BD, AD, CD
        bd_line = Line3D(B, D0, color=RED, thickness=0.025)
        ad_line = Line3D(A, D0, color=GREEN, thickness=0.02)
        cd_line = Line3D(C, D0, color=GREEN, thickness=0.02)
        self.play(Create(bd_line), Create(ad_line), Create(cd_line), run_time=1)

        # Show right angle at D (Thales' theorem: angle ADC = 90°)
        ra_size = 0.2
        ra_p1 = D0 + normalize(A - D0) * ra_size
        ra_p2 = D0 + normalize(A - D0) * ra_size + normalize(C - D0) * ra_size
        ra_p3 = D0 + normalize(C - D0) * ra_size
        ra_sq = Polygon(ra_p1, ra_p2, ra_p3, D0, color=GREEN, stroke_width=1.5, fill_opacity=0)
        # Just the L-shape
        ra_lines = VGroup(
            Line3D(ra_p1, ra_p2, color=GREEN, thickness=0.01),
            Line3D(ra_p2, ra_p3, color=GREEN, thickness=0.01),
        )
        self.play(Create(ra_lines), run_time=0.5)

        thales = MathTex(r"\angle ADC = 90^\circ", font_size=14, color=GREEN)
        thales.to_corner(DR, buff=0.3)
        self.add_fixed_in_frame_mobjects(thales)
        self.play(Write(thales), run_time=0.5)
        self.wait(1)

        self.play(FadeOut(step2))

        # ── Step 3: Animate D moving along the semicircle ──
        step3 = Text("Step 3: D moves along semicircle", font_size=14, color=TEAL)
        step3.to_corner(UR, buff=0.2)
        self.add_fixed_in_frame_mobjects(step3)
        self.play(Write(step3), run_time=0.3)

        theta_tracker = ValueTracker(theta0)

        def get_D():
            t = theta_tracker.get_value()
            return M + radius * (np.cos(t) * ac_dir + np.sin(t) * perp_dir)

        d_dot_dyn = always_redraw(lambda: Dot3D(get_D(), color=RED, radius=0.06))
        bd_dyn = always_redraw(lambda: Line3D(B, get_D(), color=RED, thickness=0.025))
        ad_dyn = always_redraw(lambda: Line3D(A, get_D(), color=GREEN, thickness=0.015))
        cd_dyn = always_redraw(lambda: Line3D(C, get_D(), color=GREEN, thickness=0.015))

        self.play(
            FadeOut(d_dot), FadeOut(bd_line), FadeOut(ad_line), FadeOut(cd_line), FadeOut(ra_lines), FadeOut(d_label),
            run_time=0.3,
        )
        self.add(d_dot_dyn, bd_dyn, ad_dyn, cd_dyn)

        # Sweep D
        self.play(theta_tracker.animate.set_value(0.15), run_time=2, rate_func=smooth)
        self.play(theta_tracker.animate.set_value(PI - 0.15), run_time=2, rate_func=smooth)
        self.play(theta_tracker.animate.set_value(PI / 2), run_time=1.5, rate_func=smooth)
        self.wait(0.5)

        self.play(FadeOut(step3))

        # ── Step 4: Prove BD ⊥ plane ACC'A' ──
        step4 = Text("Step 4: BD perp plane ACC'A'", font_size=14, color=TEAL)
        step4.to_corner(UR, buff=0.2)
        self.add_fixed_in_frame_mobjects(step4)
        self.play(Write(step4), run_time=0.3)

        # At D = midpoint angle (pi/2), the D is at the "peak"
        D_mid = get_D()

        # Highlight plane ACC'A'
        plane_acc1 = Polygon(A, C, C1, A1, fill_color=ORANGE, fill_opacity=0.2, stroke_color=ORANGE, stroke_width=1)
        self.play(FadeIn(plane_acc1), run_time=0.8)

        # BD ⊥ AC (because angle BDC = 90°, Thales in triangle)
        proof1 = MathTex(r"BD \perp AC", font_size=14, color=GREEN)
        proof1.to_corner(DR, buff=0.3).shift(UP * 0.4)
        self.add_fixed_in_frame_mobjects(proof1)
        self.play(Write(proof1), run_time=0.4)

        # BD ⊥ AA1 (BD in base plane, AA1 lateral edge, prism lateral edges ⊥ base)
        proof2 = MathTex(r"BD \perp AA'", font_size=14, color=GREEN)
        proof2.next_to(proof1, DOWN, buff=0.1)
        self.add_fixed_in_frame_mobjects(proof2)
        self.play(Write(proof2), run_time=0.4)

        concl = MathTex(r"\therefore BD \perp \text{plane } ACC'A'", font_size=16, color=GOLD)
        concl.next_to(proof2, DOWN, buff=0.15)
        self.add_fixed_in_frame_mobjects(concl)
        conclbox = SurroundingRectangle(concl, color=GOLD, buff=0.06)
        self.add_fixed_in_frame_mobjects(conclbox)
        self.play(Write(concl), Create(conclbox), run_time=0.6)
        self.wait(1.5)

        # Rotate camera to show perpendicularity
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()

        self.play(FadeOut(step4), FadeOut(proof1), FadeOut(proof2), FadeOut(concl), FadeOut(conclbox), FadeOut(thales))

        # ── Step 5: Dihedral angle with coordinate system ──
        step5 = Text("Step 5: Dihedral angle via coordinates", font_size=14, color=TEAL)
        step5.to_corner(UR, buff=0.2)
        self.add_fixed_in_frame_mobjects(step5)
        self.play(Write(step5), run_time=0.3)

        # Build coordinate at B: x along BA, z up, y = z × x
        bx = normalize(A - B)
        bz = np.array([0, 0, 1])
        by = np.cross(bz, bx)

        ax_len = 1.5
        x_ax = Arrow3D(B, B + bx * ax_len, color=RED)
        y_ax = Arrow3D(B, B + by * ax_len, color=GREEN)
        z_ax = Arrow3D(B, B + bz * ax_len, color=BLUE)
        self.play(Create(x_ax), Create(y_ax), Create(z_ax), run_time=0.8)

        ax_labels = VGroup()
        for label, pos in [("x", B + bx * ax_len * 1.1), ("y", B + by * ax_len * 1.1), ("z", B + bz * ax_len * 1.1)]:
            l = Text(label, font_size=12, color=WHITE)
            self.add_fixed_orientation_mobjects(l)
            l.move_to(pos)
            ax_labels.add(l)
            self.play(FadeIn(l), run_time=0.1)

        # Normal vectors for the two half-planes of dihedral angle
        # plane A1B1A and plane A1B1C
        n1_dir = np.cross(A1 - B1, A - B1)
        n1_dir = n1_dir / np.linalg.norm(n1_dir)
        n2_dir = np.cross(A1 - B1, C - B1)
        n2_dir = n2_dir / np.linalg.norm(n2_dir)

        n1_arr = Arrow3D(B1, B1 + n1_dir * 1.0, color=PURPLE)
        n2_arr = Arrow3D(B1, B1 + n2_dir * 1.0, color=MAROON)
        self.play(Create(n1_arr), Create(n2_arr), run_time=0.8)

        n1_lab = MathTex(r"\vec{n}_1", font_size=12, color=PURPLE)
        n2_lab = MathTex(r"\vec{n}_2", font_size=12, color=MAROON)
        self.add_fixed_orientation_mobjects(n1_lab, n2_lab)
        n1_lab.move_to(B1 + n1_dir * 1.2)
        n2_lab.move_to(B1 + n2_dir * 1.2)
        self.play(FadeIn(n1_lab), FadeIn(n2_lab), run_time=0.3)

        cos_val = np.dot(n1_dir, n2_dir)
        angle_deg = np.degrees(np.arccos(np.clip(cos_val, -1, 1)))

        angle_res = MathTex(rf"\cos\theta = {cos_val:.3f} \;\Rightarrow\; \theta \approx {angle_deg:.1f}^\circ",
                            font_size=16, color=GOLD)
        angle_res.to_edge(DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(angle_res)
        abox = SurroundingRectangle(angle_res, color=GOLD, buff=0.08)
        self.add_fixed_in_frame_mobjects(abox)
        self.play(Write(angle_res), Create(abox))

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(step5))

        # ── Step 6: D sweep & dihedral angle changes ──
        step6 = Text("Step 6: D sweeps → angle varies", font_size=14, color=TEAL)
        step6.to_corner(UR, buff=0.2)
        self.add_fixed_in_frame_mobjects(step6)
        self.play(Write(step6), run_time=0.3)

        # Animate D sweeping again and show the angle changing
        angle_label_dyn = always_redraw(lambda: self._angle_at_theta(theta_tracker.get_value(), M, radius, ac_dir, perp_dir, A, B, C, A1, B1, C1))
        self.add_fixed_in_frame_mobjects(angle_label_dyn)

        self.play(theta_tracker.animate.set_value(0.2), run_time=3)
        self.play(theta_tracker.animate.set_value(PI - 0.2), run_time=3)
        self.play(theta_tracker.animate.set_value(PI / 2), run_time=2)

        self.wait(3)

    def _angle_at_theta(self, theta, M, radius, ac_dir, perp_dir, A, B, C, A1, B1, C1):
        D = M + radius * (np.cos(theta) * ac_dir + np.sin(theta) * perp_dir)
        bd = D - B
        bd_len = np.linalg.norm(bd)
        txt = MathTex(rf"|BD| = {bd_len:.2f}", font_size=14, color=RED)
        txt.to_edge(DOWN, buff=0.6)
        return txt
