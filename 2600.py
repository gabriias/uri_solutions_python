n = int(input())
for x in range(n):
    l1 = int(input())
    l2,l3,l4,l5 = [int(x) for x in input().split()]
    l6 = int(input())

    if l1==l2 or l1==l3 or l1==l4 or l1==l5 or l1==l6 or l2==l3 or l2==l4 or l2==l5 or l2==l6 or l3==l4 or l3==l5 or l3==l6 or l4==l5 or l4==l6 or l5==l6:
        print("NAO")
    elif l1<=0 or l2<=0 or l3<=0 or l4<=0 or l5<=0 or l6<=0:
        print("NAO")
    elif l1+l6==7 and l2+l4==7 and l3+l5==7:
        print("SIM")
    else:
        print("NAO")
