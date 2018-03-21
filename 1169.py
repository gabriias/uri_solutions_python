import math
repeticoes = int(input(""))
for cont in range (repeticoes):
    soma_gramas = 0
    casas = int(input(""))
    ultimo = 1
    for cont2 in range (casas):
        soma_gramas += ultimo
        ultimo = ultimo * 2
    print ("%.0f kg" % math.floor(soma_gramas/12000))
