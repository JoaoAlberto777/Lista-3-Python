from Pilha import Pilha

def main(string):
    pilha = Pilha()
    Num = int(string)
    for n in range(0,Num):
        resto = Num % 2 
        Num = Num // 2
        pilha.insert(resto)
        print("O Resto é: ",resto)
        print("Resto da divisão:",Num)
        if Num == 1:
            break
    if not Num % 2 == 0:
        pilha.insert(1)
    
    binario = []
    while not pilha.is_empty():
        pilha.top()
        binario.append(pilha.top())
        pilha.remove()

    return binario
string = input("Digite um número: ")
bin = main(string)
print(f"O número {string} em binário é: ")
for i in bin:
    print(i, end="")
    