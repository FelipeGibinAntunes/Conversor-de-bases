simbolos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
          "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
         "U", "V", "W", "X", "Y", "Z"]

def BaseParaDecimal(numero,base):
     resultado = 0
     numero = str(numero)
     base = int(base)
     temp = list(numero)
     temp.reverse()
     for x,i in enumerate(temp):
         resultado += simbolos.index(i) * base**(x)
     return str(resultado)
 
def DecimalParaAlvo(numero,baseAlvo):
     resultado = ""
     baseAlvo = int(baseAlvo)
     numero = int(numero)
     temp = []
     while True:
         algarismo = numero%baseAlvo
         temp.append(algarismo)
         if int(numero/baseAlvo) == 0:
             break
         numero = int(numero/baseAlvo)
     temp.reverse()
     for i in temp:
         resultado += simbolos[i]     
     return resultado
 
def BaseParaAlvo(numero,base,baseAlvo):
     decimal = BaseParaDecimal(numero,base)
     resultado = DecimalParaAlvo(decimal,baseAlvo)
     return resultado

n = input("Digite o número a ser convertido: ")
b = int(input("Digite a base inicial do número: "))
tb = int(input("Digite a base alvo da conversão: "))
r = BaseParaAlvo(n,b,tb)
print("O número indicado na base {} é {}".format(tb,r))