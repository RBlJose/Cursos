import pandas as pd

#series en pandas
numeros = [3,4,5,6,7,8]
serie = pd.Series(numeros)
print(serie, type(serie))

data = {
    'nombre': ['ana', 'juan', 'pedro', 'maria', 'luis'],
    'edad': [22, 25, 26, 19, 31],
    'cuidad': ['madrid', 'barcelona', 'valencia', 'sevilla', 'bilboa']
}

print(data, type(data))

# generamos dataframe

df = pd.DataFrame(data=data)

print(df, type(df))

#exportar datafram

df.to_csv('Data.csv')

#importar un datafram

import_df = pd.read_csv('data.csv')
print(import_df)


# seleccionar una columna

nombre = df['nombre']
print(nombre)


#seleccionar una o mas columnas
edad_nombre = df[['nombre' , 'edad']]
print(edad_nombre)

#filtrar por indice
fila = df.loc[2]
print(fila)

# filtrar por condiciones
fila = df[df['edad'] > 23]
print(fila)

#filtrar por dos o mas condiciones
filtro = (df['edad'] > 23)  &  (df['nombre'].str.startswith('p')) 
print(df[filtro])

#filtro por query
filtro = df.query('edad < 23')
print(filtro)

#filtro por condiciones de nombre
filtro =df[df['nombre'].isin(['ana', 'carlos', 'jose', 'pedro'])]
print(filtro)

#filtro por condiciones de longitud de la variable
def longitud(nombre):
    return len(nombre) == 5

print(df[df['nombre'].apply(longitud)])

#filtrar por condiciones multiples
filtro = df[df['edad'].between(25, 35)]
print(filtro)



