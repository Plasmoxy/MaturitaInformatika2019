a = 7
b = 14

sucin = a*b

print(f"Delitelne {a} a {b}")
for i in range(0, 1001, 1):
    if i%a==0 and i%b==0 :
        print(i)

print(f"Delitelne {sucin}")
for i in range(0, 1001, 1):
    if i%sucin == 0 :
        print(i)