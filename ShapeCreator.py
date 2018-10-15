from Shape import *
from Constants import *
from time import sleep

DELAY = 0.2

class ShapeCreator:
    def __init__(self, parent, shape_type, height, width, start_coords=[30, 30]):
        self.parent = parent
        self.template = None
        self.shape_type = shape_type
        self.width = width
        self.height = height
        self.canvas_width = parent.winfo_width()
        self.canvas_height = parent.winfo_height()
        self.new_shape_coords = [0, 0]
        self.scrollbar = ...

        self.playing_area_map = [list()]
        self.playing_area_row = 0
        self.playing_area_col = 0
        self.playing_area_row_template = 0
        self.playing_area_col_template = 1

        self.shape_setup = None

        self.parent.update()

    def add_template(self):
        self.set_shape_coords()
        shape = self.shape_type(self.parent, self.new_shape_coords, self.height, self.width)
        shape.create()
        shape.set_template()
        self.template = shape
        self.playing_area_map[self.playing_area_row].append(self.template)
        sleep(DELAY)
        self.parent.update()

    def move_template(self):

        next_template_space = CANVAS_BORDER + ((self.width + SHAPE_BORDER) * (self.playing_area_col_template + 1))
        if next_template_space > self.parent.winfo_width():
            self.playing_area_map[self.playing_area_row_template].pop()
            # if not self.playing_area_map[self.playing_area_row_template]:
            #     self.playing_area_map.pop()
            # else:
            self.playing_area_map.append(list())
            self.playing_area_row_template += 1
            self.playing_area_col_template = 0
            self.playing_area_map[self.playing_area_row_template].append(self.template)

        x = CANVAS_BORDER + (self.width + SHAPE_BORDER) * (self.playing_area_col_template)
        y = CANVAS_BORDER + (self.height + SHAPE_BORDER) * (self.playing_area_row_template)

        self.template.move_shape(x, y)
        self.playing_area_col_template += 1
        sleep(DELAY)
        self.parent.update()

    def set_shape_coords(self):
        self.check_border()
        self.new_shape_coords[0] = CANVAS_BORDER + (self.width + SHAPE_BORDER) * self.playing_area_col
        self.new_shape_coords[1] = CANVAS_BORDER + (self.height + SHAPE_BORDER) * self.playing_area_row

    def add_new(self):
        # nezabudni vzdy posunut template
        # !!!!!!!!!!!!!!!
        # if self.shape_setup.click()
        # if self.shape_setup.template_clicked:
        #     ...
        self.move_template()
        self.set_shape_coords()
        shape = self.shape_type(self.parent, self.new_shape_coords, self.height, self.width)
        shape.create()

        # self.shape_setup.objects.append(shape)

        # print(self.playing_area_col)
        # self.print_map()
        self.playing_area_map[self.playing_area_row].insert(self.playing_area_col, shape)
        self.playing_area_col += 1

        # self.print_map()
        sleep(DELAY)
        self.parent.update()

        return shape

    def check_border(self):
        next_shape_space = CANVAS_BORDER + ((self.width + SHAPE_BORDER) * (self.playing_area_col + 1))
        if next_shape_space > self.parent.winfo_width():
            self.playing_area_row += 1
            self.playing_area_col = 0
            # self.playing_area_map.append(list())

    def print_map(self):
        pole = []
        for row in range(len(self.playing_area_map)):
            pole.append([])
            for col in range(len(self.playing_area_map[row])):
                if self.playing_area_map[row][col]:
                    pole[row].append(self.playing_area_map[row][col].name)
                else:
                    pole[row].append(None)
        print(pole)

    def remove(self, shape):
        if self.template == shape:
            return

        for row in range(len(self.playing_area_map)):
            print(row)
            if not self.playing_area_map[row]:
                self.playing_area_map.pop()
            for col in range(len(self.playing_area_map[row])):
                if self.playing_area_map[row][col] == shape:
                    self.playing_area_map[row][col] = None
                    self.rearrangement(row, col)
                    shape.delete_shape()
                    self.shape_setup.delete_object()
                    self.parent.update()
                    sleep(DELAY)
                    break

    def rearrangement(self, _row=0, _col=0):
        for row in range(_row, len(self.playing_area_map)):
            if not self.playing_area_map[row]:
                self.playing_area_map.pop()

        for row in range(_row, len(self.playing_area_map)):
            for col in range(_col, len(self.playing_area_map[row])):

                next_col = col + 1
                next_row = row
                if next_col == len(self.playing_area_map[row]):
                    next_col = 0
                    next_row = row + 1
                    _col = 0

                if next_row + 1 == len(self.playing_area_map):
                    self.playing_area_row = row
                    self.playing_area_col = col

                if next_row == len(self.playing_area_map):
                    self.playing_area_row_template = row
                    self.playing_area_col_template = col

                    self.playing_area_map[row].pop()
                    if not self.playing_area_map[row]:
                        self.playing_area_map.pop()
                    break

                self.print_map()
                self.playing_area_map[row][col], self.playing_area_map[next_row][next_col] = \
                    self.playing_area_map[next_row][next_col], self.playing_area_map[row][col]

                self.move(row, col)

    def move(self, row, col):
        shape = self.playing_area_map[row][col]
        self.new_shape_coords[0] = CANVAS_BORDER + (self.width + SHAPE_BORDER) * col
        self.new_shape_coords[1] = CANVAS_BORDER + (self.height + SHAPE_BORDER) * row

        shape.move_shape(self.new_shape_coords[0], self.new_shape_coords[1])
        sleep(DELAY)
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
    sc.add_template()
    rr = sc.add_new() #1
    jj = sc.add_new() #2
    sc.add_new() #3
    sc.add_new() #4
    a = sc.add_new() #5
    # sc.add_new()
    # sc.add_new()
    # sc.add_new()
    sc.print_map()
    print('pred zmazanim')
    sc.remove(a) #5
    sc.remove(rr)
    sc.remove(jj)
    print('zmazany')
    sc.print_map()
    # sc.add_new()
    # sc.print_map()
    # sc.add_new()
    # sc.print_map()
    # sc.add_new()
    # sc.print_map()
    # b = sc.add_new()
    # sc.print_map()
    # # sc.remove(b)
    # sc.print_map()
    c.update()
    p.mainloop()
