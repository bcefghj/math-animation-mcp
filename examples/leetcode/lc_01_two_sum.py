# LeetCode #1: Two Sum — Long visual-first animation (~2min)
from manim import *
import numpy as np

class LeetCode_TwoSum_Long(Scene):
    def construct(self):
        # ── Title ──
        title = Text("LeetCode #1 · Two Sum", font_size=36, color=BLUE)
        subtitle = Text("Find two numbers that add up to target", font_size=20, color=GRAY)
        VGroup(title, subtitle).arrange(DOWN, buff=0.2).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP*0.2), run_time=0.5)
        self.wait(1)

        # ── Problem Setup: Array visual ──
        nums = [2, 7, 11, 15, 1, 8, 3]
        target = 9
        bw, bh = 0.9, 0.7

        arr = VGroup()
        for i, v in enumerate(nums):
            r = Rectangle(width=bw, height=bh, color=WHITE, stroke_width=2,
                          fill_color=DARK_BLUE, fill_opacity=0.3)
            vt = Text(str(v), font_size=26, color=WHITE).move_to(r)
            it = Text(str(i), font_size=12, color=GRAY).next_to(r, DOWN, buff=0.03)
            arr.add(VGroup(r, vt, it))
        arr.arrange(RIGHT, buff=0.1).move_to(UP * 1)

        target_box = VGroup(
            Rectangle(width=1.6, height=0.6, color=GOLD, stroke_width=2, fill_color=GOLD, fill_opacity=0.15),
            MathTex(r"\text{target}=9", font_size=20, color=GOLD),
        )
        target_box[1].move_to(target_box[0])
        target_box.to_corner(UR, buff=0.3)

        self.play(FadeOut(subtitle))
        self.play(LaggedStart(*[GrowFromCenter(a) for a in arr], lag_ratio=0.08), run_time=1.5)
        self.play(FadeIn(target_box, shift=LEFT * 0.3), run_time=0.5)
        self.wait(0.8)

        # ── Part 1: Brute Force O(n²) ──
        bf_title = Text("Approach 1: Brute Force", font_size=22, color=RED).to_edge(LEFT, buff=0.4).shift(DOWN*0.3)
        complexity = MathTex(r"O(n^2)", font_size=20, color=RED).next_to(bf_title, RIGHT, buff=0.3)
        self.play(Write(bf_title), Write(complexity))

        # Two nested loops visualized
        comparisons = 0
        comp_counter = always_redraw(lambda: Text(
            f"Comparisons: {comparisons}", font_size=14, color=GRAY
        ).to_edge(DOWN, buff=0.3))
        self.add(comp_counter)

        found_bf = False
        for i in range(len(nums)):
            hi_i = arr[i][0].copy().set_fill(RED, opacity=0.4).set_stroke(RED, width=3)
            i_label = Text("i", font_size=14, color=RED).next_to(arr[i], UP, buff=0.08)
            self.play(FadeIn(hi_i), FadeIn(i_label), run_time=0.15)

            for j in range(i + 1, len(nums)):
                hi_j = arr[j][0].copy().set_fill(YELLOW, opacity=0.3).set_stroke(YELLOW, width=3)
                j_label = Text("j", font_size=14, color=YELLOW).next_to(arr[j], UP, buff=0.08)
                self.play(FadeIn(hi_j), FadeIn(j_label), run_time=0.08)

                s = nums[i] + nums[j]
                comparisons += 1
                # Show addition
                add_eq = MathTex(f"{nums[i]}+{nums[j]}={s}", font_size=18,
                                 color=GREEN if s == target else GRAY)
                add_eq.move_to(DOWN * 1.5)
                self.play(Write(add_eq), run_time=0.1)

                if s == target:
                    self.play(
                        hi_i.animate.set_fill(GREEN, opacity=0.6),
                        hi_j.animate.set_fill(GREEN, opacity=0.6),
                        Flash(arr[i], color=GREEN), Flash(arr[j], color=GREEN),
                    )
                    result = Text(f"Found! [{i}, {j}]", font_size=22, color=GREEN).next_to(add_eq, DOWN, buff=0.2)
                    self.play(Write(result))
                    self.wait(1.5)
                    self.play(FadeOut(result), FadeOut(add_eq), FadeOut(hi_j), FadeOut(j_label))
                    found_bf = True
                    break

                self.play(FadeOut(hi_j), FadeOut(j_label), FadeOut(add_eq), run_time=0.05)

            self.play(FadeOut(hi_i), FadeOut(i_label), run_time=0.08)
            if found_bf:
                break

        self.play(FadeOut(comp_counter))
        self.wait(0.5)

        # Show why brute force is bad: nested loop diagram
        loop_box = VGroup()
        for i in range(6):
            for j in range(6):
                sq = Square(side_length=0.15, color=RED if j > i else DARK_GRAY,
                           fill_opacity=0.3 if j > i else 0.05, stroke_width=0.5)
                sq.move_to(DOWN * 1.5 + RIGHT * (j * 0.18 - 0.5) + DOWN * (i * 0.18))
                loop_box.add(sq)
        loop_box.move_to(DOWN * 2)
        n2_label = MathTex(r"\frac{n(n-1)}{2}", font_size=16, color=RED).next_to(loop_box, RIGHT, buff=0.2)
        self.play(FadeIn(loop_box), Write(n2_label), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(loop_box), FadeOut(n2_label), FadeOut(bf_title), FadeOut(complexity))

        # ── Part 2: HashMap O(n) — The smart way ──
        hm_title = Text("Approach 2: HashMap", font_size=22, color=GREEN).to_edge(LEFT, buff=0.4).shift(DOWN*0.3)
        complexity2 = MathTex(r"O(n)", font_size=20, color=GREEN).next_to(hm_title, RIGHT, buff=0.3)
        self.play(Write(hm_title), Write(complexity2))

        # HashMap as a visual structure on the right
        hm_header = Text("HashMap {val: idx}", font_size=14, color=TEAL).move_to(DOWN * 0.5 + RIGHT * 4)
        hm_bg = RoundedRectangle(width=2.8, height=3.2, corner_radius=0.1, color=TEAL,
                                  stroke_width=1, fill_opacity=0.05).next_to(hm_header, DOWN, buff=0.1)
        self.play(Write(hm_header), Create(hm_bg))

        hashmap = {}
        hm_entries = VGroup()
        step_count = 0

        for i, v in enumerate(nums):
            step_count += 1
            # Pointer arrow on current element
            ptr = Triangle(fill_color=GREEN, fill_opacity=1, color=GREEN).scale(0.12).rotate(-PI/2)
            ptr.next_to(arr[i], UP, buff=0.05)
            arr[i][0].set_stroke(GREEN, width=4)
            self.play(FadeIn(ptr), run_time=0.2)

            complement = target - v
            # Show complement computation
            comp_eq = MathTex(f"{target}-{v}={complement}", font_size=16, color=YELLOW)
            comp_eq.move_to(DOWN * 0.5 + LEFT * 2)
            self.play(Write(comp_eq), run_time=0.3)

            # Check in HashMap
            if complement in hashmap:
                j = hashmap[complement]
                arr[j][0].set_stroke(GOLD, width=5).set_fill(GOLD, opacity=0.4)
                arr[i][0].set_fill(GOLD, opacity=0.4)
                found_label = Text(f"Found! complement {complement} at index {j}", font_size=16, color=GOLD)
                found_label.move_to(DOWN * 1.5)
                self.play(Write(found_label), Flash(arr[i], color=GOLD), Flash(arr[j], color=GOLD))

                # Animated connection line
                conn = Line(arr[j].get_center(), arr[i].get_center(), color=GOLD, stroke_width=3)
                self.play(Create(conn))

                result = MathTex(rf"\text{{return }} [{j}, {i}]", font_size=24, color=GOLD)
                result.move_to(DOWN * 2.5)
                box = SurroundingRectangle(result, color=GOLD, buff=0.1)
                self.play(Write(result), Create(box))
                self.wait(2)
                break
            else:
                miss = Text("Not in map", font_size=12, color=GRAY).next_to(comp_eq, DOWN, buff=0.1)
                self.play(FadeIn(miss), run_time=0.15)

                # Add to hashmap with animation
                entry = MathTex(f"{v} \\to {i}", font_size=14, color=TEAL)
                entry.move_to(hm_bg.get_top() + DOWN * (0.25 + len(hm_entries) * 0.32))
                hm_entries.add(entry)
                hashmap[v] = i

                # Arrow from array element to hashmap entry
                add_arrow = Arrow(arr[i].get_bottom(), entry.get_left(), color=TEAL,
                                  stroke_width=1.5, max_tip_length_to_length_ratio=0.15, buff=0.1)
                self.play(Write(entry), GrowArrow(add_arrow), run_time=0.3)
                self.play(FadeOut(add_arrow), FadeOut(miss), run_time=0.15)

            self.play(FadeOut(ptr), FadeOut(comp_eq), arr[i][0].animate.set_stroke(WHITE, width=2), run_time=0.15)

        self.wait(3)
