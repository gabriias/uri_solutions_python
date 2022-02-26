entrada = int(input())
qtdNotas = 0
resto = 0

print(entrada)

qtdNotas = entrada//100
resto = entrada - (qtdNotas*100)
print('{} nota(s) de R$ 100,00'.format(qtdNotas))

qtdNotas = resto//50
resto = resto - (qtdNotas*50)
print('{} nota(s) de R$ 50,00'.format(qtdNotas))

qtdNotas = resto//20
resto = resto - (qtdNotas*20)
print('{} nota(s) de R$ 20,00'.format(qtdNotas))

qtdNotas = resto//10
resto = resto - (qtdNotas*10)
print('{} nota(s) de R$ 10,00'.format(qtdNotas))

qtdNotas = resto//5
resto = resto - (qtdNotas*5)
print('{} nota(s) de R$ 5,00'.format(qtdNotas))

qtdNotas = resto//2
resto = resto - (qtdNotas*2)
print('{} nota(s) de R$ 2,00'.format(qtdNotas))

qtdNotas = resto//1
resto = resto - (qtdNotas*1)
print('{} nota(s) de R$ 1,00'.format(qtdNotas))