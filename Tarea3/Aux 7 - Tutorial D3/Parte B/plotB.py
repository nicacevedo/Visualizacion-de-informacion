#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data
category1 = ['Fossil', 'Fossil', 'Fossil', 'Fossil', 'Renewable', 'Renewable', 'Renewable', 'Renewable']
category2 = ['CO2', 'CO2', 'Traditional', 'Traditional', 'Corn Ethanool', 'Corn Ethanool', 'Traditional', 'Traditional']
cat1 = ['{} ({})'.format(c2,c1) for c1, c2 in zip(category1, category2)]
cat2 = ['Tax Breaks', 'Direct Spending','Tax Breaks', 'Direct Spending','Tax Breaks', 'Direct Spending','Tax Breaks', 'Direct Spending']
values = [0.3, 2, 53.9, 16.3, 6.2, 6, 11.8, 5]

# Create a dataframe
df = pd.DataFrame({'cat1': cat1, 'Federal Subsidies': cat2, 'Sub': values})
df.head()

# Barplot of Sub values by cat1 and cat2
plt.figure(figsize=(10,5))
bp = sns.barplot(x='cat1', y='Sub', hue='Federal Subsidies', data=df)
for container in bp.containers:
    bp.bar_label(container)
plt.title('Federal Subsidies in different Energy Categories')
plt.xlabel('Energy Category')
plt.ylabel('Federal Subsidies (billion USD)')
plt.savefig('Barplot_Subsidies.pdf')
plt.show()
# %%
