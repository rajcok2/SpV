from tkinter import Frame, Canvas, Scrollbar
from tkinter.constants import *

from Shape import Ball


class PlayingAreaPanel(Frame):

    def __init__(self, parent=None, color='red'):
        Frame.__init__(self, parent, bg = color)
        self.canvas = None
        self.parent = parent

    def create(self):
        self.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
        canv = Canvas(self, bg="white", relief=SUNKEN)
        # canv.config(width=300, height=200)
        canv.config(scrollregion=(0,0,300, 1000))
        canv.config(highlightthickness=0) #, scrollregion=canv.bbox(ALL))

        sbar = Scrollbar(self)
        sbar.config(command=canv.yview)
        canv.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        canv.pack(expand=YES, fill=BOTH, scrollregion=canv.bbox(ALL))

        for i in range(10):
            canv.create_text(150, 50+(i*100), text='spam'+str(i), fill='beige')
        canv.bind('<Double-1>', self.onDoubleClick)       # set event handler
        self.canvas = canv
        # self.canvas.bind('<4>', lambda event: self.canvas.xview('scroll', -1, 'units'))
        # self.canvas.bind('<5>', lambda event: self.canvas.xview('scroll', 1, 'units'))

        canv.bind('<MouseWheel>', self.rollWheel)
        # canv.bind('<Button-5>', self.rollWheel)

        self.parent.update()


    def rollWheel(self, event):
        print(self.canvas.winfo_height())
        print(self.canvas.winfo_width())
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def onDoubleClick(self, event):
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        print( event.x, event.y)
        print( self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))

    # def draw(self):
    #     ball = Ball(self.canvas, [20, 500])
    #     ball.create()