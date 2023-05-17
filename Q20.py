from Pilha import Pilha

def Convert_Dec(Binario):
    pilha = Pilha()
    Tam = 0

    for digito in Binario:
        valor = int(digito)
        pilha.insert(valor)
        Tam += 1
  
    Decimal = 0
    for cont in range(0,Tam):
        valor = pilha.remove()
        if valor == 1:
            Decimal += (valor * 2) ** cont

    return Decimal

def Dec_Hexa(Decimal):
    pilha = Pilha()
    Num = Decimal
    while Num > 0:
        Resto = Num % 16 
        Num = Num // 16
        if Resto >=10 :
            match Resto:
                case 10:
                    Resto = 'A'
                case 11:
                    Resto = 'B'
                case 12:
                    Resto = 'C'
                case 13:
                    Resto = 'D'
                case 14: 
                    Resto = 'E'
                case 15:
                    Resto = 'F'       
        pilha.insert(Resto)
        print("O Resto é: ",Resto)
        print("Resto da divisão é:",Num)
    if Num != 0:
        pilha.insert(Num)
    
    Hexa = []
    while not pilha.is_empty():
        pilha.top()
        Hexa.append(pilha.top())
        pilha.remove()

    return Hexa

Binario = input("Digite o número em binário : ")
print("Número em binário: ",Binario)
Bin_Dec = Convert_Dec(Binario)
Hexa = Dec_Hexa(Bin_Dec)
print("O número {Binario} em Hexadecimal é: ",end="")
for i in Hexa:
    print(i, end="")
    