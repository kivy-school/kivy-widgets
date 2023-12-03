from kivy.lang import Builder, global_idmap
from kivy.properties import ColorProperty
from kivy.uix.floatlayout import FloatLayout


class CFloatLayout(FloatLayout):
    bg_color = ColorProperty(global_idmap["white"])


# fmt: off
Builder.load_string("""
<CFloatLayout>:
    canvas.before:
        Color:
            rgba: self.bg_color
        Rectangle:
            size: self.size
            pos: self.pos
""")
# fmt: on
