while 1:
    N = int(input(""))
    if N == 0:
        break
    for i in range(N):
        teste = 0
        valores = input()
        partes = valores.split()
        A = int(partes[0])
        B = int(partes[1])
        C = int(partes[2])
        D = int(partes[3])
        E = int(partes[4])

        if A <= 127:
            teste += 1
            A = 1
        else:
            A = 0
            
        if B <= 127:
            teste += 1
            B = 1
        else:
            B = 0

        if C <= 127:
            teste += 1
            C = 1
        else:
            C = 0
            
        if D <= 127:
            teste += 1
            D = 1
        else:
            D = 0
            
        if E <= 127:
            teste += 1
            E = 1
        else:
            E = 0

        if teste == 1:
            if A==1:
                print("A")
            if B==1:
                print("B")
            if C==1:
                print("C")
            if D==1:
                print("D")
            if E==1:
                print("E")
        else:
            print("*")
