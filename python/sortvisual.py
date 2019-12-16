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

    
ls = sample(range(0, 200), 200)
ls_i = 0
ls_len = len(ls)

def loop():
    global root, c, ls
    c.delete("all")

    # SORT ALG ITER START
    global ls_i

    if ls_i < ls_len:
        # najdi najmensie cislo v rozsahu <i, len-1)
        x = minimumpos(ls, ls_i, ls_len)

        # trepni ho na zaciatok
        ls[ls_i], ls[x] = ls[x], ls[ls_i]

        # VISUALIZE
        draw_list(ls)
        ls_i += 1
    else:
        draw_list(ls)

    # SORT ALG ITER END

    root.update()
    root.after(1, loop)

loop()
root.mainloop()