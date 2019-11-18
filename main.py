from redeNeural import NeuralNetwork
from matriz import *

""" entrada, oculta e saida"""
redeNeural = NeuralNetwork(1, 3, 2, 0.1)

lista = [1, 2]

redeNeural.backpropagation(lista, [0, 1])

