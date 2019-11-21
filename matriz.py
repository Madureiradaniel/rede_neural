from random import *
import math

class Matriz(object):

    def __init__(self, linhas, colunas):
        self.matriz = []
        self.linhas = linhas
        self.colunas = colunas

        for i in range(self.linhas):
            self.matriz.append([])
            for j in range(self.colunas):
                self.matriz[i].append(random())

    def printMatriz(self):
        for i in self.matriz:
            print(i)

    def __sigmoide(self, x):
        x = 1/(1 + math.exp(-x))
        return x

    def aplicarSigmoid(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                self.matriz[i][j] = self.__sigmoide(self.matriz[i][j])


    @staticmethod
    def transporMatriz(m1):

        transposta = Matriz(m1.colunas, m1.linhas)
        for i in range(m1.linhas):
            for j in range(m1.colunas):
                transposta.matriz[j][i] = m1.matriz[i][j]

        return transposta

    @staticmethod
    def produtoEscalar(m1, escalar):

        linhas = len(m1.matriz)
        colunas = len(m1.matriz[0])
        m3 = Matriz(linhas,colunas)

        for i in range(linhas):
            for j in range(colunas):
                m3.matriz[i][j] = m1.matriz[i][j] * escalar
        return m3

    @staticmethod
    def hadamard(m1, m2):

        linhas = len(m1.matriz)
        colunas = len(m1.matriz[0])
        m3 = Matriz(linhas,colunas)

        for i in range(linhas):
            for j in range(colunas):
                m3.matriz[i][j] = m1.matriz[i][j] * m2.matriz[i][j]
        return m3

    @staticmethod
    def somarDuasMatriz(m1, m2):

        linhas = m1.linhas
        colunas = m1.colunas
        m3 = Matriz(linhas,colunas)

        for i in range(linhas):
            for j in range(colunas):
                m3.matriz[i][j] = m1.matriz[i][j] + m2.matriz[i][j]
        return m3

    @staticmethod
    def subtrairMatriz(m1, m2):

        linhas = len(m1.matriz)
        colunas = len(m1.matriz[0])
        m3 = Matriz(linhas,colunas)

        for i in range(linhas):
            for j in range(colunas):
                m3.matriz[i][j] = m1.matriz[i][j] - m2.matriz[i][j]
        return m3

    @staticmethod
    def multiplicaDuasMatriz(m1, m2):
        m3 = Matriz(m1.linhas, m2.colunas)

        #zerar matriz 3
        for i in range(m3.linhas):
            for j in range(m3.colunas):
                m3.matriz[i][j] = 0

        for m1Linha in range(m1.linhas):
            for m1Coluna in range(m1.colunas):
                for m2Coluna in range(m2.colunas):
                    # print(m1.matriz[m1Linha][m1Coluna] * m2.matriz[m1Coluna][m2Coluna])
                    m3.matriz[m1Linha][m2Coluna] += m1.matriz[m1Linha][m1Coluna] * m2.matriz[m1Coluna][m2Coluna]
                    #print("---------debug------")
                    #m3.printMatriz()
        return m3

    @staticmethod
    def array2object(lista):
        m1 = Matriz(len(lista), 1)

        for i in range(m1.linhas):
            for j in range(m1.colunas):
                m1.matriz[i][j] = lista[i]

        return m1














