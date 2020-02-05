from codecs import open as copen
from operator import itemgetter

f = copen("ziaci.txt", "r", "utf-8")
ziaci = [[int(splitted[0]), splitted[1]] for splitted in [l.strip().split(" ") for l in f.readlines()]]

ziaci = sorted(ziaci, key=itemgetter(0))
print(f"Najstarší: {ziaci[-1]}")

dospeli = list(filter(lambda x: x[0] >= 18, ziaci))
print(f"Dospelí: {dospeli}")

print(f"Vzostupne: {ziaci}")
print(f"Zostupne: {sorted(ziaci, key=itemgetter(0), reverse=True)}")