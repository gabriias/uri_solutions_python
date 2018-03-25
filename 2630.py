T=int(input())
for i in range(T):
    hana=input()
    a,b,c=[int(x) for x in input().split()]
    if hana =="min":
        p=int(min(a,b,c))
    elif hana=="mean":
        p=int((a+b+c)/3)
    elif hana=="eye":
        p=int((0.30*a)+(0.59*b)+(0.11*c))
    elif hana=="max":
        p=int(max(a,b,c))
    print("Caso #%d: %d"%(i+1,p))
