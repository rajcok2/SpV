from tkinter import *
from ShapeCreator_v2 import *
from Constants import *
from ToolsPanel import *
import random
import itertools
from MainElements import MainElements

objects = []
canvas_in_shapes = None
nastavena_farba = '#2ecc71'

class Template:
    def __init__(self, parent, *args):
        self.parent = parent
        self.shapes = [*args]
        self.name = 'template'
        self.configure_shapes()

    def move_shape(self, x, y):
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        self.parent.coords(self.shapes[0], x, y, x + self.shapes[0].diameter, y + self.shapes[0].diameter)

    def configure_shapes(self):
        for index in range(len(self.shapes)-2):
            self.parent.itemconfig(self.shapes[index], fill='dark gray', outline='dark gray')


class Plus:
    def __init__(self, parent, object_center, length):
        self.parent = parent
        self.object_center = object_center
        self.length = length
        self.horizontal_line = None
        self.vertical_line = None

    def create(self):
        x = self.object_center[0]
        y = self.object_center[1]
        self.horizontal_line = self.parent.create_line(x - self.length / 2,
                                                       y,
                                                       x + self.length / 2,
                                                       y,
                                                       width=2, fill='ghost white')
        self.vertical_line = self.parent.create_line(x,
                                                     y - self.length / 2,
                                                     x,
                                                     y + self.length / 2,
                                                     width=2, fill='ghost white')


class Ball:
    def __init__(self, parent, coords, height, width):
        self.oval = None
        self.parent = parent
        self.coords = coords
        self.height = height
        self.width = width
        self.diameter = width
        self.radius = width / 2
        self.center = [coords[0] + width / 2, coords[1] + width / 2]
        self.ball_color = None
        # self.tag = 'ball' + str(random.randint(1000, 4000))
        self.name = 'ball'
        self.template = None

    def delete_shape(self):
        self.parent.delete(self.oval)
        self.parent.update()

    def create(self):
        x = self.coords[0]
        y = self.coords[1]
        self.oval = self.parent.create_oval(x, y,
                                            x + self.diameter, y + self.diameter,
                                            fill='white', outline='black')
                                            # tags=self.tag)

    def move_shape(self, x, y):
        self.parent.coords(self.oval, x, y, x + self.diameter, y + self.diameter)

    def get_colors(self):
        self.ball_color = self.parent.itemcget(self.oval, 'fill')
        return (self.ball_color,)

    def set_template(self):
        if self.oval:
            plus = Plus(self.parent, self.center, self.radius)
            plus.create()
            self.template = Template(self.parent, self.oval,
                                plus.horizontal_line, plus.vertical_line)
            self.name = 'template'
            self.parent.itemconfig(self.oval, tags='template')
        return self.template


class House:
    def __init__(self, parent, coords, height, width):
        self.parent = parent
        self.house_1 = None
        self.house_2 = None
        self.coords = coords
        self.height = height
        self.width = width
        self.house_1_height = self.height / 3
        self.house_2_height = 2 * self.height / 3
        self.house_1_color = None
        self.house_2_color = None
        self.house_colors = ()
        self.tag = 'house' + str(random.randint(1000, 4000))
        self.center = [coords[0] + width / 2, coords[1] + height / 2]
        print(self.coords[0], coords[1])
        print(self.center)

        self.name = 'house'

    def create(self):
        x = self.coords[0]
        y = self.coords[1]

        self.house_1 = self.parent.create_polygon(x, y + self.house_1_height,
                                                  x + self.width, y + self.house_1_height,
                                                  x + self.width / 2, y,
                                                  fill='white', outline='black')
                                                  # tags=self.tag)

        left_x = self.coords[0] + 10
        right_x = self.coords[0] - 10
        self.house_2 = self.parent.create_polygon(left_x, y + self.house_1_height,
                                                  left_x, y + self.house_2_height,
                                                  right_x + self.width, y + self.house_2_height,
                                                  right_x + self.width, y + self.house_1_height,
                                                  fill='white', outline='black',
                                                  tags=self.tag)

    def move_shape(self, x, y):
        self.parent.coords(self.house_1,
                           x,                   y + self.house_1_height,
                           x + self.width,      y + self.house_1_height,
                           x + self.width / 2,  y)

        left_x = x + 10
        right_x = x - 10
        self.parent.coords(self.house_2,
                           left_x,                  y + self.house_1_height,
                           left_x,                  y + self.house_2_height,
                           right_x + self.width,    y + self.house_2_height,
                           right_x + self.width,    y + self.house_1_height)

    def get_colors(self):
        self.house_1_color = self.parent.itemcget(self.house_1, 'fill')
        self.house_2_color = self.parent.itemcget(self.house_2, 'fill')
        self.house_colors = (self.house_1_color, self.house_2_color)
        return self.house_colors

    def set_template(self):
        template = None
        if self.house_1 and self.house_2:
            plus = Plus(self.parent, self.center, self.width / 3)
            plus.create()
            template = Template(self.parent, self.house_1, self.house_2,
                                plus.horizontal_line, plus.vertical_line)
            self.name = 'template'
            self.parent.itemconfig(self.house_1, tags='template')
            self.parent.itemconfig(self.house_2, tags='template')
        return template

    def delete_shape(self):
        self.parent.delete(self.house_1)
        self.parent.delete(self.house_2)
        self.parent.update()


class Flag:
    def __init__(self, parent, coords, height, width):
        self.parent = parent
        self.flag_1 = None
        self.flag_2 = None
        self.flag_3 = None
        self.coords = coords
        self.height = height
        self.width = width
        self.flag_1_color = None
        self.flag_2_color = None
        self.flag_3_color = None
        self.flag_colors = ()
        self.tag = 'flag' + str(random.randint(1000, 4000))
        self.center = [coords[0] + width / 2, coords[1] + height / 2]

        self.name = 'flag'

    def create(self):
        x = self.coords[0]
        y = self.coords[1]

        flag_height = self.height / 3
        self.flag_1 = self.parent.create_polygon(x, y,
                                                 x, y + flag_height,
                                                 x + self.width, y + flag_height,
                                                 x + self.width, y,
                                                 fill='white', outline='black',
                                                 tags=self.tag)

        y += flag_height
        self.flag_2 = self.parent.create_polygon(x, y,
                                                 x, y + flag_height,
                                                 x + self.width, y + flag_height,
                                                 x + self.width, y,
                                                 fill='white', outline='black',
                                                 tags=self.tag)

        y += flag_height
        self.flag_3 = self.parent.create_polygon(x, y,
                                                 x, y + flag_height,
                                                 x + self.width, y + flag_height,
                                                 x + self.width, y,
                                                 fill='white', outline='black',
                                                 tags=self.tag)

    def move_shape(self, x, y):
        flag_height = self.height / 3
        self.parent.coords(self.flag_1,
                           x, y,
                           x, y + flag_height,
                           x + self.width, y + flag_height,
                           x + self.width, y)
        y += flag_height
        self.parent.coords(self.flag_2,
                           x, y,
                           x, y + flag_height,
                           x + self.width, y + flag_height,
                           x + self.width, y)
        y += flag_height
        self.parent.coords(self.flag_3,
                           x, y,
                           x, y + flag_height,
                           x + self.width, y + flag_height,
                           x + self.width, y)

    def get_colors(self):
        self.flag_1_color = self.parent.itemcget(self.flag_1, 'fill')
        self.flag_2_color = self.parent.itemcget(self.flag_2, 'fill')
        self.flag_3_color = self.parent.itemcget(self.flag_3, 'fill')
        self.flag_colors = (self.flag_1_color, self.flag_2_color,
                                self.flag_3_color)
        return self.flag_colors

    def set_template(self):
        template = None
        if self.flag_1 and self.flag_2 and self.flag_3:
            plus = Plus(self.parent, self.center, self.height / 2)
            plus.create()
            template = Template(self.parent, self.flag_1, self.flag_2, self.flag_3,
                                plus.horizontal_line, plus.vertical_line)
            self.name = 'template'
            self.parent.itemconfig(self.flag_1, tags='template')
            self.parent.itemconfig(self.flag_2, tags='template')
            self.parent.itemconfig(self.flag_3, tags='template')
        return template

    def delete_shape(self):
        self.parent.delete(self.flag_1)
        self.parent.delete(self.flag_2)
        self.parent.delete(self.flag_3)
        self.parent.update()


if __name__ == '__main__':
    p = Tk()
    frame = Frame(p)
    frame.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
    c = Canvas(frame, bg="white", relief=SUNKEN)
    # c.bind("<Button-1>", click)
    # c.bind("<Button-2>", iterate_objects_and_compare)
    # c.bind("<Button-3>", delete_object)
    c.config(scrollregion=(0, 0, 300, 1000))
    c.config(highlightthickness=0)
    c.pack(expand=YES, fill=BOTH, scrollregion=c.bbox(ALL))
    objects = []
    # add_object(House(c, [40, 40], 120, 80))
    # add_object(House(c, [40, 160], 120, 80))
    # add_object(House(c, [140, 40], 120, 80))
    # add_object(House(c, [140, 160], 120, 80))
    # add_object(Ball(c, [140, 40], 50))
    # add_object(Ball(c, [80, 40], 50))
    # add_object(Flag(c, [40, 140], 60, 100))
    # print(combinations(1, ['red', 'blue']))
    # print(combinations(2, ['red', 'blue']))
    # print(combinations(3, ['red', 'blue', 'yellow']))

    # b = Ball(c, [40, 40], 50)
    # b.create()
    # b.template()
    # f = Flag(c, [40, 40], 60, 100)
    # f.create()
    # f.template()
    # h = House(c, [40, 40], 120, 80)
    # h.create()
    # h.template()
    p.mainloop()
