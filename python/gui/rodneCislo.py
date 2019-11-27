from tkinter import *


"""
vstup 1 = den.mesiac.roknarodenia
vypis prvych 6 cisel
"""


root = Tk()
root.title("Kalkulacka rodneho cisla")
f = Frame(root, padx=60, pady=50)

l = Text(f, height=1, width="12", borderwidth=0, font=("Comic Sans MS", 20), fg="red")
l.pack()

Label(f, text="Zadaj datum narodenia: ").pack()

entryText = StringVar()
e = Entry(f, textvariable=entryText)
e.pack()



def parsujRodneCislo(tx):

    spl = tx.split(".")
    if len(spl) != 3:
        return ""

    print(spl)

    # i       i    s
    den, mesiac, rok = spl
    den, mesiac = int(den), int(mesiac)
    
    return (
        rok[-2:] +
        ("0" if mesiac < 10 else "") + str(mesiac) +
        ("0" if den < 10 else "") + str(den)
    )

def entryTextOnChange(*args):
    global entryText, l
    result = parsujRodneCislo(entryText.get())

    l.config(state=NORMAL)
    l.delete(1.0, END)
    l.insert(END, result if result != "" else "Zlý formát.")
    l.config(state=DISABLED)
    
entryText.trace("w", entryTextOnChange)

f.pack()
root.mainloop()