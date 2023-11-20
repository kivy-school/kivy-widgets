import os

from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.lang import Builder, global_idmap
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout

from .icon_definitions import icon_unicodes


class Icon(Label):
    icon = StringProperty("android")
    font_name = StringProperty(global_idmap["icon_font"])
    icon_color = ColorProperty([0, 0, 0, 0.1])
    icon_size = NumericProperty(dp(21))
    bg_color = ColorProperty([0, 0, 0, 0])
    mode = OptionProperty(
        "default", options=["default", "stretch-background", "stretch-icon"]
    )


class IconViewer(RelativeLayout):
    icons = ListProperty()
    cache_icons = ListProperty()
    selected_icon = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_list_md_icons()
        self.cache_icons = self.icons

    def set_list_md_icons(self, text="", search=False):
        """
        Set list of icons to display
        """
        if search:
            self.icons = [
                {"icon": name_icon, "viewer": self}
                for name_icon in icon_unicodes.keys()
                if text in name_icon
            ]
        else:
            self.icons = [
                {"icon": name_icon, "viewer": self}
                for name_icon in icon_unicodes.keys()
            ]


class IconViewerItem(ButtonBehavior, BoxLayout):
    bg_color = ListProperty([0, 0, 0, 0.2])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.check_collision)

    def check_collision(self, _, pos):
        """
        Checks if mouse is over icon,
        updates icon background color
        and tipbox position/opacity.
        """
        if self.collide_point(*self.to_widget(*pos)):
            self.bg_color = [0, 0, 0, 0.4]

            self.viewer.tipbox.pos = (
                self.to_window(*self.pos)[0] - self.width / 2,
                self.to_window(*self.pos)[1] + self.height,
            )

            def update_opacity(*args):
                self.viewer.tipbox.opacity = 1

            if self.viewer.selected_icon == self.icon:
                Clock.schedule_once(update_opacity)

            self.viewer.selected_icon = self.icon
        else:
            self.bg_color = [0, 0, 0, 0.2]
            self.viewer.tipbox.opacity = 0

    def on_release(self):
        """
        Copy icon name to clipboard
        and update tipbox text
        """
        Clipboard.copy(self.icon)
        self.viewer.tipbox.children[0].text = "Copied successfully!"


# fmt: off
Builder.load_string("""
<Icon>:
    text: u"{}".format(unicode[root.icon]) if root.icon in unicode else "blank"
    size_hint: (None, None) if root.mode == "default" else (1, 1)
    size: (root.icon_size, root.icon_size) if root.mode == "default" else (self.texture_size[0], self.texture_size[1]) # this is the background size
    font_size: root.icon_size if root.mode in ["default", "stretch-background"] else (root.size[0] if root.size[0] < root.size[1] else root.size[1]) # this is the icon size
    pos_hint: {"center_x": .5, "center_y": .5}
    color: root.icon_color
    
    canvas.before:
        Color:
            rgba: root.bg_color or (0, 0, 0, 0)
        Rectangle:
            pos: self.pos
            size: self.size

<IconViewer>:
    available_space: self.width - dp(30)
    number_of_spacings: int((root.available_space - 2*dp(20)) / dp(150)) - 1
    cols: int((root.available_space - 2*dp(20) - root.number_of_spacings*dp(10)) / dp(150))
    left_padding: (root.available_space - root.cols*dp(150) - (root.cols-1)*dp(10)) / 2

    rv_grid: rv_grid.__self__
    tipbox: tipbox.__self__

    BoxLayout:
        orientation: "vertical"
        padding: dp(15), 0
        spacing: dp(5)
        
        TextInput:
            id: search
            size_hint_y: None
            height: dp(40)
            hint_text: "Search"
            multiline: False
            on_text: root.set_list_md_icons(self.text, True)

        RecycleView:
            viewclass: "IconViewerItem"
            data: root.icons
            pos_hint: {"center_x": .5}

            bar_width: dp(20)
            bar_color: blue
            scroll_type: ["bars", "content"]
            canvas.before:
                Color:
                    rgba: white
                Rectangle:
                    pos: self.pos
                    size: self.size
            
            RecycleGridLayout:
                id: rv_grid
                cols: root.cols
                padding: root.left_padding, 0, dp(20), 0
                spacing: dp(10)
                default_size: dp(150), dp(100)
                default_size_hint: None, None
                size_hint_y: None
                height: self.minimum_height

    FloatLayout:
        BoxLayout:
            id: tipbox
            size_hint: None, None
            size: self.minimum_size
            padding: dp(14)
            opacity: 0

            canvas.before:
                Color:
                    rgba: white
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(5), dp(5), 0, 0]
            Label:
                size_hint: None, None
                size: self.texture_size
                text: "Click to copy icon name: \\n[b]{}".format(root.selected_icon)
                color: blue_400
                halign: "center"
                markup: True
                font_size: dp(21)
            

<IconViewerItem>:
    orientation: "vertical"
    icon: 'android'

    canvas.before:
        Color:
            rgba: gray_300
        Line:
            rectangle: self.x, self.y, self.width, self.height
            width: dp(1)

    canvas.after:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: self.pos
            size: self.size

    Icon:
        mode: "stretch-icon"
        icon: root.icon
        icon_color: rgba("#5F6368")
        bg_color: slate_200
    Label:
        text: root.icon
        font_size: dp(16)
        size_hint_y: None
        height: dp(20)
        color: black
        shorten: True
        shorten_from: "right"
        text_size: dp(135), None
        halign: "center"
""")
