from manimlib.imports import *

class CrossSectionView(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() # creates a 3D Axis
        circle=Circle()
        self.set_camera_orientation(phi=0 * DEGREES)
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.wait()

class ZoomedOut(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle(radius=2)
        self.set_camera_orientation(phi=80 * DEGREES,theta=45*DEGREES) # distance=14/gamma
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.wait()

class Movement(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.move_camera(phi=30*DEGREES,theta=-45*DEGREES,run_time=3)
        self.wait()


class MovementAndPan(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80 * DEGREES)           
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=80*DEGREES,theta=-PI/2)
        self.wait()

class NumberPlaneTransformTorous(SpecialThreeDScene):
    def construct(self):
        sphere = Sphere(checkerboard_colors=[YELLOW, YELLOW], color_opacity = 0.5, stroke_color=BLUE)
        circle = Circle()
        self.add_axes()
        self.play(ShowCreation(sphere), ShowCreation(circle))
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
