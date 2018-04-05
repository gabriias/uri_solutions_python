n = int(input())
aux = 1
for x in range(n):
    for y in range(4):
        if y == 3:
            print('PUM')
            aux += 1
        else:
            print(aux, end=' ')
            aux += 1
