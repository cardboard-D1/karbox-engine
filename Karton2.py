class LineLow:


    def __init__(
            self, starting_x: int, starting_y: int,
            finish_x: int, finish_y: int):
        self.x = []
        self.y = []

        distance_x = finish_x-starting_x
        distance_y = finish_y-starting_y

        direction_y = 1
        if distance_y < 0:
            direction_y = -1
            distance_y = -distance_y

        D = (2*distance_y) - distance_x
        y = starting_y

        for x in range(starting_x, finish_x):
            self.x.append(x)
            self.y.append(y)
            if D > 0:
                y += direction_y
                D += 2 * (distance_x - distance_y)
            else:
                D += 2 * distance_y


class LineHigh:


    def __init__(
            self, starting_x: int, starting_y: int, 
            finish_x: int, finish_y: int):
        self.x = []
        self.y = []

        distance_x = finish_x-starting_x
        distance_y = finish_y-starting_y

        directionX = 1
        if distance_x < 0:
            directionX = -1
            distance_x = -distance_x

        D = (2*distance_x) - distance_y
        x = starting_x

        for y in range(starting_y, finish_y):
            self.x.append(x)
            self.y.append(y)
            if D > 0:
                x += directionX
                D += 2 * (distance_x - distance_y)
            else:
                D += 2 * distance_x


class Stage:


    def __init__(self, width: int, height: int):
        self.image = {}
        self.width = width
        self.height = height
        self.selected_layer = "#"
        
        Stage.new_layer(self, "#")

    def new_layer(self, name: str):
        self.image[name] = []
        for H in range(self.height):
            self.image[name].append([])
            for W in range(self.width):
                self.image[name][-1].append(" ")

    def hide_layer(self, name: str):
        if name in self.image:
            self.image["."+name] = self.image.pop(name)

    def show_layer(self, name: str):
        if "."+name in self.image:
            self.image[name] = self.image.pop("."+name)

    def insert_(self, x: int, y: int, char: str, ansi: str = ""):
        if ansi:
            ansi1 = f"\033[{ansi}m"
            ansi2 = "\033[0m"
        else:
            ansi1 = ""
            ansi2 = ""
        try:
            self.image[self.selected_layer][round(y)][round(x)] \
            = ansi1 + char + ansi2
        except IndexError:
            pass
            
    def refresh(self):
        print("\033c", end="")

        for layer in self.image:
            if layer[0] != ".":
                for Y in range(self.height):
                    for X in range(self.width):
                        if self.image[layer][Y][X] != " ":
                            print(f"\033[{Y+1};{X+1}H" 
                                  + self.image[layer][Y][X],
                                  end="")
                        else:
                            print(f"\033[{Y+1};{X+1}H", end="")
            print("\033[0;0H", end="")
        print(f"\033[{self.height + 1};0H", end="")

    def debug_layer(self):
        for Y in range(self.height):
            for X in range(self.width):
                if X == self.width - 1:
                    print(self.image[self.selected_layer][Y][X])
                else:
                    print(self.image[self.selected_layer][Y][X], end="")

    def fill(
            self, starting_x: int, starting_y: int, 
            finish_x: int, finish_y: int, char: str, 
            mode=1, ansi: str="", corners:list = [None],
            outlines:list=[None]):
        if starting_x > finish_x:
            x1, x2 = finish_x, starting_x
        else:
            x1, x2 = starting_x, finish_x

        if starting_y > finish_y:
            y1, y2 = finish_x, starting_y
        else:
            y1, y2 = starting_y, finish_y
            
        if mode in (1, "solid", "full"):
            for Y in range(y1, y2+1):
                for X in range(x1, x2+1):
                    self.insert_(X, Y, char, ansi=ansi)

        if mode in (2, "outline", "border") or outlines[0] != None:
            if outlines[0] != None and (len(outlines) == 2 or len(outlines) == 4):
                if len(outlines) == 2:
                    left, right = outlines[0], outlines[0]
                    top, bottom = outlines[1], outlines[1]
                elif len(outlines) == 4:
                    left, right, top, bottom = outlines[0], outlines[1], outlines[2], outlines[3]
            else:
                left, right, top, bottom = char, char, char, char
            
            for X in range(x1, x2+1):
                self.insert_(X, starting_y, top, ansi=ansi)

            for Y in range(starting_y+1, finish_y):
                self.insert_(starting_x, Y, left, ansi=ansi)
                self.insert_(finish_x, Y, right, ansi=ansi)

            for X in range(x1, x2+1):
                self.insert_(X, finish_y, bottom, ansi=ansi)
                
        if corners[0] != None:
            if len(corners) == 4:
                self.insert_(x1, y1, corners[0], ansi = ansi)
                self.insert_(x2, y1, corners[1], ansi = ansi)
                self.insert_(x1, y2, corners[2], ansi = ansi)
                self.insert_(x2, y2, corners[3], ansi = ansi)
            elif len(corners) == 2:
                self.insert_(x1, y1, corners[0], ansi = ansi)
                self.insert_(x2, y1, corners[0], ansi = ansi)
                self.insert_(x1, y2, corners[1], ansi = ansi)
                self.insert_(x2, y2, corners[1], ansi = ansi)
            elif len(corners) == 1:
                self.insert_(x1, y1, corners[0], ansi = ansi)
                self.insert_(x2, y1, corners[0], ansi = ansi)
                self.insert_(x1, y2, corners[0], ansi = ansi)
                self.insert_(x2, y2, corners[0], ansi = ansi)
                
    def text(
            self, x: int, y: int,
            text: str, max_x: int=999,
            max_y: int=999, ansi: str=""):
        i = 0
        text_list = text.split()

        while i < len(text_list)-1:
            # If lenght of the current word and next word combined is 
            # smaller than maximum x (width): 
            if len(text_list[i]) + 1 + len(text_list[i+1]) < max_x:
                text_list[i] += " " + text_list[i+1]
                text_list.pop(i+1)
                # Then fuse current word and next word.
            else:
                i += 1
                # next
                
        i = 0
        while i < len(text_list):
            if len(text_list[i]) > max_x:
                text_list.insert(i+1, text_list[i][max_x:])
                text_list[i] = text_list[i][:max_x]
                i += 1
            else:
                i += 1

        if len(text_list) > max_y:
            text_list = text_list[:max_y]

        for line in range(len(text_list)):
            for X in range(len(text_list[line])):
                self.insert_(X+x, line+y, text_list[line][X], ansi=ansi)

    def line(
            self, starting_x: int, starting_y: int,
            finish_x: int, finish_y: int, char: str,
            ansi: str=""):
        if abs(finish_y-starting_y) < abs(finish_x - starting_x):
            if starting_x > finish_x:
                path = LineLow(finish_x, finish_y, starting_x, starting_y)
            else:
                path = LineLow(starting_x, starting_y, finish_x, finish_y)
        else:
            if starting_y > finish_y:
                path = LineHigh(finish_x, finish_y, starting_x, starting_y)
            else:
                path = LineHigh(starting_x, starting_y, finish_x, finish_y)

        for i in range(len(path.x)):
            self.insert_(path.x[i], path.y[i], char, ansi=ansi)

    def getFromPos(self, x: int, y: int):
        try:
            return self.image[self.selected_layer][y][x]
        except:
            pass

    def input_at(
            self, x: int, y: int,
            ansi: str="", label: str="", label_ansi: str="90", 
            input_stay: bool=True, label_stay: bool=True):
        # \033[x;yH -> Moves the cursor to the given row and column.
        print(f"\033[{y+1};{x+1}H", end="")
        print(f"\033[{label_ansi}m" + label
              + "\033[0m" if label_ansi else label, end=""
              )
        print(f"\033[{y+1};{x+1}H", end="")
        inp = input(f"\033[{ansi}m" if ansi else "")

        if label_stay:
            self.text(x, y, label, ansi=label_ansi)
                
        if input_stay:
            self.text(x, y, inp, ansi=ansi)

        return inp


class Group:

    def __init__(self, stage):
        self.pos = (None, None)
        self.pos_end = (None, None)
        self.size = (None, None)
        self.image = None
        self.stage = stage

    def define_pos(
            self, starting_x: int, starting_y: int,
            finish_x: int, finish_y: int):
        self.image = []

        if finish_x < starting_x:
            x1, x2 = finish_x, starting_x
        else:
            x1, x2 = starting_x, finish_x

        if finish_y < starting_y:
            y1, y2 = finish_y, starting_y
        else:
            y1, y2 = starting_y, finish_y

        for Y in range(y1, y2+1):
            self.image.append([])
            for X in range(x1, x2+1):
                self.image[-1].append(
                    self.Stage.image[self.stage.selected_layer][Y][X]
                )

        self.pos = (x1, y1)
        self.pos_end = (x2, y2)
        self.size = (x2-x1+1, y2-y1+1)

    def load_file(self, filepath):
        try:
            file = open(filepath)
            image = file.read().splitlines()
            # Get width and height
            width = 0
            height = len(image)

            for line in image:
                if len(line) > width:
                    width = len(line)
            # Enlongate shorter elements
            for i in range(len(image)):
                if len(image[i]) < width:
                    image[i] += " "*(width - len(image[i]))
            # Convert to format readable by Karton2
            self.image = []
            for Y in range(height):
                self.image.append([])
                for X in range(width):
                    self.image[-1].append(image[Y][X])
            # Edit group atributes
            self.pos = (None, None)
            self.pos_end = (None, None)
            self.size = (width, height)
        finally:
            file.close()

    def load_file_color(self, filepath):
        try:
            file = open(filepath)
            image = file.read()

            image = image.split("§")

            for elem in range(len(image)):
                image[elem] = image[elem].split("⍽")

            self.image = image
            self.size = (len(image[0]), len(image))
        finally:
            file.close()

    def paste(self, x: int, y: int, ansi: str = ""):
        for Y in range(self.size[1]):
            for X in range(self.size[0]):
                self.stage.insert_(X+x, Y+y, self.image[Y][X], ansi=ansi)

        if self.pos[0] == None:
            self.pos = (x, y)
            self.pos_end = (x+self.size[0], y+self.size[1])

    def move(self, x:int = 0, y:int = 0):
        # Errase previous position
        self.stage.fill(self.pos[0], self.pos[1],
                        self.pos_end[0], self.pos_end[1], " ")
        # Insert to new pos
        self.pos = (self.pos[0] + x, self.pos[1] + y)
        self.pos_end = (self.pos_end[0] + x, self.pos_end[1] + y)

        self.paste(self.pos[0], self.pos[1])

    def set_pos(self, x:int = 0, y:int = 0):
        # Errase previous position
        self.stage.fill(self.pos[0], self.pos[1],
                        self.pos_end[0], self.pos_end[1], " ")
        # Insert to new pos
        self.pos = (x, y)
        self.pos_end = (x + self.size[0], y + self.size[1])

        self.paste(self.pos[0], self.pos[1])

    def touching(self, group):
        return self.pos[0] <= group.pos_end[0] and \
               self.pos[1] <= group.pos_end[1] and \
               self.pos_end[0] >= group.pos[0] and \
               self.pos_end[1] >= group.pos[1]

    def save(self, destination):
        try:
            file = open(destination, "w")
            to_save = ""
            
            for element in self.image:
                for char in element:
                    to_save += char + "⍽"
                to_save = to_save[:-1]
                to_save += "§"
            to_save = to_save[:-1]
            file.write(to_save)
        finally:
            file.close()


def touching_groups(group1, group2):
    return group1.pos[0] <= group2.pos_end[0] and \
           group1.pos[1] <= group2.pos_end[1] and \
           group1.pos_end[0] >= group2.pos[0] and \
           group1.pos_end[1] >= group2.pos[1]
