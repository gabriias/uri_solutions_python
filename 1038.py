valores = input()
partes = valores.split()
cod = int(partes[0])
quant = int(partes[1])

if cod == 1:
    print("Total: R$ %0.2f" % (4*quant))
elif cod == 2:
    print("Total: R$ %0.2f" % (4.5*quant))
elif cod == 3:
    print("Total: R$ %0.2f" % (5*quant))
elif cod == 4:
    print("Total: R$ %0.2f" % (2*quant))
elif cod == 5:
    print("Total: R$ %0.2f" % (1.5*quant))
