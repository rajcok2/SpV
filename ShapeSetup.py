import Shape
from ShapeCreator_v3 import ShapeCreator
from MainElements import  MainElements


class ShapeSetup:
    def __init__(self):
        self.canvas = None
        self.template_clicked = False
        self.objects = list()
        self.main_elements = MainElements()
        # self.tools_panel = ToolsPanel(self.main_elements.canvas)
        # self.colors_used = self.tools_panel.generate_colors()
        # self.object_shape = self.main_elements.current_task[0]
        # self.shape_creator = ShapeCreator(self.main_elements.canvas, self.main_elements.shape_type,
        #                                   self.main_elements.canvas.winfo_width(),
        #                                   self.main_elements.canvas.winfo_height())  # shape type nastavime pri citani uloh

    # def add_object(obj):
    #     objects.append(obj)
    #     # obj.create()

    # def iterate_objects_and_compare(ojb_shape):
    #     right_colored = 0
    #     used_options = []
    #     com = combinations(obj_shape, self.main_elements.colors)
    #     for o in objects:
    #         print(o.get_colors())
    #         for i in range(len(com)):
    #             if (o.get_colors() == com[i]) and (com[i] not in used_options):
    #                 right_colored += 1
    #                 used_options.append(com[i])
    #
    #     if len(com) == right_colored and len(com) == len(objects):
    #         print('Trafil si vsetky spravne kombinacie')
    #     else:
    #         print('Netrafil si vsetky spravne kombinacie')

    def click(self, event):
        " po kliknuti na template chceme aby sa pridal novy prazdny objekt a vsetko sa posunulo doprava"
        token, a = self.canvas.itemcget(CURRENT, 'tags').split()
        print(token, a)
        if token.strip() == 'template':
            self.template_clicked = True
            print('klikol si na template')
            print('toto je main_array =====> ', self.main_elements.main_array)
            self.shape_creator.add_new()  # zavola pridanie noveho shapu a posunie template
        elif self.canvas.find_withtag(CURRENT):
            self.canvas.itemconfig(CURRENT, fill=self.main_elements.color)
            self.check_colored_objects()
            # print(c.itemcget(CURRENT, 'fill'))  # => Returns color of object
            # print(c.itemcget(CURRENT, 'tags'))
            # print(c.itemconfigure(CURRENT))

    # def check_colored_objects(self):
    #     #  1.prejde prvky hl.pola a zisti kolko objektov je zafarbenych
    #     #  2.nasledne zvysi/znizi cislo v Entry

    def delete_object(self, event):
        token, a = self.canvas.itemcget(CURRENT, 'tags').split()
        print(token, a)
        if token.strip() == 'template':
            print('chces zmazat template')
        elif token.strip() in self.canvas.gettags(self.canvas.find_withtag(CURRENT)):
            self.canvas.delete(token.strip())
            self.check_colored_objects()

    def combinations(self, object_shape, colors_used):
        if object_shape == 'lopta':
            print('vosiel som do lopty a toto su farby', colors_used)
            p = [p for p in itertools.product(colors_used, repeat=1)]
        elif object_shape == 'dom':
            p = [p for p in itertools.product(colors_used, repeat=2)]
        elif object_shape == 'vlajka':
            p = [p for p in itertools.product(colors_used, repeat=3)]
        else:
            return
        print('toto su vsetky kombinacie: ', len(p), p)
        if len(p) == int(self.main_elements.entry_label.get()):
            print('uhadol si vsetky spravne moznosti')
            #  teraz vsetko vynuluj a nastav dalsiu ulohu
            self.main_elements.current_task_number += 1
            if self.main_elements.current_task_number <= 7:
                self.main_elements.current_task = TASKS[self.main_elements.current_task_number]
                # print(self.main_elements.current_task)
                #  nastav vsetko na novu ulohu
            else:
                #  dokoncil vsetky ulohy
                return
        else:
            print('NE-uhadol si vsetky spravne moznosti')

    def set_binds(self):
        self.canvas.bind("<Button-1>", self.click)
        # self.canvas.bind("<Button-2>", self.iterate_objects_and_compare)
        self.canvas.bind("<Button-3>", self.delete_object)
