from Shape import *
from Constants import *
from time import sleep

DELAY = 0.05


class ShapeCreator:
    def __init__(self, parent, shape_type, height, width):
        self.parent = parent
        self.template = None
        self.shape_type = shape_type
        self.width = width
        self.height = height
        self.canvas_width = parent.winfo_width()
        self.canvas_height = parent.winfo_height()
        self.scrollbar = ...

        self.playing_area_map = [[None]]
        self.playing_area_row = 0
        self.playing_area_col = 0
        self.playing_area_row_template = 0
        self.playing_area_col_template = 0
        self.template_coords = [SHAPE_BORDER, SHAPE_BORDER]
        self.coords_for_new_shape = [0, 0]

        self.shape_setup = None

        self.parent.update()

    def print_map(self, map=None):
        if not map:
            map = self.playing_area_map

        playing_area = []
        for row in range(len(map)):
            playing_area.append([])
            for col in range(len(map[row])):
                if map[row][col]:
                    playing_area[row].append(map[row][col].name)
                else:
                    playing_area[row].append(None)
        print(playing_area)

    def create_template(self):
        shape = self.shape_type(self.parent, self.template_coords, self.height, self.width)
        shape.create()
        shape.set_template()   # premenuj na get_template

        self.template = shape
        self.playing_area_map[self.playing_area_row_template][self.playing_area_col_template] = self.template

        sleep(DELAY)
        self.parent.update()

    def move_template(self):

        self.set_shape_position(self.playing_area_row_template, self.playing_area_col_template + 1)
        x, y = self.template_coords
        self.template.move_shape(x, y)

        sleep(DELAY)
        self.parent.update()

    def update_playing_area(self, shape):
        if self.playing_area_row == self.playing_area_row_template:
            if len(self.playing_area_map[self.playing_area_row_template]) == self.playing_area_col_template:
                self.playing_area_map[self.playing_area_row_template].insert(self.playing_area_col_template, None)

        elif len(self.playing_area_map) == self.playing_area_row_template:
                self.playing_area_map.insert(self.playing_area_row_template, [None])

        self.playing_area_map[self.playing_area_row][self.playing_area_col] = shape
        self.playing_area_map[self.playing_area_row_template][self.playing_area_col_template] = self.template

    def set_template_coords_after_removing(self):
        template_row = 0
        template_col = 0
        for row in range(len(self.playing_area_map)):
            for col in range(len(self.playing_area_map[row])):
                if self.playing_area_map[row][col] == self.template:
                    template_row = row
                    template_col = col

        self.template_coords[0], self.template_coords[1] = self.compute_coords(template_col, template_row)

    def compute_coords(self, col, row):
        x = CANVAS_BORDER + (self.width + SHAPE_BORDER) * col
        y = CANVAS_BORDER + (self.height + SHAPE_BORDER) * row
        return x, y

    def set_shape_position(self, _row, _col):
        row, col = self.check_border(_row, _col)
        x, y = self.compute_coords(col, row)

        self.playing_area_col = _col - 1
        self.playing_area_row = _row
        self.playing_area_col_template = col
        self.playing_area_row_template = row

        self.coords_for_new_shape[0] = self.template_coords[0]
        self.coords_for_new_shape[1] = self.template_coords[1]
        self.template_coords[0] = x
        self.template_coords[1] = y

    def check_border(self, _row, _col):
        next_shape_width_space = CANVAS_BORDER + ((self.width + SHAPE_BORDER) * (_col + 1))
        row = _row
        col = _col
        if next_shape_width_space > self.parent.winfo_width():
            row += 1
            col = 0

        next_shape_width_space =  CANVAS_BORDER + ((self.height + SHAPE_BORDER) * (_row + 1))

        if self.parent.winfo_height() < next_shape_width_space:
            print('ooooooo')
            self.parent.config(scrollregion=(0,0,300, 1000))

        return row, col

    def add_new(self, shape=None):

        self.move_template()
        x, y = self.coords_for_new_shape

        if not shape:
            shape = self.shape_type(self.parent, [x, y], self.height, self.width)
            shape.create()
        else:
            shape.move_shape(x, y)

        self.update_playing_area(shape)

        print('po pridani')
        self.print_map()

        self.parent.update()
        sleep(DELAY)
        return shape

    def remove(self, shape):
        if self.template == shape:
            return

        for row in range(len(self.playing_area_map)):
            for col in range(len(self.playing_area_map[row])):
                if self.playing_area_map[row][col] == shape:

                    self.playing_area_map[row][col] = None

                    shape.delete_shape()  # dorobit pre kazdy

                    self.rearrangement(row, col)
                    self.parent.update()
                    sleep(DELAY)
                    break

        self.set_template_coords_after_removing()
        self.parent.update()

        print('po zmazani')
        self.print_map()
        print(self.coords_for_new_shape)

    def rearrangement(self, _row=0, _col=0):
        for row in range(_row, len(self.playing_area_map)):
            for col in range(_col, len(self.playing_area_map[row])):

                if row + 1 == len(self.playing_area_map) and col + 1 == len(self.playing_area_map[row]):
                    return

                next_col = col + 1
                next_row = row

                if next_col == len(self.playing_area_map[row]):
                    next_col = 0
                    next_row = row + 1
                    _col = 0

                self.playing_area_map[row][col], self.playing_area_map[next_row][next_col] = \
                    self.playing_area_map[next_row][next_col], self.playing_area_map[row][col]

                if self.playing_area_map[row][col]:
                    self.move(row, col)
                    self.playing_area_col_template = col
                    self.playing_area_row_template = row
                else:
                    return

    def move(self, row, col):
        shape = self.playing_area_map[row][col]
        self.coords_for_new_shape[0] = CANVAS_BORDER + (self.width + SHAPE_BORDER) * col
        self.coords_for_new_shape[1] = CANVAS_BORDER + (self.height + SHAPE_BORDER) * row

        shape.move_shape(self.coords_for_new_shape[0], self.coords_for_new_shape[1])

        sleep(DELAY)
        self.parent.update()

    def resize_map(self):
        old_map = self.playing_area_map[:]

        self.playing_area_map = [[None]]
        self.playing_area_row = 0
        self.playing_area_col = 0
        self.playing_area_row_template = 0
        self.playing_area_col_template = 0
        self.template_coords = [SHAPE_BORDER, SHAPE_BORDER]
        self.coords_for_new_shape = [0, 0]

        for row in range(len(old_map)):
            for col in range(len(old_map[row])):
                if old_map[row][col] and old_map[row][col] is not self.template:
                    self.add_new(old_map[row][col])
        self.parent.update()


if __name__ == '__main__':
    p = Tk()
    frame = Frame(p)
    frame.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
    c = Canvas(frame, width=270, height=300, bg="white", relief=SUNKEN)
    c.config(scrollregion=(0, 0, 300, 1000))
    c.config(highlightthickness=0)
    c.pack(expand=YES, fill=BOTH, scrollregion=c.bbox(ALL))
    sc = ShapeCreator(c, Ball, BALL_HEIGHT, BALL_WIDTH)
    sc.create_template()

    r = sc.add_new()
    j = sc.add_new()
    o = sc.add_new()
    a = sc.add_new()

    sc.remove(a)
    a = sc.add_new()
    r = sc.add_new()
    j = sc.add_new()
    sc.remove(a)
    o = sc.add_new()
    a = sc.add_new()

    a = sc.add_new()
    r = sc.add_new()
    j = sc.add_new()

    # sc.remove(r)
    # sc.remove(j)
    # sc.remove(o)

    # sc.add_new()
    # sc.add_new()
    # sc.add_new()
    # j = sc.add_new()
    # sc.add_new()
    # sc.add_new()

    # o = sc.add_new()
    # sc.remove(o)
    # sc.remove(j)
    #
    # c.update()
    c.config(width = 500)
    sc.resize_map()
    p.mainloop()