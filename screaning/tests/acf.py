from load_csv_bonds import load_bonds
from rename_columns import rename_col
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

df = load_bonds()
rename_col(df)
# df = df[-200:]
df = df.rename(columns=lambda x: x[:5])
print(df.columns[0])
col = df.columns[0]
df = df.dropna()
df = df[-100:]
for i in df.columns:
    plot_acf(df[i])
    plt.title(i)
plt.show()