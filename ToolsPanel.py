from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.constants import *
import Constants
import random
from MainElements import MainElements


class ToolsPanel(Frame):

    def __init__(self, parent):
        super().__init__(master=parent)
        self.buttons_panel = None
        self.active_button = None
        self.buttons = list()
        self.fc = list()
        self.number_of_colors = None
        self.main_elements = MainElements()

    def create(self):
        self.configure(background=Constants.BACKGROUND_COLOR)
        self.pack(side=RIGHT, fill=BOTH, expand=FALSE)
        self.create_buttons()

    def get_down_frame(self):
        frame = Frame(self.buttons_panel,
                      highlightbackground=Constants.BACKGROUND_COLOR,
                      highlightcolor=Constants.BACKGROUND_COLOR,
                      highlightthickness=2,
                      borderwidth=0,
                      height=40, width=40)
        frame.pack()
        frame.pack_propagate(False)
        return frame

    def generate_colors(self):
        i = 0
        self.number_of_colors = random.choice(self.main_elements.current_task[1])
        while i != self.number_of_colors:
            color = '#' + "%06x" % random.randint(0, 0xFFFFFF)
            if color not in self.fc:
                self.fc.append(color)
                i += 1
        self.main_elements.final_colors = self.fc
        print(self.fc)
        return self.fc

    def create_buttons(self):
        self.buttons_panel = Frame(self, width=80, background=Constants.BACKGROUND_COLOR)
        self.buttons_panel.pack(fill=BOTH, expand=True, padx=30, pady=30)
        self.set_colors()

    def set_button(self, frame, color, img=None):
        btn = Button(frame)
        btn.config(bg=color, relief='flat', bd=0, activebackground='white', image=img)
        if img:
            btn.image = img
        btn.pack(fill=BOTH, expand=True)
        setattr(btn, 'my_color', color)
        setattr(btn, 'is_active', False)
        btn.bind('<Button-1>', lambda e: self.get_color(e))

        return btn

    def set_rubber(self):
        down_frame = self.get_down_frame()
        img = ImageTk.PhotoImage(Image.open(Constants.RUBBER))
        self.set_button(down_frame, 'white', img)

    def set_colors(self):
        colors = self.generate_colors()
        self.main_elements.colors = colors
        self.main_elements.color = colors[0]  #nastavi prvu vygenerovanu farbu
        for color in colors:
            down_frame = self.get_down_frame()
            btn = self.set_button(down_frame, color)
            self.buttons.append(btn)
        self.set_rubber()
        self.active_button = self.buttons[0]
        print(self.active_button)
        self.active_button.is_active = True
        self.active_button.master['highlightbackground'] = Constants.ACTIVE_TOOL_COLOR

    def get_color(self, event):
        btn = event.widget
        print(btn.my_color)
        print(btn)
        self.main_elements.color = btn.my_color
        parent = btn.master
        if not self.active_button == btn:
            print('eeeeeeeeeeeeeeeeeeee')
            print(parent['highlightbackground'])
            parent['highlightbackground'] = Constants.ACTIVE_TOOL_COLOR
            btn.is_active = True
            self.active_button.is_active = False
            self.active_button.master['highlightbackground'] = Constants.BACKGROUND_COLOR
            self.active_button = btn
