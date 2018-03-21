n1 = int(input())
aux=0
sucessor=0
while True:
    try:

        n2=int(input())
        if (n2<n1 and c==0):
            aux=n1+1
            sucessor=1
        n1=n2
    except:
        break
if(sucessor==1):
   print(aux)
if(sucessor==0):
   print(n1+1)
