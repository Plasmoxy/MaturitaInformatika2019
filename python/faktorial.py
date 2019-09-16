from functools import reduce

n = int(input("Cislo: "))
fakt = reduce(lambda a,x: a*x, range(1, n+1))
neparnesucet = reduce(lambda a,x: a+x, range(1, n+1, 2))

print(f"faktorial -> {fakt}")
print(f"sucet neparnych -> {neparnesucet}")