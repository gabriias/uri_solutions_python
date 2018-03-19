maior = 0
medio = 0
menor = 0

valores = input()
partes = valores.split()
x = int(partes[0])
y = int(partes[1])
z = int(partes[2])

if x>y and x>z:
    maior=x
    if y>z:
        medio=y
        menor=z
    else:
        medio=z
        menor=y
elif y>x and y>z:
    maior=y
    if x>z:
        medio=x
        menor=z
    else:
        medio=z
        menor=x
elif z>x and z>y:
    maior=z
    if y>x:
        medio=y
        menor=x
    else:
        medio=x
        menor=y
        
print(menor)
print(medio)
print(maior)
print("")
print(x)
print(y)
print(z)
