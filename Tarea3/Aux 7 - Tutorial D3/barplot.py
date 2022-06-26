#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the data from the csv file
df = pd.read_csv('ive-basica-2022.csv')

# Rename columns
rename_cols = {
'PRIMERA_PRIORIDAD'  : 'vulnerables',
'DS_REGION_ESTABLE'  : 'region',
'DS_TIPO_DEPENDENCIA': 'dependencia'
}
df.rename(columns=rename_cols, inplace=True)

# Drop ll the columns that are not in ['vulnerables', 'region', 'dependencia']
df = df[['vulnerables', 'region', 'dependencia']].copy()

# Group by region and dependencia, and sum the number of vulnerables
df = df.groupby(['region', 'dependencia']).sum()
df.head()
# %%

# Create a barplot by region and dependencia
# df.reset_index(inplace=True)
sns.barplot(x='region', y='vulnerables', hue='dependencia', data=df)
plt.show()
# %%
