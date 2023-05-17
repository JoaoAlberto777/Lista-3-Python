from Pilha import Pilha
    
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
           
expressao = input("Digite os seguintes caracteres '(,),{,},[,]': ")
if balanceada(expressao):
    print("Os caracteres estão BALANCEADOS!")
else:
    print("Os caracteres estão DESBALANCEADOS!")