"""
funkcia ktora kresli kruh so sadanymi suradnicami stredu
"""

from tkinter import *

W = 900
H = 300
a = W/H # dy/dx
c = Canvas(width=W, height=H)
c.pack()

kruh = lambda x, y, R: c.create_oval(x-R, y-R, x+R, y+R, fill="red")

r = 5
x = 0
y = 0
dy = ( 4*r**2 / (a**2 + 1) )**0.5
dx = a*dy

while x < W:
    kruh(x, y, r)

    x += dx
    y += dy

c.mainloop()