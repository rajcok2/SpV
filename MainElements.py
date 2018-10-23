from Constants import *

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MainElements(metaclass=Singleton):
    def __init__(self, main_window=None):
        self.main_window = main_window
        self.menu_panel = None
        self.color = None
        self.colors = []
        self.main_array = []
        self.canvas = None
        self.shape_type = None
        self.final_colors = []
        self.entry_label = None
        self.current_task_number = 0
        self.current_task = TASKS[self.current_task_number]
