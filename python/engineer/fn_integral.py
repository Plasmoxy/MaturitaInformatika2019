# vypocet integralu pomocou obdlznikovej metody
# ZADANIE: výpočet obsahu polochy pod grafom nejakej funkcie na intervale <x1, x2>
from math import pi

def integral(f, a, b, n):
    S = 0

    dx = (b - a)/n
    x = a

    while x <= b:
        S += f(x)*dx # cast integralu
        x += dx

    return S

f = lambda x: x
print(integral(f, 0, 5, 1000000))