import tkinter

root = tkinter.Tk()
root.title("Basics")
# https://iconarchive.com/
root.iconbitmap('thinking.ico') #string -> refrence to bitmap
root.geometry('400x400')
root.resizable(0,1) # 1 allow, 0 not allow
root.config(bg='blue')

# second window
top = tkinter.Toplevel()
top.title('Second window')
top.config(bg='#123456')
top.geometry('400x400+500+500') # first +500 x, second+500 y
lbl1 = tkinter.Label(top, text="hello, I am label 1", font=("Cambria", 10), bg="#ff0000", fg='white')
lbl1.pack(padx=10, pady=50)

lbl2 = tkinter.Label(top, text="I am the second label", font=("Robot", 12))
lbl2.pack(pady=(0,10), ipadx=50, ipady=10, anchor='w') # 0 - top, 10 - bottom, ipad - internal padding, ancor - west east

lbl3 = tkinter.Label(top, text="I am the third label", font=('Courier', 12), bg='#ffffff', fg='#123456')
lbl3.pack(fill='x')
# lbl3.pack(fill='y', expend=True)
# lbl3.pack(fill='both', expend=True, padx=10,pady=10)
root.mainloop()

