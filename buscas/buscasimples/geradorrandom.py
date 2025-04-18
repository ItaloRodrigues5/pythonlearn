# #GERADOR DE NÚMEROS ALEAGTÓRIO NA LISTA
# import random

# def gerar_lista():
#     return [random.randint(1, 10001) for _ in range(10000)]

# # Exemplo de uso
# lista_numeros = gerar_lista()
# print(lista_numeros)  # Exibe os primeiros 100 números gerados


#GERADOR DE NÚMEROS ALEATÓRIO
# import random

# # Gerar uma lista de números de 1 a 1000
# numeros = list(range(1, 1001))

# # Embaralhar a lista
# random.shuffle(numeros)

# # Imprimir a lista desordenada
# print(numeros)

# PEGAR O VALOR DO MEIO DA LISTA

def meio(lista):
    tamanho = len(lista)

    if tamanho == 0:
        return None
    
    meio = tamanho // 2

    if tamanho % 2 == 1:
        return lista[meio]
    
    else:
        return (lista[meio - 1] + lista[meio]) // 2

listaDesordenada = [10, 20, 30, 40, 50, 60]

resultado = meio(listaDesordenada)

print(resultado)