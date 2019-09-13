from manimlib.imports import *

class CircleToSquare(Scene):
    def construct(self):
        circle = Circle()
        sq = Square()
        tr = Triangle()
        self.play(ShowCreation(circle))
        self.wait(2)
        self.play(Transform(circle, sq))
        self.wait(2)
        self.play(Transform(sq, tr))
