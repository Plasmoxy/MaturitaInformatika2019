from tkinter import *
from collections import *
from random import *

root = Tk()

c = Canvas(root)
c.pack()

state = type("State", (), dict(sx = 0, sy = 0, pressed = False))()

# EVENTY

def b1Pressed(e):
    global state
    state.sx = e.x
    state.sy = e.y
    state.pressed = True
root.bind("<Button-1>", b1Pressed)

def b1Released(e):
    global state
    state.pressed = False
root.bind("<ButtonRelease-1>", b1Released)

def close(e):
    global root
    root.destroy()
root.bind("<Button-3>", close)

# MAIN

def main():
    global state

    if state.pressed :
        c.create_oval(state.sx - 20, state.sy - 20, state.sx + 20, state.sy + 20, fill=choice(["red", "green", "blue", "yellow"]))
    
    root.update()
    root.after(100, main)


root.after(0, main)
root.mainloop()