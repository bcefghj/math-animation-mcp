# LeetCode #206: Reverse Linked List — Long visual-first animation (~2min)
from manim import *
import numpy as np

class LeetCode_ReverseList_Long(Scene):
    def construct(self):
        title = Text("LeetCode #206 · Reverse Linked List", font_size=34, color=BLUE)
        subtitle = Text("Reverse a singly linked list in-place", font_size=18, color=GRAY)
        VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.25)
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP*0.2), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(subtitle))

        vals = [1, 2, 3, 4, 5]
        n = len(vals)
        r = 0.38
        sp = 1.7

        # Build linked list: circles + arrows, Y = +0.8
        nodes = VGroup()
        arrows = VGroup()
        base_y = 0.8
        start_x = -(n-1)*sp/2

        for i, v in enumerate(vals):
            pos = RIGHT * (start_x + i*sp) + UP * base_y
            circ = Circle(radius=r, color=BLUE, fill_opacity=0.15, fill_color=BLUE).move_to(pos)
            txt = Text(str(v), font_size=28, color=WHITE).move_to(pos)
            idx = Text(f"node {i}", font_size=10, color=GRAY_B).next_to(circ, DOWN, buff=0.08)
            nodes.add(VGroup(circ, txt, idx))

        for i in range(n-1):
            a = Arrow(
                nodes[i][0].get_right(), nodes[i+1][0].get_left(),
                color=WHITE, buff=0.08, stroke_width=2.5,
                max_tip_length_to_length_ratio=0.12,
            )
            arrows.add(a)

        null_end = Text("null", font_size=14, color=GRAY_B).next_to(nodes[-1][0], RIGHT, buff=0.3)

        self.play(LaggedStart(*[GrowFromCenter(nd) for nd in nodes], lag_ratio=0.1), run_time=1.2)
        self.play(
            LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1),
            FadeIn(null_end),
            run_time=1,
        )
        self.wait(1)

        # ── Show the concept: what we want ──
        want_label = Text("Goal: reverse all arrow directions", font_size=18, color=GOLD).to_edge(DOWN, buff=0.4)
        self.play(Write(want_label))
        self.wait(1.5)
        self.play(FadeOut(want_label))

        # ── Three pointers ──
        PREV_C = RED
        CURR_C = GREEN
        NEXT_C = YELLOW

        legend = VGroup(
            VGroup(Dot(color=PREV_C, radius=0.06), Text("prev", font_size=12, color=PREV_C)).arrange(RIGHT, buff=0.1),
            VGroup(Dot(color=CURR_C, radius=0.06), Text("curr", font_size=12, color=CURR_C)).arrange(RIGHT, buff=0.1),
            VGroup(Dot(color=NEXT_C, radius=0.06), Text("next_node", font_size=12, color=NEXT_C)).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.15)
        self.play(FadeIn(legend))

        # Initial state: prev=null, curr=head
        null_label = Text("null", font_size=14, color=PREV_C)
        null_label.next_to(nodes[0][0], LEFT, buff=0.8)
        prev_arrow = Arrow(ORIGIN, DOWN*0.35, color=PREV_C, stroke_width=3,
                           max_tip_length_to_length_ratio=0.4).scale(0.6)
        prev_arrow.next_to(null_label, UP, buff=0.04)
        prev_tag = Text("prev", font_size=11, color=PREV_C).next_to(prev_arrow, UP, buff=0.02)

        curr_arrow = Arrow(ORIGIN, DOWN*0.35, color=CURR_C, stroke_width=3,
                           max_tip_length_to_length_ratio=0.4).scale(0.6)
        curr_arrow.next_to(nodes[0][0], UP, buff=0.05)
        curr_tag = Text("curr", font_size=11, color=CURR_C).next_to(curr_arrow, UP, buff=0.02)

        prev_group = VGroup(prev_arrow, prev_tag, null_label)
        curr_group = VGroup(curr_arrow, curr_tag)

        self.play(FadeIn(prev_group), FadeIn(curr_group))
        self.wait(1)

        # Step counter
        step_txt = Text("", font_size=16, color=GOLD).to_corner(DL, buff=0.3)

        reversed_arrows = VGroup()

        for step in range(n):
            # Step label
            new_step = Text(f"Step {step+1} / {n}", font_size=16, color=GOLD).to_corner(DL, buff=0.3)
            self.play(FadeOut(step_txt), FadeIn(new_step), run_time=0.2)
            step_txt = new_step

            # Highlight current node
            nodes[step][0].set_stroke(CURR_C, width=4)
            self.play(Flash(nodes[step][0], color=CURR_C, flash_radius=0.5, line_length=0.15), run_time=0.4)

            # 1) Save next
            if step < n - 1:
                nxt_arrow = Arrow(ORIGIN, DOWN*0.3, color=NEXT_C, stroke_width=2,
                                  max_tip_length_to_length_ratio=0.4).scale(0.6)
                nxt_arrow.next_to(nodes[step+1][0], UP, buff=0.35)
                nxt_tag = Text("next", font_size=11, color=NEXT_C).next_to(nxt_arrow, UP, buff=0.02)
                save_text = Text("save next", font_size=12, color=NEXT_C).move_to(DOWN * 2 + RIGHT * 3)
                self.play(FadeIn(nxt_arrow), FadeIn(nxt_tag), FadeIn(save_text), run_time=0.4)
                self.wait(0.3)
                self.play(FadeOut(save_text), run_time=0.2)

            # 2) Reverse the arrow: curr.next = prev
            nodes[step][0].set_fill(ORANGE, opacity=0.35)
            action_text = Text("reverse: curr.next = prev", font_size=12, color=ORANGE).move_to(DOWN * 2 + RIGHT * 3)
            self.play(FadeIn(action_text), run_time=0.3)

            if step < len(arrows):
                self.play(arrows[step].animate.set_opacity(0.15), run_time=0.3)

            if step > 0:
                rev = Arrow(
                    nodes[step][0].get_left(), nodes[step-1][0].get_right(),
                    color=RED, buff=0.08, stroke_width=3,
                    max_tip_length_to_length_ratio=0.12,
                )
                reversed_arrows.add(rev)
                self.play(GrowArrow(rev), run_time=0.5)
            else:
                # First node now points to null
                null_new = Text("null", font_size=12, color=RED).next_to(nodes[0][0], LEFT, buff=0.3)
                rev0 = Arrow(nodes[0][0].get_left(), null_new.get_right(), color=RED, buff=0.05,
                             stroke_width=2, max_tip_length_to_length_ratio=0.15)
                self.play(FadeIn(null_new), GrowArrow(rev0), run_time=0.5)

            self.play(FadeOut(action_text), run_time=0.2)
            self.wait(0.3)

            # 3) Move prev to curr
            move_text = Text("prev = curr", font_size=12, color=PREV_C).move_to(DOWN * 2 + RIGHT * 3)
            self.play(FadeIn(move_text), run_time=0.2)

            new_prev_arrow = Arrow(ORIGIN, DOWN*0.35, color=PREV_C, stroke_width=3,
                                   max_tip_length_to_length_ratio=0.4).scale(0.6)
            new_prev_arrow.next_to(nodes[step][0], UP, buff=0.05)
            new_prev_tag = Text("prev", font_size=11, color=PREV_C).next_to(new_prev_arrow, UP, buff=0.02)

            self.play(Transform(prev_group, VGroup(new_prev_arrow, new_prev_tag)), run_time=0.3)
            self.play(FadeOut(move_text), run_time=0.15)

            # 4) Move curr to next
            move_text2 = Text("curr = next", font_size=12, color=CURR_C).move_to(DOWN * 2 + RIGHT * 3)
            self.play(FadeIn(move_text2), run_time=0.2)

            if step < n - 1:
                new_curr_arrow = Arrow(ORIGIN, DOWN*0.35, color=CURR_C, stroke_width=3,
                                       max_tip_length_to_length_ratio=0.4).scale(0.6)
                new_curr_arrow.next_to(nodes[step+1][0], UP, buff=0.05)
                new_curr_tag = Text("curr", font_size=11, color=CURR_C).next_to(new_curr_arrow, UP, buff=0.02)
                self.play(Transform(curr_group, VGroup(new_curr_arrow, new_curr_tag)), run_time=0.3)
                self.play(FadeOut(nxt_arrow), FadeOut(nxt_tag), run_time=0.15)
            else:
                self.play(FadeOut(curr_group), run_time=0.2)

            self.play(FadeOut(move_text2), run_time=0.15)
            nodes[step][0].set_fill(GREEN, opacity=0.2).set_stroke(BLUE, width=2)
            self.wait(0.4)

        self.wait(0.5)

        # ── Final result ──
        self.play(FadeOut(step_txt), FadeOut(prev_group), FadeOut(legend), FadeOut(null_end))

        result_label = Text("Reversed:", font_size=20, color=GOLD).to_edge(DOWN, buff=0.5)
        result = Text("5 -> 4 -> 3 -> 2 -> 1 -> null", font_size=24, color=GOLD).next_to(result_label, DOWN, buff=0.1)
        box = SurroundingRectangle(result, color=GOLD, buff=0.1)
        self.play(Write(result_label), Write(result), Create(box))

        # Animate all nodes lighting up in reverse
        for i in range(n-1, -1, -1):
            self.play(Flash(nodes[i][0], color=GREEN, flash_radius=0.4), run_time=0.3)

        self.wait(3)
