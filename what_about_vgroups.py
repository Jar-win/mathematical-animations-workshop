from manimlib.imports import *

class WithoutVGroup(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(ShowCreation(circle), ShowCreation(square))

        self.play(ApplyMethod(circle.shift, 2*RIGHT))
        self.play(ApplyMethod(square.shift, 2*RIGHT))
        self.wait()

class WithVGroup(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        
        circare = VGroup(circle, square)

        self.play(ShowCreation(circare))

        self.play(ApplyMethod(circare.shift, 2*RIGHT))
        self.wait()
