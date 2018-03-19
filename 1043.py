valores = input()
partes = valores.split()
A = float(partes[0])
B = float(partes[1])
C = float(partes[2])

if (((abs(B-C)) < A) and (A < (B+C))) or (((abs(A-C)) < B) and (B < (A+C))) or (((abs(A-B)) < C) and (C < (A+B))):
    perimetro = A+B+C
    print("Perimetro = %0.1f" % perimetro)
else:
    area = (A+B)*C/2
    print("Area = %0.1f" % area)
