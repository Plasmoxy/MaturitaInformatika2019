"""
input veta
vypise vetu do riadku
"""

v = input("Veta: ")
l = len(v)

# succ
for z in v:
    print(z, end=" ")
print()

for i in range(l):
    print(v[l-i-1], end="")
print()

