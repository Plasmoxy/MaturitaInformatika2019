from functools import reduce

n = int(input("Cislo: "))
fakt = reduce(lambda a,x: a*x, range(1, n+1))

print(f"faktorial -> {fakt}")