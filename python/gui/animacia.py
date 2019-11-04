from tkinter import *

c = Canvas(bg="black", width=1000, height=500)
c.pack()

x = 0
y = 0

c.pack()

active = True
while active:
    c.delete("all")
    c.create_oval(x, y, x+10,y+10, fill="red")
    x += 1
    y += 1

    c.update()
    c.after(16)