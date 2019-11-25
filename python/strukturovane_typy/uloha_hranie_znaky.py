"""
vstup: 2 rovnako dlhe retazce
program vytvori spojeny retazec v ktorom sa striedaju znaky z prveho a druheho
"""

v1 = input("Zajdajte prvy retazec: ")
v2 = input("Zadajkte druhy retazec: ")

def pomiesany_retazec(a, b):
    out = ""
    
    # nech a je kratsi retazec!
    if len(a) > len(b):
        a, b = b, a

    for i in range(0, len(b)):
        out += a[i] if i < len(a) else ""
        out += b[i]
    
    return out

print(f"pomiesany retazec: {pomiesany_retazec(v1, v2)}")