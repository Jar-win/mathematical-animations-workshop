from manimlib.imports import *

class SuperAwesomClass(Scene):
    def construct(self):
        circle = Circle(radius=3) 
        sq = Square(side_length=2)
        self.play(ShowCreation(circle))
        self.wait(2)
        self.play(Transform(circle, sq))
        self.wait(2)

# similarly make a new class with Bigger Square being converted to a circle. What do you think would be required as a parameter?
