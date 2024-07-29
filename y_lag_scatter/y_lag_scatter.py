from load_csv_bonds import load_bonds
from rename_columns import rename_col
import pandas as pd
import matplotlib.pyplot as plt

df = load_bonds()
rename_col(df)
start_date = -200
print(df.index[start_date])
df = df[start_date:]

colx = 4
df["y_lag"] = df.iloc[:,[colx]].shift(-1)
for i in range(6):
    if i == colx: continue
    df.plot(kind="scatter", x=df.columns[colx], y=df.columns[i])
plt.show()
