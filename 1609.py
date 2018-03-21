T = int(input())
for cont in range (T):
    N = int(input())
    carn = [int (x) for x in input().split()]
    carn = sorted(set(carn))
    print(len(carn))
