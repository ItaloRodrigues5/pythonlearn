import time

def BuscaSimples(lista, alvoDesejado):
    for i, elemento in enumerate(lista):
        if elemento == alvoDesejado:
            return i
    return - 1


listaDeNumeros = [1, 9, 8, 4, 3, 2, 0, 5, 6, 7]
alvoDesejado = 1


inicio = time.time()  # Tempo inicial
resultado = BuscaSimples(listaDeNumeros, alvoDesejado)
fim = time.time()  # Tempo final

tempo_execucao = (fim - inicio) * 1000  # Converte para milissegundos
print(f"Tempo de execução: {tempo_execucao:.6f} ms")