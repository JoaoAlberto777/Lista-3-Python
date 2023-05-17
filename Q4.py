from Pilha import Pilha

def converter(Num):
    p = Pilha()

    while Num > 0:
        RestoDiv = Num % 2
        p.insert(RestoDiv)
        Num = Num // 2
    return p
    
Num = int(input("\nDigite um número: "))

RestoDiv = converter(Num)

print(f"O Número {Num} em binário é: ")
while not RestoDiv.is_empty():
        print(RestoDiv.remove(), end="")