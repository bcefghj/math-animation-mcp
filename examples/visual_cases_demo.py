# 6 visual-first long animations: LeetCode x3 + Gaokao 2024 x3
# Design: Graphics occupy 80%+ of screen, text is small side labels
from manim import *
import numpy as np
import math

# ══════════════════════════════════════════════════════════════════
# LeetCode 1: Two Sum — Array scanning + HashMap building
# ══════════════════════════════════════════════════════════════════
class LeetCode_TwoSum(Scene):
    def construct(self):
        title = Text("LeetCode #1 · Two Sum", font_size=32, color=BLUE).to_edge(UP, buff=0.2)
        target_label = MathTex(r"\text{target} = 9", font_size=24, color=GOLD).next_to(title, DOWN, buff=0.15)
        self.play(Write(title), Write(target_label))

        nums = [2, 7, 11, 15]
        target = 9
        box_w, box_h = 1.2, 0.8
        arr_group = VGroup()
        for i, v in enumerate(nums):
            rect = Rectangle(width=box_w, height=box_h, color=WHITE, stroke_width=2)
            val = Text(str(v), font_size=28, color=WHITE).move_to(rect)
            idx = Text(f"[{i}]", font_size=14, color=GRAY).next_to(rect, DOWN, buff=0.05)
            arr_group.add(VGroup(rect, val, idx))
        arr_group.arrange(RIGHT, buff=0.15).move_to(UP * 1.2)
        arr_title = Text("nums[]", font_size=18, color=GRAY).next_to(arr_group, LEFT, buff=0.3)
        self.play(LaggedStart(*[FadeIn(a) for a in arr_group], lag_ratio=0.15), Write(arr_title), run_time=1.5)
        self.wait(0.5)

        # HashMap area
        hm_title = Text("HashMap", font_size=18, color=TEAL).move_to(DOWN * 0.8 + LEFT * 4)
        hm_box = Rectangle(width=4, height=2.5, color=TEAL, stroke_width=1).next_to(hm_title, DOWN, buff=0.1)
        self.play(Write(hm_title), Create(hm_box))

        # Result area
        result_area = VGroup()
        result_title = Text("Result", font_size=18, color=GOLD).move_to(DOWN * 0.8 + RIGHT * 4)
        self.play(Write(result_title))

        # Brute force first: O(n²) visualized
        bf_label = Text("Brute Force O(n^2)", font_size=20, color=RED).to_edge(DOWN, buff=0.3)
        self.play(Write(bf_label))

        for i in range(len(nums)):
            hi_i = arr_group[i][0].copy().set_fill(RED, opacity=0.3)
            self.play(FadeIn(hi_i), run_time=0.3)
            for j in range(i + 1, len(nums)):
                hi_j = arr_group[j][0].copy().set_fill(YELLOW, opacity=0.3)
                self.play(FadeIn(hi_j), run_time=0.15)
                s = nums[i] + nums[j]
                check = MathTex(f"{nums[i]}+{nums[j]}={s}", font_size=18, color=YELLOW).move_to(DOWN * 2.5 + RIGHT * 2)
                self.play(Write(check), run_time=0.2)
                if s == target:
                    check.set_color(GREEN)
                    found = Text(f"Found! [{i},{j}]", font_size=22, color=GREEN).next_to(check, DOWN)
                    self.play(Write(found), hi_i.animate.set_fill(GREEN, opacity=0.5), hi_j.animate.set_fill(GREEN, opacity=0.5))
                    self.wait(1)
                    self.play(FadeOut(found))
                self.play(FadeOut(hi_j), FadeOut(check), run_time=0.1)
            self.play(FadeOut(hi_i), run_time=0.1)

        self.play(FadeOut(bf_label))
        self.wait(0.5)

        # HashMap approach O(n)
        hm_label = Text("HashMap O(n)", font_size=20, color=GREEN).to_edge(DOWN, buff=0.3)
        self.play(Write(hm_label))

        # Clear hashmap
        hm_entries = VGroup()
        hashmap = {}
        pointer = Arrow(UP * 0.3, DOWN * 0.1, color=RED, stroke_width=3, max_tip_length_to_length_ratio=0.3)

        for i, v in enumerate(nums):
            # Move pointer
            ptr = pointer.copy().next_to(arr_group[i], UP, buff=0.05)
            self.play(FadeIn(ptr), arr_group[i][0].animate.set_stroke(RED, width=4), run_time=0.3)

            complement = target - v
            comp_text = MathTex(f"9-{v}={complement}", font_size=16, color=YELLOW).move_to(DOWN * 2.5 + RIGHT * 3)
            self.play(Write(comp_text), run_time=0.3)

            if complement in hashmap:
                j = hashmap[complement]
                arr_group[j][0].set_stroke(GREEN, width=5)
                arr_group[i][0].set_stroke(GREEN, width=5)
                res = Text(f"Return [{j}, {i}]", font_size=24, color=GOLD).move_to(DOWN * 2 + RIGHT * 3)
                self.play(Write(res), Flash(arr_group[j][0], color=GREEN), Flash(arr_group[i][0], color=GREEN))
                self.wait(2)
                break
            else:
                # Add to hashmap
                entry = MathTex(f"{v} \\to {i}", font_size=16, color=TEAL)
                entry.move_to(hm_box.get_top() + DOWN * (0.3 + len(hm_entries) * 0.35))
                hm_entries.add(entry)
                hashmap[v] = i
                self.play(Write(entry), run_time=0.3)
                miss = Text("Not in map", font_size=14, color=GRAY).next_to(comp_text, DOWN, buff=0.1)
                self.play(FadeIn(miss), run_time=0.2)
                self.play(FadeOut(miss), run_time=0.1)

            self.play(FadeOut(ptr), FadeOut(comp_text), arr_group[i][0].animate.set_stroke(WHITE, width=2), run_time=0.2)

        self.wait(2)


# ══════════════════════════════════════════════════════════════════
# LeetCode 206: Reverse Linked List — Pointer animation
# ══════════════════════════════════════════════════════════════════
class LeetCode_ReverseList(Scene):
    def construct(self):
        title = Text("LeetCode #206 · Reverse Linked List", font_size=30, color=BLUE).to_edge(UP, buff=0.2)
        self.play(Write(title))

        vals = [1, 2, 3, 4, 5]
        node_r = 0.35
        spacing = 1.6
        start_x = -3.5

        # Build linked list nodes
        nodes = VGroup()
        arrows = VGroup()
        for i, v in enumerate(vals):
            circ = Circle(radius=node_r, color=BLUE, fill_opacity=0.2, fill_color=BLUE)
            circ.move_to(RIGHT * (start_x + i * spacing) + UP * 0.5)
            txt = Text(str(v), font_size=24, color=WHITE).move_to(circ)
            nodes.add(VGroup(circ, txt))
            if i > 0:
                arr = Arrow(nodes[i-1][0].get_right(), circ.get_left(), color=WHITE, buff=0.1, stroke_width=2, max_tip_length_to_length_ratio=0.15)
                arrows.add(arr)

        null_end = Text("null", font_size=16, color=GRAY).next_to(nodes[-1][0], RIGHT, buff=0.3)
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.1), run_time=1)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1), FadeIn(null_end), run_time=1)
        self.wait(1)

        # Three pointers: prev, curr, next
        prev_label = Text("prev", font_size=16, color=RED)
        curr_label = Text("curr", font_size=16, color=GREEN)
        next_label = Text("next", font_size=16, color=YELLOW)

        # Initial: prev = null, curr = head
        null_pos = nodes[0][0].get_left() + LEFT * 0.8
        prev_dot = Dot(null_pos, color=RED, radius=0.06)
        prev_text = Text("null", font_size=14, color=RED).next_to(prev_dot, DOWN, buff=0.1)
        prev_ptr = VGroup(prev_dot, prev_text)
        prev_lbl = prev_label.copy().next_to(prev_ptr, UP, buff=0.05)

        curr_arrow = Arrow(ORIGIN, DOWN * 0.4, color=GREEN, stroke_width=3, max_tip_length_to_length_ratio=0.3)
        curr_arrow.next_to(nodes[0][0], UP, buff=0.05)
        curr_lbl = curr_label.copy().next_to(curr_arrow, UP, buff=0.02)

        self.play(FadeIn(prev_ptr), FadeIn(prev_lbl), FadeIn(curr_arrow), FadeIn(curr_lbl))
        self.wait(0.5)

        step_label = Text("", font_size=18, color=GOLD).to_edge(DOWN, buff=0.3)

        # Reversal steps
        reversed_arrows = VGroup()
        for i in range(len(vals)):
            # Step label
            new_step = Text(f"Step {i+1}/{len(vals)}", font_size=18, color=GOLD).to_edge(DOWN, buff=0.3)
            self.play(FadeOut(step_label), FadeIn(new_step), run_time=0.2)
            step_label = new_step

            # Save next
            if i < len(vals) - 1:
                nxt_arrow = Arrow(ORIGIN, DOWN * 0.3, color=YELLOW, stroke_width=2, max_tip_length_to_length_ratio=0.3)
                nxt_arrow.next_to(nodes[i+1][0], UP, buff=0.3)
                nxt_lbl = next_label.copy().next_to(nxt_arrow, UP, buff=0.02)
                self.play(FadeIn(nxt_arrow), FadeIn(nxt_lbl), run_time=0.3)

            # Reverse: curr.next = prev
            nodes[i][0].set_fill(ORANGE, opacity=0.4)
            if i < len(arrows):
                self.play(FadeOut(arrows[i]), run_time=0.2)

            if i > 0:
                rev_arr = Arrow(
                    nodes[i][0].get_left(), nodes[i-1][0].get_right(),
                    color=RED, buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.15,
                )
                reversed_arrows.add(rev_arr)
                self.play(GrowArrow(rev_arr), run_time=0.4)
            self.wait(0.3)

            # Move prev to curr
            old_prev = prev_ptr.copy()
            self.play(
                prev_ptr.animate.move_to(nodes[i][0].get_center() + DOWN * 0.6),
                run_time=0.3,
            )
            prev_lbl_new = prev_label.copy().next_to(nodes[i][0], DOWN, buff=0.35)
            self.play(Transform(prev_lbl, prev_lbl_new), run_time=0.2)

            # Move curr to next
            if i < len(vals) - 1:
                self.play(
                    curr_arrow.animate.next_to(nodes[i+1][0], UP, buff=0.05),
                    curr_lbl.animate.next_to(nodes[i+1][0], UP, buff=0.45),
                    run_time=0.3,
                )
                self.play(FadeOut(nxt_arrow), FadeOut(nxt_lbl), run_time=0.15)
            else:
                self.play(FadeOut(curr_arrow), FadeOut(curr_lbl), run_time=0.2)

            nodes[i][0].set_fill(GREEN, opacity=0.3)
            self.wait(0.3)

        # Final null at end
        null_start = Text("null", font_size=14, color=GRAY).next_to(nodes[0][0], LEFT, buff=0.3)
        rev_arr_last = Arrow(nodes[0][0].get_left(), null_start.get_right(), color=RED, buff=0.05, stroke_width=2, max_tip_length_to_length_ratio=0.15)
        self.play(FadeIn(null_start), GrowArrow(rev_arr_last))

        result = Text("5 -> 4 -> 3 -> 2 -> 1 -> null", font_size=22, color=GOLD).to_edge(DOWN, buff=0.5)
        self.play(FadeOut(step_label), Write(result))
        self.wait(3)


# ══════════════════════════════════════════════════════════════════
# LeetCode 102: Binary Tree Level Order Traversal
# ══════════════════════════════════════════════════════════════════
class LeetCode_BFS(Scene):
    def construct(self):
        title = Text("LeetCode #102 · Binary Tree Level Order", font_size=28, color=BLUE).to_edge(UP, buff=0.2)
        self.play(Write(title))

        # Build a binary tree:    3
        #                        / \
        #                       9   20
        #                          /  \
        #                         15   7
        r = 0.35
        positions = {
            3: UP * 1.2,
            9: UP * 1.2 + LEFT * 2.2 + DOWN * 1.4,
            20: UP * 1.2 + RIGHT * 2.2 + DOWN * 1.4,
            15: UP * 1.2 + RIGHT * 2.2 + DOWN * 1.4 + LEFT * 1.3 + DOWN * 1.4,
            7: UP * 1.2 + RIGHT * 2.2 + DOWN * 1.4 + RIGHT * 1.3 + DOWN * 1.4,
        }
        tree_nodes = {}
        tree_circles = {}
        for val, pos in positions.items():
            circ = Circle(radius=r, color=BLUE, fill_opacity=0.15, fill_color=BLUE).move_to(pos)
            txt = Text(str(val), font_size=22, color=WHITE).move_to(pos)
            tree_nodes[val] = VGroup(circ, txt)
            tree_circles[val] = circ
            self.play(FadeIn(tree_nodes[val]), run_time=0.3)

        edges = [(3, 9), (3, 20), (20, 15), (20, 7)]
        for p, c in edges:
            arr = Line(positions[p] + DOWN * r, positions[c] + UP * r, color=WHITE, stroke_width=2)
            self.play(Create(arr), run_time=0.2)
        self.wait(0.5)

        # Queue visualization at bottom
        queue_title = Text("Queue", font_size=18, color=TEAL).move_to(DOWN * 2 + LEFT * 4.5)
        queue_box = Rectangle(width=8, height=0.8, color=TEAL, stroke_width=1).next_to(queue_title, RIGHT, buff=0.2)
        self.play(Write(queue_title), Create(queue_box))

        # Result on right
        res_title = Text("Result", font_size=18, color=GOLD).move_to(DOWN * 2 + RIGHT * 4.5)
        self.play(Write(res_title))

        # BFS animation
        levels = [[3], [9, 20], [15, 7]]
        level_colors = [RED, GREEN, PURPLE]
        result_rows = VGroup()
        queue_items = VGroup()

        # Enqueue root
        q_item = Text("3", font_size=18, color=WHITE)
        q_item.move_to(queue_box.get_left() + RIGHT * 0.5)
        queue_items.add(q_item)
        self.play(FadeIn(q_item), run_time=0.3)

        for lvl_idx, level in enumerate(levels):
            color = level_colors[lvl_idx]
            lvl_label = Text(f"Level {lvl_idx}", font_size=16, color=color).to_edge(LEFT, buff=0.3).shift(DOWN * (0.5 + lvl_idx * 0.4))
            self.play(Write(lvl_label), run_time=0.3)

            level_vals = []
            next_queue = []

            for val in level:
                # Highlight node being processed
                tree_circles[val].set_fill(color, opacity=0.6)
                self.play(Flash(tree_circles[val], color=color, flash_radius=0.5), run_time=0.4)
                level_vals.append(str(val))

                # Dequeue
                if queue_items:
                    self.play(FadeOut(queue_items[0]), run_time=0.2)
                    queue_items.remove(queue_items[0])

                # Enqueue children
                children = {3: [9, 20], 9: [], 20: [15, 7], 15: [], 7: []}
                for child in children[val]:
                    cq = Text(str(child), font_size=18, color=WHITE)
                    cq.move_to(queue_box.get_left() + RIGHT * (0.5 + len(queue_items) * 0.7))
                    queue_items.add(cq)
                    next_queue.append(child)
                    tree_circles[child].set_stroke(YELLOW, width=3)
                    self.play(FadeIn(cq), run_time=0.2)

            # Show level result
            res_text = Text(f"[{', '.join(level_vals)}]", font_size=18, color=color)
            res_text.next_to(res_title, DOWN, buff=0.2 + lvl_idx * 0.35)
            result_rows.add(res_text)
            self.play(Write(res_text), run_time=0.4)
            self.wait(0.5)

        final = Text("[[3], [9, 20], [15, 7]]", font_size=22, color=GOLD).to_edge(DOWN, buff=0.3)
        self.play(Write(final))
        self.wait(3)


# ══════════════════════════════════════════════════════════════════
# Gaokao 2024: Solid Geometry — 图形为主
# 正三棱柱，D为BC中点，全程3D图形+小标签
# ══════════════════════════════════════════════════════════════════
class Gaokao2024_Solid(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65*DEGREES, theta=-50*DEGREES)

        tag = Text("2024 Gaokao · Solid Geometry", font_size=24, color=GOLD)
        tag.to_corner(UL, buff=0.3)
        self.add_fixed_in_frame_mobjects(tag)
        self.play(Write(tag))

        # Regular triangular prism ABC-A1B1C1, side=2, height=2
        s = 2
        h = 2
        A = np.array([-1, -np.sqrt(3)/3, 0]) * s
        B = np.array([1, -np.sqrt(3)/3, 0]) * s
        C = np.array([0, 2*np.sqrt(3)/3, 0]) * s
        A1 = A + np.array([0, 0, h])
        B1 = B + np.array([0, 0, h])
        C1 = C + np.array([0, 0, h])
        D = (B + C) / 2

        verts = {'A': A, 'B': B, 'C': C, 'A1': A1, 'B1': B1, 'C1': C1, 'D': D}

        bottom_edges = [(A, B), (B, C), (C, A)]
        top_edges = [(A1, B1), (B1, C1), (C1, A1)]
        side_edges = [(A, A1), (B, B1), (C, C1)]

        all_lines = VGroup()
        for v1, v2 in bottom_edges + top_edges + side_edges:
            line = Line3D(v1, v2, color=WHITE, thickness=0.015)
            all_lines.add(line)
        self.play(LaggedStart(*[Create(l) for l in all_lines], lag_ratio=0.05), run_time=2)

        for name, pos in verts.items():
            dot = Dot3D(pos, color=YELLOW, radius=0.05)
            label = Text(name, font_size=14, color=YELLOW)
            self.add_fixed_orientation_mobjects(label)
            offset = normalize(pos - np.array([0, 0, h/2])) * 0.3
            if 'D' in name:
                offset = RIGHT * 0.3
            label.move_to(pos + offset)
            self.play(FadeIn(dot), FadeIn(label), run_time=0.15)

        # D = midpoint of BC
        d_dot = Dot3D(D, color=RED, radius=0.07)
        self.play(FadeIn(d_dot))
        self.wait(0.5)

        # Part 1: Show AD line and prove BC ⊥ plane AA1D
        ad_line = Line3D(A, D, color=RED, thickness=0.03)
        a1d_line = Line3D(A1, D, color=RED, thickness=0.03)
        self.play(Create(ad_line), Create(a1d_line), run_time=0.8)

        # Highlight plane AA1D
        plane_aa1d = Polygon(A, A1, D, fill_color=ORANGE, fill_opacity=0.25, stroke_color=ORANGE, stroke_width=1)
        self.play(FadeIn(plane_aa1d), run_time=0.8)

        # Show BC is perpendicular to AD (isosceles triangle, D midpoint)
        bc_line = Line3D(B, C, color=BLUE, thickness=0.03)
        self.play(Create(bc_line))

        perp_label = MathTex(r"BC \perp AD", font_size=18, color=GREEN)
        perp_label.to_corner(DR, buff=0.3)
        self.add_fixed_in_frame_mobjects(perp_label)
        self.play(Write(perp_label))

        # BC ⊥ AA1 (lateral edge ⊥ base diagonal since prism is regular)
        perp_label2 = MathTex(r"BC \perp AA_1", font_size=18, color=GREEN)
        perp_label2.next_to(perp_label, DOWN, aligned_edge=RIGHT, buff=0.15)
        self.add_fixed_in_frame_mobjects(perp_label2)
        self.play(Write(perp_label2))

        concl1 = MathTex(r"\therefore BC \perp \text{plane } AA_1D", font_size=18, color=GOLD)
        concl1.next_to(perp_label2, DOWN, aligned_edge=RIGHT, buff=0.15)
        self.add_fixed_in_frame_mobjects(concl1)
        self.play(Write(concl1))
        self.wait(1)

        # Rotate to show the geometry
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        # Part 2: Build coordinate system at D, compute dihedral angle
        coord_label = Text("Coordinate system at D", font_size=16, color=TEAL)
        coord_label.to_corner(UL, buff=0.3).shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(coord_label)
        self.play(Write(coord_label))

        # Show axes at D
        ax_len = 1.5
        dx = normalize(B - C)
        dy = normalize(A - D)
        dz = np.array([0, 0, 1])
        x_ax = Arrow3D(D, D + dx * ax_len, color=RED)
        y_ax = Arrow3D(D, D + dy * ax_len, color=GREEN)
        z_ax = Arrow3D(D, D + dz * ax_len, color=BLUE)
        self.play(Create(x_ax), Create(y_ax), Create(z_ax), run_time=0.8)

        # Show normal vectors for dihedral angle
        n1_dir = np.cross(A1 - D, A - D)
        n1_dir = n1_dir / np.linalg.norm(n1_dir)
        n1_arrow = Arrow3D(D, D + n1_dir * 1.2, color=PURPLE)
        self.play(Create(n1_arrow))

        n_label = MathTex(r"\vec{n}", font_size=16, color=PURPLE)
        self.add_fixed_orientation_mobjects(n_label)
        n_label.move_to(D + n1_dir * 1.4)
        self.play(Write(n_label))

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
        self.stop_ambient_camera_rotation()

        angle_result = MathTex(r"\cos\theta = \frac{\sqrt{6}}{3}", font_size=22, color=GOLD)
        angle_result.to_edge(DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(angle_result)
        box = SurroundingRectangle(angle_result, color=GOLD, buff=0.1)
        self.add_fixed_in_frame_mobjects(box)
        self.play(Write(angle_result), Create(box))
        self.wait(3)


# ══════════════════════════════════════════════════════════════════
# Gaokao 2024: Analytic Geometry (Ellipse) — 图形为主
# 椭圆 x²/4+y²/3=1, 过焦点直线交椭圆于AB, 三角形面积
# ══════════════════════════════════════════════════════════════════
class Gaokao2024_Conic(Scene):
    def construct(self):
        tag = Text("2024 Gaokao · Conic Section (Ellipse)", font_size=24, color=GOLD).to_edge(UP, buff=0.2)
        self.play(Write(tag))

        a, b = 2.0, np.sqrt(3)
        c = np.sqrt(a**2 - b**2)  # c = 1

        axes = Axes(x_range=[-3.5, 3.5, 1], y_range=[-2.5, 2.5, 1], x_length=9, y_length=6,
                    axis_config={"include_tip": True, "stroke_width": 1}).shift(DOWN * 0.1)
        self.play(Create(axes), run_time=0.8)

        # Draw ellipse
        ellipse = ParametricFunction(
            lambda t: axes.c2p(a * np.cos(t), b * np.sin(t)),
            t_range=[0, 2 * PI], color=BLUE, stroke_width=3,
        )
        self.play(Create(ellipse), run_time=2)

        eq = MathTex(r"\frac{x^2}{4}+\frac{y^2}{3}=1", font_size=18, color=BLUE).to_corner(UR, buff=0.3)
        self.play(Write(eq))

        # Mark foci
        F1 = axes.c2p(-c, 0)
        F2 = axes.c2p(c, 0)
        f1_dot = Dot(F1, color=RED, radius=0.06)
        f2_dot = Dot(F2, color=RED, radius=0.06)
        f1_lab = MathTex("F_1", font_size=14, color=RED).next_to(f1_dot, DL, buff=0.05)
        f2_lab = MathTex("F_2", font_size=14, color=RED).next_to(f2_dot, DR, buff=0.05)
        self.play(FadeIn(f1_dot), FadeIn(f2_dot), Write(f1_lab), Write(f2_lab))

        # Vertices
        for pt, name in [(axes.c2p(a, 0), "A'"), (axes.c2p(-a, 0), "A"), (axes.c2p(0, b), "B'"), (axes.c2p(0, -b), "B")]:
            d = Dot(pt, color=WHITE, radius=0.04)
            self.play(FadeIn(d), run_time=0.1)
        self.wait(0.5)

        # Animate a chord through F1 at varying angles
        slope_tracker = ValueTracker(0.5)

        def get_chord_points(k):
            # Line through F1(-1, 0): y = k(x+1)
            # Substitute: x²/4 + k²(x+1)²/3 = 1
            # (3 + 4k²)x² + 8k²x + 4k²-12 = 0
            A_coeff = 3 + 4*k**2
            B_coeff = 8*k**2
            C_coeff = 4*k**2 - 12
            disc = B_coeff**2 - 4*A_coeff*C_coeff
            if disc < 0:
                return None, None
            x1 = (-B_coeff + np.sqrt(disc)) / (2*A_coeff)
            x2 = (-B_coeff - np.sqrt(disc)) / (2*A_coeff)
            y1 = k*(x1 + 1)
            y2 = k*(x2 + 1)
            return (x1, y1), (x2, y2)

        chord = always_redraw(lambda: self._make_chord(axes, slope_tracker.get_value(), c, a, b))
        triangle = always_redraw(lambda: self._make_triangle(axes, slope_tracker.get_value(), c, a, b))
        area_label = always_redraw(lambda: self._make_area_label(axes, slope_tracker.get_value(), c, a, b))

        self.add(triangle, chord, area_label)
        self.wait(0.5)

        # Sweep the slope
        self.play(slope_tracker.animate.set_value(3), run_time=3, rate_func=smooth)
        self.play(slope_tracker.animate.set_value(-2), run_time=3, rate_func=smooth)
        self.play(slope_tracker.animate.set_value(1), run_time=2, rate_func=smooth)
        self.wait(0.5)

        # Show the specific case for maximum area
        self.play(slope_tracker.animate.set_value(0.001), run_time=2)
        self.wait(0.5)

        # Vertical chord (infinite slope)
        vert_chord = Line(axes.c2p(-1, b * np.sqrt(1 - 1/4)), axes.c2p(-1, -b * np.sqrt(1 - 1/4)),
                         color=YELLOW, stroke_width=3)
        vert_label = MathTex(r"x = -1", font_size=16, color=YELLOW).next_to(vert_chord, LEFT, buff=0.1)
        self.play(Create(vert_chord), Write(vert_label))

        # Triangle with origin for vertical chord
        y_top = b * np.sqrt(1 - 1/4)
        tri_vert = Polygon(
            axes.c2p(0, 0), axes.c2p(-1, y_top), axes.c2p(-1, -y_top),
            fill_color=GREEN, fill_opacity=0.3, stroke_color=GREEN,
        )
        self.play(FadeIn(tri_vert))

        # Area = 1/2 * |AB| * d = 1/2 * 2*y_top * 1
        area_val = y_top * 1
        max_area = MathTex(rf"S_{{\triangle OAB}} = {area_val:.2f}", font_size=20, color=GOLD).to_edge(DOWN, buff=0.3)
        self.play(Write(max_area))

        # Animate |PF1| + |PF2| = 2a property
        self.play(FadeOut(vert_chord), FadeOut(vert_label), FadeOut(tri_vert), FadeOut(max_area))

        theta_tracker = ValueTracker(0)
        p_dot = always_redraw(lambda: Dot(
            axes.c2p(a*np.cos(theta_tracker.get_value()), b*np.sin(theta_tracker.get_value())),
            color=YELLOW, radius=0.07,
        ))
        pf1_line = always_redraw(lambda: Line(
            F1, axes.c2p(a*np.cos(theta_tracker.get_value()), b*np.sin(theta_tracker.get_value())),
            color=GREEN, stroke_width=2,
        ))
        pf2_line = always_redraw(lambda: Line(
            F2, axes.c2p(a*np.cos(theta_tracker.get_value()), b*np.sin(theta_tracker.get_value())),
            color=PURPLE, stroke_width=2,
        ))
        sum_label = always_redraw(lambda: MathTex(
            rf"|PF_1|+|PF_2| = {self._pf_sum(a, b, c, theta_tracker.get_value()):.2f}",
            font_size=16, color=GOLD,
        ).to_edge(DOWN, buff=0.3))

        self.add(p_dot, pf1_line, pf2_line, sum_label)
        self.play(theta_tracker.animate.set_value(2*PI), run_time=6, rate_func=linear)

        const_label = MathTex(r"|PF_1|+|PF_2| = 2a = 4", font_size=22, color=GOLD).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(sum_label), Write(const_label))
        self.wait(3)

    def _pf_sum(self, a, b, c, theta):
        x = a * np.cos(theta)
        y = b * np.sin(theta)
        d1 = np.sqrt((x + c)**2 + y**2)
        d2 = np.sqrt((x - c)**2 + y**2)
        return d1 + d2

    def _make_chord(self, axes, k, c, a, b):
        if abs(k) < 0.01:
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
        return Line(axes.c2p(x1, y1), axes.c2p(x2, y2), color=YELLOW, stroke_width=2)

    def _make_triangle(self, axes, k, c, a, b):
        if abs(k) < 0.01:
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
        return Polygon(
            axes.c2p(0, 0), axes.c2p(x1, y1), axes.c2p(x2, y2),
            fill_color=GREEN, fill_opacity=0.2, stroke_color=GREEN, stroke_width=1,
        )

    def _make_area_label(self, axes, k, c, a, b):
        if abs(k) < 0.01:
            return VMobject()
        A_c = 3 + 4*k**2
        B_c = 8*k**2
        C_c = 4*k**2 - 12
        disc = B_c**2 - 4*A_c*C_c
        if disc < 0:
            return MathTex("S=?", font_size=16).to_edge(DOWN, buff=0.3)
        x1 = (-B_c + np.sqrt(disc)) / (2*A_c)
        x2 = (-B_c - np.sqrt(disc)) / (2*A_c)
        y1, y2 = k*(x1+1), k*(x2+1)
        area = abs(x1*y2 - x2*y1) / 2
        return MathTex(rf"S_{{\triangle OAB}} = {area:.2f}", font_size=16, color=GOLD).to_edge(DOWN, buff=0.3)


# ══════════════════════════════════════════════════════════════════
# Gaokao 2024: Derivative — 图形为主
# f(x)=e^x-x-1, 讨论单调性+极值+图形全程可见
# ══════════════════════════════════════════════════════════════════
class Gaokao2024_Derivative(Scene):
    def construct(self):
        tag = Text("2024 Gaokao · Derivative & Function", font_size=24, color=GOLD).to_edge(UP, buff=0.2)
        self.play(Write(tag))

        # Full-screen axes
        axes = Axes(x_range=[-3, 3, 1], y_range=[-2, 6, 1], x_length=10, y_length=6,
                    axis_config={"include_tip": True, "stroke_width": 1}).shift(DOWN * 0.2)
        self.play(Create(axes), run_time=0.8)

        # f(x) = e^x - x - 1
        f = lambda x: np.exp(x) - x - 1
        f_graph = axes.plot(f, x_range=[-2.8, 2.3], color=BLUE, stroke_width=3)
        f_label = MathTex(r"f(x) = e^x - x - 1", font_size=18, color=BLUE).to_corner(UR, buff=0.3)
        self.play(Create(f_graph), Write(f_label), run_time=2)
        self.wait(0.5)

        # f'(x) = e^x - 1
        fp = lambda x: np.exp(x) - 1
        fp_graph = axes.plot(fp, x_range=[-2.8, 2.0], color=YELLOW, stroke_width=2, stroke_opacity=0.7)
        fp_label = MathTex(r"f'(x) = e^x - 1", font_size=16, color=YELLOW).next_to(f_label, DOWN, aligned_edge=RIGHT, buff=0.1)
        self.play(Create(fp_graph), Write(fp_label), run_time=1.5)
        self.wait(0.5)

        # Zero of f': x=0
        zero_dot = Dot(axes.c2p(0, 0), color=RED, radius=0.08)
        zero_label = MathTex("(0, 0)", font_size=14, color=RED).next_to(zero_dot, DR, buff=0.05)
        self.play(FadeIn(zero_dot), Write(zero_label))

        # Minimum point on f
        min_dot = Dot(axes.c2p(0, f(0)), color=GREEN, radius=0.08)
        min_label = MathTex(r"f(0)=0 \;\text{min}", font_size=14, color=GREEN).next_to(min_dot, DL, buff=0.05)
        v_dash = DashedLine(axes.c2p(0, 0), axes.c2p(0, f(0)+0.01), color=GREEN, stroke_opacity=0.5)
        self.play(FadeIn(min_dot), Write(min_label), Create(v_dash))
        self.wait(0.5)

        # Animate tangent line sweeping across the curve
        x_val = ValueTracker(-2)

        tangent = always_redraw(lambda: self._tangent_line(axes, f, fp, x_val.get_value()))
        tang_dot = always_redraw(lambda: Dot(
            axes.c2p(x_val.get_value(), f(x_val.get_value())), color=ORANGE, radius=0.06,
        ))
        slope_label = always_redraw(lambda: MathTex(
            rf"k = {fp(x_val.get_value()):.2f}",
            font_size=14, color=ORANGE,
        ).next_to(axes.c2p(x_val.get_value(), f(x_val.get_value())), UP, buff=0.2))

        self.add(tangent, tang_dot, slope_label)
        self.play(x_val.animate.set_value(2), run_time=5, rate_func=smooth)
        self.wait(0.5)

        # Show decreasing/increasing regions with shading
        self.play(FadeOut(tangent), FadeOut(tang_dot), FadeOut(slope_label))

        dec_region = axes.get_area(fp_graph, x_range=[-2.5, 0], color=RED, opacity=0.15)
        inc_region = axes.get_area(fp_graph, x_range=[0, 2], color=GREEN, opacity=0.15, bounded_graph=axes.plot(lambda x: 0, x_range=[0, 2]))

        dec_text = MathTex(r"f'<0 \;\downarrow", font_size=16, color=RED).move_to(axes.c2p(-1.5, -0.5))
        inc_text = MathTex(r"f'>0 \;\uparrow", font_size=16, color=GREEN).move_to(axes.c2p(1.5, 1.5))

        self.play(FadeIn(dec_region), Write(dec_text))
        self.play(FadeIn(inc_region), Write(inc_text))
        self.wait(1)

        # f(x) >= 0 proof visualization: shade the area above x-axis
        self.play(FadeOut(dec_region), FadeOut(inc_region), FadeOut(dec_text), FadeOut(inc_text),
                  FadeOut(fp_graph), FadeOut(fp_label))

        # x-axis as baseline
        x_axis_highlight = DashedLine(axes.c2p(-3, 0), axes.c2p(3, 0), color=GRAY)
        self.play(Create(x_axis_highlight))

        # Show f(x) >= 0: the curve is always above or on x-axis
        above_area = axes.get_area(f_graph, x_range=[-2.5, 2.3], color=BLUE, opacity=0.15)
        self.play(FadeIn(above_area))

        proof_text = MathTex(r"f(x) \ge f(0) = 0, \;\forall x \in \mathbb{R}", font_size=20, color=GOLD)
        proof_text.to_edge(DOWN, buff=0.3)
        box = SurroundingRectangle(proof_text, color=GOLD, buff=0.1)
        self.play(Write(proof_text), Create(box))
        self.wait(1)

        # Parametric family: vary a in f(x) = e^x - ax - 1
        self.play(*[FadeOut(m) for m in [above_area, proof_text, box, x_axis_highlight, zero_dot, zero_label, min_dot, min_label, v_dash]])

        a_tracker = ValueTracker(1)
        param_curve = always_redraw(lambda: axes.plot(
            lambda x: np.exp(x) - a_tracker.get_value() * x - 1,
            x_range=[-2.8, 2.3], color=BLUE, stroke_width=3,
        ))
        param_label = always_redraw(lambda: MathTex(
            rf"f(x) = e^x - {a_tracker.get_value():.1f}x - 1",
            font_size=18, color=BLUE,
        ).to_corner(UR, buff=0.3))

        # Find and mark minimum for current a
        min_marker = always_redraw(lambda: Dot(
            axes.c2p(np.log(max(0.01, a_tracker.get_value())),
                     np.exp(np.log(max(0.01, a_tracker.get_value()))) - a_tracker.get_value() * np.log(max(0.01, a_tracker.get_value())) - 1),
            color=RED, radius=0.08,
        ))

        self.play(FadeOut(f_graph), FadeOut(f_label))
        self.add(param_curve, param_label, min_marker)

        a_label = always_redraw(lambda: MathTex(
            rf"a = {a_tracker.get_value():.1f}", font_size=20, color=ORANGE,
        ).to_edge(DOWN, buff=0.3))
        self.add(a_label)

        # Sweep a from 0 to 4
        self.play(a_tracker.animate.set_value(0.1), run_time=2)
        self.play(a_tracker.animate.set_value(4), run_time=4, rate_func=smooth)
        self.play(a_tracker.animate.set_value(1), run_time=2)
        self.wait(0.5)

        # At a=1: minimum is exactly 0 (tangent to x-axis)
        final = MathTex(r"a=1: f_{\min}=f(0)=0 \;\;\text{tangent to x-axis}", font_size=18, color=GOLD)
        final.to_edge(DOWN, buff=0.3)
        self.play(FadeOut(a_label), Write(final))
        self.wait(3)

    def _tangent_line(self, axes, f, fp, x0):
        y0 = f(x0)
        k = fp(x0)
        x_left = x0 - 1.5
        x_right = x0 + 1.5
        return Line(
            axes.c2p(x_left, y0 + k*(x_left - x0)),
            axes.c2p(x_right, y0 + k*(x_right - x0)),
            color=ORANGE, stroke_width=2, stroke_opacity=0.7,
        )
