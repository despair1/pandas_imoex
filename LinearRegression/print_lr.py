import scr_init
import lrinit
from load_csv_bonds import  load_bonds
from rename_columns import rename_col
from sklearn.linear_model import LinearRegression
import pandas as pd
from predict import predict
from sklearn.metrics import mean_absolute_error


df = load_bonds(start_day=scr_init.start_hist)
rename_col(df)
df = df.dropna()
ycol = df.columns.to_series().str.contains(lrinit.testing).idxmax()
df[lrinit.ylag1] = df[ycol].shift(-1)
# print(df[[ycol,lrinit.ylag1]])
x_col = [ycol]
prev = df.index[-2]
print("DDDDDDDDDD",prev)
df1 = predict(df, x_col, prev, lrinit.ylag1, lrinit.ypred)
print(df1[[lrinit.ylag1,lrinit.ypred]])
df1 = df1[:prev]
mae1 = mean_absolute_error(df1[lrinit.ylag1],df1[lrinit.ypred])
print("XXXXXXXXXXXX", mae1)
print(df.columns[0])
x_col = [df.columns[0],df.columns[1], df.columns[4],
         df.columns[3],]
df1 = predict(df, x_col, prev, lrinit.ylag1, lrinit.ypred)
print(df1[[lrinit.ylag1,lrinit.ypred]])
df1 = df1[:prev]
mae2 = mean_absolute_error(df1[lrinit.ylag1],df1[lrinit.ypred])
print("XXX2222222222XXXXXXXXX", mae2)
