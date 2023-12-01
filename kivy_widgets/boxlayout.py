from kivy.lang import Builder, global_idmap
from kivy.properties import ColorProperty
from kivy.uix.boxlayout import BoxLayout


class CBoxLayout(BoxLayout):
    bg_color = ColorProperty(global_idmap["white"])


# fmt: off
Builder.load_string("""
<CBoxLayout>:
    canvas.before:
        Color:
            rgba: self.bg_color
        Rectangle:
            size: self.size
            pos: self.pos
""")
# fmt: on
