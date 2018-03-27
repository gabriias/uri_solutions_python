entrada = int(input())

matriz = []
lista = []

soma = 0

for x in range(entrada):
    linha = input().split()
    matriz.append(linha)

for y in range(entrada * 2):
    a,b = [int(c) for c in input().split()]
    a = a - 1
    b = b - 1
    if matriz[a][b] not in lista:
        p = matriz[a][b]
        lista.append(p)

print(len(lista))
