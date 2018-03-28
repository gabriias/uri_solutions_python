caso = 0
while True:
    try:

        lista = []
        lista2 = []
        soma = 0
        somaf = 0
        somam = 0
        entrada = input()
        entrada2 = input().split()
        for x in entrada2:
            if x.isdigit() == True:
                lista.append(x)
            else:
                lista2.append(x)
        for a,b in enumerate(lista):
            if b == entrada:
                soma += 1
                if lista2[a] == "F":
                    somaf += 1
                else:
                    somam += 1
                    
        if caso >= 1:
            print("")
        caso += 1
        print("Caso %d:" % caso)
        print("Pares Iguais: %d" % soma)
        print("F: %d" % somaf)
        print("M: %d" % somam)
        

        
    except:
        break
