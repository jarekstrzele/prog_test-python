from tkinter import *

win = Tk()
win.title("drag and drop")
win.geometry("400x400")

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
   
def drag_motion(event):
    widget = event.widget
    print("Widget " , widget)
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

lbl=Label(win, bg="red", width=10, height=5)
lbl.place(x=0, y=0)
lbl.bind("<Button-1>", drag_start)
lbl.bind("<B1-Motion>", drag_motion)

lbl2=Label(win, bg="green", width=10, height=5)
lbl2.place(x=100, y=200)
lbl2.bind("<Button-1>", drag_start)
lbl2.bind("<B1-Motion>", drag_motion)

win.mainloop()



