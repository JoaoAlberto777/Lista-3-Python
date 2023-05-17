from Pilha import Pilha

def Convert_Polonesa(expressao):
    P = Pilha()
    Not_Polonesa = []
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}

    for char in expressao:
        if char.isnumeric():
            Not_Polonesa.append(char)
        elif char in '+-*/':
            while not P.is_empty() and P.top() in '+-*/' and precedencia[char] <= precedencia[P.top()]:
                Not_Polonesa.append(P.remove())
            P.insert(char)
        elif char == '(':
            P.insert(char)
        elif char == ')':
            while not P.is_empty() and P.top() != '(':
                Not_Polonesa.append(P.remove())
            P.remove()

    while not P.is_empty():
        Not_Polonesa.append(P.remove())

    return ''.join(Not_Polonesa)

expressao = input("Digite uma expressão matematica: ")
Not_Polonesa = Convert_Polonesa(expressao)
print(f"A Equação {expressao} Na Notação polonesa reversa é:", Not_Polonesa)