"""
Zisti najvacsi spolocny delitel 2 cisel

NSD(a,b)

NSD(132, 56)
132 = 56*2 + 20
56 = 20*2 + 16
20 = 16*1 + 4 // NSD = 4 (posledny nenulovy zvysok)
16 = 4*4 + 0
"""

def NSD(a, b):
    if a < b: # b musi byt mensie
        a, b = b, a

    zv = a % b
    while zv > 0:
        a = b
        b = zv # predposledny zvysok je v bcku
        zv = a % b
    
    return b

if __name__ == "__main__":
    print(NSD(4, 2))