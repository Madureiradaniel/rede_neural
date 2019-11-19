from redeNeural import NeuralNetwork
from matriz import *

"""xor"""
entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
saida = [[0], [1], [1], [0]]
""""""

qtd_camadas_ocultas = 3
criterio_parada = 0.01  # todos os elementos devem ter apenas essa diferenca da sua saida

""" entrada, oculta, saida, learning reate"""
redeNeural = NeuralNetwork(len(entrada[0]), qtd_camadas_ocultas, len(saida[0]), 0.1)


"""TREINANDO A REDE"""
treino = True
epoca = 1

while (treino):

    for i in range(100):
        aux = randint(0, len(entrada) - 1)
        redeNeural.backpropagation(entrada[aux], saida[aux])
        epoca += 1

    """condição de parada"""
    """todos os elementos devem ter o erro em relacao a saida menor que o valor passado"""
    erro = []
    for i in range(len(saida)):
        erro_saida = Matriz.subtrairMatriz(Matriz.array2matriz(saida[i]), redeNeural.feedfoward(entrada[i])).matriz

        for j in erro_saida:
            for k in j:
                erro.append(abs(k))
                # print(abs(k))

    if all(elemento < criterio_parada for elemento in erro):
        treino = False
        print("\n REDE TREINADA")
        print("Qtd de Loops: " + str(epoca) + "\n")


parada = True
while (parada):
    entrada = input("Digite a entrada: ")
    entrada = [int(i) for i in entrada.split(",")]
    print("SAIDA: " + str(redeNeural.feedfoward(entrada).matriz))
