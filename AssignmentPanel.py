from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import Constants
from ShapeSetup import ShapeSetup
from MainElements import *

class AssignmentPanel:
    def __init__(self, parent):
        self.parent = parent
        self.button_panel_top = Frame(self.parent)
        self.button_panel_bottom = Frame(self.parent)
        self.btn_connect = None
        self.btn_show_metadata = None
        self.shape_setup = ShapeSetup()
        self.main_elements = MainElements()

    def create(self):
        self.button_panel_top.configure(background=Constants.BACKGROUND_COLOR)
        self.button_panel_top.pack(side=TOP, fill=X, expand=FALSE, ipady=5)

        self.button_panel_bottom.configure(background=Constants.BACKGROUND_COLOR)
        self.button_panel_bottom.pack(side=TOP, fill=X, expand=FALSE, ipady=5)

        ttk.Separator(self.button_panel_bottom, orient=HORIZONTAL)\
            .pack(side=TOP, fill=X, expand=FALSE, pady=(3, 2), padx=(8, 8))
        ttk.Separator(self.button_panel_bottom, orient=HORIZONTAL)\
            .pack(side=BOTTOM, fill=X, expand=FALSE, pady=(3, 1), padx=(8, 8))

        self.configure_buttons()
        self.set_text()

    def set_text(self):
        ttk.Separator(self.button_panel_top, orient=VERTICAL) \
            .pack(side=LEFT, fill=Y, expand=FALSE, pady=2, padx=4)

        ttk.Separator(self.button_panel_top, orient=VERTICAL) \
            .pack(side=RIGHT, fill=Y, expand=FALSE, pady=2, padx=4)

        self.text = Text(self.button_panel_top, height=3, bg=Constants.BACKGROUND_COLOR, relief = FLAT, cursor="arrow",
                         wrap=WORD, font="Arial 13", fg = '#404040')
        self.text.pack(expand = False, fill=X, pady=(30,10), padx=(80, 80))
        self.text.insert(END, Constants.ASSIGNMENT)
        self.text.config(state=DISABLED)


        # self.text.tag_configure("center", justify='center')
        # self.text.tag_add("center", 1.0, "end")

        # self.text.bind('<Control-x>', lambda e: 'break')  # disable cut
        # self.text.bind('<Control-c>', lambda e: 'break')  # disable copy
        # self.text.bind('<Control-v>', lambda e: 'break')  # disable paste
        # self.text.bind('<Button-3>', lambda e: 'break')  # disable right-click
        self.text.bind('<Button-1>', lambda e: 'break')
        # self.text.bind("<Enter>", self.on_enter)

    # def on_enter(self):

    def configure_buttons(self):

        ttk.Style().configure("TButton", padding=2, relief=SUNKEN, background=Constants.BACKGROUND_COLOR, anchor=CENTER)

        ttk.Separator(self.button_panel_bottom, orient=VERTICAL)\
            .pack(side=LEFT, fill=Y, expand=FALSE, pady=2, padx=4)

        # print(Constants.RUBBER)
        import os.path
        # print(os.path.exists(Constants.RUBBER))
        self.search_string = Entry(self.button_panel_bottom, width=6)
        self.search_string.insert(0, 0)
        self.main_elements.entry_label = self.search_string
        self.search_string.pack(side=LEFT, padx=(20, 5))

        img = ImageTk.PhotoImage(Image.open(Constants.RUBBER))
        self.btn_show_metadata = ttk.Button(self.button_panel_bottom, text="Skontroluj", width=0, compound=CENTER,
                                            command=lambda i=self.main_elements.current_task[0],
                                                           j=self.main_elements.colors:
                                            self.shape_setup.combinations(i, j))
        self.btn_show_metadata.image = img
        self.btn_show_metadata.pack(side=LEFT, padx=5)
        #ToolTip(self.btn_show_metadata, Constants.SHOW_METADATA)

        ttk.Separator(self.button_panel_bottom, orient=VERTICAL)\
            .pack(side=RIGHT, fill=Y, expand=False, pady=2, padx=4)
