from manimlib.imports import *

class ShiftScene(Scene):
    def construct(self):
        circle = Circle()
        circle.shift(2*RIGHT)
        circle.shift(2*DOWN)
        self.play(ShowCreation(circle))
        self.wait(3)

class MoveScene(Scene):
    def construct(self):
        circle = Circle()
        circle.move_to(2*RIGHT)
        circle.move_to(2*DOWN)
        self.play(ShowCreation(circle))
        self.wait(3)
