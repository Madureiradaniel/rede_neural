from redeNeural import NeuralNetwork
from matriz import *

""" entrada, oculta, saida, learning reate"""
redeNeural = NeuralNetwork(2, 3, 1, 0.1)

entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
saida = [[1], [0], [0], [1]]

"""TREINANDO A REDE"""
treino = True

while(treino):
    for i in range(5000):
        aux = randint(0, 3)
        redeNeural.backpropagation(entrada[aux], saida[aux])

    esperado = redeNeural.feedfoward([0, 1])
    esperadoAux = redeNeural.feedfoward([1,1])

    if esperado[0][0] < 0.02 and esperadoAux[0][0] > 0.98:
        treino = False
        print("treinamento terminado\n")

print("TESTE - 0,0")
print(str(redeNeural.feedfoward([0, 0])))

print("TESTE - 0,1")
print(str(redeNeural.feedfoward([0, 1])))

print("TESTE - 1,0")
print(str(redeNeural.feedfoward([1, 0])))

print("TESTE - 1,1")
print(str(redeNeural.feedfoward([1, 1])))