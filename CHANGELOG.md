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
