lista = []
for x in range(10):
    n = int(input())
    if n <=0:
        lista.append(1)
    else:
        lista.append(n)
for x in range(10):
    print('X[%d] = %d' %(x,lista[x]))
