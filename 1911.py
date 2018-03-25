n = 1
while True:
    n = int(input(""))
    if n == 0:
        break
    ata = {}

    for x in range(n):
        entrada1 = input().split()
        ata[entrada1[0]] = entrada1[1]

    alunos = int(input(""))
    erro, ass = 0,0
    for x in range(alunos):
        cont = 0
        nomes_ata = input().split()
        for y in ata[nomes_ata[0]]:
            if y != nomes_ata[1][cont]:
                erro = erro + 1
            cont = cont + 1
        if erro > 1:
            ass = ass + 1
        erro = 0
    print(ass)
