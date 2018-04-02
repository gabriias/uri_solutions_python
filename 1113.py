while True:
    entrada = [int(x) for x in input().split()]
    if entrada[0] == entrada[1]:
        break
    else:
        if entrada[0] < entrada[1]:
            print('Crescente')
        else:
            print('Decrescente')
