while True:
    lista = []
    entrada = [int(x) for x in input().split()]
    if entrada[0] <= 0 or entrada[1] <= 0:
        break
    else:
        if entrada[1] > entrada[0]:
            entrada[1], entrada[0] = entrada[0], entrada[1]
        while entrada[0] >= entrada[1]:
            lista.append(entrada[1])
            print(entrada[1],end=' ')
            entrada[1] += 1
        else:
            print('Sum=%d'%sum(lista))
        
