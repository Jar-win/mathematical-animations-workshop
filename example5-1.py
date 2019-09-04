from manimlib.imports import *
import numpy as np

class SquareAcrobatics(Scene):
    def construct(self):
        sq = Square()
        sq.rotate(np.pi/4)
        self.play(GrowFromCenter(sq))
        self.wait(2)    
