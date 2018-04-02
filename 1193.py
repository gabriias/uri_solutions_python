n = int(input())
for cont in range (n+1)[1::]:    
    valores = input()
    entrada = valores.split()
    x = str(entrada[0])
    y = str(entrada[1])

    if y=='bin':
        print('Case %d:' % cont)
        aux = int(x,2)
        print(aux, 'dec')
        print(hex(aux)[2::], end=' ')
        print('hex')
        print()
    elif y=='dec':
        print('Case %d:' % cont)
        aux = int(x)
        print(hex(aux)[2::], end=' ')
        print('hex')
        print(bin(aux)[2::], end=' ')
        print('bin')
        print()
    else:
        print('Case %d:' % cont)
        aux = int(x,16)
        print(aux, 'dec')
        print(bin(aux)[2::], end=' ')
        print('bin')
        print()
        
        
