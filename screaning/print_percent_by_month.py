from load_bonds import load_bonds
from rename_columns import rename_col
import pandas as pd

df = load_bonds()
rename_col(df)
df = df.resample("ME").mean()
df.columns = [col[:5] for col in df.columns]
print(df)
# print(range(df.shape[1]))
pd.options.display.float_format = '{:.2f}'.format
for i in range(df.shape[1]):
    df["y"] = df.iloc[:,i].shift(-1)
    c = df.columns[i]
    df[c] = df["y"]/df[c]
    df[c] = (df[c]**12-1)*100
del df["y"]
print(df)