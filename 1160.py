import math
t = int(input())
for cont in range(t):
  anos = 0
  entrada = input()
  valores = entrada.split()
  pa = int(valores[0])
  pb = int(valores[1])
  ga = float(valores[2])
  gb = float(valores[3])

  while pa<=pb and anos<=100:
    pa += math.floor((pa*ga)/100)
    pb += math.floor((pb*gb)/100)
    anos+=1
  if anos > 100:
    print("Mais de 1 seculo.")
  else:
    print("%d anos." %(anos))
    
