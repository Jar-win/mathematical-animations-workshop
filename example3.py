from manimlib.imports import *

class CircleToSquare(Scene):
    def construct(self):
        circle = Circle()
        sq = Square()
        self.play(ShowCreation(circle))
        self.wait(2)
        self.play(Transform(circle, sq))


