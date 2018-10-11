from tkinter import Tk, Frame
from tkinter.constants import *

from MenuPanel import MenuPanel
from ToolsPanel import ToolsPanel
from PlayingAreaPanel import PlayingAreaPanel
from AssignmentPanel import AssignmentPanel
import Constants


class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.menu_panel = MenuPanel(self)
        self.assignment_panel = AssignmentPanel(self)
        self.playing_area_panel = PlayingAreaPanel(self)
        self.tools_panel = ToolsPanel(self, 3)

    def create(self):
        self.configure_main_window()

        self.menu_panel.create()
        self.assignment_panel.create()
        self.tools_panel.create()
        self.playing_area_panel.create()
        self.playing_area_panel.draw()


    def configure_main_window(self):
        self.title(Constants.APP_NAME)
        self.configure(background=Constants.BACKGROUND_COLOR)
        self.iconbitmap(default=Constants.LOGO)
        self.minsize(width=Constants.MIN_WIDTH, height=Constants.MIN_HEIGHT)
        self.geometry(Constants.INITIAL_SIZE_AND_POSITION)
        # self.state(Constants.INITIAL_STATE)

if __name__ == '__main__':
    mw = MainWindow()
    mw.create()
    mw.mainloop()