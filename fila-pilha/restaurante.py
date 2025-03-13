class GerenciamentoPedidos:
    def __init__(self):
        self.pedidos = []
        self.acao_undo = []
        self.acao_redo = []


    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)
        self.acao_undo.append(("adicionar", pedido))
        self.acao_redo.clear()

    def atender_pedido(self):
        if self.pedidos:
            pedido = self.pedidos.pop(0)
            self.acao_undo.append(("atender", pedido))
            self.acao_redo.clear()
            return pedido
        return None

    def desfazer(self):
        if self.acao_undo:
            acao, pedido = self.acao_undo.pop()
            if acao == "adicionar":
                self.pedidos.remove(pedido)  
            elif acao == "atender":
                self.pedidos.insert(0, pedido)
            self.acao_redo.append((acao, pedido))

    def refazer(self):
        if self.acao_redo:
            acao, pedido = self.acao_redo.pop()
            if acao == "adicionar":
                self.pedidos.append(pedido)
            elif acao == "atender":
                self.pedidos.pop(0)
            self.acao_undo.append((acao, pedido))

    def pedidos_vazia(self):
        return len(self.pedidos) == 0

restaurante = GerenciamentoPedidos()

restaurante.adicionar_pedido("Pedido 1")
restaurante.adicionar_pedido("Pedido 2")
restaurante.adicionar_pedido("Pedido 3")
print("Fila de pedidos:", restaurante.pedidos)

restaurante.atender_pedido()
print("Após atender um pedido:", restaurante.pedidos)

restaurante.desfazer()
print("Após desfazer:", restaurante.pedidos)

restaurante.refazer()
print("Após refazer:", restaurante.pedidos)
