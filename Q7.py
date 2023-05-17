from Pilha import Pilha

def convert(num):
    p = Pilha()
    while num > 0:
        resto = num % 8
        p.insert(resto)
        num //= 8

    Octal = ''
    while not p.is_empty():
        Octal += str(p.remove())

    return Octal

NumDec = int(input("Digite um número decimal: "))

Octal = convert(NumDec)

print(f"{NumDec} Convertido para Octal é:",Octal)