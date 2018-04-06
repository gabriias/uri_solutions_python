n = int(input())
lista = []
aux = 1
for x in range(n+1)[1::]:
    lista.append([x,x**2,x**3])

for x in range(n):
    for y in range(3):
        if y == 2:
            print(lista[x][y])
        else:
            print(lista[x][y], end=' ')
