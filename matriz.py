from random import *

class Matriz(object):

    def __init__(self, linhas, colunas):
        self.matriz = []
        self.linhas = linhas
        self.colunas = colunas

        for i in range(self.linhas):
            self.matriz.append([])
            for j in range(self.colunas):
                self.matriz[i].append(randrange(1,8))

    def printMatriz(self):
        for i in self.matriz:
            print(i)

    @staticmethod
    def somarDuasMatriz(m1, m2):

        linhas = len(m1.matriz)
        colunas = len(m1.matriz[0])
        m3 = Matriz(linhas,colunas)

        for i in range(linhas):
            for j in range(colunas):
                m3.matriz[i][j] = m1.matriz[i][j] + m2.matriz[i][j]
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












