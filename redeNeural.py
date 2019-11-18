from matriz import Matriz
import math

class NeuralNetwork(object):

    def __init__(self, nos_entrada, nos_oculto, nos_saida):
        self.nos_entrada = nos_entrada
        self.nos_oculto = nos_oculto
        self.nos_saida = nos_saida

        print("\n------bias entrada para oculta---")
        self.bias_entrada_oculta = Matriz(self.nos_oculto, 1)
        self.bias_entrada_oculta.printMatriz()

        print("\n------bias oculta para saida---")
        self.bias_oculta_saida = Matriz(self.nos_saida, 1)
        self.bias_oculta_saida.printMatriz()

        print("\n------pesos entrada para oculta---")
        self.pesos_entrada_oculta = Matriz(self.nos_oculto, self.nos_entrada)
        self.pesos_entrada_oculta.printMatriz()

        print("\n------pesos da oculta para a saida-----")
        self.pesos_oculta_saida = Matriz(self.nos_saida, self.nos_oculto)
        self.pesos_oculta_saida.printMatriz()


    def feedforward(self, entrada):
        """transformando a entrada em matriz"""
        matriz_entrada = Matriz.array2matriz(entrada)

        """ CAMADA DE ENTRADA PARA CAMADA OCULTA"""
        print("\n------ CAMADA ENTRADA => CAMADA OCULTA -----")
        camada_oculta = Matriz.multiplicaDuasMatriz(self.pesos_entrada_oculta, matriz_entrada)
        camada_oculta = Matriz.somarDuasMatriz(camada_oculta, self.bias_entrada_oculta)
        camada_oculta.aplicarSigmoid()
        camada_oculta.printMatriz()

        """ CAMADA OCULTA PARA CAMADA DE SAIDA"""
        print("\n------CAMADA OCULTA -> CAMADA SAIDA-----")
        camada_saida = Matriz.multiplicaDuasMatriz(self.pesos_oculta_saida, camada_oculta)
        camada_saida = Matriz.somarDuasMatriz(camada_saida, self.bias_oculta_saida)
        camada_saida.aplicarSigmoid()
        camada_saida.printMatriz()

