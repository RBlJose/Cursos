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

#agrupaciond de datos por ciudad
grouped = df.groupby('Ciudad')
print (grouped.groups)

grouped = df.groupby('Nombre')
print (grouped.groups)