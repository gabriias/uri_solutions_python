valores = input()
partes = valores.split()
A = int(partes[0])
B = int(partes[1])

soma = int(((A+B)*(B-A+1))/2)
print(soma)
