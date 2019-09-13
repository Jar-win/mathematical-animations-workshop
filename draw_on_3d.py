from manimlib.imports import *

class DrawOnSphere(SpecialThreeDScene):
     def construct():
        sphere = Sphere()

class NumberPlaneTransformTorous(SpecialThreeDScene):
    def construct(self):
        sphere = Sphere(checkerboard_colors=[YELLOW, YELLOW], color_opacity = 0.5, stroke_color=BLUE)
        circle = Circle()
        # body = self.get_sphere(
            # checkerboard_colors=[
                # YELLOW, RED
            # ],
            # color=BLUE,
            # stroke_width=1,
        # )
        # body.set_opacity(0.5)


        self.add_axes()
        self.play(ShowCreation(sphere), ShowCreation(circle))
        #self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(3)

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
