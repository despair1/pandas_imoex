from load_csv_bonds import load_bonds
from rename_columns import rename_col
import pandas as pd
import matplotlib.pyplot as plt

df = load_bonds()
rename_col(df)
df = df[-200:]

colx = 4
for i in range(4):
    df.plot(kind="scatter", x=df.columns[colx], y=df.columns[i])
plt.show()
