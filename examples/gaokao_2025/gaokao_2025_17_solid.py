# 2025 Gaokao I - Problem 17: Solid Geometry (Quadrilateral Pyramid)
from manim import *
import numpy as np

class Gaokao2025_17_SolidGeometry(ThreeDScene):
    def construct(self):
        # ══════════════════════════════════════════════════════════
        # Scene 1: Title & Problem Statement (2D, fixed in frame)
        # ══════════════════════════════════════════════════════════
        main_title = Text("2025 New Gaokao I — Problem 17", font_size=36, color=GOLD)
        sub = Text("Solid Geometry: Quadrilateral Pyramid", font_size=24, color=GRAY)
        sub.next_to(main_title, DOWN, buff=0.2)
        self.add_fixed_in_frame_mobjects(main_title, sub)
        self.play(Write(main_title), FadeIn(sub))
        self.wait(2)

        # Problem conditions
        conds = VGroup(
            MathTex(r"PA \perp \text{plane } ABCD", font_size=22),
            MathTex(r"BC \parallel AD, \quad AB \perp AD", font_size=22),
            MathTex(r"PA = AB = \sqrt{2}", font_size=22),
            MathTex(r"AD = \sqrt{3}+1, \quad BC = 2", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).to_edge(DOWN, buff=0.5)
        for c in conds:
            self.add_fixed_in_frame_mobjects(c)
        self.play(LaggedStart(*[Write(c) for c in conds], lag_ratio=0.3), run_time=2)
        self.wait(2)

        self.play(*[FadeOut(m) for m in [main_title, sub, *conds]])

        # ══════════════════════════════════════════════════════════
        # Scene 2: Build the 3D Pyramid
        # ══════════════════════════════════════════════════════════
        self.set_camera_orientation(phi=65*DEGREES, theta=-50*DEGREES)

        s2 = np.sqrt(2)
        s3 = np.sqrt(3)

        A = np.array([0, 0, 0])
        B = np.array([s2, 0, 0])
        D = np.array([0, s3+1, 0])
        C = np.array([s2, s3+1, 0])  # BC=2 not correct, need BC parallel AD
        # BC ∥ AD means C is at (something, BC_length_along_AD_dir, 0)
        # AD is along y-axis, BC ∥ AD means BC is also along y-axis
        # B = (√2, 0, 0), C must be at (√2, BC, 0) with BC=2
        C = np.array([s2, 2, 0])
        P = np.array([0, 0, s2])  # PA ⊥ plane ABCD, PA=√2

        verts = {'A': A, 'B': B, 'C': C, 'D': D, 'P': P}

        # Draw edges
        edges_list = [
            (A, B, WHITE), (B, C, WHITE), (C, D, WHITE), (D, A, WHITE),
            (P, A, BLUE), (P, B, BLUE), (P, C, BLUE), (P, D, BLUE),
        ]
        edge_objs = VGroup()
        for v1, v2, col in edges_list:
            line = Line3D(v1, v2, color=col, thickness=0.02)
            edge_objs.add(line)

        self.play(LaggedStart(*[Create(e) for e in edge_objs], lag_ratio=0.1), run_time=2)

        # Vertex labels
        offsets = {'A': DL*0.3, 'B': DR*0.3, 'C': RIGHT*0.4, 'D': LEFT*0.4+UP*0.2, 'P': UP*0.3}
        for name, pos in verts.items():
            dot = Dot3D(pos, color=YELLOW, radius=0.05)
            label = Text(name, font_size=18, color=YELLOW)
            self.add_fixed_orientation_mobjects(label)
            label.move_to(pos + offsets[name])
            self.play(FadeIn(dot), FadeIn(label), run_time=0.3)

        self.wait(1)

        # ── Highlight conditions ──
        cond_text = Text("PA perp plane ABCD, AB perp AD, BC // AD", font_size=18, color=YELLOW)
        cond_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(cond_text)
        self.play(Write(cond_text))

        # Show right angle at A (AB⊥AD) using small square
        ra_size = 0.25
        ra_corner = A + normalize(B - A) * ra_size + normalize(D - A) * ra_size
        ra_square = Polygon(
            A + normalize(B - A) * ra_size,
            ra_corner,
            A + normalize(D - A) * ra_size,
            color=RED, stroke_width=2,
        )
        self.play(Create(ra_square))
        self.wait(1)

        # Rotate to view
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        # ══════════════════════════════════════════════════════════
        # Scene 3: Part (1) — Prove plane PAB ⊥ plane PAD
        # ══════════════════════════════════════════════════════════
        part1_title = Text("Part (1): Prove plane PAB perp plane PAD", font_size=22, color=GREEN)
        part1_title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(part1_title)
        self.play(FadeOut(cond_text), Write(part1_title))

        # Highlight plane PAB
        plane_pab = Polygon(P, A, B, fill_color=RED, fill_opacity=0.2, stroke_color=RED)
        plane_pad = Polygon(P, A, D, fill_color=BLUE, fill_opacity=0.2, stroke_color=BLUE)
        self.play(Create(plane_pab), run_time=1)
        self.play(Create(plane_pad), run_time=1)
        self.wait(1)

        # Proof steps (fixed in frame)
        proof1 = VGroup(
            MathTex(r"\text{Since } PA \perp \text{plane } ABCD", font_size=18),
            MathTex(r"\Rightarrow PA \perp AD", font_size=18, color=YELLOW),
            MathTex(r"\text{Given } AB \perp AD", font_size=18),
            MathTex(r"\Rightarrow AD \perp PA \text{ and } AD \perp AB", font_size=18, color=ORANGE),
            MathTex(r"PA \cap AB = A, \; PA, AB \subset \text{plane } PAB", font_size=18),
            MathTex(r"\Rightarrow AD \perp \text{plane } PAB", font_size=18, color=GREEN),
            MathTex(r"AD \subset \text{plane } PAD", font_size=18),
            MathTex(r"\therefore \text{plane } PAB \perp \text{plane } PAD \;\; \blacksquare", font_size=20, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_corner(DL, buff=0.3)

        for p in proof1:
            self.add_fixed_in_frame_mobjects(p)
            self.play(Write(p), run_time=0.7)
            self.wait(0.3)

        self.wait(2)

        # Clean proof
        self.play(*[FadeOut(p) for p in proof1], FadeOut(part1_title),
                  FadeOut(plane_pab), FadeOut(plane_pad))

        # ══════════════════════════════════════════════════════════
        # Scene 4: Part (2)(i) — Sphere center on plane ABCD
        # ══════════════════════════════════════════════════════════
        part2i_title = Text("Part (2)(i): Sphere center O on plane ABCD", font_size=22, color=GREEN)
        part2i_title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(part2i_title)
        self.play(Write(part2i_title))

        # Coordinate system: A as origin
        coord_info = VGroup(
            Text("Set up coordinates: A = origin", font_size=16, color=TEAL),
            MathTex(r"A(0,0,0),\; B(\sqrt2,0,0)", font_size=16),
            MathTex(r"D(0,\sqrt3+1,0),\; C(\sqrt2,2,0)", font_size=16),
            MathTex(r"P(0,0,\sqrt2)", font_size=16),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08).to_corner(DL, buff=0.3)

        for ci in coord_info:
            self.add_fixed_in_frame_mobjects(ci)
            self.play(Write(ci), run_time=0.5)

        self.wait(1)

        # Show sphere center reasoning
        proof2i = VGroup(
            MathTex(r"\text{Let } O = (x, y, z), \;\; |OP|=|OB|=|OC|=|OD|", font_size=16),
            MathTex(r"|OP|^2 = x^2 + y^2 + (z-\sqrt2)^2", font_size=16),
            MathTex(r"|OB|^2 = (x-\sqrt2)^2 + y^2 + z^2", font_size=16),
            MathTex(r"|OP|^2 = |OB|^2 \Rightarrow z = x", font_size=16, color=YELLOW),
            MathTex(r"|OB|^2 = |OD|^2 \Rightarrow \text{solve for } x, y", font_size=16),
            MathTex(r"|OB|^2 = |OC|^2 \Rightarrow z = 0", font_size=16, color=RED),
            MathTex(r"\Rightarrow z = 0 \;\;\text{(O on plane ABCD)} \;\; \blacksquare", font_size=18, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08).to_corner(DR, buff=0.3)

        for p in proof2i:
            self.add_fixed_in_frame_mobjects(p)
            self.play(Write(p), run_time=0.6)
            self.wait(0.2)

        self.wait(2)

        # Visualize: show the circumsphere
        # O = (x, y, 0), solve: from z=0 and OP=OB=OC=OD
        # |OP|^2 = x^2 + y^2 + 2
        # |OB|^2 = (x-s2)^2 + y^2
        # OP=OB => x^2+y^2+2 = x^2-2s2*x+2+y^2 => 2s2*x=0 => x=0 (since z=x=0)
        # Wait: z=x from OP=OB. If z=0 then x=0.
        # |OD|^2 = (s3+1)^2 - 2(s3+1)*y + y^2  (with x=0)
        # |OB|^2 = 2 + y^2
        # OB=OD => 2 + y^2 = y^2 - 2(s3+1)*y + (s3+1)^2
        # 2 = -2(s3+1)y + (s3+1)^2
        # y = ((s3+1)^2 - 2)/(2*(s3+1)) = (3+2s3+1-2)/(2(s3+1)) = (2+2s3)/(2(s3+1)) = 1
        # So O = (0, 1, 0), R^2 = 0 + 1 + 2 = 3, R = √3
        O_center = np.array([0, 1, 0])
        R_sphere = np.sqrt(3)
        sphere = Sphere(radius=R_sphere, color=BLUE, fill_opacity=0.08, stroke_width=0.5)
        sphere.move_to(O_center)
        o_dot = Dot3D(O_center, color=RED, radius=0.08)
        o_label = Text("O", font_size=18, color=RED)
        self.add_fixed_orientation_mobjects(o_label)
        o_label.move_to(O_center + np.array([0.3, -0.3, 0]))

        self.play(FadeIn(sphere), FadeIn(o_dot), FadeIn(o_label), run_time=2)

        # Rotate
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        # Clean up
        self.play(*[FadeOut(m) for m in [*coord_info, *proof2i, part2i_title]])

        # ══════════════════════════════════════════════════════════
        # Scene 5: Part (2)(ii) — Angle between AC and PO
        # ══════════════════════════════════════════════════════════
        part2ii_title = Text("Part (2)(ii): Angle between AC and PO", font_size=22, color=GREEN)
        part2ii_title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(part2ii_title)
        self.play(Write(part2ii_title))

        # Draw AC and PO
        line_AC = Line3D(A, C, color=YELLOW, thickness=0.04)
        line_PO = Line3D(P, O_center, color=RED, thickness=0.04)
        ac_label = Text("AC", font_size=16, color=YELLOW)
        po_label = Text("PO", font_size=16, color=RED)
        self.add_fixed_orientation_mobjects(ac_label, po_label)
        ac_label.move_to((A + C)/2 + np.array([0, -0.3, 0]))
        po_label.move_to((P + O_center)/2 + np.array([0.3, 0, 0]))

        self.play(Create(line_AC), Create(line_PO), FadeIn(ac_label), FadeIn(po_label))
        self.wait(1)

        # Calculation
        vec_AC = C - A  # (√2, 2, 0)
        vec_PO = O_center - P  # (0, 1, -√2)
        dot_product = np.dot(vec_AC, vec_PO)
        mag_AC = np.linalg.norm(vec_AC)
        mag_PO = np.linalg.norm(vec_PO)
        cos_angle = abs(dot_product) / (mag_AC * mag_PO)

        calc = VGroup(
            MathTex(r"\vec{AC} = (\sqrt2, 2, 0)", font_size=18, color=YELLOW),
            MathTex(r"\vec{PO} = (0, 1, -\sqrt2)", font_size=18, color=RED),
            MathTex(r"\vec{AC} \cdot \vec{PO} = 0 + 2 + 0 = 2", font_size=18),
            MathTex(r"|\vec{AC}| = \sqrt{2+4} = \sqrt6", font_size=18),
            MathTex(r"|\vec{PO}| = \sqrt{0+1+2} = \sqrt3", font_size=18),
            MathTex(r"\cos\alpha = \frac{|2|}{\sqrt6 \cdot \sqrt3} = \frac{2}{3\sqrt2} = \frac{\sqrt2}{3}", font_size=18, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_corner(DL, buff=0.3)

        for c in calc:
            self.add_fixed_in_frame_mobjects(c)
            self.play(Write(c), run_time=0.6)
            self.wait(0.2)

        # Final answer
        answer = MathTex(
            r"\cos\alpha = \frac{\sqrt{6}}{3}",
            font_size=28, color=GOLD,
        ).to_edge(DOWN, buff=0.3)
        box = SurroundingRectangle(answer, color=GOLD, buff=0.1)
        self.add_fixed_in_frame_mobjects(answer, box)
        self.play(Write(answer), Create(box))

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait(2)

