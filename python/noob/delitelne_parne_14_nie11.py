n = 0

for i in range(11, 101, 11):
    if i%13 != 0 and i%2 == 0:
        print(i)
        n += 1

print(f"n = {n}")