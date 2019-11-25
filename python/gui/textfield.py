from tkinter import *


"""
vstup 1 = den.mesiac.roknarodenia
vypis prvych 6 cisel
"""


root = Tk()
f = Frame(root, padx=100, pady=50)

labelText = StringVar()
l = Label(f, font=("Comic Sans MS", 40), fg="red", textvariable=labelText)
l.pack()

entryText = StringVar()
e = Entry(f, textvariable=entryText)
e.pack()



def parsujRodneCislo(tx):

    spl = tx.split(".")
    if len(spl) != 3:
        return ""

    den, mesiac, rok = spl
    
    return (
        rok[-2:] +
        ("0" if int(mesiac) < 10 else "") + mesiac +
        ("0" if int(den) < 10 else "") + den
    )

def entryTextOnChange(*args):
    global labelText, entryText
    result = parsujRodneCislo(entryText.get())

    labelText.set(result if result != "" else "CHYBA")
    
entryText.trace("w", entryTextOnChange)

f.pack()
root.mainloop()