#%%
# Change the name of the files in the folder
import os
import glob
for file in glob.glob('*'):
    print(file)
    os.rename(file, file.replace('IF_2015', 'IF_temporada2015'))


# %%
