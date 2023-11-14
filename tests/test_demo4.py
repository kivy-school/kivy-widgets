import sys
sys.path.append('..')
from kivy.app import App 
from kivy.lang import Builder
from kivy_widgets.buttons import CButton


kv = """
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
    CButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
"""



class TestApp(App):
    def build(self):
        return Builder.load_string(kv)
    
if __name__ == '__main__':
    TestApp().run()