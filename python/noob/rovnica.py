print("ax**2 + bx + c = 0")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - 4*a*c

if D < 0 :
    print("nemá riešenie v R")
elif D == 0 :
    x = -b/2*a
    print(f"x1, x2 = {x:0.3f}")
    print(f"Súčin: (x - {-x:0.3f})(x - {-x:0.3f})")
else : # D > 0
    x1 = (-b + D**0.5)/2*a
    x2 = (-b - D**0.5)/2*a
    print(f"x1 = {x1:0.3f}")
    print(f"x2 = {x2:0.3f}")
    print(f"Súčin: (x - {-x1:0.3f})(x - {-x2:0.3f})")