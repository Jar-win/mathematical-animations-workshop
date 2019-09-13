from manimlib.imports import *
class Special3DTransformation(SpecialThreeDScene):
    CONFIG = {
        "camera_class": ThreeDCamera,
        "ambient_camera_rotation": None,
        "default_angled_camera_orientation_kwargs":{ "phi": 70 * DEGREES, "theta": -135 * DEGREES,}
        }

    def construct(self):
        # creating objects
        grid = NumberPlane()
        i_hat = Vector(direction=RIGHT, color=ORANGE)
        j_hat = Vector(direction=UP, color=RED)
        sphere = Sphere()
        circle = Circle(color=YELLOW)
        self.add(grid)
        self.add_axes()

        self.play(FadeIn(sphere))
        self.play(ShowCreation(circle), ShowCreation(i_hat), ShowCreation(j_hat))
        grid.prepare_for_nonlinear_transform()

        nonLinear_Transform = lambda p: p + np.array([p[0]**2, p[1]+p[0] ,p[0]*p[1]])
        self.play(grid.apply_function, nonLinear_Transform,
                  sphere.apply_function, nonLinear_Transform,
                  circle.apply_function, nonLinear_Transform,
                  i_hat.apply_function, nonLinear_Transform,
                  j_hat.apply_function, nonLinear_Transform, run_time=4)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(30)

    def add_axes(self):
        axes = self.axes = self.get_axes()
        axes.set_stroke(width=0.5)
        self.add(axes)

        # Orient
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-110 * DEGREES,
        )
        self.begin_ambient_camera_rotation()

class InfoText(Scene):
    def construct(self):
        text1 = TextMobject("Transofrmation")
        text2 = TextMobject("$f(x,y) = (x^{2}, x+y, xy)$")
        text3 = TextMobject(r"""The following transformations shows a $2D -\textgreater 3D$ Transofrmation.\\
                            It shows how the unit circle, sphere, and the basis vector changes when subjected to the said transformation""")
        text3.scale(0.7)
        text1.shift(2*UP)
        text3.shift(2*DOWN)
        self.play(Write(text1), Write(text2))
        self.wait()
        self.play(FadeIn(text3))
        self.wait(4)
        self.play(FadeOut(text3), FadeOut(text2), FadeOut(text1))
