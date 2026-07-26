from karbox import Stage
from os import get_terminal_size

term_size = get_terminal_size()
root = Stage(term_size.columns, term_size.lines)

root.fill(
    0, 0, # x position
    root.width - 1, root.height - 1, # y position
    char = " ",
    mode = "solid",
    corners = [
        "┏", "┓", "┗", "┛"
    ],
    outlines = [
        "┃", "━"
    ],
    ansi = "44;37"
)
root.fill(
    0, root.height//2 - 1,
    root.width-1, root.height//2 + 1,
    char = " ",
    mode = "outline",
    corners = [
        "┠", "┨", "┠", "┨"
    ],
    outlines = [
        "┃", "─"
    ],
    ansi = "44;37"
)
root.text(
    root.width/2 - 6, # x pos 
    root.height//2, # y pos
    text = "Welcome to Karbox!",
    ansi = "44;37"
)

root.refresh()
input()

# characters:
# ┗ ┛ ┏ ┓ ┠ ┨ ─ ┃ ━
