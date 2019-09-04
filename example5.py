# vlc /home/major-tom/Documents/fossee/workshops/Day1/SecretFolder/videos/example5/1440p60/TwoOsculatingCircles.mp4
from manimlib.imports import *

class TwoOsculatingCircles(Scene):
    def construct(self):
        circle1 = Circle() # is-a relationship
        circle2 = Circle() 
        circle2.shift(2*RIGHT)
        # modify the code to transform circle2 into a square
        self.play(ShowCreation(circle1), ShowCreation(circle2))
        self.wait(2)

# try shifting the same square to the top (Hint: Apply Method)

