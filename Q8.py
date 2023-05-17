from Pilha import Pilha

def convertHexa(num):
    p = Pilha()
    while num > 0:
        resto = num % 16
        if resto < 10:
            p.insert(resto)
        else:
            p.insert(chr(resto + 55))
        num //= 16

    hexa = ''
    while not p.is_empty():
        hexa += str(p.remove())

    return hexa

NumDec = int(input("Digite um número decimal: "))

hexa = convertHexa(NumDec)

print(f"{NumDec} Convertido para hexadcimal é:",hexa) 