from manimlib.imports import *

class MakeGrid(Scene):
    def construct(self):
        grid = NumberPlane()
        circle = Circle()
        self.play(ShowCreation(grid))
        self.play(FadeIn(circle))
        self.wait(2)


class SimpleNonLinearTransform(Scene):
    def construct(self):
        grid = NumberPlane()
        circle = Circle()
        self.play(ShowCreation(grid))
        self.play(FadeIn(circle))
        self.wait(2)

        grid.prepare_for_nonlinear_transform()
        nonLinear_Transform = lambda p:  p + np.array([np.power(p[0], 2) + p[1], 0.5*p[1] ,0])
        self.play(grid.apply_function, nonLinear_Transform,
                  circle.apply_function, nonLinear_Transform, run_time=3)
        self.wait(2)
        

EXAMPLE_TRANFORM = [[2, 1], [-3, 1]]
TRANFORMED_VECTOR = [[1], [1]]


class TestLinearTransformation(LinearTransformationScene):
    def construct(self):
        self.setup()
        self.add_vector(np.array(TRANFORMED_VECTOR).flatten())
        self.apply_matrix(EXAMPLE_TRANFORM)
        self.wait()

  
