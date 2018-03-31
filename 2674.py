def primo(x):
    lim =int( x ** 0.5)
    cont = 0
    for i in range (1, lim+1):
        if x % i == 0:
            cont+=1
        if cont > 1:
            break
    if cont > 1 or x == 1 or x == 0:
        return False
    else:
        return True
    
while True:
    try:
        ent = input()
        sup = True
        prim = primo(int(ent))
        
        
        if prim   == False  :
            print ("Nada")
        else:
            for i in ent:
                
                if primo(int (i)) == False:

                    sup = False
                    break
            
            if sup :
                print ("Super")
            else:
                print ("Primo")
            
        
    except:
        break
