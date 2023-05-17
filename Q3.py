from Pilha import Pilha
    
def infixa_para_posfixa(expressao):
    preced = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'
    for char in expressao:
        if char in numeros:
            posfixa.append(char)
        elif char in preced:
            while not operadores.is_empty()  \
                and operadores.top() != '(' \
                and preced[char] <= preced[operadores.top()]:
                posfixa.append(operadores.remove())
            operadores.insert(char)
    while not operadores.is_empty():
        posfixa.append(operadores.remove())
    return ''.join(posfixa)

def calcular(expressao):
    p = Pilha()
    for c in expressao:
        if c.isdigit():
            p.insert(int(c))
        elif c in "+-*/":
            b = p.remove()
            a = p.remove()
            if c == "+":
                p.insert(a + b)
            elif c == "-":
                p.insert(a - b)
            elif c == "*":
                p.insert(a * b)
            elif c == "/":
                p.insert(a / b)
    return p.remove()

s = input("Digite a expressão infixa: ")

posfixa = infixa_para_posfixa(s)

r = calcular(posfixa)

print("\nResultado: ",r)
