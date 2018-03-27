while True:
    n,m = [int(x) for x in input().split()]
    if n == 0 and m == 0:
        break
    else:
        lista = []
        lista2 = []
        soma = 0
        g = 0
        k = 0
        entrada = input().split()
        for y in entrada:
            y = int(y)
            lista.append(y)
        while k < len(lista):
            if lista.count(lista[k]) > 1:
                if lista[k] in lista2:
                    k+= 1
                else:    
                    lista2.append(lista[k])
                    soma = soma + 1
                    k += 1
            else:
                k += 1
            

        print(soma)
