import tkinter, random

def main():
    Program()
    tkinter.mainloop()
    
class House:
    ...

class Circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.id = None
        self.typ = 'kruh'

    def is_clicked(self,x,y):
        return (self.x-x)**2+(self.y-y)**2 < self.r**2

    def draw(self,g):
        self.g = g
        self.id = g.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r)

    def change_color(self, color):
        self.color = color
        self.g.itemconfig(self.id,fill=self.color)
    
class Flag:
    ...

class AddNewObject:
    ...

class Program:
    def __init__(self):
        self.g = tkinter.Canvas(bg='white',width=800,height=600)
        self.g.pack()
        self.objects = []
        self.add_object(Circle(100, 50, 30))

    def who(self,e):
        ix = len(self.objects)-1
        while ix >= 0 and not self.objects[ix].is_clicked(e.x,e.y):
            ix -= 1
        if ix < 0:
            return
        else:
            return self.objects[ix]

    def add_object(self,obj):
        self.objects.append(obj)
        obj.draw(self.g)


