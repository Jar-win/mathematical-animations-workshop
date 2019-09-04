from manimlib.imports import *

class ScaleShape(Scene):
    def construct(self):
        circle1= Circle(radius=0.5, color= WHITE, fill_color = BLUE, fill_opacity=1)
        self.play(ShowCreation(circle1))
        self.wait(2)

        circle1.scale(2)
        self.wait(2)

class ScaleText(Scene):
    def construct(self):
        text = TextMobject("'Yer a Wizard, Harry!")
        self.play(ShowCreation(text))
        self.wait(2)

        text.scale(2)
        self.wait(2)
