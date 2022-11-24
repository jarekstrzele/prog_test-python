import tkinter


class App(tkinter.Tk):
    text_color = "#fffacd"
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
        self.menu = Menu(self, App.menu_color)
        self.menu.pack(padx=5, pady=5)
        #self.text = MyFrame(self, App.text_color)
        self.pack(padx=5, pady=5)


class Menu(tkinter.Frame):
    new_img = tkinter.PhotoImage(image='images/new.png')
    def __init__(self, master, color):
        super().__init__(self, master, color)
        self.img = tkinter.PhotoImage(file=Menu.new_img)
        self.btn = tkinter.Button(self, image=self.img)
        self.btn.grid(row=0, column=0, padx=5, pady=5)

        

    


if __name__ == "__main__":
    app = App()

    app.run()


