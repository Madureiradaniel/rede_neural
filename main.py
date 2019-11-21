from redeNeural import NeuralNetwork
from matriz import *

entrada = []
saida = []

print("================================================")
print("        PORTAS LÓGICAS REDES NEURAIS   ")
print("================================================")
print("1 - AND")
print("2 - OR")
print("3 - XOR")
print("4 - NAND")
print("5 - XNOR")

op = int(input())

if op == 1:
    """AND"""
    entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
    saida = [[0], [0], [0], [1]]
    """"""
elif op == 2:
    """OR"""
    entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
    saida = [[0], [1], [1], [1]]
    """"""
elif op == 3:
    """xor"""
    entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
    saida = [[0], [1], [1], [0]]
    """"""
elif op == 4:
    """NAND"""
    entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
    saida = [[1], [1], [1], [0]]
    """"""
elif op == 5:
    """XNOR"""
    entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
    saida = [[1], [0], [0], [1]]
    """"""

qtd_camadas_ocultas = 10
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
        erro_saida = Matriz.subtrairMatriz(Matriz.array2object(saida[i]), redeNeural.feedfoward(entrada[i])).matriz

        for j in erro_saida:
            for k in j:
                erro.append(abs(k))
                # print(abs(k))pra eu pegar
    print("ERRO DA SAIDA\n")
    print(erro)

    if all(elemento < criterio_parada for elemento in erro):
        treino = False
        print("\n REDE TREINADA")
        print("Qtd de Loops: " + str(epoca) + "\n")


parada = True
while (parada):
    entrada = input("Digite a entrada: ")
    entrada = [int(i) for i in entrada.split(",")]
    print("SAIDA: " + str(redeNeural.feedfoward(entrada).matriz))
