import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from load_csv_bonds import load_bonds
from rename_columns import rename_col


df = load_bonds()
rename_col(df)
# df = df[-200:]
df = df.rename(columns=lambda x: x[:5])
print(df.index[-200])
# df = df[-100:]
for i in df.columns:
    sns.boxplot(data = df , x= pd.PeriodIndex(df.index, freq='W'),
            y=df[i])
    plt.show()



# sns.violinplot(data = df,x=df.columns[0])
# plt.show()