
from random import randint

heslo = ""

for i in range(0, 8):
    heslo += chr(randint(ord("a"), ord("z")))

print(heslo)