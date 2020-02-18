# === Úloha 3===
# Vytvorte program, ktorý bude simulovať semafor. Pri stlačení tlačidla preblikne na ďalší povel v poradí. Na vykresľovanie semafora vytvorte funkciu s vhodným počtom parametrov.

from tkinter import Canvas

canvas = Canvas(width=200, height=400)
canvas.pack() # DOLEZITE

teraz_povel = 0

def vykresli(povel):
    global canvas
    canvas.delete("all") # vymaze canvas CELY

    if povel == 0: # cervena
        canvas.create_oval(20, 20, 60, 60, fill="red")
    elif povel == 1: # priprav sa
        canvas.create_oval(20, 20, 60, 60, fill="red")
        canvas.create_oval(20, 60, 60, 100, fill="orange")
    elif povel == 2: # zelena
        canvas.create_oval(20, 100, 60, 140, fill="green")
    elif povel == 3: # spomal
        canvas.create_oval(20, 60, 60, 100, fill="orange")

def klik(event):
    global teraz_povel # ak chcem menit premennu vo funkcii, musim najprv dat global na zaciatku funkcie
    teraz_povel += 1 # prida 1 ku povelu = zmen na dalsi povel

    if teraz_povel == 4: # povel 4 nemame, tak zmen naspet na 0 (cervena sama)
        teraz_povel = 0
    
    vykresli(teraz_povel) # vykresli ten povel teraz co mame

canvas.bind("<Button-1>", klik) # klik BEZ ZATVORIEK ked davam do canvas.bind

vykresli(teraz_povel) # prvy povel treba vykreslit manualne!!!
canvas.mainloop() # TOTO NEMUSIS PISAT AK POUZIVAS IDLE