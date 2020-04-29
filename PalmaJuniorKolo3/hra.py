from random import choice

"""

 0(n+1)   1  2  3     
[štart]   [] [] [] ... [] [n]

"""

class Hrac:
  p = -1 # pozicia, -1 = domcek
  i = 0 # vnutorny index hodu hraca nezavisly od kola
  def __init__(self, hody):
    self.hody = hody # int array hodov
    
  def __str__(self):
    return f"Hrac[p={self.p} i={self.i}]"

# n = pocet policok BEZ domcekov, VRATANE startovacieho policka
# hody -> zoznam zoznamov hodov hracov (int[][])
def korytnacky_sa_nehnevaju(n_policok, hody_jednotlivych_hracov):
  
  # helper funkcia
  # return True ak moze dalsie kolo ist, mutuje iba array hracov pure, ak nemoze pokracovat dalsim kolom (dosli nam hody) => False
  def kolo(hraci):
    # pre kazdeho hraca
    for ihraca in range(0, len(hraci)):
      h = hraci[ihraca] # zober hraca
      
      # ak ma nastaveny tracking index na neexitujuci hod,
      # znamena to ze mu uz dosli hody a tak ukoncime hru
      # (nedovolime dalsie kolo) (out of range)
      if h.i > len(h.hody) - 1:
        print(f"Ukoncujem hru, hrac {ihraca} uz nemal hody.")
        return False
      
      # ak je v domceku
      if h.p == -1:
        if h.hody[h.i] == 6:
          h.p = 0 # vyslobod
      # ak uz je na doske
      else:
        # POZNAMKA: ak moze dostat iba 1 reset hodu zo šestky, tak iba staci zmenit while na if
        
        dp = 0 # zmena hodu <local>
        
        # ak hodil 6 a mame este nejaky hod ZA TOU SESTKOU (nit posledny index), pripocitavaj mu vsetky postupné 6 a preskoc ich (resetuj mu hody)
        
        while h.hody[h.i] == 6 and h.i != len(h.hody) - 1:
          print(f"Hrac {ihraca} hadzal znova!")
          dp += 6
          h.i += 1
          
        dp += h.hody[h.i] # pridaj mu hod podla current indexu
        
        # predpokladana pozicia hraca po hode
        # ak p == n, tak p = 0 (mame cyklicku dosku)
        predpoklad_p = (h.p + dp) % n_policok 
        
        # checknem ci v tomto kole predpokladana pos. nebude kolidovat s inym hracom
        kolizia = False
        for hrac in hraci:
          # ak to neje toten isty hrac (objekt)
          # a zaroven kolidujeme
          if hrac != h and hrac.p == predpoklad_p:
            kolizia = True
        
        if kolizia:
          print(f"KOLIZIA NASTALA, davam hraca {ihraca} do domca !")
          h.p = -1 # daj do domu
        else:
          # ak no problem, nastav mu tu poziciu
          h.p = predpoklad_p
      
      h.i += 1 # dalsi hod pre hraca automaticky (skoncilo kolo)
    # end for hraci
    
    return True # dalsie kolo moze ist !
  # end def kolo
  
  hraci_arr = [ Hrac(hody) for hody in hody_jednotlivych_hracov ]
  
  index_kola = 1
  while kolo(hraci_arr):
    print(f"== Koniec {index_kola}. kola ==")
    print(", ".join([str(x) for x in hraci_arr]))
    index_kola += 1
    
  print(f"== Koniec posledneho - {index_kola}. kola ==")
  print(", ".join([str(x) for x in hraci_arr]))
   
  # vrat pozicie vysledne hracov
  return [ h.p for h in hraci_arr ] 
  
if __name__ == "__main__":
  # test
  hody_dev = [
    [3, 6, 6, 6, 3, 4, 2 , 3 ,4], # overflow checkcc
    [3, 6, 6],
    [3, 6, 6],
    [3, 6, 2],
  ]
  
  pozicie = korytnacky_sa_nehnevaju(10, hody_dev)
  print(f"Vysledne pos: {pozicie}")