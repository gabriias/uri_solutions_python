entrada = int(input())
for h in range(entrada):
            
    lista = []
    lista2 = []
    entrada2 = int(input())
    entrada3 = input().split()
    entrada4 = input()
    soma = 0
    k = 0
    for x in entrada3:
        x = int(x)
        lista.append(x)
    while k < len(entrada4):
        lista2.append(entrada4[k])
        k+=1
    for a,b in enumerate(lista2):
        if b == "J" and lista[a] > 2:
            soma += 1
        elif b == "S" and lista[a] >= 1 and lista[a] <= 2:
            soma += 1
        else:
            soma = soma
    print(soma)
