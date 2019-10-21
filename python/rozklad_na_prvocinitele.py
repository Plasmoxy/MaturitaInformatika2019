"""
prvociselny rozklad -> delime prvocislami kym sa da


56 | 2
28 | 2
14 | 2
7  | nie 2, nie 3, nie 5, áno 7
1  -> koniec

56 = 2**3 * 7
neviem, kolkokrat sa bude opakovat tak pouzijem while

mozem iba pripocitavat cislo ku delitelovi = lebo predchadzajuce prvocinitele
toho delitela sa uz vydelili (vyhodili prec)
= Eratostenovo sito (vyhodia sa nasobky toho cisla a tym padom mam prvocisla)
vyhodim 2, 2 -> 4kou urcite to dalsie uz nebude delitelne lebo som vyhodil vsetky dvojky

"""

x = int(input("Zadajte x, ja rozdelim na prvocisla: "))
d = 2 # prve prvocislo
zv = 0
podiel = 0

print(f"{x} = ", end="") # na zaciatok

while x > 1:
    if x % d == 0:
        if x // d == 1:
            print(d)
        else:
            print(d, end=" * ")
        x //= d
    else:
        d += 1
