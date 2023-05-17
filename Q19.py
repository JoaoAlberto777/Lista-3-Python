from Pilha import Pilha

def Convert_Dec(Binario):
    pilha = Pilha()
    tam = 0
    
    for digito in Binario:
        valor = int(digito)
        pilha.insert(valor)
        tam += 1
    
    Decimal = 0
    for cont in range(0,tam):
        valor = pilha.remove()
        if valor == 1:
            Decimal+= (valor * 2) ** cont

    return Decimal
def Convert_Oc(Decimal):
    pilha = Pilha()
    Num = Decimal
    
    while Num > 0:
        resto = Num % 8 
        Num = Num // 8
        pilha.insert(resto)
        print("O resto é: ",resto)
        print("Resto da divisão:",Num)
    if Num != 0:
        pilha.insert(Num)
    
    octal = []
    while not pilha.is_empty():
        pilha.top()
        octal.append(pilha.top())
        pilha.remove()

    return octal
Binario = input("Digite o número em binário: ")
print("Número em binário: ",Binario)
Decimal= Convert_Dec(Binario)
octal = Convert_Oc(Decimal)
print(f"O Número {Binario} em octal é: ", end="")

for i in octal:
    print (i, end="")