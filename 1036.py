valores = input()
partes = valores.split()
A = float(partes[0])
B = float(partes[1])
C = float(partes[2])

delta = (B*B)-(4*A*C)

if A==0:
    print("Impossivel calcular")
elif delta<=0:
    print("Impossivel calcular")
elif delta>0:
    r1 = ((-B)+(delta ** (1/2)))/(2*A)
    r2 = ((-B)-(delta ** (1/2)))/(2*A)
    print("R1 = %0.5f" % r1)
    print("R2 = %0.5f" % r2)
