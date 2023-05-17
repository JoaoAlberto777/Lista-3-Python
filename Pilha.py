class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self._top = None
        self.tamanho = 0
   
    def __len__(self):
        return self.tamanho
   
    def is_empty(self):
        return self.tamanho == 0
   
    def insert(self, valor):
        no = No(valor)
        no.proximo = self._top
        self._top = no
        self.tamanho += 1
   
    def remove(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self._top.valor
        self._top = self._top.proximo
        self.tamanho -= 1
        return valor
   
    def top(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._top.valor