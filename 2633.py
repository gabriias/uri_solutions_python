while True:
    try:
        dicionario = {}
        aux = []
        n = int(input())
        for x in range (n):
            entrada = input().split()
            dicionario[int(entrada[1])] = entrada[0]
            aux.append(int(entrada[1]))
        aux.sort()
        
        for x, y in enumerate(aux):
            if x == len(dicionario)-1:
                print(dicionario[y])
            else:
                print(dicionario[y], end=" ")
    except:
        break
