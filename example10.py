from manimlib.imports import *
import numpy as np

#crude graph
class Scene1(GraphScene):
    CONFIG = {
    "x_min": -5,
    "x_max": 5,
    "y_min": -5,
    "y_max": 5,
    }

    def construct(self):
        self.setup_axes(animate = True)
        func_graph = self.get_graph(self.mygraph, YELLOW_E) #HAS TO BE AFTER SETUP of AXES
        self.play(ShowCreation(func_graph))
        self.wait(2)

    def mygraph(self,x):
        return x

#change graph origin
class Scene2(GraphScene):
    CONFIG = {
    "x_min": -5,
    "x_max": 5,
    "y_min": -5,
    "y_max": 5,
    "graph_origin": ORIGIN,
    }

    def construct(self):
        self.setup_axes(animate = True)
        func_graph = self.get_graph(self.mygraph, YELLOW_E) #HAS TO BE AFTER SETUP of AXES
        self.play(ShowCreation(func_graph))
        self.wait(2)

    def mygraph(self,x):
        return x

#make sin graph
class Scene3(GraphScene):
    CONFIG = {
    "x_min": -5,
    "x_max": 5,
    "y_min": -5,
    "y_max": 5,
    "graph_origin": ORIGIN,
    }

    def construct(self):
        self.setup_axes(animate = True)
        func_graph = self.get_graph(self.mygraph, YELLOW_E) #HAS TO BE AFTER SETUP of AXES
        self.play(ShowCreation(func_graph))
        self.wait(2)

    def mygraph(self,x):
        return np.sin(x)

#add ticks
class Scene4(GraphScene):
    CONFIG = {
    "x_min": -5,
    "x_max": 5,
    "y_min": -5,
    "y_max": 5,
    "x_labeled_nums": range(-5, 6),
    "graph_origin": ORIGIN,
    }

    def construct(self):
        self.setup_axes(animate = True)
        func_graph = self.get_graph(self.mygraph, YELLOW_E) #HAS TO BE AFTER SETUP of AXES
        self.play(ShowCreation(func_graph))
        self.wait(2)

    def mygraph(self,x):
        return np.sin(x)

# exclude 0 label and changing width
# X_TICKS_DISTANCE = self.x_axis_width/(self.x_max- self.x_min)
# Y_TICKS_DISTANCE = self.y_axis_height/(self.y_max- self.y_min)
class Scene5(GraphScene):
    CONFIG = {
    "x_min": -5,
    "x_max": 5,
    "y_min": -3,
    "y_max": 3,
    "x_axis_width": 8,
    "y_axis_height": 4.8,
    "x_labeled_nums": list(range(-5, 6)),
    "graph_origin": ORIGIN+DOWN,
    "exclude_zero_label": True, #when using a list to denote rage of values

    }

    def construct(self):
        self.setup_axes(animate = True)
        func_graph = self.get_graph(self.mygraph, YELLOW_E) #HAS TO BE AFTER SETUP of AXES
        dot = Dot()
        dot.shift(self.graph_origin RIGHT+UP)
        self.add(dot)
        self.play(ShowCreation(func_graph))
        self.wait(2)


    def mygraph(self,x):
        return np.sin(x)

#Other nice tweaks of the CONFIG dictionary:
# "x_leftmost_tick"
# "y_tick_frequency": 1,
# "x_axis_label": "$x$",

#trying different graphs
class Scene6(GraphScene):
    CONFIG = {
    "x_min": -20,
    "x_max": 20,
    "y_min": -3,
    "y_max": 3,
    "x_axis_width": 10,
    "y_axis_height": 10,
    "x_labeled_nums": list(range(-5, 6)),
    "graph_origin": ORIGIN,
    "exclude_zero_label": True, #when using a list to denote rage of values

    }

    def construct(self):
        self.setup_axes(animate = True)
        func_graph = self.get_graph(self.mygraph, YELLOW_E) #HAS TO BE AFTER SETUP of AXES
        self.play(ShowCreation(func_graph))
        self.wait(2)

    def mygraph(self,x):
        return np.tan(x)
        # return x*x
        # return np.sqrt(x)
