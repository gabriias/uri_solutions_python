maior = ""
palavras = [ ]
while True:
    palavras = [str (x) for x in input().split()]
    if palavras[0] == "0":
        print ()
        print ("The biggest word: %s" % maior)
        break

    resposta = ""
    for i in range(len(palavras)):
       resposta = resposta + str(len(palavras[i])) + "-"
       if (len(palavras[i]) >= len(maior)) and (palavras[0] != "0"):
           maior = palavras[i]
    print(resposta[:-1])
