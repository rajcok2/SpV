from tkinter import Menu
import Constants


class MenuPanel(Menu):

    def __init__(self, parent):
        super().__init__(master=parent)
        parent.configure(menu=self)
        self.file_menu = Menu(self, tearoff=0)

    def create(self):
        self.file_menu.add_command(label=Constants.START)
        self.file_menu.add_separator()
        self.file_menu.add_command(label=Constants.MINIMIZE)
        self.file_menu.add_command(label=Constants.EXIT)

        self.add_cascade(label="Možnosti", menu=self.file_menu, underline=0)
