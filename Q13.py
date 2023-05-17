from Pilha import Pilha
    
def convert(binario):
    p = Pilha()
    
    for n in binario:
        p.insert(int(n))
   
    potencia = 0
    SomaPotencias = 0
     
    while not p.is_empty():
        SomaPotencias += p.remove() * (2 ** potencia)
        potencia += 1
    
    return SomaPotencias
    
numero = input("Digite um número binário: ")

Decimal = convert(numero)
print(f"O número {numero} em Decimal é: ", Decimal)