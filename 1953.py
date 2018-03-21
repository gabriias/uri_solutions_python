while True:
    try:
        epr = 0
        ehd = 0
        intrusos = 0
        n = int(input(""))
        for cont in range(n):
            valores = input()
            partes = valores.split()
            matricula = int(partes[0])
            sigla = str(partes[1])
            if sigla == "EPR":
                epr += 1
            elif sigla == "EHD":
                ehd += 1
            else:
                intrusos += 1
        print("EPR: %d" % (epr))
        print("EHD: %d" % (ehd))
        print("INTRUSOS: %d" % (intrusos))
    except:
        break
