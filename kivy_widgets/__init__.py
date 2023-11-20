import os

from kivy.lang import global_idmap

import kivy_widgets.color_definitions

from .icon_definitions import icon_unicodes

__file__ = os.path.abspath(__file__)
font_path = os.path.join(
    os.path.dirname(__file__), "fonts", "materialdesignicons-webfont.ttf"
)

global_idmap["unicode"] = icon_unicodes
global_idmap["icon_font"] = font_path

__all__ = ["buttons", "dropdown", "icons", "textinput"]
