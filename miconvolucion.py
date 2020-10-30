import numpy as np

#Funcion que calcula la matriz resultante C despues de aplicar la operacion convolcion de A*B

def convolucion (A,B,C):
	for row in range (0, len(A)-2):
		for col in range (0, len(A[row])-2):
			C[row][col] = A[row][col]*B[0][0]+A[row][col+1]*B[0][1]+A[row][col+2]*B[0][2]+A[row+1][col]*B[1][0]+A[row+1][col+1]*B[1][1]+A[row+1][col+2]*B[1][2]+A[row+2][col]*B[2][0]+A[row+2][col+1]*B[2][1]+A[row+2][col+2]*B[2][2]
	return C 

Matriz1 = [[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
Filtro = [[1,0,2],[5,0,9],[6,2,1]]

A = np.array(Matriz1)
B = np.array(Filtro)
C = np.zeros((2,2))


def convolucion (X,Y,Z):
        for row in range (0, len(X)-2):
                for col in range (0, len(X[row])-2):
                        Z[row][col] = X[row][col]*Y[0][0]+X[row][col+1]*Y[0][1]+X[row][col+2]*Y[0][2]+X[row+1][col]*Y[1][0]+X[row+1][col+1]*Y[1][1]+X[row+1][col+2]*Y[1][2]+X[row+2][col]*Y[2][0]+X[row+2][col+1]*Y[2][1]+X[row+2][col+2]*Y[2][2]
        return Z

Matriz2 = [[1,3,5,7,9,11],[2,4,6,8,10,12],[0,1,0,7,23,2,4],[1,7,6,5,4,3],[0,0,1,16,17,18]]
Filtro2 = [[0,0,0],[1,1,1],[1,10,2]]

X = np.array(Matriz2)
Y = np.array(Filtro2)
Z = np.zeros((3,4))


print("\Clase\n")
print(convolucion(A,B,C))

print("\Actividad\n")
print(convolucion(X,Y,Z))
