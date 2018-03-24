l_joia = []
tesouros = 0
joia = str(input())
while joia != "":
    try:
        if joia not in l_joia:
            l_joia.append(joia)
            tesouros+=1
        joia = str(input())
    except:
        break
print(tesouros)
