from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import (
    AliasProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class CButton(ButtonBehavior, BoxLayout):
    """
    Custom button with icon and text
    """

    text = StringProperty()
    font_size = NumericProperty(sp(18))
    icon = StringProperty()
    bg_color = ColorProperty([1, 1, 1, 1])
    font_color = ColorProperty([0, 0, 0, 1])
    icon_color = ColorProperty([0, 0, 0, 1])
    radius = ListProperty([dp(5)])
    icon_size = NumericProperty(dp(24))
    border_color = ColorProperty([1, 1, 1, 1])
    border_width = NumericProperty(1)
    # icon_position = OptionProperty("left", options=["left", "right"])
    # text_pos = OptionProperty("left", options=["left", "center"])

    def get_current_color(self):
        if self.state == "normal":
            return self.bg_color
        else:
            return [
                self.bg_color[0] * 0.8,
                self.bg_color[1] * 0.8,
                self.bg_color[2] * 0.8,
                self.bg_color[3] * 1,
            ]

    current_color = AliasProperty(
        get_current_color,
        bind=["state", "bg_color"],
    )

    def get_current_mode(self):
        if self.text and self.icon:
            return "both"
        elif self.text:
            return "text"
        elif self.icon:
            return "icon"

    current_mode = AliasProperty(
        get_current_mode,
        bind=["text", "icon"],
    )

    def on_current_mode(self, *args):
        if len(self.children) > 2:
            children_to_remove = [
                child for child in self.children if not isinstance(child, Label)
            ]
            for child in children_to_remove:
                self.remove_widget(child)

        if self.current_mode in ["icon", "text"]:
            self.add_widget(Widget(), index=2)
            self.add_widget(Widget(), index=0)
        else:
            self.add_widget(Widget(), index=0)
            self.add_widget(Widget(), index=2)
            self.add_widget(Widget(), index=4)

    def on_kv_post(self, *args):
        if not self.text and not self.icon:
            self.text = "Button"


# fmt: off
Builder.load_string("""
<-CButton>:
    size_hint: None, None
    _width: None
    width: (label.texture_size[0] + icon.size[0] + dp(35) if icon.size[0] < dp(50) and icon.icon and label.text else label.texture_size[0] + icon.size[0]+ dp(20)) if not self._width else self._width

    _height: None
    height: (dp(50) if icon.size[1] < dp(50) else icon.size[1]) if not self._height else self._height

    canvas.before:
        Color:
            rgba: root.current_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius
        Color:
            rgba: root.border_color if root.border_width else (0,0,0,0)
        SmoothLine:
            width: root.border_width
            rounded_rectangle: (self.x, self.y, self.width, self.height, root.radius[0])

    Label:
        id: icon
        text: u"{}".format(unicode[root.icon]) if root.icon in unicode else "blank"
        icon: root.icon
        font_name: icon_font
        size_hint: (None, None)
        size: self.texture_size if self.icon else (dp(0), dp(0))
        font_size: root.icon_size # this is the icon size
        pos_hint: {"center_x": .5, "center_y": .5}
        color: root.icon_color

        canvas.before:
            Color:
                rgba: root.current_color
            Rectangle:
                pos: self.pos
                size: self.size

    Label:
        id: label
        text: root.text
        font_size: root.font_size
        size_hint: None, None
        size: self.texture_size
        color: root.font_color
        pos_hint: {'center_y': .5}
""")
# fmt: on
