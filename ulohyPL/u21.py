# === Úloha 21===
# Napíšte program, ktorý po stlačení tlačidla vykreslí terč pozostávajúci z 10 sústredných kružníc náhodnej farby. Na vykresľovanie terča vytvorte procedúru, ktorej  parametre budú určovať pozíciu terča.

from tkinter import Canvas
from random import choice

c = Canvas(width=600, height=600)
c.pack()

def terc(x, y):
  global c
  for i in range(11, 1, -1):
    c.create_oval(x - i*10, y - i*10, x + i*10, y + i*10, fill=choice(["red", "green", "blue", "yellow", "black", "magenta"]))

terc(300, 300)

c.mainloop()
