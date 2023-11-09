# CButton

## Overview
CButton is a custom Kivy button widget that belongs to the custom widgets in the `kivy-widgets` package. It's a customizable button equipped with optional icon and text.

## Properties

### 1. `text`
- Type: `StringProperty`
- Example: "Hello, World!"
- Description: This property is used to set the text to be displayed on the button. It's optional, and the default is an empty string.

### 2. `markup`
- Type: `BooleanProperty`
- Example: True, False
- Description: This property opens up the text property to being edited with Kivy's Markup language. The default is `False`.

### 3. `font_size`
- Type: `NumericProperty`
- Example: dp(50), '50dp', etc.
- Description: Dictates the size of the text on the button, indirectly determining the button's size. The default is `sp(18)`.

### 4. `font_color`
- Type: `ColorProperty`
- Example: [0,0,0,0]
- Description: Dictates the color of the button's text. The default is [0,0,0,1].

### 5. `halign`
- Type: `OptionProperty`
- Options: 'center', 'left', 'right'
- Description: Dictates the horizontal alignment of the button's text within the button space. The default is 'center'.

### 6. `icon`
- Type: `StringProperty`
- Description: Dictates the icon the button should contain/use. This property works in collaboration with `kivy_widgets.icon_definitions.icon_unicodes`. Check the documentation of [icon_unicodes](link_here) for more information.
