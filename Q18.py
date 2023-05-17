from Pilha import Pilha

def infixa_para_posfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'
    for char in expressao:
        if char in numeros:
            posfixa.append(char)
        elif char in precedencia:
            while not operadores.is_empty()  \
                and operadores.top() != '(' \
                and precedencia[char] <= precedencia[operadores.top()]:
                posfixa.append(operadores.remove())
            operadores.insert(char)
    while not operadores.is_empty():
        posfixa.append(operadores.remove())
    return ''.join(posfixa)

def calcular(expressao):
    pilha = Pilha()
    for c in expressao:
        if c.isdigit():
            pilha.insert(int(c))
        elif c in "+-*/":
            b = pilha.remove()
            a = pilha.remove()
            if c == "+":
                pilha.insert(a + b)
            elif c == "-":
                pilha.insert(a - b)
            elif c == "*":
                pilha.insert(a * b)
            elif c == "/":
                pilha.insert(a / b)
    return pilha.remove()

S = input("Digite a expressão infixa: ")

posfixa = infixa_para_posfixa(S)

resultado = calcular(posfixa)

print(f"\nO Resultado da Expressão {S} é: ",resultado)