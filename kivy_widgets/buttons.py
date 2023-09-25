from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
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
    markup = BooleanProperty(False)
    font_size = NumericProperty(sp(18))
    font_color = ColorProperty([0, 0, 0, 1])
    halign = OptionProperty("center", options=["left", "center", "right"])

    icon = StringProperty()
    icon_color = ColorProperty([0, 0, 0, 1])
    icon_size = NumericProperty(dp(24))
    icon_position = OptionProperty("left", options=["left", "right"])

    bg_color = ColorProperty([1, 1, 1, 1])
    border_color = ColorProperty([1, 1, 1, 1])
    border_width = NumericProperty(1)
    radius = ListProperty([dp(5)])

    align_on_left = BooleanProperty(False)
    left_padding = NumericProperty(dp(10))

    shorten = BooleanProperty(False)
    shorten_from = OptionProperty("right", options=["left", "center", "right"])
    max_width = NumericProperty(0)  # useful for expandable buttons

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

    def on_align_on_left(self, *args):
        self.on_current_mode()

    def on_left_padding(self, *args):
        self.on_current_mode()

    def on_icon_position(self, *args):
        self.on_current_mode()

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
            if not self.align_on_left:
                if self.icon_position == "left":
                    if self.children[0].icon:
                        # should put icon on the left
                        icon = self.children[0]
                        self.remove_widget(icon)
                        self.add_widget(icon, index=2)
                else:
                    if self.children[1].icon:
                        # should put icon on the right
                        icon = self.children[1]
                        self.remove_widget(icon)
                        self.add_widget(icon, index=0)

                self.add_widget(Widget(), index=0)
                self.add_widget(Widget(), index=3)

            else:
                self.add_widget(
                    Widget(size_hint_x=None, width=dp(self.left_padding)), index=2
                )

    def on_kv_post(self, *args):
        if not self.text and not self.icon:
            self.text = "Button"

    def on_shorten(self, *args):
        Clock.schedule_once(self.update_label_text_size, 0)

    def update_label_text_size(self, *args):
        if self.shorten and self.current_mode == "both":
            if self.icon_position == "left":
                if not self.align_on_left:
                    icon = self.children[2]
                    label = self.children[1]

                    available = (
                        self.width - self.left_padding - self.spacing - icon.width
                    )

                    if label.texture_size[0] < available:
                        label.text_size = (
                            label.texture_size[0] + dp(15),
                            None,
                        )
                    else:
                        label.text_size = (
                            available + dp(5),
                            None,
                        )
                else:
                    icon = self.children[1]
                    label = self.children[0]

                    if self.max_width:
                        available = (
                            self.max_width
                            - self.left_padding
                            - self.spacing
                            - icon.width
                        )
                    else:
                        available = (
                            self.width - self.left_padding - self.spacing - icon.width
                        )

                    if label.texture_size[0] < available:
                        label.text_size = (
                            label.texture_size[0] + dp(15),
                            None,
                        )
                    else:
                        label.text_size = (
                            available - dp(10),
                            None,
                        )
            else:
                if not self.align_on_left:
                    icon = self.children[1]
                    label = self.children[2]

                    if self.max_width:
                        available = (
                            self.max_width
                            - self.left_padding
                            - self.spacing
                            - icon.width
                        )
                    else:
                        available = (
                            self.width - self.left_padding - self.spacing - icon.width
                        )

                    if label.texture_size[0] < available:
                        label.text_size = (
                            label.texture_size[0] + dp(15),
                            None,
                        )
                    else:
                        label.text_size = (
                            available - dp(25),
                            None,
                        )
                else:
                    icon = self.children[1]
                    label = self.children[0]

                    if self.max_width:
                        available = (
                            self.max_width
                            - self.spacing
                            - icon.width
                            - self.left_padding
                        )
                    else:
                        available = (
                            self.width - self.spacing - icon.width - self.left_padding
                        )

                    if label.texture_size[0] < available:
                        label.text_size = (
                            label.texture_size[0] + dp(15),
                            None,
                        )
                    else:
                        label.text_size = (
                            available - dp(10),
                            None,
                        )

        elif self.shorten and self.current_mode == "text":
            label = self.children[1]
            if self.max_width:
                available = self.max_width
            else:
                available = self.width

            if label.texture_size[0] < available:
                label.text_size = (
                    label.texture_size[0] + dp(15),
                    None,
                )
            else:
                label.text_size = (
                    available - dp(10),
                    None,
                )


# fmt: off
Builder.load_string("""
<-CButton>:
    spacing: dp(10) if self.current_mode == "both" else 0
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
        halign: root.halign
        markup: root.markup
        font_size: root.font_size
        size_hint: None, None
        size: self.texture_size
        color: root.font_color
        pos_hint: {'center_y': .5}
        shorten: root.shorten
        shorten_from: root.shorten_from
""")
# fmt: on
