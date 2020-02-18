"""
Stale menim dva medzi sebou nasledujuce.
Cisla bublaju na koniec.
Ak uz nebude ziadna vymena = koniec = sorted.
Posledny uz nema kontrolovat potom neskor.
"""

from random import sample, randint
from typing import *
from time import time

def bublo_srot(l: List[int]) -> List[int]:
    ll = len(l)
    iter_counter = 0 # porovnania
    last = 0 # ak posledny je uz zosortovany, nechaj tak

    while True:
        
        vymeny = 0
        for i in range(1, ll-last):
            iter_counter += 1
            # ak cislo nalavo je vacsie ako cislo napravo
            if l[i-1] > l[i]:
                l[i], l[i-1] = l[i-1], l[i]
                vymeny += 1
            
        # ak dana hodnota uz dobublala (sme na konci), limituj dlzku aby sme uz neoverovali posledny prvok
        last += 1

        #print(f"bubble sort l = {l}, hranica ukonceneho sortovania(ll-last) = {ll-last}")
        
        # ukonci ak nebolo nic vymenene
        if vymeny == 0:
            #print(f"[Prebehlo {iter_counter} iteracii (vymen).]")
            break
    
    return l

lcisla = [randint(0, 10000) for i in range(0, 10000)]
#print(f"Cisla = {lcisla}, len={len(lcisla)}")

pred = time()
sorted = bublo_srot(lcisla)
potom = time()

#print(f"Sorted = {sorted}")
print(f"Cas trvania: {potom-pred}")