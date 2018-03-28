n = int(input())

for x in range(n):
    lista = []
    k = int(input())
    for y in range(k):
        s = str(input())
        lista.append(s)
    z = 0
    soma = 0
    while z < len(lista):
        if lista[0] != lista[z]:
            z += 1
            soma += 1
        else:
            z += 1
    if soma > 0:
        print("ingles")
    else:
        print("%s" % lista[0])
