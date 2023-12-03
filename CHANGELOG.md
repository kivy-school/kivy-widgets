# Version: 0.1.38

✨ feat: Created new CFloatLayout component

# Version: 0.1.37

✨ feat: Created new CBoxLayout component

# Version: 0.1.36

✨ feat: Created 5 new CTextInput events:

- on_icon_left_color_active
- on_foreground_active_color
- on_foreground_color
- on_hint_text_color_active
- on_line_color_active

# Version: 0.1.35

🐛 fix: Fixed line color update of CTextInput in fill mode

# Version: 0.1.34

✨ feat: Added `icon_left` and `fill` mode to CTextInput

# Version: 0.1.33

✨ feat: Added `halign` property to `CTextInput`

# Version: 0.1.32

✨ feat: Updated `insert_text` from `CTextInput`: now the user has the option to handle the insert_text and not dispatch super.insert_text
✨ feat: Added `focus` property to `CTextInput`

# Version: 0.1.31

✨ feat: Created two CTextInput custom handlers:

- insert_text_filter: an optional function that receives str and returns str
- keyboard_down: an optional function to do anything the user want to the input/text_field

✨ feat: Added `input_type` property to CTextInput
✨ feat: Created `RoundedRectangleRippleBehavior` component

# Version: 0.1.30

✨ feat: Added `target` property to `CTextInput`
✨ feat: Created `RetargetTextInput` component
🐛 fix: Fixed `create_initial_line` and `on_complete_restore` from CTextInput

# Version: 0.1.29

✨ feat: Created new `CTextInput` component

# Version: 0.1.28

✨ feat: Created `CircularRippleBehavior` component

# Version: 0.1.27

✨ feat: Loading icon unicodes on **init**

# Version: 0.1.26

🐛 fix: Fixed CButton `shorten` function when the user gives some value to `max_width`

# Version: 0.1.25

✨ feat: Added `halign` property to `CButton`
✨ feat: Importing `buttons`, `dropdown` and `icons` modules when using star (\*) import

# Version: 0.1.24

✨ feat: Binding `CDropDown.build_canvas` to changes on `x` property

# Version: 0.1.23

✨ feat: Added `markup` property to CDropDown.

# Version: 0.1.22

✨ feat: Added `markup` property to CButton.

# Version: 0.1.21

✨ feat: Added `shorten` functionality to CDropDown:

- Now you can pass `shorten`, `shorten_from` and `max_width` to CDropDown, and it will apply these properties to the main CDropDown label

# Version: 0.1.20

- 🐛 fix: Fixed CButton spacing when `current_mode` is "both"

# Version: 0.1.19

- ✨ feat: Added shorten/shorten_from to CButton
- ✨ feat: Added icon_position property to CButton
- ✨ feat: Added align_on_left property to CButton
- ✨ feat: Added left_padding property to CButton

# Version: 0.1.18

- 🐛 fix: `CDropDown._update_dropdown` does not pass `viewclass` attributes directly on `__init__`, avoiding TypeError.

# Version: 0.1.17

- ✨ feat: Added defaut `effect_cls` to Container from CDropDown

# Version: 0.1.16

- 🐛 fix: CDropDown updates container.scroll_y to 1 on animation progress

# Version: 0.1.15

- ✨ feat: Updated `CDropdown`:
  - Binding `build_canvas` to `y` value
  - Fixed name collision with `dp` from kivy.metrics

# Version: 0.1.14

- ✨ feat: Created two design modes for `CDropDown`:
  - rectangle (default)
  - line

# Version: 0.1.13

- ✨ feat: Added `reset_text` behaviour to `CDropDown`

# Version: 0.1.12

- ✨ feat: Added `border_color` and `border_width` to `Container`
- ✨ feat: Added `transparent` color to definitions

# Version: 0.1.11

- ✨ feat: Updated CDropDown:
  - "Bottom" alignment is the default one
  - Now you can define the `container_width`
  - Created two alignments for Container: "left-aligned", "right-aligned"

# Version: 0.1.10

- ✨ feat: Added `container_bg_color` property to CDropDown

# Version: 0.1.9

- 🐛 fix: Fixed bug in CDropDown: - Making `auto_width = True` when container_width is not provided

# Version: 0.1.8

- ✨ feat: Created `CDropDown` and related classes:
  - DropDownItem (a clickable Label)
  - Container (a container for all items of the DropDown, with custom initial position)

# Version: 0.1.7

- 🐛 fix: Removed padding and spacing from `CButton` (replaced by dummy widgets).

# Version: 0.1.6

- 🐛 fix: Created `CButton` (Custom Button) widget.

# Version: 0.1.5

- 🐛 fix: Fixed `font_name` from `Icon` class.

# Version: 0.1.4

- [#6](https://github.com/kivy-school/kivy-widgets/pull/7): "✨ feat: Create Icon and IconViewer + icon_definitions"
- ✨ feat: Created Created icon_definitions.py
- ✨ feat: Created icons.py

IconViewer implements hover functionality (tooltip) over all icons. You can copy any icon name by clicking on its `IconViewerItem`

# Version: 0.1.3

- [#3](https://github.com/kivy-school/kivy-widgets/pull/3): "⬆️ chore: Downgraded python version”

# Version: 0.1.2

- [#1](https://github.com/kivy-school/kivy-widgets/issues/1): ”✨ feat: Created color definitions - Tailwind standard color palette”
