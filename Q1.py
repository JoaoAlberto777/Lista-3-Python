from Pilha import Pilha

def main():
    
    p = Pilha()
    expressao = []
    expressao = str(input("Digite uma expressão matematica com parênteses: "))
    for valor in expressao:
        if valor == "(":
            p.insert(valor)
        if valor == ")":
            p.remove()
    if p.is_empty() == True:
        print("Os parenteses estão balanceados !")
    else:
        print("Os parenteses estão desbalanceados !")  

if __name__ == "__main__":
    main()    
