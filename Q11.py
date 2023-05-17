from Pilha import Pilha
    
def OrdenLista(lista):
    intList=[]
    for i in lista:
        intList.append(int(i))
        
    p = Pilha()
    lista_ordenada = []

    for num in intList:
        p.insert(num)

    while not p.is_empty():
        elemento = p.remove()
        posicao = 0
        while posicao < len(lista_ordenada) and elemento > lista_ordenada[posicao]:
            posicao += 1
        lista_ordenada.insert(posicao, elemento)

    return lista_ordenada

Nums = input("Digite os números separado por espaços: ").split()
Nums_ordenados = OrdenLista(Nums)

print(f"Os Números {Nums} ordenados são:", Nums_ordenados)  