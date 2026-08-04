from karbox import *

# ╭╮╰╯─│
# ┤├

root = Stage(64, 18)

root.fill(
    0, 0,
    62, 17,
    char = " ",
    corners = ["╭", "╮", "╰", "╯"],
    outlines = ["│", "─"],
    ansi = "38;5;15" + ";48;5;52"
)

root.fill(
    0, 7,
    62, 9,
    char = " ",
    corners = ["├", "┤", "├", "┤"],
    outlines = ["│", "─"],
    ansi = "38;5;15" + ";48;5;52"
)

root.text(
    29, 8,
    text = "Karbox!",
    ansi = "38;5;15" + ";48;5;52"
)

x_pos = 2

for i in range(7):
    root.fill(
        x_pos, 12,
        x_pos + 3, 13,
        char = " ",
        ansi = str(40 + i)
    )
    x_pos += 4

x_pos = 2

for i in range(7):
    root.fill(
        x_pos, 14,
        x_pos + 3, 16,
        char = " ",
        ansi = str(100 + i)
    )
    x_pos += 4

root.text(
    32, 12,
    text = "<- Wow color, oh man, crazy stuff",
    ansi = "38;5;15" + ";48;5;52",
    max_x = 22
)

root.text(
    39, 12,
    text = "color",
    ansi = "38;5;15" + ";48;5;52;5",
)

root.refresh()
input()
