
# m = matica 3x3
def determinant3x3(m):
    a = m[0][0]
    b = m[0][1]
    c = m[0][2]
    d = m[1][0]
    e = m[1][1]
    f = m[1][2]
    g = m[2][0]
    h = m[2][1]
    i = m[2][2]

    return a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h

print("Zadajte 3 riadky po 3 číslach oddelených medzerou...")
A = input("Riadok 1: ")
B = input("Riadok 2: ")
C = input("Riadok 3: ")

matica = [
    [int(s) for s in A.split(" ")],
    [int(s) for s in B.split(" ")],
    [int(s) for s in C.split(" ")],
]

print(f"{matica}")

D = determinant3x3(matica)
print(f"D = {D}")


