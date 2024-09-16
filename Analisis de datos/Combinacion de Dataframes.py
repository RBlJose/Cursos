import pandas as pd
data1 = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Lauara', 'Pedro'],
    'Edad': [25, 33, 30, 28, 45],
    'Ciudad' : ['Madrid', 'Barcelona', 'Madrid', 'Valencia', 'Barcelona']
}

df1 = pd.DataFrame(data1)
print(df1)


data2 = {
    'Nombre' : ['Carla', 'Irene'],
    'Edad': [38, 27],
    'Ciudad': ['Madrid', 'Bilbao']
}

df2 = pd.DataFrame(data2)
print(df2)

#combinar ambos dataframes
df_combined = pd.concat([df1, df2], ignore_index= True)
print(df_combined)