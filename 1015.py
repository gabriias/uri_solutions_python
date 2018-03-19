import math
valores1 = input()
partes1 = valores1.split()
x1 = float(partes1[0])
y1 = float(partes1[1])
valores2 = input()
partes2 = valores2.split()
x2 = float(partes2[0])
y2 = float(partes2[1])

print("%0.4f" % (math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))))
