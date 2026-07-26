# Getting Started

## Downloading

1. Clone the repository: `$ git clone https://github.com/cardboard-D1/karbox-engine.git` into your project's directory
- Or just download `karbox.py` from the main page and move it to your project's directory

## Importing

1. Import `karbox.py` into your python file
```python
from karbox import Group, Stage
```
or
```python
from karbox import *
```

Now you are ready!

# Stage

## What is a stage?

A `Stage` is like a canvas of a picture, like a paper of a drawing. 

`Stage` in karbox is a python object, an image buffer, containing multiple layers, that is displayed on the screen (terminal) when the refresh function is called.
It's assigned to a variable and it accepts commands, functions.

## Initializing a stage

- Simply assign `Stage(<x, columns>, <y, rows>)` to a variable

```python
root = Stage(10, 10)
root.function(...)
```

- **This makes an inital layer `"#"`** and sets `selected_layer` to `"#"`, more on that later

## Position marks

This is how positions are marked on a `Stage`:
```
 x   0 1 2 ...
y
0    # # #
1    # # #
2    # # #
...
```

## Stage functions

This functions are methods of the Stage class, so prefix them with the variable you assigned `Stage` with:

`root.function()`

`*` marks attributes as non-optional

### New Layer

- **Syntax:** `new_layer(<name*>)`
- example: `new_layer("My Layer")`

This stacks a layer on top of previously created layers
so first create layers that you want to appear behind. Example is:

```python
root.new_layer("Background")
root.new_layer("A Sprite")
```

### Hide Layer

- **Syntax:** `hide_layer(<name*>)`
- This prefixes the layer name with a period "."

### Show Layer

- **Syntax:** `show_layer(<name*>)`
- You don't need to prefix the layer name with a period, the function does it for you ;)

### Selected Layer

- Tells on which layer drawing functions are applied on. 
**Drawing functions also include group movement, so be carefull!**

- **Syntax:** `root.selected_layer = "<layer name>"`

### Refresh

- This function displays the image the gamer should see
- Displays every layer combined

- **Syntax:** `refresh()`

### Insert

- **Syntax:** `insert_(<x*>, <y*>, <char*>, <ansi>)`

**`<ansi>` is automaticaly prefixed with `\033[` and sufixed with `m`** like the following:

`\033[` `<ansi>` `m`

- For more info, read about [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code#Select_Graphic_Rendition_parameters)

### Debug Layer

- This displays the layer specified by the `selected_layer` variable for debuging purposes *(maybe even for something else?)*

- **Syntax:** `debug_layer()`

### Fill

- **Syntax:** `fill(<starting_x*>, <starting_y*>, <finish_x*>, <finish_y*>, <char*>, <mode, default is solid>, <ansi>, <corners>, <outlines>)`
- Where `<corners>` and `<outlines>` are lists, more bellow

#### Corners

- It adds specified characters to corners of the fill/rectangle
- You can specify the list with one, two or four elements

1. **One Element:**
`root.fill(..., corners = ["1"], ...)` gives you:
```
~~~~~~~~~~~~
~~1######1~~
~~#~~~~~~#~~
~~#~~~~~~#~~
~~#~~~~~~#~~
~~1######1~~
~~~~~~~~~~~~
```
2. **Two Elements:**
`root.fill(..., corners = ["1", "2"], ...)` gives you:
```
~~~~~~~~~~~~
~~1######1~~
~~#~~~~~~#~~
~~#~~~~~~#~~
~~#~~~~~~#~~
~~2######2~~
~~~~~~~~~~~~
```
3. **Four Elements:**
`root.fill(..., corners = ["1", "2", "3", "4"], ...)` gives you:
```
~~~~~~~~~~~~
~~1######2~~
~~#~~~~~~#~~
~~#~~~~~~#~~
~~#~~~~~~#~~
~~3######4~~
~~~~~~~~~~~~
```

#### Outlines

- Similar as the corners, but with outlines
- You can specify the list with two or four elements

1. **Two Elements:**
`root.fill(..., outlines = ["1", "2"], ...)` gives you:
```
~~~~~~~~~~~~
~~22222222~~
~~1~~~~~~1~~
~~1~~~~~~1~~
~~1~~~~~~1~~
~~22222222~~
~~~~~~~~~~~~
```
2. **Four Elements:**
`root.fill(..., outlines = ["1", "2", "3", "4"], ...)` gives you:
```
~~~~~~~~~~~~
~~33333333~~
~~1~~~~~~2~~
~~1~~~~~~2~~
~~1~~~~~~2~~
~~44444444~~
~~~~~~~~~~~~
```












