from Pilha import Pilha

def palindromo(Numero):
    p = Pilha()
    for digito in Numero:
        p.insert(digito)

    palindromo = True
    for digito in Numero:
        if digito != str(p.remove()):
            palindromo = False
            break

    return palindromo

Numero = input("Digite um número: ")

r = palindromo(Numero)

if r == True:
    print(f"\nO número {Numero} é um palíndromo")
else:
    print(f"\nO número {Numero} não é um palíndromo")