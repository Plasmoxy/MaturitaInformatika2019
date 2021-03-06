from tkinter import *
from typing import List
from random import randint, sample

W = 800
H = 500
root = Tk()

c = Canvas(root, width=W, height=H, bg="black")
c.pack()

# minimum v <a, b>
def minimumpos(l, a, b):
    mpoz = a
    for i in range(a, b):
        if l[i] < l[mpoz]:
            mpoz = i
    return mpoz

def draw_list(l: List[int]):
    global c, W, H

    lenl = len(l)
    maxl = max(l)
    dx = W/lenl
    dy = H/maxl

    for i in range(0, lenl):
        c.create_rectangle(i*dx, H, i*dx + dx, H - l[i]*dy, fill="cyan", outline="cyan")

    
# sample zoznam cisel pre sortovaci algoritmus
ls = sample(range(0, 200), 200)
ls_i = 0
ls_len = len(ls)

def loop():
    global root, c, ls, ls_i
    c.delete("all")

    # SORT ALG ITER START
    
    

    # SORT ALG ITER END

    root.update()
    root.after(0, loop)

loop()
root.mainloop()