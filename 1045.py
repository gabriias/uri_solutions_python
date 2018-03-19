valores = input()
partes = valores.split()
A = float(partes[0])
B = float(partes[1])

if B>A:
    maior = B
    B = A
    A = maior
    
C = float(partes[2])

if C>A:
    maior = C
    C = A
    A = maior

if A>= (B+C):
    print("NAO FORMA TRIANGULO")
elif (A*A)==(B*B)+(C*C):
    print("TRIANGULO RETANGULO")
elif (A*A) > (B*B)+(C*C):
    print("TRIANGULO OBTUSANGULO")
elif (A*A) < (B*B)+(C*C):
    print("TRIANGULO ACUTANGULO")

if A==B==C:
    print("TRIANGULO EQUILATERO")
elif A==B or A==C or B==C:
    print("TRIANGULO ISOSCELES")
