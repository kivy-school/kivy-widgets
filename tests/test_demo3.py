import os

from icecream import ic
from kivy.tests.common import GraphicUnitTest


class MyTestCase(GraphicUnitTest):
    def run(self, *args, **kwargs):
        """Extend the run of unittest, to check if results directory have been
        found. If no results directory exists, the test will be ignored.
        """
        from os.path import dirname, exists, join

        results_dir = join(dirname(__file__), "results")
        ic(results_dir)

        if not exists(results_dir):
            os.mkdir(results_dir)
        self.test_counter = 0
        self.results_dir = results_dir
        self.test_failed = False
        return super(GraphicUnitTest, self).run(*args, **kwargs)


class VertexInstructionTestCase(MyTestCase):
    def test_ellipse(self):
        from kivy.graphics import Color, Ellipse
        from kivy.uix.widget import Widget

        r = self.render

        # create a root widget
        wid = Widget()

        # put some graphics instruction on it
        with wid.canvas:
            Color(1, 1, 1)
            self.e = Ellipse(pos=(100, 100), size=(200, 100))

        # render, and capture it directly
        r(wid)

        # # as alternative, you can capture in 2 frames:
        # r(wid, 2)

        # # or in 10 frames
        # r(wid, 10)
