import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from load_csv_bonds import load_bonds
from rename_columns import rename_col


df = load_bonds()
rename_col(df)
# df = df[-200:]
# df = df.rename(columns=lambda x: x[:5])
print(df.index[-200])
# sns.pairplot(data = df)
# plt.show()

sns.jointplot(data=df, x=df.columns[0], y=df.columns[1])
df = df[-200:]
sns.jointplot(data=df)
plt.show()