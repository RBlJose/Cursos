import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')
df= sns.load_dataset('tips')
print(df)

#analisis exploratorio
print(df.head())
print(df.info())
print(df.describe())

#analis univariado
sns.histplot(data=df, x= 'total_bill', kde= True)
plt.plot()
plt.show()

sns.boxplot(data=df, x= 'total_bill')
plt.plot()
plt.show()

sns.kdeplot(data=df, x= 'total_bill')
plt.plot()
plt.show()