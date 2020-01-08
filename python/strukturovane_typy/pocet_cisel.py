from random import *
from tkinter import *

W = 900
H = 500

root = Tk()
canv = Canvas(root, width=W+100, height=H+100, bg="black")
canv.pack()

# -> 49 cisel
# od 1 po 49, access = [n-1] !!!
frekvencie = [0]*49
pocitadlo = 0

def loop():
    global pocitadlo, frekvencie, canv
    canv.delete("all")

    c = 0

    # alg
    if (pocitadlo < 10000):
        c = int(gauss(24, 4))
        if c in range(0, 48):
            frekvencie[c-1] += 1 # pridaj frekvenciu
        pocitadlo += 1
    
    # kreslenie ...
    for i in range(0, len(frekvencie)):
        
        dx = W/len(frekvencie)
        dy = H/max(frekvencie)
        canv.create_rectangle(i*dx, H, (i+1)*dx, H - frekvencie[i]*dy, outline="black", fill=("red" if c==i else "cyan"))
        canv.create_text(i*dx + dx/2, H+10, text=str(i), fill="white")

        canv.create_oval(i*dx + 0, H+1, i*dx + dx - 1, H+20, outline="purple")

    root.update()
    root.after(1, loop)

    
loop()
root.mainloop()