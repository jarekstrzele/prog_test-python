from tkinter import *

class Main(Tk):
    def __init__(self, size="400x400", title="Nowe puste okno"):
        super().__init__()
        self.geometry(size)
        self.title(title)
    
    def start(self):
        super().mainloop()

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets(master)
 
    def create_widgets(self, master):
        self.lbl=Square(master, bg="red", width=10, height=5, x= 10, y=5)
        self.lbl=Square(master, bg="green", width=10, height=5, x= 10, y=5)

      
class Square(Label):

    def __init__(self, master, bg="red", width=10, height=5, x=0, y=0):
        super().__init__(master, bg=bg, width=width, height=height )
        self.place(x=x, y=y)
        self.bind("<Button-1>", self.drag_start)
        self.bind("<B1-Motion>", self.drag_motion)

    def drag_start(self, event):
        self.startX = event.x
        self.startY = event.y
    
    def drag_motion(self, event):
        x = self.winfo_x() - self.startX + event.x
        y = self.winfo_y() - self.startY + event.y
        self.place(x=x, y=y)



if __name__ == '__main__':
    win = Main(title='drag and drop')
    app = App(win)
     
    win.start()



