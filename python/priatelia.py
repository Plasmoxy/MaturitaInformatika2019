s = 0
n = 0

vek = int(input("Zadajte vek priatela (ukonci 0kou): "))
while vek > 0:
    s += vek
    n += 1
    vek = int(input("Zadajte vek priatela (ukonci 0kou): "))

print(f"Priemerny vek priatelov je {s/n}")