from kivy.animation import Animation
from kivy.clock import Clock
from kivy.factory import Factory

# import Color, Rectangle, SmoothLine
from kivy.graphics import Color, Line, SmoothLine
from kivy.graphics.instructions import InstructionGroup
from kivy.lang import Builder, global_idmap
from kivy.metrics import dp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label

from .color_definitions import *


class DropDownItem(ButtonBehavior, Label):
    color = ColorProperty([0, 0, 0, 1])
    text = StringProperty()
    bg_color = ListProperty([1, 1, 1, 1])

    def get_current_bg_color(self):
        if self.state == "normal":
            return self.bg_color
        else:
            return [
                self.bg_color[0] * 0.8,
                self.bg_color[1] * 0.8,
                self.bg_color[2] * 0.8,
                1,
            ]

    current_bg_color = AliasProperty(get_current_bg_color, bind=["state", "bg_color"])


# fmt: off
Builder.load_string("""
<DropDownItem>:
    size_hint_y: None
    height: dp(50)

    canvas.before:
        Color:
            rgba: root.current_bg_color or white
        Rectangle:
            size: self.size
            pos: self.pos

        Color:
            rgba: slate_400
        Line:
            width: 1
            points: self.x, self.y+self.height, self.x+self.width, self.y+self.height

""")
# fmt: off


class Container(DropDown):
    container_position = OptionProperty(
        "auto", options=["auto", "left-top", "top", "right-top", "left", "center", "right", "left-bottom", "bottom", "right-bottom", "left-aligned", "right-aligned"]
    )
    bg_color = ColorProperty([1,1,1,1])
    initial_width = NumericProperty(0)
    border_color = ColorProperty(global_idmap["slate_400"])
    border_width = NumericProperty(1)
    effect_cls = StringProperty("ScrollEffect")

    def __init__(self, max_height=dp(200), **kwargs):
        super().__init__(**kwargs)
        self.max_height = max_height

    def _reposition(self, *largs):
        # calculate the coordinate of the attached widget in the window
        # coordinate system
        win = self._win
        if not win:
            return
        widget = self.attach_to
        if not widget or not widget.get_parent_window():
            return
        wx, wy = widget.to_window(*widget.pos)
        wright, wtop = widget.to_window(widget.right, widget.top)

        if self.auto_width:
            self.width = wright - wx
        else:
            self.width = self.initial_width
        
        if self.container_position == 'auto':
            # ensure the dropdown list doesn't get out on the X axis, with a
            # preference to 0 in case the list is too wide.
            x = wright - self.width
            if x + self.width > win.width:
                x = win.width - self.width
            elif x < 0:
                x = 0

            self.x = x

            # determine if we display the dropdown upper or lower to the widget
            if self.max_height is not None:
                height = min(self.max_height, self.container.minimum_height)
            else:
                height = self.container.minimum_height

            h_bottom = wy - height
            h_top = win.height - (wtop + height)
            if h_bottom > 0:
                self.top = wy
                self.height = height
            elif h_top > 0:
                self.y = wtop
                self.height = height
            else:
                # none of both top/bottom have enough place to display the
                # widget at the current size. Take the best side, and fit to
                # it.
                if h_top < h_bottom:
                    self.top = self.height = wy
                else:
                    self.y = wtop
                    self.height = win.height - wtop

            return
        
        if self.container_position == "left-top":
            self.x = wx - self.width/2
            self.y = wtop

        elif self.container_position == "top":
            self.x = wx - (self.width - widget.width)/2
            self.y = wtop

        elif self.container_position == "right-top":
            self.x = wx + widget.width / 2
            self.y = wtop

        elif self.container_position == "left":
            self.x = wx - self.width
            self.y = wy - self.height/2 + widget.height/2

        elif self.container_position == "center":
            self.x = wx - (self.width - widget.width)/2
            self.y = wy - self.height/2 + widget.height/2

        elif self.container_position == "right":
            self.x = wx + widget.width
            self.y = wy - self.height/2 + widget.height/2

        elif self.container_position == "left-bottom":
            self.x = wx - self.width/2
            self.y = wy - self.height

        elif self.container_position == "bottom":
            self.x = wx - (self.width - widget.width)/2
            self.y = wy - self.height

        elif self.container_position == "right-bottom":
            self.x = wx + widget.width/2
            self.y = wy - self.height

        elif self.container_position == "left-aligned":
            self.x = wx 
            self.y = wy - self.height

        elif self.container_position == "right-aligned":
            self.x = wright - self.width
            self.y = wy - self.height


class CDropDown(ButtonBehavior, BoxLayout):
    values = ListProperty()
    text_autoupdate = BooleanProperty(False)
    dropdown_cls = ObjectProperty(Container)
    is_open = BooleanProperty(False)

    container_height = NumericProperty(dp(200))
    container_width = NumericProperty()
    container_position = OptionProperty(
        "auto", options=["auto", "left-top", "top", "right-top", "left", "center", "right", "left-bottom", "bottom", "right-bottom", "left-aligned", "right-aligned"]
    )
    container_bg_color = ColorProperty()
    container_border_color = ColorProperty(global_idmap["slate_400"])
    container_border_width = NumericProperty(1)

    effect_cls = StringProperty("ScrollEffect")

    text = StringProperty()
    markup = BooleanProperty(False)
    initial_text = StringProperty()

    shorten = BooleanProperty(False)
    shorten_from = OptionProperty(
        "right", options=["left", "center", "right"]
    )
    max_width = NumericProperty(allownone=True, default=None)

    font_size = NumericProperty(dp(18))
    font_color = ColorProperty([0,0,0,1])
    bold = BooleanProperty(False)
    
    icon = StringProperty("chevron-down")
    icon_color = ColorProperty(global_idmap["slate_500"])
    icon_size = NumericProperty(dp(21))

    border_color = ColorProperty(global_idmap["slate_400"])
    border_width = NumericProperty(1)

    reset_text = BooleanProperty(False)

    bg_color = ListProperty([1, 1, 1, 1])
    radius = ListProperty([0, 0, 0, 0])

    mode = OptionProperty(
        "rectangle", options=[
            "rectangle", "line"
        ]
    )


    def __init__(self, **kwargs):
        self._dropdown = None
        super().__init__(**kwargs)
        fbind = self.fbind
        build_dropdown = self._build_dropdown
        fbind("on_release", self._toggle_dropdown)
        fbind("dropdown_cls", build_dropdown)
        fbind("values", self._update_dropdown)
        fbind("text_autoupdate", self._update_dropdown)
        
        build_dropdown()
        Clock.schedule_interval(self._check_container_width, 1/15)


    def on_text(self, *args):
        self._label.text_size = (None, None)
        if not self.initial_text:
            self.initial_text = self.text

        Clock.schedule_once(self.update_label_text_size)

    def _check_container_width(self, t):
        if self.width != 0:
            if not self.container_width:
                self._dropdown.initial_width = self.width
            else:
                self._dropdown.initial_width = self.container_width
            self._dropdown.auto_width = False
            self.fbind("width", lambda *_: Clock.schedule_once(self.build_canvas))
            self.fbind("mode", lambda *_: Clock.schedule_once(self.build_canvas))
            self.fbind("y", lambda *_: Clock.schedule_once(self.build_canvas))
            self.fbind("x", lambda *_: Clock.schedule_once(self.build_canvas))
            self.build_canvas()
            return False
        return True
    
    def build_canvas(self, *args):
        """
        On mode 'rectangle', should create the following canvas:
        canvas.before:
            Color:
                rgba: root.border_color
            SmoothLine:
                width: root.border_width
                rounded_rectangle: (self.x, self.y, self.width, self.height, root.radius[0]) if root.radius[0] else (self.x, self.y, self.width, self.height, 1)

        On mode 'line', should create the following canvas:
        canvas.before:
            Color:
                rgba: root.border_color
            Line:
                width: 1
                points: self.x, self.y, self.x+self.width, self.y
        """

        if "line" in self.__dict__:
            self.line.clear()
            self.canvas.remove(self.line)

        self.line = InstructionGroup()

        if self.mode == 'rectangle':
            self.line.add(Color(
                rgba=self.border_color
            ))
            self.line.add(SmoothLine(
                width=self.border_width,
                rounded_rectangle=(self.x, self.y, self.width, self.height, self.radius[0]) if self.radius[0] else (self.x, self.y, self.width, self.height, 1)
            ))
        elif self.mode == 'line':
            self.line.add(
                Color(
                    rgba=self.border_color
                )
            )
            self.line.add(
                Line(
                    width=1,
                    points=(self.x, self.y+dp(5), self.x+self.width, self.y+dp(5))
                )
            )
        
        self.canvas.add(self.line)

    def on_container_height(self, *args):
        self._dropdown.max_height = self.container_height

    def on_container_position(self, *args):
        self._dropdown.container_position = self.container_position
        self._dropdown._reposition()

    def on_container_bg_color(self, *args):
        self._dropdown.bg_color = self.container_bg_color

    def on_container_border_color(self, *args):
        self._dropdown.border_color = self.container_border_color

    def on_container_border_width(self, *args):
        self._dropdown.border_width = self.container_border_width

    def on_effect_cls(self, *args):
        self._dropdown.effect_cls = self.effect_cls

    def _build_dropdown(self, *largs):
        if self._dropdown:
            self._dropdown.unbind(on_select=self._on_dropdown_select)
            self._dropdown.unbind(on_dismiss=self._close_dropdown)
            self._dropdown.dismiss()
            self._dropdown = None

        self._dropdown = self.dropdown_cls()

        self._dropdown.bind(on_select=self._on_dropdown_select)
        self._dropdown.bind(on_dismiss=self._close_dropdown)
        self._update_dropdown()

    def _update_dropdown(self, *largs):
        """
        Update the dropdown with the values. Each value is a dict with the
        following keys:
            - text: text displayed in the dropdown
            - viewclass: class used for displaying the text
            - anything else: added as an attribute to the viewclass

        """
        dropdown = self._dropdown
        values: dict[str:str] = self.values
        text_autoupdate = self.text_autoupdate
        dropdown.clear_widgets()
        for value in values: 
            classname = value.get("viewclass")

            if not classname:
                classname = "DropDownItem"
            
            copy_value = value.copy()
            copy_value.pop("viewclass", None)
            cls = Factory.get(classname)
            item = cls()
            for k, v in copy_value.items():
                setattr(item, k, v)
            item.size_hint_y = None

            height = copy_value.get("height")
            if height or hasattr(cls, "height"):
                item.height = height or item.height
            else:
                item.height = self.height
            
            item.bind(on_release=lambda option: dropdown.select(option.text))
            dropdown.add_widget(item)

        if text_autoupdate:
            if values:
                if not self.text or self.text not in values:
                    self.text = values[0]
            else:
                self.text = ""

    def _toggle_dropdown(self, *largs):
        if self.values:
            self.is_open = not self.is_open

    def _close_dropdown(self, *largs):
        self.is_open = False

    def _on_dropdown_select(self, instance: object, text: str, *largs):
        """
        Callback called when the dropdown select an option.
        e.g.: data = {'text': 'option1', 'viewclass': 'MyOption'}
        """
        if self.text != text:
            self.text = text
        elif self.reset_text:
            self.text = self.initial_text
        self.is_open = False

    def on_is_open(self, instance, value):
        if value:
            height = self.container_height
            self._dropdown.open(self)
            self._dropdown.height = 0
            anim = Animation(height=height, d=0.2, t="out_cubic")
            anim.bind(on_progress=lambda *_: setattr(self._dropdown, "scroll_y", 1))
            anim.start(self._dropdown)
        else:
            if self._dropdown.attach_to:
                self._dropdown.dismiss()

    def update_label_text_size(self, *args):
        if self.max_width and self._label.texture_size[0] >= self.max_width:
            self._label.text_size = (min(self._label.texture_size[0], self.max_width), None)
                

# fmt: off
Builder.load_string("""
<CDropDown>:
    padding: dp(10), 0
    size_hint: None, None
    height: dp(50)
    width: self.minimum_width
    _label: _label.__self__
                
    canvas.before:
        Color:
            rgba: root.bg_color if self.state == "normal" else [root.bg_color[0]*0.9, root.bg_color[1]*0.9, root.bg_color[2]*0.9, root.bg_color[3]]
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius

    Label:
        id: _label
        markup: root.markup
        text: root.text if not root.bold else f'[b]{root.text}[/b]'
        color: root.font_color
        font_size: root.font_size
        size_hint_x: None
        width: self.texture_size[0] + dp(10)
        shorten: root.shorten
        shorten_from: root.shorten_from
    Icon:
        icon: root.icon
        icon_color: root.icon_color
        icon_size: root.icon_size

<Container>
    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: self.pos
            size: self.size

    canvas.after:
        Color:
            rgba: root.border_color
        Line:
            width: root.border_width
            rectangle: (self.x, self.y, self.width, self.height)
""")
