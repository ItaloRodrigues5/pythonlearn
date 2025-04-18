import time

def BuscaSimples02(lista, alvoDesejado):
    for i, elemento in enumerate(lista):
        if elemento == alvoDesejado:
            return i
    return - 1


listaDeNumeros = [23, 45, 12, 78, 34, 67, 91, 56, 43, 100,
                  87, 54, 67, 88, 32, 76, 45, 98, 65, 32,
                  11, 22, 33, 44, 55, 66, 77, 88, 99, 10,
                  20, 30, 40, 50, 60, 70, 80, 90, 1, 2,
                  3, 4, 5, 6, 7, 8, 9, 13, 14, 15,
                  16, 17, 18, 19, 21, 24, 25, 26, 27, 28,
                  29, 31, 35, 36, 37, 38, 39, 41, 42, 46,
                  47, 48, 49, 51, 52, 53, 57, 58, 59, 61,
                  62, 63, 64, 68, 69, 71, 72, 73, 74, 75,
                  79, 81, 82, 83, 84, 85, 86, 89, 92, 93,
                  94, 95, 96, 97, 98, 99, 100]
alvoDesejado = 100


inicio = time.time()  # Tempo inicial
resultado = BuscaSimples02(listaDeNumeros, alvoDesejado)
fim = time.time()  # Tempo final

tempo_execucao = (fim - inicio) * 1000  # Converte para milissegundos
print(f"Tempo de execução: {tempo_execucao:.6f} ms")