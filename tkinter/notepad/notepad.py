import tkinter
from tkinter import StringVar, IntVar, scrolledtext


class App(tkinter.Tk):
   
    menu_color = "#bdb9db"
    root_color = "#6c809a"
      
    def __init__(self, title="Notepad", icon="images/pad.ico", size="600x600", shape=(0,0)):
        super().__init__()
        self.title(title)
        self.iconbitmap(icon)
        self.geometry(size)
        self.resizable(*shape)
        self.config(bg=App.root_color)
       
    def run(self):
        self.mainloop()

    def create_wigets(self):
        self.notebook=Notebook(self)
        self.menu = Menu(self, notebook=self.notebook)
        self.notebook.config(font=("Arial", 32, "normal"))
        # print(id(self.notebook))
        # self.notes.config(font=self.menu.fonts_types.chosen_font.get())
        # self.notebook.font=(self.menu.fonts_types.change_font,
        #                  self.menu.sizes_types.chosen_size.get())
       
        self.menu.pack(padx=5, pady=5)
        self.notebook.pack()
       

class Menu(tkinter.Frame):
    families=['Terminal', 'Modern', 'Lato', 'Roboto', 'Noto', 'Alef', 'Carlito', 'Arial', 'Calibri', 'Impact']
    sizes=[8,10,12,14,16,20,24,32,48,64,72,96]
    formats=['normal', 'bold', 'italic']

    def __init__(self, master, notebook):
        super().__init__(master)
        self.notebook = notebook
        # self.new_img = tkinter.PhotoImage(file='images/new.png')
        # self.new_btn = tkinter.Button(self, image=self.new_img)
        # self.new_btn.grid(row=0, column=0, padx=5, pady=5)

        # self.open_img = tkinter.PhotoImage(file='images/open.png')
        # self.open_btn = tkinter.Button(self, image=self.open_img)
        # self.open_btn.grid(row=0, column=1, padx=5, pady=5)

        # self.save_img = tkinter.PhotoImage(file='images/save.png')
        # self.save_btn = tkinter.Button(self, image=self.save_img)
        # self.save_btn.grid(row=0, column=2, padx=5, pady=5)

        # self.close_img = tkinter.PhotoImage(file='images/close.png')
        # self.close_btn = tkinter.Button(self, image=self.close_img)
        # self.close_btn.grid(row=0, column=3, padx=5, pady=5)

        self.new=MenuWidgets(self, 'images/new.png')
        self.open=MenuWidgets(self, 'images/open.png', column=1)
        self.save=MenuWidgets(self, 'images/save.png', column=2)
        self.close=MenuWidgets(self, 'images/close.png', column=3)
        self.close.btn.config(command=quit)
        
        self.chosen_font=StringVar()
        self.chosen_font.set('Robot')
        self.font_types=tkinter.OptionMenu(self, self.chosen_font, *Menu.families, command=self.change_font)
        self.font_types.grid(row=0, column=4)
        
        self.chosen_size=IntVar()
        self.chosen_size.set(32)
        self.size_types=tkinter.OptionMenu(self, self.chosen_size, *Menu.sizes,  command=self.change_font)
        self.size_types.grid(row=0, column=5)

        self.chosen_format=StringVar()
        self.chosen_format.set('normal')
        self.format_types=tkinter.OptionMenu(self, self.chosen_format, *Menu.formats, command=self.change_font)
        self.format_types.grid(row=0, column=6)


    def change_font(self,event):
        self.notebook.config(font=(self.chosen_font.get(),
                                   self.chosen_size.get(), 
                                   self.chosen_format.get()))

class MenuWidgets(tkinter.Button):

    def __init__(self, master, image_path, row=0, column=0, padx=5, pady=5):
        super().__init__(master)
        self.img=tkinter.PhotoImage(file=image_path)
        self.btn=tkinter.Button(master, image=self.img) 
        self.btn.grid(row=row,column=column, padx=padx, pady=pady)  
      
class Notebook(tkinter.scrolledtext.ScrolledText):
    text_color = "#fffacd"
    
    def __init__(self, master):
        super().__init__(master, bg=Notebook.text_color, width=400, height=200)

    
         
        

        
       



    


if __name__ == "__main__":
    app = App()
    app.create_wigets()
    app.run()


