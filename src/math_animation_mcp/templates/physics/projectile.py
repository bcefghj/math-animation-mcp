"""抛体运动
Projectile motion with trajectory, velocity components, and equations.
Keywords: 抛体运动, projectile, 弹道, trajectory, 重力, gravity, 物理
Difficulty: 3
"""
from manim import *
import numpy as np


class ProjectileMotion(Scene):
    def construct(self):
        title = Text("抛体运动", font_size=48)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.6))

        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 5, 1],
            x_length=8, y_length=4.5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.5)
        x_label = axes.get_x_axis_label("x(m)")
        y_label = axes.get_y_axis_label("y(m)")
        self.play(Create(axes), Write(x_label), Write(y_label))

        v0 = 7
        angle = PI / 4
        g = 9.8

        def trajectory(t):
            x = v0 * np.cos(angle) * t
            y = v0 * np.sin(angle) * t - 0.5 * g * t**2
            return np.array([x, max(y, 0), 0])

        t_flight = 2 * v0 * np.sin(angle) / g

        path = axes.plot_parametric_curve(
            lambda t: np.array([
                v0 * np.cos(angle) * t,
                max(v0 * np.sin(angle) * t - 0.5 * g * t**2, 0), 0
            ]),
            t_range=[0, t_flight],
            color=YELLOW,
        )
        self.play(Create(path), run_time=2)

        # Animate the projectile
        t_tracker = ValueTracker(0)
        ball = always_redraw(lambda: Dot(
            axes.c2p(*trajectory(t_tracker.get_value())[:2]),
            color=RED, radius=0.08,
        ))
        self.add(ball)
        self.play(t_tracker.animate.set_value(t_flight), run_time=3, rate_func=linear)

        # Equations
        eqs = VGroup(
            MathTex(r"x = v_0 \cos\theta \cdot t", font_size=24),
            MathTex(r"y = v_0 \sin\theta \cdot t - \frac{1}{2}gt^2", font_size=24),
            MathTex(r"R = \frac{v_0^2 \sin 2\theta}{g}", font_size=24, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(DR, buff=0.3)

        for eq in eqs:
            self.play(Write(eq), run_time=0.8)
        self.wait(2)
