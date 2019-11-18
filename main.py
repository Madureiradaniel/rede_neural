from redeNeural import NeuralNetwork
from matriz import *

""" entrada, oculta e saida"""
redeNeural = NeuralNetwork(1,3,1)
lista = [6, 3, 4, 5, 1]

redeNeural.feedforward(lista)