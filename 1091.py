while 1:
    K = int(input(""))
    if K == 0:
        break
    
    valores = input()
    partes = valores.split()
    N = int(partes[0])
    M = int(partes[1])

    for i in range (K):
        valores = input()
        partes = valores.split()
        X = int(partes[0])
        Y = int(partes[1])

        if (X == N or Y == M):
            print("divisa")
        elif (X > N and Y > M):
            print("NE")
        elif (X > N and Y < M):
            print("SE")
        elif (X < N and Y > M):
            print("NO")
        elif (X < N and Y < M):
            print("SO")
