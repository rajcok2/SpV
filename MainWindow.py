from tkinter import Tk, Frame
from tkinter.constants import *

from MenuPanel import MenuPanel
from ToolsPanel import ToolsPanel
from PlayingAreaPanel import PlayingAreaPanel
from AssignmentPanel import AssignmentPanel
from Constants import *
from ShapeCreator import ShapeCreator
from Shape import *


class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.menu_panel = MenuPanel(self)
        self.assignment_panel = AssignmentPanel(self)
        self.playing_area_panel = PlayingAreaPanel(self)
        self.tools_panel = ToolsPanel(self, 3)
        self.shape_creator = None
        self.shape_setup = ShapeSetup()
        self.playing_area_panel.shape_setup = self.shape_setup

    def create(self):
        self.configure_main_window()

        self.menu_panel.create()
        self.assignment_panel.create()
        self.tools_panel.create()
        self.playing_area_panel.create()
        self.playing_area_panel.shape_setup = self.shape_setup
        # self.playing_area_panel.draw()

        c = self.playing_area_panel.canvas

        self.shape_creator = ShapeCreator(c, Ball, BALL_HEIGHT, BALL_WIDTH)
        self.shape_creator.add_template()
        self.shape_creator.add_new()
        self.shape_creator.shape_setup = self.shape_setup


    def configure_main_window(self):
        self.title(APP_NAME)
        self.configure(background=BACKGROUND_COLOR)
        # self.iconbitmap(default=LOGO)
        self.minsize(width=MIN_WIDTH, height=MIN_HEIGHT)
        self.geometry(INITIAL_SIZE_AND_POSITION)
        # self.state(Constants.INITIAL_STATE)

if __name__ == '__main__':
    mw = MainWindow()
    mw.create()
    mw.mainloop()