while True:
    matriz = []
    x,y = [int(a) for a in input().split()]
    if x == 0 and y == 0:
        break
    else:
        for b in range(y):
            l = input().split()
            matriz.append(l)
        cont = 0
        s = 0
        for d in range(x):
            e, cont = 0,0
            for e in range(y):
                if matriz[e][d] == '1':
                    cont += 1
                    e += 1
                else:
                    e += 1
            d += 1
            if cont == y:
                s += 1
                
        if s > 0:
            print('yes')
        else:
            print('no')
