positivo = 0
media = 0
n1 = float(input(""))
if n1>0:
    positivo = positivo+1
    media = media+n1
n2 = float(input(""))
if n2>0:
    positivo = positivo+1
    media = media+n2
n3 = float(input(""))
if n3>0:
    positivo = positivo+1
    media = media+n3
n4 = float(input(""))
if n4>0:
    positivo = positivo+1
    media = media+n4
n5 = float(input(""))
if n5>0:
    positivo = positivo+1
    media = media+n5
n6 = float(input(""))
if n6>0:
    positivo = positivo+1
    media = media+n6
print("%d valores positivos" % positivo)
print("%0.1f" % (media/positivo))
