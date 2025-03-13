class Fila:
    def __init__(self):
        self.itens = []
    
    def inserir(self, item):
        self.itens.append(item)
    
    def remover(self, item):
        return self.itens.pop(item)
    
    def esta_vazia(self):
        if len(self.itens) == 0:
            return True
        else:
            return False

class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)
    
    def desempilhar(self):
        return self.itens.pop()

    def esta_vazia(self):
        if len(self.itens) == 0:
            return True
        else:
            return False
            
#CLASSE FILA
print("CLASSE FILA")
        
fila = Fila()

fila.inserir(1)
fila.inserir(2) #Aff, cansei. Vou embora.
fila.inserir(3)

#[0, 1, 2]
#[1, 2, 3]

print(fila.remover(0))

print(fila.esta_vazia())

#CLASSE PILHA

print("")
print("CLASSE PILHA")

pilha = Pilha()

pilha.empilhar("A")
pilha.empilhar("B")
pilha.empilhar("C")

print(pilha.desempilhar())

print(pilha.esta_vazia())
