import tkinter 

root=tkinter.Tk()
root.title("Btb")
root.geometry('500x500')
root.resizable(0,0)

btn1 = tkinter.Button(root, text="Name")
btn1.grid(row=0, column=0)

btn2 = tkinter.Button(root, text="Time", bg="#00ffff")
btn2.grid(row=0, column=1)


btn3 = tkinter.Button(root, text="Time", bg="#00ffff", activebackground="#ff0000")
btn3.grid(row=0, column=2, padx=10, pady=10, ipadx=15)

btn4 = tkinter.Button(root, text="Day", bg="black", fg="white", borderwidth=5)
btn4.grid(row=1, column=0, columnspan=3, sticky="WE")

root.mainloop();

