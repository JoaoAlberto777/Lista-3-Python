from Pilha import Pilha

str = input("\nDigite uma palavra: ")
p = Pilha() 

for letra in str:
    p.insert(letra)

strInvert = "" 
while not p.is_empty():
    strInvert += p.remove() 
print("Palavra invertida:", strInvert)

if strInvert == str:
    print("A palavra é um políndromo")
else:
    print("A palavra não é um políndromo")