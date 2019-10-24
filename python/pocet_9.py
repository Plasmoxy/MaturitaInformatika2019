
x = int(input("Zadajte prir. c. : "))
c = 0

while x > 1:
    if x % 10 == 9:
        c += 1
    x //= 10

print(f"Pocet cislic 9 v cisle je {c}")