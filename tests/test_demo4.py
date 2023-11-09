import sys
sys.path.append('..')
from kivy.app import App 
from kivy.lang import Builder
from kivy_widgets.buttons import CButton
from kivy_widgets.dropdown import CDropDown
from kivy.metrics import dp, sp


kv = """
#:import icon_unicodes kivy_widgets.icon_definitions.icon_unicodes
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
    CButton:
        text: "[b]Hello, World![b]"
        markup: True
        font_size: sp(50)
        font_color: 0.5, 0.7, 0.3, 1
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        
        icon: icon_unicodes['account']
        icon_color: 0.5, 0.7, 0.3, 1
        icon_size: dp(60)
        icon_position: "left"

"""



class TestApp(App):
    def build(self):
        return Builder.load_string(kv)
    
if __name__ == '__main__':
    TestApp().run()