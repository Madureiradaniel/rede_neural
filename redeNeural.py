from matriz import Matriz
import math

class NeuralNetwork(object):

    def __init__(self, nos_entrada, nos_oculto, nos_saida, learning_rate):
        self.nos_entrada = nos_entrada
        self.nos_oculto = nos_oculto
        self.nos_saida = nos_saida
        self.learning_rate = learning_rate

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

    def feedfoward(self, lista):

        entrada = Matriz.array2matriz(lista)
        """ CAMADA DE ENTRADA PARA CAMADA OCULTA"""
        #print("\n------ CAMADA ENTRADA => CAMADA OCULTA -----")
        camada_oculta = Matriz.multiplicaDuasMatriz(self.pesos_entrada_oculta, entrada)
        camada_oculta = Matriz.somarDuasMatriz(camada_oculta, self.bias_entrada_oculta)
        camada_oculta.aplicarSigmoid()
        #camada_oculta.printMatriz()

        """ CAMADA OCULTA PARA CAMADA DE SAIDA"""
        #print("\n------CAMADA OCULTA -> CAMADA SAIDA-----")
        camada_saida = Matriz.multiplicaDuasMatriz(self.pesos_oculta_saida, camada_oculta)
        camada_saida = Matriz.somarDuasMatriz(camada_saida, self.bias_oculta_saida)
        camada_saida.aplicarSigmoid()
        #camada_saida.printMatriz()

        return camada_saida

    def backpropagation(self, entrada, esperado):
        """transformando a entrada em matriz"""
        entrada = Matriz.array2matriz(entrada)

        """feedfoward"""
        """ CAMADA DE ENTRADA PARA CAMADA OCULTA"""
        print("\n------ CAMADA ENTRADA => CAMADA OCULTA -----")
        camada_oculta = Matriz.multiplicaDuasMatriz(self.pesos_entrada_oculta, entrada)
        camada_oculta = Matriz.somarDuasMatriz(camada_oculta, self.bias_entrada_oculta)
        camada_oculta.aplicarSigmoid()
        camada_oculta.printMatriz()

        """ CAMADA OCULTA PARA CAMADA DE SAIDA"""
        print("\n------CAMADA OCULTA -> CAMADA SAIDA-----")
        camada_saida = Matriz.multiplicaDuasMatriz(self.pesos_oculta_saida, camada_oculta)
        camada_saida = Matriz.somarDuasMatriz(camada_saida, self.bias_oculta_saida)
        camada_saida.aplicarSigmoid()
        camada_saida.printMatriz()

        """backpropagation"""
        esperado = Matriz.array2matriz(esperado)

        """SAIDA P/ OCULTA"""
        """calculo do erro"""
        erro_de_saida  = Matriz.subtrairMatriz(esperado, camada_saida)
        #erro_de_saida.printMatriz()

        derivada_da_saida = self.derivadaElementosMatriz(camada_saida)
        #derivada_da_saida.printMatriz()

        """multiplicacao hadamard"""
        gradiente = Matriz.hadamard(erro_de_saida, derivada_da_saida)
        #gradiente.printMatriz()

        """aplicando learning_rate"""
        gradiente = Matriz.produtoEscalar(gradiente, self.learning_rate)

        """AJUSTAR BIA"""
        self.bias_oculta_saida = Matriz.somarDuasMatriz(self.bias_oculta_saida, gradiente)


        """multiplicando pela camada oculta transposta"""
        oculta_transposta = Matriz.transporMatriz(camada_oculta)
        gradiente = Matriz.multiplicaDuasMatriz(gradiente, oculta_transposta)
        #gradiente.printMatriz()

        self.pesos_oculta_saida = Matriz.somarDuasMatriz(self.pesos_oculta_saida, gradiente)
        """"""

        """CAMADA OCULTA P/ ENTRADA """
        peso_oculta_saida_transposta = Matriz.transporMatriz(self.pesos_oculta_saida)
        erro_oculta = Matriz.multiplicaDuasMatriz(peso_oculta_saida_transposta, erro_de_saida)
        #erro_oculta.printMatriz()

        """aplicando derivada camada oculta"""
        derivada_camada_oculta = self.derivadaElementosMatriz(camada_oculta)
        entrada_transposta = Matriz.transporMatriz(entrada)

        gradiente_oculta = Matriz.hadamard(erro_oculta, derivada_camada_oculta)
        gradiente_oculta = Matriz.produtoEscalar(gradiente_oculta, self.learning_rate)

        """AJUSTAR BIA"""
        self.bias_entrada_oculta = Matriz.somarDuasMatriz(self.bias_entrada_oculta, gradiente_oculta)

        gradiente_oculta = Matriz.multiplicaDuasMatriz(gradiente_oculta, entrada_transposta)
        self.pesos_entrada_oculta = Matriz.somarDuasMatriz(self.pesos_entrada_oculta, gradiente_oculta)


    """derivada sigmoid  = sigmoid * (1 - sigmoid) """
    def derivadaSigmoide(self, x):
        return x * (1 - x)

    """aplicando derivada em toda matriz"""
    def derivadaElementosMatriz(self, camada):
        matriz = Matriz(camada.linhas, camada.colunas)
        for i in range(matriz.linhas):
            for j in range(matriz.colunas):
                matriz.matriz[i][j] = self.derivadaSigmoide(camada.matriz[i][j])
        return matriz

