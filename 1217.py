n = int(input())
soma, soma2, x = 0,0,0
for x in range(n):
    v = float(input())
    soma += v
    frutas = [str(x) for x in input().split()]
    soma2 += len(frutas)
    p = x+1
    print("day %d: %d kg" % (p,len(frutas)))
    x += 1

print("%0.2f kg by day" % (soma2/n))
print("R$ %0.2f by day" % (soma/n))
