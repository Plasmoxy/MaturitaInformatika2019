from functools import reduce

n = int(input("Zadajte maximalne cislo: "))
sum = reduce(lambda a,x: a+x, range(1, n+1))

print(f"Suma cisel od 1 po {n} je {sum}")