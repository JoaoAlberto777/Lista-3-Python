from Pilha import Pilha
  
def infixa_para_posfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    Numeros = '0123456789'
    for char in expressao:
        if char in Numeros:
            posfixa.append(char)
        elif char == '(':
            operadores.insert(char)
        elif char == ')':
            while operadores.Top() != '(':
                posfixa.append(operadores.remove())
            operadores.remove()
        elif char in precedencia:
            while not operadores.is_empty()  \
                and operadores.Top() != '(' \
                and precedencia[char] <= precedencia[operadores.top()]:
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

def balanceada(expressao):
    p = Pilha()
    for char in expressao:
        if char in '({[':
            p.insert(char)
        elif char in ')}]':
            if p.is_empty():
                return False
            topo = p.remove()
            if not corresponde(topo, char):
                return False
    return p.is_empty()

def corresponde(abertura, fechamento):
    return abertura == '(' and fechamento == ')' or \
           abertura == '{' and fechamento == '}' or \
           abertura == '[' and fechamento == ']'

s = input("Digite a expressão: ")
balanco = balanceada(s)
posfixa = infixa_para_posfixa(s)

r = calcular(posfixa)
if balanceada(s):
    print("A equação é válida !")
    print("Resultado: ",r)
else:
    print("A equação não é válida!")