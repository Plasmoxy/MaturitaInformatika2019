"""
zistite sqrt(x) bez volania funkcie sqrt / **
"""


x = int(input("Zadaj x: "))

# jednoduchy algoritmus ...

def jednoduchy(x, a=0):
    while a**2 < x:
        a = a + 0.01

    print(f"Odmocnina z {x} je {a}")


# algoritmus polenim intervalu

def polenim(x, presnost=3):
    a = 0
    b = float(x)
    s = 0
    
    while abs(x-a**2) >= 0.1**presnost:
        s = (a+b)/2.0 # stred intervalu

        if s**2 > x: # vacsie
            b = s
        elif s**2 < x: # rovne
            a = s
    
    return round(s, presnost)

presnost = 3
p = polenim(x, presnost)
print(f"Polenim odmocnina z {x} presna na {presnost} desatinnych miest je {p} a rozdiel od sqrt je {x**0.5 - p}")
