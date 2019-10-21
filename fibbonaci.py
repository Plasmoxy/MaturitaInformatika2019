"""
a(n+2) = a(n+1) + a(n)
kazde dalsie cislo je suctom dvoch predchadzajucich

uloha = najvacsie fibbonaciho cislo mensie ako 1 000 000
"""

a = 0
b = 1

c = 0

while a+b <= 1000000:
    c = a + b
    a, b = b, c

print(c)
