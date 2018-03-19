X = int(input(""))
aux = 0
if X % 2 == 0:
    X=X+1
    print(X)
    while aux <= 4:
        X=X+2
        print(X)
        aux=aux+1
else:
    print(X)
    while aux <= 4:
        X=X+2
        print(X)
        aux=aux+1
