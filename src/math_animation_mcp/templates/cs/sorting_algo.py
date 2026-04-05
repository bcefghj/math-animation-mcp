"""冒泡排序可视化
Bubble sort algorithm visualization with animated bar swaps.
Keywords: 排序, sorting, 冒泡, bubble sort, 算法, algorithm, 可视化
Difficulty: 2
"""
from manim import *
import numpy as np


class BubbleSort(Scene):
    def construct(self):
        title = Text("冒泡排序", font_size=48)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        data = [5, 3, 8, 1, 6, 2, 7, 4]
        n = len(data)

        bars = VGroup()
        labels = VGroup()
        max_val = max(data)

        for i, val in enumerate(data):
            bar = Rectangle(
                width=0.6, height=val * 0.4,
                fill_color=BLUE, fill_opacity=0.7,
                stroke_color=WHITE, stroke_width=1,
            )
            bar.move_to(LEFT * 3 + RIGHT * i * 0.8 + UP * (val * 0.2 - 1.5))
            bars.add(bar)

            label = Text(str(val), font_size=20)
            label.next_to(bar, DOWN, buff=0.1)
            labels.add(label)

        self.play(*[Create(b) for b in bars], *[Write(l) for l in labels])
        self.wait(0.5)

        step_counter = Text("步骤: 0", font_size=24).to_corner(UR)
        self.play(Write(step_counter))

        step = 0
        for i in range(n):
            for j in range(n - i - 1):
                step += 1
                # Highlight comparison pair
                self.play(
                    bars[j].animate.set_fill(YELLOW),
                    bars[j + 1].animate.set_fill(YELLOW),
                    run_time=0.2,
                )

                if data[j] > data[j + 1]:
                    # Swap
                    data[j], data[j + 1] = data[j + 1], data[j]
                    self.play(
                        bars[j].animate.set_fill(RED),
                        bars[j + 1].animate.set_fill(RED),
                        run_time=0.15,
                    )

                    pos_j = bars[j].get_center()
                    pos_j1 = bars[j + 1].get_center()
                    self.play(
                        bars[j].animate.move_to(np.array([pos_j1[0], pos_j[1] + (data[j] - data[j+1]) * 0.2, 0])),
                        bars[j + 1].animate.move_to(np.array([pos_j[0], pos_j1[1] + (data[j+1] - data[j]) * 0.2, 0])),
                        run_time=0.3,
                    )
                    bars[j], bars[j + 1] = bars[j + 1], bars[j]
                    labels[j], labels[j + 1] = labels[j + 1], labels[j]

                self.play(
                    bars[j].animate.set_fill(BLUE),
                    bars[j + 1].animate.set_fill(GREEN if j + 1 >= n - i - 1 else BLUE),
                    run_time=0.15,
                )

                if step > 15:
                    break
            if step > 15:
                break

        # Final state all green
        self.play(*[b.animate.set_fill(GREEN) for b in bars])
        done = Text("排序完成!", font_size=36, color=GREEN).to_edge(DOWN)
        self.play(Write(done))
        self.wait(1)
