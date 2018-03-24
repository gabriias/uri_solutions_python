n = int(input())
if n == 1:
    print("0 1")
else:
    print("0 1",end=" ")
    a = 0
    b = 1
    i = 2
    while i < n-1:
        a,b = b, a+b
        print(b,end=" ")
        i +=1
    print(a+b)
