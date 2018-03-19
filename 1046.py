tempo = 0
hi, hf = [int(x) for x in input().split()]
if hi > hf:
    tempo = (24-hi)+hf
elif hi < hf:
    tempo = hf-hi
else:
    tempo = 24
print("O JOGO DUROU %d HORA(S)" % tempo)
