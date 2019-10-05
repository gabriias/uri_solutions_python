def verifica(entrada,t,v):
    string = ""
    tamanho = 0
    for todos in range(t):
        if tamanho == (t-v):
            break
        i = str(todos+1)
        if i not in entrada:
            string+=i
            string+=" "
            tamanho+=1
    return string

while True:
    try:
        t,v = [int(x) for x in input().split()]
        entrada = input().split()
        if t == v:
            print("*")
        else:
            entrada.sort()
            print(verifica(entrada,t,v))
    except:
        break
