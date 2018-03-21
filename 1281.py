dic = {}
N = int(input())
for x in range(N):
    M = int(input())

    for y in range(M):
        a,b = [n for n in input().split()]
        b = float(b)
        dic[a] = b
    P = int(input())
    soma = 0

    for z in range(P):
        c,d = [e for e in input().split()]
        d = int(d)
        soma = soma + (dic[c] * d)         
    print("R$ %0.2f" % soma)
