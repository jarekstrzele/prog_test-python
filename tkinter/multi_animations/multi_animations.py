import time
from tkinter import *
from ball import Ball

WIDTH = 500
HEIGHT = 500

win=Tk()

canvas= Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball= Ball(canvas, 0,0,100,1,4,"white")
tennis_ball= Ball(canvas, 0,0,50,4,3,"green")
basket_ball= Ball(canvas, 0,0,23,2,4,"red")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    win.update()
    time.sleep(0.01)




win.mainloop()