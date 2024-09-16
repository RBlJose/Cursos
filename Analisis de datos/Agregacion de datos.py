import numpy as np
import pandas as pd

data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Laura', 'Pedro', 'Carla'],
    'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia', 'Barcelona', 'Madrid'], 
    'Edad': [25, 33, 30, 28, 45, 38],
    'Puntuación': [80, 90, 85, 88, 75, 91]
    }

df = pd.DataFrame(data)
print(df)

grouped = df.groupby('Ciudad')
print (grouped.groups)

# calcular la suma de las edades y puntuaciones por ciudad
agregated_data = grouped.agg(
    {
        'Edad':'mean',
        'Puntuación':'sum'
    }
)

print(agregated_data)

#definir una funcion de agrefacion
def rango(series):
    return series.max() - series.min()

agregated_data_custom = grouped.agg(
    {
        'Edad': rango,
        'Puntuación': rango
    }
)

print(agregated_data_custom)

data ['Categoria'] = ['A', 'B', 'A', 'B', 'A','B']
df = pd.DataFrame(data)

#agregacion multiple
grouped_multi = df.groupby(['Ciudad', 'Categoria'])
print(grouped_multi.groups)

agregated_data_multi = grouped_multi.agg(
    {
        'Edad': 'mean',
        'Puntuación': 'sum'
    }
)
print(agregated_data_multi)

data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Lauara'],
    'Edad': [25, 33, 30, 28]
}

df = pd.DataFrame(data)
print(df)

#agregar una columna
df['Ciudad'] = ['Madrid', 'Barcelona', 'Madrid', 'Valencia']
print(df)

#agregar una fila
new_row = pd.Series(
    {
        'Nombre': 'Pedro',
        'Edad': 45,
        'Ciudad': 'Barcelona'
    }
)

df = pd.concat([df, new_row.to_frame().T])
print(df)