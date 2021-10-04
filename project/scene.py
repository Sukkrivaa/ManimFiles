from manim import *
from math import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity = 0.5)
        square = Square()
        square.rotate(PI/4)

        m0 = LabeledDot(MathTex(r"\gamma").set_color(ORANGE))
        self.wait(1)
        self.add(m0)
        self.wait(2)
        self.remove(m0)
        self.wait(1)
        self.play(Create(square))
        self.play(Transform(square,circle))
        self.play(FadeOut(square))
        self.wait(1)
        m1 = Circle()
        m2 = Square()
        m3 = Triangle()
        m1.shift(LEFT)
        m2.shift(IN)
        m3.shift(RIGHT)
        self.add(m1,m2,m3)
        self.wait(1)