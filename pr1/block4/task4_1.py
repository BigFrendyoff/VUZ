from tkinter import *

root = Tk()
root.geometry('300x300')

canvas = Canvas(bg = "white", width=300, height=300)
canvas.pack(anchor=CENTER, expand=1)

canvas.create_rectangle(50, 50, 250, 250, fill="black")

root.mainloop()