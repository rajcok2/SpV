from tkinter import *


class Template:
    def __init__(self, parent, *args):
        self.parent = parent
        self.shapes = [*args]
        self.configure_shapes()

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
    def __init__(self, parent, coords, diameter):
        self.oval = None
        self.parent = parent
        self.coords = coords
        self.diameter = diameter
        self.radius = diameter / 2
        self.center = [coords[0] + diameter / 2, coords[1] + diameter / 2]

    def create(self):
        x = self.coords[0]
        y = self.coords[1]
        self.oval = self.parent.create_oval(x, y,
                                            x + self.diameter, y + self.diameter)

    def template(self):
        template = None
        if self.oval:
            plus = Plus(self.parent, self.center, self.radius)
            plus.create()
            template = Template(self.parent, self.oval,
                                plus.horizontal_line, plus.vertical_line)
        return template


class House:
    def __init__(self, parent, coords, height, width):
        self.parent = parent
        self.house_1 = None
        self.house_2 = None
        self.coords = coords
        self.height = height
        self.width = width
        self.center = [coords[0] + width / 2, coords[1] + height / 2]
        print(self.coords[0], coords[1])
        print(self.center)

    def create(self):
        x = self.coords[0]
        y = self.coords[1]
        house_1_height = self.height / 3
        self.house_1 = self.parent.create_polygon(x, y + house_1_height,
                                                  x + self.width, y + house_1_height,
                                                  x + self.width / 2, y,
                                                  fill='white', outline='black')

        house_2_height = 2 * self.height / 3
        left_x = self.coords[0] + 10
        right_x = self.coords[0] - 10
        self.house_2 = self.parent.create_polygon(left_x, y + house_1_height,
                                                  left_x, y + house_2_height,
                                                  right_x + self.width, y + house_2_height,
                                                  right_x + self.width, y + house_1_height,
                                                  fill='white', outline='black')

    def template(self):
        template = None
        if self.house_1 and self.house_2:
            plus = Plus(self.parent, self.center, self.width / 3)
            plus.create()
            template = Template(self.parent, self.house_1, self.house_2,
                                plus.horizontal_line, plus.vertical_line)
        return template


class Flag:
    def __init__(self, parent, coords, height, width):
        self.parent = parent
        self.flag_1 = None
        self.flag_2 = None
        self.flag_3 = None
        self.coords = coords
        self.height = height
        self.width = width
        self.center = [coords[0] + width / 2, coords[1] + height / 2]

    def create(self):
        x = self.coords[0]
        y = self.coords[1]

        flag_height = self.height / 3
        self.flag_1 = self.parent.create_polygon(x, y,
                                                 x, y + flag_height,
                                                 x + self.width, y + flag_height,
                                                 x + self.width, y,
                                                 fill='white', outline='black')

        y += flag_height
        self.flag_2 = self.parent.create_polygon(x, y,
                                                 x, y + flag_height,
                                                 x + self.width, y + flag_height,
                                                 x + self.width, y,
                                                 fill='white', outline='black')

        y += flag_height
        self.flag_3 = self.parent.create_polygon(x, y,
                                                 x, y + flag_height,
                                                 x + self.width, y + flag_height,
                                                 x + self.width, y,
                                                 fill='white', outline='black')

    def template(self):
        template = None
        if self.flag_1 and self.flag_2 and self.flag_3:
            plus = Plus(self.parent, self.center, self.height / 2)
            plus.create()
            template = Template(self.parent, self.flag_1, self.flag_2, self.flag_3,
                                plus.horizontal_line, plus.vertical_line)
        return template


if __name__ == '__main__':
    p = Tk()
    frame = Frame(p)
    frame.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
    c = Canvas(frame, bg="white", relief=SUNKEN)
    c.config(scrollregion=(0, 0, 300, 1000))
    c.config(highlightthickness=0)
    c.pack(expand=YES, fill=BOTH, scrollregion=c.bbox(ALL))
    # b = Ball(c, [40, 40], 50)
    # b.create()
    # b.template()
    # f = Flag(c, [40, 40], 60, 100)
    # f.create()
    # f.template()
    h = House(c, [40, 40], 120, 80)
    h.create()
    # h.template()
    p.mainloop()
