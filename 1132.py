x, y = int(input()), int(input())
soma = 0
if x>y:
    x,y = y,x
for cont in range(x,y+1):
    if cont % 13 != 0:
        soma+=cont
print(soma)
