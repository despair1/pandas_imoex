import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from load_csv_bonds import load_bonds
from rename_columns import rename_col
from statsmodels.tsa.stattools import adfuller


df = load_bonds()
rename_col(df)
# df = df[-200:]
df = df.rename(columns=lambda x: x[:5])
print(df.columns[0])
col = df.columns[0]
df = df.dropna()
# print(adfuller(df[:,[0]]))
for i in df.columns:
    print(i,adfuller(df[i]))