while True:
    dic = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    dic2 = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    entrada = str(input())
    if entrada[0]  == "-":
        break
    else:
        if len(entrada) < 2:
            x = int(entrada)
            print("0x%d" % x)
        else:
            if entrada[1] == "x" or entrada[1] == "X":
                
                soma = 0
                m = len(entrada) - 1
                n = 0
                while m >= 2:
                    if entrada[m].upper() in dic2:
                        h = entrada[m].upper()
                        soma = soma + (dic2[h] * 16 ** n)
                        m = m - 1
                        n = n + 1
                    else:
                        f = int(entrada[m])
                        soma = soma + (f * 16 ** n)
                        m = m - 1
                        n = n + 1
                print(soma)
            else:
                lista = ""
                l = 0
                n = int(entrada)
                m = str(hex(n))
                while l < len(m):
                    if m[l] != "x":
                        x = m[l]
                        x = x.upper()
                        lista = lista + x
                        l+=1
                    else:
                        x = m[l]
                        lista = lista + x
                        l+=1
                print(lista)
