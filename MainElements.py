import random


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
        self.colors = None
        # self.task_templates = [{'lopta': random.choice(1)},
        #                        {'dom': random.choice(1, 4)},
        #                        {'vlajka': random.choice(1, 3)}]
