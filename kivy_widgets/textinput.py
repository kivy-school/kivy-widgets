from functools import partial

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, Line, Rectangle, SmoothLine
from kivy.lang import Builder, global_idmap
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    DictProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout


class CTextInput(ButtonBehavior, FloatLayout):
    text_input = ObjectProperty()
    background_color = ColorProperty(global_idmap["transparent"])
    foreground_color = ColorProperty(global_idmap["stone_400"])
    foreground_active_color = ColorProperty(global_idmap["sky_400"])
    font_size = NumericProperty(dp(16))

    text = StringProperty()
    hint_text = StringProperty()
    hint_text_color = ColorProperty(global_idmap["stone_400"])
    hint_text_color_active = ColorProperty(global_idmap["sky_400"])
    hint_text_label = ObjectProperty()
    hint_text_pos_hint = DictProperty({"x": 0, "y": 0})

    helper_text = StringProperty()
    helper_text_color = ColorProperty(global_idmap["stone_400"])
    helper_text_label = ObjectProperty()

    line_color = ColorProperty(global_idmap["stone_400"])
    line_color_active = ColorProperty(global_idmap["sky_400"])

    cursor_blink = BooleanProperty(True)
    cursor_color = ColorProperty(global_idmap["sky_400"])

    mode = OptionProperty(None, options=["line", "fill", "rectangle"], allownone=True)

    use_bubble = BooleanProperty(False)
    use_handles = BooleanProperty(False)
    write_tab = BooleanProperty(False)
    selection_color = ColorProperty([0.1843, 0.6549, 0.8313, 0.5])

    instructions_to_delete = ListProperty()

    __events__ = ("on_text_validate",)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self._check_width, 1 / 15)

    def _check_width(self, t):
        print("check_width")
        if self.mode:
            if self.mode == "line":
                # self.do_line_layout()
                func = self._update_line
            elif self.mode == "rectangle":
                func = self._update_rounded_rectangle

            self.fbind("width", lambda *_: Clock.schedule_once(func))
            self.fbind("y", lambda *_: Clock.schedule_once(func))
            self.fbind("x", lambda *_: Clock.schedule_once(func))
            return False
        return True

    def on_text(self, *args):
        print("on_text")
        Clock.schedule_once(partial(self.move_hint_text_upwards, False))

    def move_hint_text_upwards(self, animate=True, *args):
        print("move_hint_text_upwards")
        if self.mode == "line":
            x = 0
            y = 1 - (self.text_input.height - dp(6)) / self.height
        elif self.mode == "rectangle":
            x = dp(12) / self.width
            y = 1 - dp(6) / self.height

        pos_hint = {"x": x, "y": y}

        if self.hint_text_label.pos_hint == pos_hint:
            if self.text_input.focus:
                self.hint_text_label.color = self.hint_text_color_active
            else:
                self.hint_text_label.color = self.hint_text_color
            return

        if animate:
            self.anim = Animation(
                pos_hint=pos_hint,
                font_size=dp(12),
                duration=0.15,
                color=self.hint_text_color_active,
            )
            self.anim.start(self.hint_text_label)
            if self.mode == "rectangle":
                self.anim.bind(on_complete=self.on_complete)
        else:
            self.hint_text_label.pos_hint = pos_hint
            self.hint_text_label.font_size = dp(12)

            Clock.schedule_once(self.on_complete)

    def on_complete(self, *args):
        print("on_complete!!!!!!!!!@!@!@!@!")
        # we need to clip the background canvas instruction
        # behind the hint_text_label
        with self.canvas.before:
            Color(rgba=(1, 1, 1, 1))
            self._rect = Rectangle(
                pos=(self.hint_text_label.pos[0] - dp(4), self.hint_text_label.pos[1]),
                size=(
                    self.hint_text_label.size[0] + dp(8),
                    self.hint_text_label.size[1],
                ),
            )
            self.instructions_to_delete.append(self._rect)

    def restore_hint_text(self, animate=True, *args):
        print("restore_hint_text")
        if self.text_input.text:
            self.hint_text_label.color = self.hint_text_color
            return

        if self.mode == "line":
            x = 0
            y = (self.helper_text_label.height + dp(8)) / self.height
        elif self.mode == "rectangle":
            x = dp(12) / self.width
            if self.helper_text:
                y = (
                    dp(20) + (self.height - dp(20) - self.hint_text_label.height) / 2
                ) / self.height
            else:
                y = ((self.height - self.hint_text_label.height) / 2) / self.height

        pos_hint = {
            "x": x,
            "y": y,
        }

        if self.hint_text_label.pos_hint == pos_hint:
            return

        if animate:
            self.anim = Animation(
                pos_hint=pos_hint,
                font_size=dp(16),
                duration=0.15,
                color=self.hint_text_color,
            )
            self.anim.start(self.hint_text_label)
            self.anim.bind(on_complete=self.on_complete_restore)
        else:
            self.hint_text_label.pos_hint = pos_hint
            self.hint_text_label.font_size = dp(16)
            self.hint_text_label.color = self.hint_text_color

    def on_complete_restore(self, *args):
        print("on_complete_restore")
        for instruction in self.instructions_to_delete:
            self.canvas.before.remove(instruction)
        self.instructions_to_delete = []

    def on_text_validate(self, *args):
        return True

    def on_kv_post(self, *args):
        if self.mode is None:
            self.mode = "line"

    def do_layout_without_helper_text(self, *args):
        print("do_layout_without_helper_text")
        self.height -= dp(16)

        pos_hint = {
            "x": 0,
            "y": (self.helper_text_label.height + dp(6)) / self.height,
        }
        self.hint_text_pos_hint = pos_hint
        self.text_input.pos_hint = pos_hint

    def on_focus_text_input(self, *args):
        if not self.text_input.focus:
            self.restore_hint_text_event = Clock.schedule_once(self.restore_hint_text)
            self.restore_line_event = Clock.schedule_once(self.restore_line)
            self.text_input.foreground_color = self.foreground_color
        else:
            if "restore_hint_text_event" in self.__dict__:
                if self.restore_hint_text_event:
                    self.restore_hint_text_event.cancel()
            if "restore_line_event" in self.__dict__:
                if self.restore_line_event:
                    print("cancel restore_line_event")
                    self.restore_line_event.cancel()
                    if "smooth_line_instruction_color" in self.__dict__:
                        Animation.cancel_all(self.smooth_line_instruction_color, "rgba")
                    if "line_instruction_color" in self.__dict__:
                        Animation.cancel_all(self.line_instruction_color, "rgba")
            self.move_hint_text_upwards()
            self.animate_line()
            self.text_input.foreground_color = self.foreground_active_color

    def animate_line(self, *args):
        print("animate_line")
        if self.mode == "line":
            if self.line_instruction_color.rgba == self.line_color_active:
                return

            # let's create a new "line" that starts on the middle of the line
            # and ends on the middle
            line_points = [
                self.center_x,
                self.helper_text_label.top + dp(4),
                self.center_x,
                self.helper_text_label.top + dp(4),
            ]

            final_line_points = [
                self.x,
                self.helper_text_label.top + dp(4),
                self.right,
                self.helper_text_label.top + dp(4),
            ]

            self._line.points = line_points

            # and let's animate the line to the new points
            anim = Animation(
                points=final_line_points,
                d=0.15,
                width=dp(0.5),
            )

            # Update the color of the line to the active color
            self.line_instruction_color.rgba = self.line_color_active

            # and start the animation
            anim.start(self._line)

        elif self.mode == "rectangle":
            # animate the color self.line_instruction_color
            self.smooth_line_instruction_color.rgba = self.line_color_active

    def restore_line(self, *args):
        if self.mode == "line":
            # animate the color self.line_instruction_color
            end_color = self.line_color

            # Define the animation duration
            duration = 0.15

            # Create an Animation instance for the color transition
            color_animation = Animation(rgba=end_color, d=duration)

            # Start the color animation
            color_animation.start(self.line_instruction_color)
        elif self.mode == "rectangle":
            self.smooth_line_instruction_color.rgba = self.line_color

    def on_helper_text(self, *args):
        print("on_helper_text")
        if self.helper_text:
            pos_hint = {
                "x": 0,
                "y": (self.helper_text_label.height + dp(8)) / self.height,
            }
            self.hint_text_pos_hint = pos_hint
            self.text_input.pos_hint = pos_hint

    def do_line_layout(self, *args):
        print("do_line_layout")
        if self.helper_text:
            if self.font_size != dp(16):
                multiplier = self.font_size / dp(16)
                if multiplier < 1:
                    self.height = dp(72) - self.font_size * 1.375 / 2
                else:
                    self.height = dp(72) + self.font_size * 1.375 / 2
            else:
                self.height = dp(72)
        else:
            if self.font_size != dp(16):
                multiplier = self.font_size / dp(16)
                if multiplier < 1:
                    self.height = dp(60) - self.font_size * 1.375 / 2
                else:
                    self.height = dp(60) + self.font_size * 1.375 / 2
            else:
                self.height = dp(64)

        # If the user sets the text initially, we are going
        # to move the hint_text_label upwards, but without animation
        if self.text:
            Clock.schedule_once(partial(self.move_hint_text_upwards, False))

        # Whenever the helper_text_label height changes, we need to update the hint_text_pos_hint
        if self.helper_text:
            self.helper_text_label.bind(height=self.on_helper_text)
            self.on_helper_text()
        else:
            self.do_layout_without_helper_text()

    def do_rectangle_layout(self, *args):
        # check if there is a helper_text
        if self.helper_text:
            # if there is, we need to increase the height of the widget
            if self.font_size != dp(16):
                multiplier = self.font_size / dp(16)
                if multiplier < 1:
                    self.height = dp(56) - self.font_size * 1.375 / 2
                elif multiplier > 1:
                    self.height = dp(56) + self.font_size * 1.375 / 2
            else:
                self.height = dp(64)
            # and we need to update the hint_text_pos_hint
            pos_hint = {
                "x": dp(12) / self.width,
                "y": (dp(20) + (self.height - dp(20) - self.text_input.height) / 2)
                / self.height,
            }
            hint_text_pos_hint = {
                **pos_hint,
                "y": (dp(20) + (self.height - dp(20) - self.hint_text_label.height) / 2)
                / self.height,
            }
            self.hint_text_label.pos_hint = hint_text_pos_hint
            self.text_input.pos_hint = pos_hint
            self.text_input.width = self.width - dp(20)
            self.helper_text_label.pos_hint = {
                "x": dp(12) / self.width,
                "y": 0,
            }
        else:
            # if there isn't, we need to decrease the height of the widget
            if self.font_size != dp(16):
                multiplier = self.font_size / dp(16)
                if multiplier < 1:
                    self.height = dp(40) - self.font_size * 1.375 / 2
                else:
                    self.height = dp(40) + self.font_size * 1.375 / 2
            else:
                self.height = dp(44)
            # and we need to update the hint_text_pos_hint
            pos_hint = {
                "x": dp(12) / self.width,
                "y": ((self.height - self.text_input.height) / 2) / self.height,
            }
            self.hint_text_pos_hint = {
                **pos_hint,
                "y": ((self.height - self.hint_text_label.height) / 2) / self.height,
            }
            self.text_input.pos_hint = pos_hint
            self.text_input.width = self.width - dp(20)

        if self.text:
            Clock.schedule_once(partial(self.move_hint_text_upwards, False))

    def on_mode(self, *args):
        self.text_input.bind(focus=self.on_focus_text_input)
        self.restore_hint_text_event = None
        self.restore_line_event = None

        if self.mode == "line":
            line_points = [
                self.x,
                self.helper_text_label.top + dp(4),
                self.right,
                self.helper_text_label.top + dp(4),
            ]

            with self.canvas.before:
                self.line_instruction_color = Color(rgba=self.line_color)
                self._line = Line(width=dp(1), points=line_points)

            self.bind(pos=self._update_line, right=self._update_line)
            Clock.schedule_once(self.do_line_layout)

        elif self.mode == "rectangle":
            # create a SmoothLine in a format of a rounded rectangle
            with self.canvas.before:
                self.smooth_line_instruction_color = Color(rgba=self.line_color)
                self.smooth_line = SmoothLine(
                    width=dp(1),
                    rounded_rectangle=(
                        self.x,
                        self.y,
                        self.width,
                        self.height,
                        dp(4),
                    ),
                )

            self.bind(
                pos=self._update_rounded_rectangle, size=self._update_rounded_rectangle
            )
            Clock.schedule_once(self.do_rectangle_layout)

        # elif self.mode == "fill":

    def _update_rounded_rectangle(self, *args):
        print("update_rounded_rectangle")
        if not self.helper_text:
            self.smooth_line.rounded_rectangle = (
                self.x,
                self.y,
                self.width,
                self.height,
                dp(4),
            )
        else:
            self.smooth_line.rounded_rectangle = (
                self.x,
                self.y + dp(20),
                self.width,
                self.height - dp(20),
                dp(4),
            )

    def _update_line(self, *args):
        print("update_line")
        line_points = [
            self.x,
            self.helper_text_label.top + dp(4),
            self.right,
            self.helper_text_label.top + dp(4),
        ]

        self._line.points = line_points


# fmt: off
Builder.load_string("""
<CTextInput>
    size_hint_y: None
    height: dp(60)

    on_release: 
        text_input.focus = True
    on_press: 
        text_input.focus = True

    helper_text_label: helper_text_label
    hint_text_label: hint_text_label
    text_input: text_input
    
    # The actual TextInput
    TextInput:
        id: text_input
        text: root.text
        size_hint: None, None
        size: root.width, dp(20) * root.font_size / dp(16)
        pos_hint: {'x': 0, 'y': 0}
        padding: 0, 0
        cursor_blink: root.cursor_blink
        cursor_color: root.cursor_color
        background_color: root.background_color
        foreground_color: root.foreground_color
        multiline: False
        use_bubble: root.use_bubble
        use_handles: root.use_handles
        selection_color: root.selection_color
        write_tab: root.write_tab
        on_text_validate: root.dispatch('on_text_validate')
        on_text: root.text = self.text
        background_active: ''
        background_normal: ''
        font_size: root.font_size

    # The hint text
    Label:
        id: hint_text_label
        text: root.hint_text
        size_hint: None, None
        size: self.texture_size
        color: root.hint_text_color
        font_size: dp(16)
        pos_hint: root.hint_text_pos_hint

    # The helper text
    Label:
        id: helper_text_label
        text: root.helper_text
        color: root.helper_text_color
        size_hint: None, None
        size: self.texture_size
        font_size: dp(12)
        pos_hint: {'x': 0, 'y': 0}
""")
# fmt: on
