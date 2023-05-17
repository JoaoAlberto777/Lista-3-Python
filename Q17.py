from Pilha import Pilha

def Convert_Dec(Octal):
    pilha = Pilha()
    Tam = 0

    for digito in Octal:
        valor = int(digito)
        pilha.insert(valor)
        Tam += 1
    
    Decimal = 0
    for cont in range(0,Tam):
        valor = pilha.remove()
        Decimal += valor * (8 ** cont)

    return Decimal

Octal = input("Digite o número em Octal: ")
print("Número em Octal: ",Octal)
Octal_Dec = Convert_Dec(Octal)
print(f"O Número {Octal} em decimal é: ",Octal_Dec)
    