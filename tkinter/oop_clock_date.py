from tkinter import *
from time import *


class App(Tk):

    def __init__(self):
        super().__init__()

    def run(self):
        self.mainloop()
    
    def create_widgets(self):
        self.time=MyTime(self)
        self.time.pack()

        self.day=MyDay(self)
        self.day.pack(fill=BOTH)

        self.date=MyDate(self)
        self.date.pack(fill=BOTH)

    def update(self):
        time_str=strftime("%I:%M:%S %p")
        self.time.config(text=time_str)
    
        day_str=strftime("%A")
        self.day.config(text=day_str)

        date_str=strftime("%B %d, %Y")
        self.date.config(text=date_str)

        # time_lbl.after(1000, update)
        self.after(1000, self.update)



class MyTime(Label):
    def __init__(self, master):
        super().__init__(master)
        self.config(font=("Symbol", 50), fg="#FFE381", bg="#1C448E")
        

class MyDay(Label):
    def __init__(self, master):
        super().__init__(master)
        self.config(font=("Cambira", 25),bg="#DBFE87", fg="#6F8695")

class MyDate(Label):
    def __init__(self, master):
        super().__init__(master)
        self.config(font=("Cambira", 15),bg="#FFE381", fg="#6F8695")
        
  
if __name__ == "__main__":
    app=App()
    app.create_widgets()
    app.update()
    app.run()