import sys
sys.path.append('..')
from kivy.app import App 
from kivy.lang import Builder


kv = """
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
"""



class TestApp(App):
    def build(self):
        return Builder.load_string(kv)
    
if __name__ == '__main__':
    TestApp().run()