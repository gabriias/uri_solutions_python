entrada = input().split()
n = int(entrada[0])
m = int(entrada[1])
o,t = [],[]

for x in range(n):
    entrada2 = input().split()
    o.append(str(entrada2[0]))
    t.append(str(entrada2[1]))
for y in range(m):
    aux = []
    frase = str(input())
    for z in frase:
        posicao = 0
        juncao = ''
        if z in t:
            posicao = t.index(z)
            juncao = juncao + o[posicao]
        elif z in o:
            posicao = o.index(z)
            juncao = juncao + t[posicao]
        else:
            juncao = juncao + z
        print(juncao, end='')
    print()
        
