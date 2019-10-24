from tkinter import *
from random import randint

WIDTH = 500
HEIGHT = 500

root = Tk()
c = Canvas(root, width=WIDTH, height=HEIGHT)

for i in range(1, 11):
    a = randint(30, 100)
    x = randint(0, WIDTH-a) # neklipuj mimo obrazovky
    y = randint(0, HEIGHT-a) # neklipuj mimo obrazovky

    c.create_rectangle(x, y, x+a, y+a)
    c.create_text(x + a//2, y + a//2, fill="darkblue", font="Times 10 italic bold", text=f"{i}")

c.pack()
mainloop()
