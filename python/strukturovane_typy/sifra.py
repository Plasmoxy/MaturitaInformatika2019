v = input("text: ")

# funguje aj na desifrovanie
def sifra(s):
    out = ""

    l = len(s)
    parne = l%2==0

    for i in range(0, l if parne else l-1, 2):
        out += s[i+1] + s[i]
    
    if not parne:
        out += s[-1] # pridaj posledny znak ak neparne
    
    return out

print(sifra(sifra(v)))

