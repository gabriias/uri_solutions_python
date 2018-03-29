d = 1
while True:
    try:
        
        x,y = [float(a) for a in input().split()]

        p = ((y - x) * 100) / x
        s = "%"
    
        print("Projeto %d:" % d)
        print("Percentual dos juros da aplicacao: %0.2f %s" % (p,s))
        print("")
        d+=1
    except:
        break
