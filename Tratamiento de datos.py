import pandas as pd
import numpy as np

df = pd.read_csv('tratamiento_datos.csv', index_col=0)

set_gen = set(df['Género'].to_list())
set_ciudad = set(df['Ciudad'].to_list())
set_estudio = set(df['Nivel_Educación'].to_list())

#tratamiento de valores negativos
df['Edad']= df['Edad'].apply(lambda x:np.nan if x < 0 else x)
df['Ingresos']= df['Ingresos'].apply(lambda x:np.nan if x < 0 else x)
df['Hijos']= df['Hijos'].apply(lambda x:np.nan if x < 0 else x)

#imputar valores faltantes
for column in ['Edad', 'Ingresos', 'Hijos']:
    median_values = df[column].median()
    df[column].fillna(median_values, inplace=True)

for column in ['Género', 'Ciudad']:
    mode_value = df[column].mode()[0]
    df[column].fillna(mode_value, inplace=True)

#Mapeo de datos
education_mapping= {
    'Bachelors':'Bachelor',
    'mastre': 'Master',
    'pHd':'PhD',
    'no education': 'None'
}

df['Nivel_Educación'].replace(education_mapping, inplace= True)
df['Nivel_Educación'].fillna('None', inplace= True)

#Casteo de tipos
df['Edad']= df['Edad'].astype(int)
df['Hijos']= df['Hijos'].astype(int)
df['Ingresos']= df['Ingresos'].astype(float)
df['Altura']= df['Altura'].astype(float)

print(df.info())
print(df.describe())

print(df['Nivel_Educación'].value_counts())


