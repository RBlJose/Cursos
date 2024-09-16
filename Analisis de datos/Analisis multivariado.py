import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')
df= sns.load_dataset('tips')
print(df)

sns.scatterplot(data=df, x='total_bill', y= 'tip')
plt.show()

sns.barplot(data=df, x='total_bill', y= 'sex', palette={'Male': 'blue', 'Female': 'red'})
plt.show()

sns.boxplot(data=df, x='total_bill', y= 'sex', palette={'Male': 'blue', 'Female': 'red'})
plt.show()

sns.pairplot(data=df, hue='sex')
plt.show()