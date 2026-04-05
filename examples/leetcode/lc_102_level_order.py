# LeetCode #102: Binary Tree Level Order Traversal — Long visual-first animation (~2min)
from manim import *
import numpy as np

class LeetCode_BFS_Long(Scene):
    def construct(self):
        title = Text("LeetCode #102 · Level Order Traversal", font_size=32, color=BLUE)
        subtitle = Text("BFS with queue, visit tree level by level", font_size=18, color=GRAY)
        VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.25)
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP*0.2), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(subtitle))

        # ── Build tree ──
        #         3
        #        / \
        #       9   20
        #      / \   / \
        #     8  12 15  7
        r = 0.35
        level_gap_y = 1.3
        tree_data = {
            3:  {'pos': UP*1.0, 'children': [9, 20]},
            9:  {'pos': UP*1.0 + LEFT*2.5 + DOWN*level_gap_y, 'children': [8, 12]},
            20: {'pos': UP*1.0 + RIGHT*2.5 + DOWN*level_gap_y, 'children': [15, 7]},
            8:  {'pos': UP*1.0 + LEFT*2.5 + DOWN*level_gap_y + LEFT*1.3 + DOWN*level_gap_y, 'children': []},
            12: {'pos': UP*1.0 + LEFT*2.5 + DOWN*level_gap_y + RIGHT*1.3 + DOWN*level_gap_y, 'children': []},
            15: {'pos': UP*1.0 + RIGHT*2.5 + DOWN*level_gap_y + LEFT*1.3 + DOWN*level_gap_y, 'children': []},
            7:  {'pos': UP*1.0 + RIGHT*2.5 + DOWN*level_gap_y + RIGHT*1.3 + DOWN*level_gap_y, 'children': []},
        }

        tree_nodes = {}
        tree_circles = {}
        edges = VGroup()

        for val, info in tree_data.items():
            pos = info['pos']
            circ = Circle(radius=r, color=BLUE, fill_opacity=0.1, fill_color=BLUE).move_to(pos)
            txt = Text(str(val), font_size=22, color=WHITE).move_to(pos)
            tree_nodes[val] = VGroup(circ, txt)
            tree_circles[val] = circ

        for val, info in tree_data.items():
            for child in info['children']:
                p1 = info['pos'] + DOWN * r
                p2 = tree_data[child]['pos'] + UP * r
                e = Line(p1, p2, color=WHITE, stroke_width=1.5)
                edges.add(e)

        # Animate tree appearing level by level
        levels_list = [[3], [9, 20], [8, 12, 15, 7]]
        for lvl in levels_list:
            anims = [FadeIn(tree_nodes[v]) for v in lvl]
            self.play(LaggedStart(*anims, lag_ratio=0.1), run_time=0.6)
        self.play(LaggedStart(*[Create(e) for e in edges], lag_ratio=0.05), run_time=0.8)
        self.wait(0.5)

        # ── Queue box at bottom ──
        q_bg = RoundedRectangle(width=9, height=0.9, corner_radius=0.08, color=TEAL,
                                 stroke_width=1, fill_opacity=0.05)
        q_bg.to_edge(DOWN, buff=0.8)
        q_label = Text("Queue", font_size=14, color=TEAL).next_to(q_bg, LEFT, buff=0.15)
        self.play(Create(q_bg), Write(q_label))

        # Result area on right
        res_header = Text("Output", font_size=14, color=GOLD).to_corner(DR, buff=0.3).shift(UP*2.5)
        self.play(Write(res_header))

        # ── BFS ──
        level_colors = [RED, GREEN, PURPLE, ORANGE]
        queue = [3]
        q_visuals = VGroup()

        # Enqueue root
        q_item = self._make_q_item(3, q_bg)
        q_visuals.add(q_item)
        self.play(FadeIn(q_item), run_time=0.3)

        result_texts = VGroup()
        for lvl_idx, level in enumerate(levels_list):
            color = level_colors[lvl_idx % len(level_colors)]

            # Level indicator
            lvl_indicator = Text(f"Level {lvl_idx}", font_size=16, color=color)
            lvl_indicator.to_edge(LEFT, buff=0.3).shift(DOWN * 3)
            self.play(Write(lvl_indicator), run_time=0.3)

            # Process current level size
            size_label = Text(f"queue size = {len(level)}", font_size=12, color=color)
            size_label.next_to(lvl_indicator, RIGHT, buff=0.3)
            self.play(Write(size_label), run_time=0.2)

            level_vals = []

            for val in level:
                # Highlight being-processed node
                tree_circles[val].set_fill(color, opacity=0.5)
                self.play(
                    Indicate(tree_circles[val], color=color, scale_factor=1.3),
                    run_time=0.5,
                )
                level_vals.append(str(val))

                # Dequeue: remove from front
                if q_visuals:
                    self.play(
                        q_visuals[0].animate.shift(DOWN * 0.5).set_opacity(0),
                        run_time=0.3,
                    )
                    q_visuals.remove(q_visuals[0])
                    # Shift remaining left
                    if q_visuals:
                        self.play(q_visuals.animate.arrange(RIGHT, buff=0.15).move_to(q_bg.get_center()), run_time=0.2)

                # Enqueue children
                for child in tree_data[val]['children']:
                    tree_circles[child].set_stroke(YELLOW, width=3)
                    cq = self._make_q_item(child, q_bg)
                    if q_visuals:
                        cq.next_to(q_visuals[-1], RIGHT, buff=0.15)
                    else:
                        cq.move_to(q_bg.get_center())
                    q_visuals.add(cq)

                    # Animate: line from parent to child, then item appears in queue
                    connect = DashedLine(
                        tree_data[val]['pos'], tree_data[child]['pos'],
                        color=YELLOW, stroke_width=1.5, dash_length=0.1,
                    )
                    self.play(Create(connect), run_time=0.2)
                    self.play(FadeIn(cq, shift=UP*0.3), run_time=0.3)
                    self.play(FadeOut(connect), run_time=0.1)

                self.wait(0.2)

            # Show level result
            res = Text(f"[{', '.join(level_vals)}]", font_size=16, color=color)
            res.next_to(res_header, DOWN, buff=0.15 + lvl_idx * 0.35)
            result_texts.add(res)
            self.play(Write(res), run_time=0.4)
            self.play(FadeOut(lvl_indicator), FadeOut(size_label), run_time=0.2)
            self.wait(0.4)

        # ── Final result ──
        self.wait(0.5)
        final = Text("[[3], [9, 20], [8, 12, 15, 7]]", font_size=22, color=GOLD)
        final.to_edge(DOWN, buff=0.2)
        box = SurroundingRectangle(final, color=GOLD, buff=0.08)
        self.play(Write(final), Create(box))

        # Flash all nodes one last time
        for val in [3, 9, 20, 8, 12, 15, 7]:
            self.play(Flash(tree_circles[val], color=GOLD, flash_radius=0.4), run_time=0.15)

        self.wait(3)

    def _make_q_item(self, val, q_bg):
        r = Rectangle(width=0.6, height=0.45, color=TEAL, stroke_width=1.5,
                       fill_color=TEAL, fill_opacity=0.15)
        t = Text(str(val), font_size=18, color=WHITE).move_to(r)
        g = VGroup(r, t)
        g.move_to(q_bg.get_center())
        return g
