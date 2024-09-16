import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import seaborn as sns

data = sns.load_dataset("iris")
print(data)

#grafico de dispersion
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data= data)
pl.xlabel('Longitud')
pl.ylabel('Ancho')
pl.title('Data set "Iris"')
pl.show()

#Grafico de Ridgeplot
print(data['species'].unique())
setosa = data[data['species']=='setosa']
versicolor = data[data['species']=='versicolor']
virginica = data[data['species']=='virginica']

fig, ax = pl.subplots(figsize=(8,6))
pl.xlabel('Longitud del petalo')
sns.kdeplot(setosa['petal_length'], label= 'Setosa', ax= ax , fill= True)
sns.kdeplot(versicolor['petal_length'], label= 'Versicolor', ax= ax , fill= True)
sns.kdeplot(virginica['petal_length'], label= 'Virginica', ax= ax , fill= True)
ax.legend(loc='upper right')
pl.title('Ridgeplot - Base "Iris"')
pl.show()

#Grafica de dispersion
sns.set_style('whitegrid')
palette = sns.color_palette('husl', 3)
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data= data, palette=palette )
pl.xlabel('Longitud')
pl.ylabel('Ancho')
pl.title('Data set "Iris"')
pl.show()


