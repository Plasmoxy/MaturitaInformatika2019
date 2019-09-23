n = int(input("Pocet riadkov: "))

for r in range(1, n+1):
    print("  "*(n-r) + "* "*(r))

for r in range(0, n):
    print("  "*r + "* "*(n-r))