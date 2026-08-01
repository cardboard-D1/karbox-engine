from karbox import Stage, Group
import time

# Load bad-apple.txt
content = open("bad-apple-highres.txt", "r").read().splitlines()

# Read metadata and create Stage "tmp"
# It will be used temporarly for reading frames

metadata = content[0].split()
tmp = Stage(
    int(metadata[0]), # Width
    int(metadata[1]), # Height
)
FPS = int(metadata[2]) # Frames per second

content.pop(0)

# Convert to karbox readable format

frames = []

for element in range(len(content) - 1):
    for character in range(len(content[element]) - 1):
        tmp.insert_(
            x = character,
            y = (element+1) % tmp.height,
            char = content[element][character]
        )
    if (element+1) % tmp.height == 0:
        frames.append(Group(tmp))
        frames[-1].define_pos(
            0, 0, 
            tmp.width - 1, tmp.height - 1
        )

# Play

period = 1 / FPS

for frame in frames:
    tmp.fill(0, 0, tmp.width - 1, tmp.height - 1, " ")
    frame.paste(0, 0)
    tmp.refresh()
    time.sleep(period)
    time.sleep(0)
