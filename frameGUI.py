import tkinter
from tkinter import BOTH

root= tkinter.Tk()
root.title("Fame")
root.geometry("500x500")

# def frames
pack_frame = tkinter.Frame(root, bg='red')
grid_frame_1 = tkinter.Frame(root, bg='blue')
grid_frame_2 = tkinter.LabelFrame(root, text="Grid sys rules", borderwidth=5)

pack_frame.pack(fill=BOTH, expand=True)
grid_frame_1.pack(fill='x', expand=True)
grid_frame_2.pack(fill=BOTH, expand=True, padx=10, pady=10)

# frame pack 
tkinter.Label(pack_frame, text='text').pack()
tkinter.Label(pack_frame, text='text').pack()
tkinter.Label(pack_frame, text='text').pack()

# frame
# grid 
tkinter.Label(grid_frame_1, text='text').grid(column=0, row=0)
tkinter.Label(grid_frame_1, text='text').grid(column=1, row=1)
tkinter.Label(grid_frame_1, text='text').grid(column=2, row=2)

tkinter.Label(grid_frame_2, text='tfweweweweweweweweweweweweweext').grid(column=0, row=0)




root.mainloop()