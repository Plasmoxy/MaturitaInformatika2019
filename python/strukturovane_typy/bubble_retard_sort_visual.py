from tkinter import *
from typing import List
from random import randint, sample, randrange
from colorsys import hsv_to_rgb

W = 1000
H = 300
root = Tk()

c = Canvas(root, width=W, height=H, bg="black")
c2 = Canvas(root, width=W, height=H, bg="black")
c.pack()
c2.pack()

# minimum v <a, b>
def minimumpos(l: List[int], a: int, b: int):
    mpoz = a
    for i in range(a, b):
        if l[i] < l[mpoz]:
            mpoz = i
    return mpoz

def draw_list(c: Canvas, l: List[int]):
    global W, H

    lenl = len(l)
    maxl = max(l)
    dx = W/lenl
    dy = H/maxl

    for i in range(0, lenl):
        kolor = "#%02x%02x%02x" % tuple(map(lambda t: int(255*t), hsv_to_rgb((l[i])/(maxl + 50), 1.0, 1.0)))
        c.create_rectangle(i*dx, H, i*dx + dx, H - l[i]*dy, fill=kolor, outline=kolor)

    
# sample zoznam cisel pre sortovaci algoritmus
ls = [randrange(0, 300) for i in range(0, 1000)]
ls_i = 0
ls_last = 0
ls_len = len(ls)
sort_active = True

# sample pre 2. algoritmus
ls2 = ls.copy()
ls2_i = 0


def loop():
    global root, c, c2
    c.delete("all")
    c2.delete("all")

    ####################################################
    # SORT ALG 1 ITER START
    global ls, ls_i, sort_active, ls_last, ls_len
    
    vymeny = 0
    for i in range(1, ls_len-ls_last):
        # ak cislo nalavo je vacsie ako cislo napravo
        if ls[i-1] > ls[i]:
            ls[i], ls[i-1] = ls[i-1], ls[i]
            vymeny += 1
    
    ls_last += 1

    # display
    draw_list(c, ls)
    
    # ukonci ak nebolo nic vymenene
    if vymeny == 0:
        sort_active = False # stop sort

    # SORT ALG 1 ITER END
    ####################################################

    ####################################################
    # SORT ALG 2 ITER START
    global ls2, ls2_i

    if ls2_i < ls_len:
        # najdi najmensie cislo v rozsahu <i, len-1)
        x = minimumpos(ls2, ls2_i, ls_len)

        # trepni ho na zaciatok
        ls2[ls2_i], ls2[x] = ls2[x], ls2[ls2_i]

        # pokracuj dalej
        ls2_i += 1

    draw_list(c2, ls2)

    # SORT ALG 2 ITER END
    ####################################################

    root.update()
    root.after(0, loop)

loop()
root.mainloop()