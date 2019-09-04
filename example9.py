from manimlib.imports import *

class TwoCirclesTwoSquares(Scene):
    def construct(self):
        circle1 = Circle() # is-a relationship
        circle2 = Circle()
        sq = Square()

        sq.shift(2*RIGHT)
        
        self.play(ShowCreation(circle1), ShowCreation(circle2))
        self.play(ApplyMethod(circle2.shift, 2*RIGHT))
        self.wait()
        self.play(Transform(circle2, sq)) # ReplacementTransform
        self.wait()
        self.play(ApplyMethod(sq.shift, 2*UP+2*LEFT))
        self.wait()
