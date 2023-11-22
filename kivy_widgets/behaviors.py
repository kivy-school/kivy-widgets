from kivy.animation import Animation
from kivy.graphics import (
    Color,
    Ellipse,
    RoundedRectangle,
    StencilPop,
    StencilPush,
    StencilUnUse,
    StencilUse,
)
from kivy.uix.behaviors import TouchRippleButtonBehavior
from kivy.uix.relativelayout import RelativeLayout


class CircularRippleBehavior(TouchRippleButtonBehavior):
    def ripple_show(self, touch):
        """Begin ripple animation on current widget.

        Expects touch event as argument.
        """
        Animation.cancel_all(self, "ripple_rad", "ripple_color")
        self._ripple_reset_pane()
        x, y = self.to_window(*self.pos)
        width, height = self.size
        if isinstance(self, RelativeLayout):
            self.ripple_pos = ripple_pos = (touch.x - x, touch.y - y)
        else:
            self.ripple_pos = ripple_pos = (touch.x, touch.y)
        rc = self.ripple_color
        ripple_rad = self.ripple_rad
        self.ripple_color = [rc[0], rc[1], rc[2], self.ripple_fade_from_alpha]
        with self.ripple_pane:
            StencilPush()
            Ellipse(size=(width, height), pos=(x, y))
            StencilUse()
            self.ripple_col_instruction = Color(rgba=self.ripple_color)
            self.ripple_ellipse = Ellipse(
                size=(ripple_rad, ripple_rad),
                pos=(
                    ripple_pos[0] - ripple_rad / 2.0,
                    ripple_pos[1] - ripple_rad / 2.0,
                ),
            )
            StencilUnUse()
            Ellipse(size=(width, height), pos=(x, y))
            StencilPop()

        anim = Animation(
            ripple_rad=max(width, height) * self.ripple_scale,
            t=self.ripple_func_in,
            ripple_color=[rc[0], rc[1], rc[2], self.ripple_fade_to_alpha],
            duration=self.ripple_duration_in,
        )
        anim.start(self)


class RoundedRectangleRippleBehavior(TouchRippleButtonBehavior):
    def ripple_show(self, touch):
        """Begin ripple animation on current widget.

        Expects touch event as argument.
        """
        Animation.cancel_all(self, "ripple_rad", "ripple_color")
        self._ripple_reset_pane()
        x, y = self.to_window(*self.pos)
        width, height = self.size
        if isinstance(self, RelativeLayout):
            self.ripple_pos = ripple_pos = (touch.x - x, touch.y - y)
        else:
            self.ripple_pos = ripple_pos = (touch.x, touch.y)
        rc = self.ripple_color
        ripple_rad = self.ripple_rad
        self.ripple_color = [rc[0], rc[1], rc[2], self.ripple_fade_from_alpha]
        with self.ripple_pane:
            StencilPush()
            RoundedRectangle(size=(width, height), pos=(x, y), radius=self.radius)
            StencilUse()
            self.ripple_col_instruction = Color(rgba=self.ripple_color)
            self.ripple_ellipse = Ellipse(
                size=(ripple_rad, ripple_rad),
                pos=(
                    ripple_pos[0] - ripple_rad / 2.0,
                    ripple_pos[1] - ripple_rad / 2.0,
                ),
            )
            StencilUnUse()
            RoundedRectangle(size=(width, height), pos=(x, y), radius=self.radius)
            StencilPop()

        anim = Animation(
            ripple_rad=max(width, height) * self.ripple_scale,
            t=self.ripple_func_in,
            ripple_color=[rc[0], rc[1], rc[2], self.ripple_fade_to_alpha],
            duration=self.ripple_duration_in,
        )
        anim.start(self)
