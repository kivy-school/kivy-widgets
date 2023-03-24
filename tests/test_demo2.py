from kivy.tests.common import GraphicUnitTest, UnitTestTouch


class MyTestCase(GraphicUnitTest):
    def test_render(self):
        from kivy.uix.button import Button

        # with GraphicUnitTest.render() you basically do this:
        # runTouchApp(Button()) + some setup before
        button = Button()
        self.render(button)

        # get your Window instance safely
        from kivy.base import EventLoop

        EventLoop.ensure_window()
        window = EventLoop.window

        touch = UnitTestTouch(*[s / 2.0 for s in window.size])

        # bind something to test the touch with
        button.bind(
            on_release=lambda instance: setattr(instance, "test_released", True)
        )

        # then let's touch the Window's center
        touch.touch_down()
        touch.touch_up()

        self.assertTrue(button.test_released)


if __name__ == "__main__":
    import unittest

    unittest.main()
