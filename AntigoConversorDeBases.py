import math

n = input("Digite o número a ser convertido: ")
b = int(input("Digite a base inicial do número: "))
tb = int(input("Digite a base alvo da conversão: "))

# Transformação do número para base 10
lCharN = []
sum = 0
for c in n:
    lCharN.append(c)
    if int(c) >= b:
        print("O número indicado não está na base indicada")
        exit()
lCharN.reverse()
for i in range(0, len(lCharN)):
    sum = sum + (math.pow(b,i) * int(lCharN[i]))

# Transformação do número para base alvo
cn = sum
ol = []
r = ""
while cn > 0:
    ol.append(int(cn%tb))
    cn = cn//tb
ol.reverse()
for i in ol:
    r = r + str(i)
print("O número indicado na base {} é {}".format(tb,r))
