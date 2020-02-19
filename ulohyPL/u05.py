# === Úloha 5===
# Napíšte program, ktorý zistí pomocou funkcie, v ktorom týždni počas roka mal Janko najvyššie výdavky na sladkosti. Jankove výdavky vygeneruje program ako desatinné čísla v rozsahu (0€-2,55€) s presnosťou na dve desatinné miesta.

from random import randint

priklad_v = [randint(0, 255)/100 for i in range(4*12)] # 4 tyzdne pre kazdy mesiac

def najvyssie(vydavky):
  i_najvisieho = 0

  for i in range(len(vydavky)):
    if vydavky[i] > vydavky[i_najvisieho]:
      i_najvisieho = i
  
  return i_najvisieho + 1

priklad_naj_tyzden= najvyssie(priklad_v)

print(f"vyd = {priklad_v}")
print(f"najvyssi vydavok je v {priklad_naj_tyzden}. tyzdni, teda {priklad_v[priklad_naj_tyzden - 1]}")