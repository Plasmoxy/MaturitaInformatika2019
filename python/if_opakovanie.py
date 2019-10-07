b = int(input("Zadajte číslo: "))
s = 0

print("Delitele čísla b: ")
for i in range(1, int(b**0.5)+2):
    if b % i == 0:
        print(f"{i}", end=" ")
        s += i
s += b
print(b)

print(f"Súčet deliteľov = {s}")