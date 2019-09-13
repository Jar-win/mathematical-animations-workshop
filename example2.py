from manimlib.imports import *

class CreateBox(Scene):
    def construct(self):
        sq = Square()#add code here 
        self.play(ShowCreation(sq))
        self.wait(2)

