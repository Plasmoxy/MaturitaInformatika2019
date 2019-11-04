# U 26/12

from random import *
from tkinter import *


W = 1920
H = 1080
c = Canvas(bg="black", width=W, height=H)
c.pack()

r = lambda: randint(0,255)
cl = lambda: '#%02X%02X%02X' % (r(),r(),r())

x = 20
y = 20

for i in range(0, 10000):
    
    x += 3
    y += 3

    # (+, const) -> (const, +)
    c.create_line(x, 20, 520, y, fill=cl(), width=2)
    c.create_line(520, y, 520-x, 520, fill=cl(), width=2)
    c.create_line(520-x, 520, 20, 520-y, fill=cl(), width=2)
    c.create_line(20, 520-y, x, 20, fill=cl(), width=2)


    c.update()
    c.after(30)

mainloop()