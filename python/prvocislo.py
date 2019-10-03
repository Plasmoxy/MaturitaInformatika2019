from math import sqrt, floor

def jePrvocislo(x):
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return x != 1 # default True ale mimo jednotky podla def

n = int(input("Zadajte cislo: "))

for i in range(1, n+1):
    if jePrvocislo(i):
        print(i)