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

### Line

Draws a line with the specified starting position and finish position

- **Syntax:** `line(<starting_x*>, <starting_y*>, <finish_x*>, <finish_y*>, <char*>, <ansi>)`

### Get from a Position

Returns an element at the `selected_layer` at the specified position

- **Syntax:** `get_from_pos(<x*>, <y*>)`

### Input at a Position

Triggers an input action at the specified position

- **Syntax:** `input_at(<x*>, <y*>, <ansi>, <label>, <label_ansi, default:90(Gray)>, <input_stay, default: True>, <label_stay, default: True>)`
- `<ansi>` - Applies to the input text
- `<label>` - Text shown bellow the input text
- `<label_ansi>` - Applies to the label text
- If `<input_stay>` is set to `True`, the input text stays visible after the user presses enter
- `<label_stay>` is the same thing, but for the label

## Stage's attributes

A stage has attributes/variables when you assign it to a variable.
There is a few of them:

### Image

This is the buffer of a stage, here are stored all layer names in an `array` and textures assigned to them.

- **To access:** `my_stage.image`

### Stage Width

- **To access:** `my_stage.width`

### Stage Height

- **To access:** `my_stage.height`

### Selected Layer

It has been talked about previously in this documentation.

- **To access:** `my_stage.selected_layer`

# Groups

Do you want to import a texture from a `.txt` file and use it in your project? 
Maybe you want to take a bigger chunk of the stage and move it around? 
Do you need touch detection between two "sprites"? (For example between a cursor and a button)

Use groups for this!

## What is a group?

In `karbox`, group is a chunk of a stage layer, or txt file, stored in a seperate buffer.
You can import plain `.txt` files into them or in a special color format for karbox.
They can be moved by a position or to a position.
And it's possible to detect collision between two groups.
It is assigned to a variable and accepts commands, functions.

## Initalizing a group

To initalize a group to a variable, assign `Group()` to a variable and specify the stage's variable. For example:

```python
root = Stage(10, 10) # stage's variable is "root"
my_group = Group(root)
```

Currently, the group's image buffer is empty.
There are three ways to give it a texture.

## Adding Texture to a Group

This functions are methods of the Group class, so prefix them with the variable you assigned `Group` with:

`my_group.function()`

### From the Stage

Copies contents of a specified area of `selected_layer` of a stage into group's image buffer.

- **Syntax:** `define_pos(<starting_x*>, <starting_y*>, <finish_x*>, <finish_y*>)`

### From a Plain txt File

Copies contents of a text file into group's image buffer.

- **Syntax:** `load_file(<filepath*>)`
- Where `<filepath>` is file's path starting from your python file's path

### From Karbox Formatted Files

Use this if you want to import a file created by the group function `save(...)`.
This decodes the file into color texture which is stored in group's image buffer.

- **Syntax:** `load_file_color(<filepath*>)`

## Group Functions

### Paste

Just slaps that group's image buffer onto the stage (at the `selected_layer`).
This paste has no relation with any group's attributes or buffers.

- **Syntax:** `paste(<x*>, <y*>, <ansi>)`
- Use `<ansi>` only if you imported the texture from a plain txt

### Moving by Values

Moves the group by specified x and y.
Changes group's position attributes.

- **Syntax:** `move(<x, default: 0>, <y, default: 0>)`

### Moving to a Position

Moves the group to a specified position.
Changes groups's position attributes.

- **Syntax:** `set_pos(<x*>, <y*>)`

### Touching

Returns `True` or `False` depending on if the group touches an other specified group.

- **Syntax:** `my_group.touching(another_group)`
- Added `my_group.` for a better measure the reader will understand this

### Touching #2

Same as previous, but written differently.

- **Syntax:** `touching_groups(first_group, second_group)`
- This one **is not** prefixed with group's name.

## Group attributes

These are variables of groups.

### Position

It's a tuple with two elements.
The first element being **x position**
and the second element **y position**.
This position marks the top left corner of the group.

- **To access:**
  - `my_group.pos` for the tuple itself
  - `my_group.pos[0]` for x position
  - `my_group.pos[1]` for y position

### End Position

Same as position, but marks the bottom right of the group.

- **To access:**
  - `my_group.pos_end` for the tuple itself
  - `my_group.pos_end[0]` for x position
  - `my_group.pos_end[1]` for y position

### Size

It's a tuple with two elements.
The first element being **width**
and the second element **height**.

- **To access:**
  - `my_group.size` for the tuple itself
  - `my_group.size[0]` for width
  - `my_group.size[1]` for height

### Image Buffer

This is the image buffer of a group.

- **To access:** `my_group.image`

### Stage

The stage object is stored here

- **To access:** `my_group.stage`
