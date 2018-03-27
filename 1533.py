n = int(input())
while n!=0:
    entrada = [int(x) for x in input().split()]
    aux = []
    aux.extend(entrada)
    entrada.remove(max(entrada))
    aux2 = int(max(entrada))
    print(aux.index(aux2)+1)
    n = int(input())
