import numpy as np
import pandas as pd

data = {
    'nombre': ['ana', 'juan', 'pedro', 'maria', 'luis'],
    'edad': [22, 25, np.nan, 19, 31],
    'ciudad': ['madrid', 'barcelona', 'valencia', None, 'bilboa']
}

df = pd.DataFrame(data)
print(df)

#rellenar valores faltantes
df1 = df.copy()
df_fill = df1.fillna(
    {
        'edad' : df1['edad'].mean(),
        'ciudad' : 'Desconocido'
    }
)
print(df_fill)

# eliminar vaores faltante
df2 = df.copy()
df_sin_nan = df2.dropna()
print(df_sin_nan)

#remplazar valores
df3 = df.copy()
df_reem = df3.replace(
    {
        'ciudad': {None : 'Desconocido'}
    }
)
print(df_reem)

#interpolar valores
df4 = df.copy()
df4['edad'] = df['edad'].interpolate()
print(df4)


data_duplicada = {
    "Nombre" : ["Ana", 'Juan', 'Pedro', 'Maria', 'Luis', 'Ana', 'Juan'], 
    "Edad" : [22, 25, np.nan, 23, 20, 22, 25],
    ' Ciudad' : ['Barcelona', 'Madrid', 'Valencia', None , 'Bilbao', 'Barcelona', 'Madrid']
}
df_duplicado = pd.DataFrame(data_duplicada)
print(df_duplicado)

#eliminar duplicados
df_sin_duplicar = df_duplicado.drop_duplicates()
print(df_sin_duplicar)

#renombrar columnas
df5 = df.copy()
df_renombrado = df5.rename(columns={'nombre' : 'name' , 'edad' : 'age' , 'ciudad' : 'city'})
print(df_renombrado)

#ordenar columnas
df6 = df.copy()
columnas = ['ciudad', 'nombre', 'edad']
df_ordenado = df6[columnas]
print ( df_ordenado)

# transformacion de datos 
df7 = df.copy()
def cuadrado (x):
    return x**2

df7['edad_cuadrado'] = df['edad'].apply(cuadrado)
print(df7)