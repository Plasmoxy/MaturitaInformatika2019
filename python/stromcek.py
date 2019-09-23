n = int(input("pocet riadkov: "))

for r in range(1, n+1):
    # r -> pocet hviezdiciek v riadku
    print( " "*(n-r) + "* "*r)