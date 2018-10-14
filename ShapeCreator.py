from Shape import *
from Constants import *


class ShapeCreator:
    def __init__(self, parent, shape_type, height, width, start_coords=[30, 30]):
        # self.last_shape_in_row_id = 0
        # self.rows_count = 0
        # self.all_shapes = dict()
        self.parent = parent
        self.template = None
        self.shape_type = shape_type
        # self.start_coords = start_coords
        # self.x_space_between_shapes = start_coords[0]
        # self.y_space_between_shapes = start_coords[1]
        self.width = width
        self.height = height
        self.canvas_width = parent.winfo_width()
        self.canvas_height = parent.winfo_height()
        self.new_shape_coords = [0, 0]
        self.scrollbar = ...

        self.playing_area_map = [list()]
        self.playing_area_row = 0
        self.playing_area_col = 0

        self.parent.update()

    def add_template(self):
        shape = self.shape_type()
        shape.create()
        self.template = shape.template()
        self.parent.itemconfig(self.template, )

    def move_template(self):
        ...

    def add_new(self):
        # nezabudni vzdy posunut template
        # !!!!!!!!!!!!!!!
        self.check_border()
        self.new_shape_coords[0] = CANVAS_BORDER + (self.width + SHAPE_BORDER) * self.playing_area_col
        self.new_shape_coords[1] = CANVAS_BORDER + (self.height + SHAPE_BORDER) * self.playing_area_row

        shape = self.shape_type(self.parent, self.new_shape_coords, self.height, self.width)
        shape.create()
        self.playing_area_col += 1
        self.playing_area_map[self.playing_area_row].append(shape)

        return shape

    def check_border(self):
        next_shape_space = CANVAS_BORDER + ((self.width + SHAPE_BORDER) * (self.playing_area_col + 1))
        if next_shape_space > self.parent.winfo_width():
            self.playing_area_row += 1
            self.playing_area_col = 0
            self.playing_area_map.append(list())

    def print_map(self):
        for row in self.playing_area_map:
            print(row)

    def remove(self, shape):
        if self.template == shape:
            return
        for row in range(len(self.playing_area_map)):
            for col in range(len(self.playing_area_map[row])):
                if self.playing_area_map[row][col] == shape:
                    self.playing_area_map[row][col] = None
                    self.rearrangement(row, col)

    def rearrangement(self, _row=0, _col=0):
        for row in range(_row, len(self.playing_area_map)):
            for col in range(_col, len(self.playing_area_map[row])):
                next_col = col + 1
                next_row = row
                if next_col == len(self.playing_area_map[row]):
                    next_col = 0
                    next_row = row + 1
                    _col = 0
                if next_row == len(self.playing_area_map):
                    self.playing_area_row = row
                    self.playing_area_col = col
                    self.playing_area_map[row].pop()
                    break

                self.playing_area_map[row][col], self.playing_area_map[next_row][next_col] = \
                    self.playing_area_map[next_row][next_col], self.playing_area_map[row][col]

                self.set_shape_positions(row, col)

    def set_shape_positions(self, row, col):
        shape = self.playing_area_map[row][col]
        self.new_shape_coords[0] = CANVAS_BORDER + (self.width + SHAPE_BORDER) * col
        self.new_shape_coords[1] = CANVAS_BORDER + (self.height + SHAPE_BORDER) * row

        shape.move(self.new_shape_coords[0], self.new_shape_coords[1])
        self.parent.sleep(200)
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
    sc.add_new()
    sc.add_new()
    sc.add_new()
    sc.add_new()
    a = sc.add_new()
    sc.add_new()
    sc.add_new()
    sc.add_new()
    sc.print_map()
    sc.remove(a)
    sc.print_map()
    sc.add_new()
    sc.print_map()
    sc.add_new()
    sc.print_map()
    sc.add_new()
    sc.print_map()
    b = sc.add_new()
    sc.print_map()
    sc.remove(b)
    sc.print_map()
    c.update()
    p.mainloop()
