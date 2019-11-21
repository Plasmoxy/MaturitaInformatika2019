"""
vstup: 2 rovnako dlhe retazce
program vytvori spojeny retazec v ktorom sa striedaju znaky z prveho a druheho
"""

v1 = input("Zajdajte prvy retazec: ")
v2 = input("Zadajkte druhy retazec: ")

def pomiesany_retazec(a, b):
    out = ""
    minl = min(len(a), len(b))

    for i in range(0, minl):
        out += a[i] + b[i]
    
    return out

print(f"pomiesany retazec: {pomiesany_retazec(v1, v2)}")