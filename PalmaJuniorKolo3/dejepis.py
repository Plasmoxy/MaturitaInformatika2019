from random import shuffle

def generuj_slovo(slovo):
  l = len(slovo)
  parne = l%2==0
  parne_slovo = slovo if parne else slovo[:-1]
  dvojice = [ parne_slovo[i:i+2] for i in range(0, len(parne_slovo), 2) ]
  
  shuffle(dvojice)
  
  return "".join(dvojice) + ("" if parne else slovo[l-1])

def test():
  print("TEST")
  print(f"PYTAGORAS -> {generuj_slovo('PYTAGORAS')}")
  print(f"HERKULES -> {generuj_slovo('HERKULES')}")
  
if __name__ == "__main__":
  test()