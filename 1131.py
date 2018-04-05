i,g = [],[]
op = 1
cont = 0
emp = 0
while op == 1:
    cont += 1
    entrada = [int(x) for x in input().split()]
    if entrada[0] == entrada[1]:
        emp += 1
    elif entrada[0] > entrada [1]:
        i.append(entrada[0])
    else:
        g.append(entrada[1])
    print('Novo grenal (1-sim 2-nao)')
    op = int(input())
print('%d grenais' %cont)
print('Inter:%d' %len(i))
print('Gremio:%d' %len(g))
print('Empates:%d' %emp)
if len(i) > len(g) and len(i) > emp:
    print('Inter venceu mais')
elif len(g) > len(i) and len(g) > emp:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
