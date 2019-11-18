from tkinter import *

c = Canvas()
c.pack()

def b1c(s):
    c.create_oval(s.x-5, s.y-5, s.x+5, s.y+5, fill="red")

c.bind("<Button-1>", b1c)
c.mainloop()