while True:
    A, B = [int(x) for x in input().split()]
    if A == 0 and B==0:
        break
    C = (2*A)-B
    print(C)
