import numpy as np

#creacion de una dimension con cinco elementos
arr1 = np.array((1, 2, 3, 4, 5, 6))
print(arr1)
print(arr1.shape)
print(arr1.dtype)

#creacion de una array de matriz 2*3
arr2 = arr1.reshape((2,3))
print(arr2)
print(arr2.shape)
print(arr2.dtype)

#creacion de una matriz aleatoria de 4*4 con numeros aleatorios entre 0 y 1
arr3 = np.random.randn(4, 4)
print(arr3)
print(arr3.shape)
print(arr3.dtype)

#crear un arry en 2D
arr = np.array([[1, 2, 3],[4, 5, 6]])
print(arr)

#crea u  array de cero
arr = np.zeros((4, 4))
print(arr)

#crear un arry de unos
arr = np.ones((4, 4))

# crea una matriz identidad
arr = np.eye(4)
print(arr)

#crea una matriz de 3D 
arr = np.zeros((2, 3, 4))
print(arr)

# trasponer un array de cero
arr = arr.T
print(arr)

arr1 = np.random.rand(2, 2)
arr2 = np.random.rand(2, 2)

#Concatenar horizontalmente
arr_h = np.hstack((arr1, arr2))
print(arr_h)

#Concatenar Verticalmente
arr_v = np.vstack((arr1, arr2))
print(arr_v)