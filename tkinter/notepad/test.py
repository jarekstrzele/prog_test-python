import tkinter

win=tkinter.Tk()
img = tkinter.PhotoImage(file='new.png')
btn = tkinter.Button(win, image=img)
btn.grid(row=0, column=0, padx=5, pady=5)


win.mainloop()