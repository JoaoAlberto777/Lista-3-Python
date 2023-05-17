from Pilha import Pilha

def inverter_palavras(frase):
    palavras = frase.split()
    p = Pilha()
    for palavra in palavras:
        p.insert(palavra)
    nova_frase = " "
    while not p.is_empty():
        nova_frase += p.remove() + " "
    return nova_frase.split()


frase = input("Digite uma frase: ")
frase_invertida = inverter_palavras(frase)
print(f"A Frase {frase} invertida é: ", frase_invertida)