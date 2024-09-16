import pandas as pd
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#convertir array en dataframes
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print (df)

#convertir data frames en array en dataframes
arr1 = df.to_numpy()
print(arr1)

#calcular el promedio de cada columna
mena= np.mean(df, axis=0)
print(mena)
mean = df.mean()
print(mean)
mean = df.mean(axis=1)
print(mean)