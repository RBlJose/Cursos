import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
edad_autos = np.random.randint(0,20, size=200)
precio_autos = 30-edad_autos + np.random.normal(-3, 3, 200)
data = pd.DataFrame(
    {
        'Precio': precio_autos,
        'Edad': edad_autos
    }
)
print(data)

fig, ax =plt.subplots(2,2 , figsize=(12,10))
ax[0,0].scatter(data['Edad'], data['Precio'], alpha= 0.5)
ax[0,0].set_xlabel('Edad del auto (años)')
ax[0,0].set_ylabel('Precio (Miles de dolares)')
ax[0,0].set_title('Edad vs Precio')

sns.histplot(data['Edad'], ax=ax[0,1], kde= True, color='g')
ax[0,1].set_xlabel('Edad del auto (años)')
ax[0,1].set_ylabel('Frecuencia')
ax[0,1].set_title('Histograma de Edad de los automotores')
 
sns.histplot(data['Precio'], ax=ax[1,0], kde= True, color='b')
ax[1,0].set_xlabel('Precio del automotores(miles de dolares)')
ax[1,0].set_ylabel('Frecuencia')
ax[1,0].set_title('Histograma del precio del automotor')

ax[1,1].axis('off')
plt.subplots_adjust(wspace=0.3 , hspace=0.3)
plt.show()