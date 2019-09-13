from manimlib.imports import *

class ButterFly(Scene):
    def construct(self):
            butterfly = ParametricFunction(
            lambda t: np.array([
                (np.sin(TAU*t))*(np.exp(np.cos(TAU*t)) - 2*np.cos(4*t*TAU) - np.power(np.sin((t*TAU)/12), 5)),
                (np.cos(TAU*t))*(np.exp(np.cos(TAU*t)) - 2*np.cos(4*t*TAU) - np.power(np.sin((t*TAU)/12), 5)),
                0
            ]),
             t_min = 0, t_max = 40, step_size = 0.04, color = YELLOW
            )
            self.play(ShowCreation(butterfly),run_time=5)

class Cylinder_parametricSurface(SpecialThreeDScene):
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

    def construct(self):
        height = 2
        cylinder = ParametricSurface(
             lambda u, v: np.array([
                 np.cos(TAU * v),
                 np.sin(TAU * v),
                 height * (1 - u)
             ]),
             resolution=(6, 32), color = YELLOW, color_opacity = 0.5
        )
        self.play(ShowCreation(cylinder))


class Surface(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        c=1
        a=1
        trr = ParametricSurface(
            lambda u, v : np.array([
                 (c + a * np.cos(TAU * v)) * np.cos(TAU*u),
                 (c + a * np.cos(TAU * v)) * np.sin(TAU * u),
                 a * np.sin(TAU * v)
             ]),
            resolution=(6, 32)).fade(0.5) #Resolution of the surfaces

        self.set_camera_orientation(phi=60 * DEGREES,theta=-45*DEGREES)
        self.add(axes)
        self.play(Write(trr))
        self.wait()



class Torous(ParametricSurface):
    CONFIG = {
        "fill_opacity": 0.75,
        "fill_color": YELLOW,
        "stroke_width": 0,
        "resolution": (32, 32),
        "radius": 1,
        "fill_opacity": 0.65
    }

    def __init__(self, **kwargs):
        ParametricSurface.__init__(
            self, self.func, **kwargs
        )
        self.scale(self.radius)

    def func(self, u, v):
        c = 2
        a = 0.6
        return np.array([
            (c + a * np.cos(TAU * v)) * np.cos(TAU*u),
            (c + a * np.cos(TAU * v)) * np.sin(TAU * u),
            a * np.sin(TAU * v)
        ])


