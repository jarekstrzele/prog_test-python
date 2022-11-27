import tkinter
from tkinter import scrolledtext

win=tkinter.Tk()
# img = tkinter.PhotoImage(file='new.png')
# btn = tkinter.Button(win, image=img)
# btn.grid(row=0, column=0, padx=5, pady=5)
scroll = scrolledtext.ScrolledText(win)
scroll.config(font="Arial")
scroll.pack()


win.mainloop()