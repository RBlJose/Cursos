import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')
df= sns.load_dataset('tips')
print(df)

# factores q afectan a que cambien las propinas en un restaurante (sexo, fumador, clima, tipo de comida)
#sexo
promedio_total_bill = df.groupby('sex')['total_bill'].mean()
promedio_tip = df.groupby('sex')['tip'].mean()
promedio_size = df.groupby('sex')['size'].mean()
print(promedio_total_bill)
print(promedio_tip)
print(promedio_size)

sns.pairplot(df, hue='sex')
plt.show()
#los hombres son los que mas gastan a comparacion de una mesa de mujeres y dato el caso por ende son los q mayor
#propinan dejan, por otro lado los hombres vienen a comer en grupo de dos a cuatro personas por grupo por otro lado
# las mujeres entran en grupo de dos personas a menudo a nuestro restaurante

#fumador
promedio_total_bill = df.groupby('smoker')['total_bill'].mean()
promedio_tip = df.groupby('smoker')['tip'].mean()
promedio_size = df.groupby('smoker')['size'].mean()
print(promedio_total_bill)
print(promedio_tip)
print(promedio_size)
sns.pairplot(df, hue='smoker')
plt.show()
#Los no fumadores consumen y dejan mas propinas q los fumadores

#dia
promedio_total_bill = df.groupby('day')['total_bill'].mean()
promedio_tip = df.groupby('day')['tip'].mean()
promedio_size = df.groupby('day')['size'].mean()
print(promedio_total_bill)
print(promedio_tip)
print(promedio_size)
sns.pairplot(df, hue='day')
plt.show()
#los dias jueves sabado y domingo son los dias q mas se consumen, por el contrario el dia viernes el tamaño 
#de la cuenta de los clientes es baja y por ende las propinas son pequeñas, dado que este dia las pesonas por mesa
#son a los mucho de dos personas 

#tipo de comida
promedio_total_bill = df.groupby('time')['total_bill'].mean()
promedio_tip = df.groupby('time')['tip'].mean()
promedio_size = df.groupby('time')['size'].mean()
print(promedio_total_bill)
print(promedio_tip)
print(promedio_size)
sns.pairplot(df, hue='time')
plt.show()
#El ser el desayuno la primera comida y dato en los menus el precio de es mucho menor a comparacion de un almuerzon q
#son platos fuertes y mas costosos se obtienen mayor ganancia de los mismo y por ende dejan una mayor propina por ello
