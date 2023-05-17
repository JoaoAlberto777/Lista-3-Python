from Pilha import Pilha

def converter_para_decimal(string):
    p = Pilha()
    for digito in string:
        p.insert(int(digito))

    result = 0
    position = 0

    while not p.is_empty():
        result += p.remove() * 10**position
        position += 1

    return result

string = input("Digite um número: ")
print("tipo original",type(string))
NumDec = converter_para_decimal(string)
print("Número convertido para inteiro: ",NumDec)
print("Tipo depois da conversão",type(NumDec))