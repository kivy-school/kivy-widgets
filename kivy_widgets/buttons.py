from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
    OptionProperty,
    AliasProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout


class CButton(ButtonBehavior, BoxLayout):
    """
    Custom button with icon and text
    """

    text = StringProperty("Button")
    font_size = NumericProperty(sp(18))
    icon = StringProperty()
    bg_color = ColorProperty([1, 1, 1, 1])
    color = ColorProperty([0, 0, 0, 1])
    icon_color = ColorProperty([0, 0, 0, 1])
    radius = ListProperty([dp(5)])
    icon_size = NumericProperty(dp(24))
    icon_position = OptionProperty("left", options=["left", "right"])
    text_pos = OptionProperty("left", options=["left", "center"])

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
        bind=["state"],
    )


# fmt: off
Builder.load_string("""
<-CButton>:
    size_hint: None, None
    _width: None
    width: (label.texture_size[0] + icon.size[0] + dp(30) if icon.size[0] < dp(50) and icon.icon and label.text else label.texture_size[0] + icon.size[0]+ dp(20)) if not self._width else self._width

    _height: None
    height: (dp(50) if icon.size[1] < dp(50) else icon.size[1]) if not self._height else self._height

    padding: dp(10)
    spacing: dp(10) if icon.icon and label.text else 0

    canvas.before:
        Color:
            rgba: root.current_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius
        
    Label:
        id: icon
        text: u"{}".format(unicode[root.icon]) if root.icon in unicode else "blank"
        icon: root.icon
        font_name: icon_font
        size_hint: (None, None)
        size: self.texture_size
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
        color: root.color
        pos_hint: {'center_y': .5}
""")
# fmt: on
