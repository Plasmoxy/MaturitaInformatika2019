import math

# n = int(input("Zadajte sirku tabulky: "))
"""
real    0m2.973s
user    0m2.625s
sys     0m0.141s
"""
n = 1000

""""
for y in range(1, n+1):
    for x in range(1, n+1):
        s = x*y
        print(s, end=(5-len(str(s))) * " ")
    print()
"""

def pocet_cifier(x):
    return math.floor(math.log10(x)) + 1

dlzka = pocet_cifier(n**2) + 1

for y in range(1, n+1):
    for x in range(1, n+1):
        print(f"{x*y:{dlzka}}", end="")
    print()