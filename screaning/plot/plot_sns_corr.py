from load_csv_bonds import load_bonds
from rename_columns import rename_col
import pandas as pd
import matplotlib.pyplot as plt



df = load_bonds()
rename_col(df)
df.plot()
# df[-50:].plot()
print(df)
plt.show()
import seaborn as sns
plt.figure(1 , figsize = (17 , 8))
cor = sns.heatmap(df.corr(), annot = True)
plt.show()