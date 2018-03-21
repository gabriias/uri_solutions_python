import re
while True:
    try:
        
        lista = str(input())
        if lista == "":
            break
        filtro = re.compile('([0-9]+)')
        resp = filtro.findall(lista)
        resp = list(map(int,resp))
        if "R" in lista:
            r1 = int(resp[0])
            r2 = int(resp[1])
            print(r2-r1)
        elif "L" in lista:
            l1 = int(resp[0])
            l2 = int(resp[1])
            print(l2-l1)
        elif "J" in lista:
            j1 = int(resp[0])
            j2 = int(resp[1])
            print(j1+j2)
    except:
        break  
