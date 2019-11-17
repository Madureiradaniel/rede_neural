from matriz import *

m1 = Matriz(2, 4)
m2 = Matriz(4, 2)
#m3 = Matriz.somarDuasMatriz(m1,m2)

m1.printMatriz()
print("-------------------")
m2.printMatriz()
print("-------------------")

m3 = Matriz.multiplicaDuasMatriz(m1, m2)
m3.printMatriz()
