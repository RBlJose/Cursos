import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

#suma
sum = np.sum(arr)
print(sum)

#promedio
mean = np.mean(arr)
print(mean)

#mediana
mediana = np.median(arr)
print(mediana)

#producto
prod = np.prod(arr)
print(prod)

#Desviacion estandar
desv_est = np.std(arr)
print(desv_est)

# varianza
var = np.var(arr)
print(var)

#minimo y maximo
min = np.min(arr)
max = np.max(arr)
print(min, max)

#Suma acumulativa
comsum = np.cumsum(arr)
print(comsum)

#Suma elemento-wise (elemento a elemento)
print(arr + arr)