x,y = [int(a) for a in input().split()]

p = (y - x)


if y % p == 0:
    print(y//p)
else:
    print((y//p) + 1)
