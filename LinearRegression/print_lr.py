import scr_init
import lrinit
from load_csv_bonds import  load_bonds
from rename_columns import rename_col
from sklearn.linear_model import LinearRegression
import pandas as pd

df = load_bonds(start_day=scr_init.start_hist)
rename_col(df)
df = df.dropna()
ycol = df.columns.to_series().str.contains(lrinit.testing).idxmax()
# ci = df.columns.get_loc(ci)
df[lrinit.ylag1] = df[ycol].shift(-1)
print(df[[ycol,lrinit.ylag1]])
x_col = [ycol]
prev = df.index[-2]
print("DDDDDDDDDD",prev)
# print(df.iloc[-1].index)
X = df.loc[:prev,x_col]
y = df.loc[:prev,lrinit.ylag1]  # target

# Train the model
model = LinearRegression()
model.fit(X, y)

# Store the fitted values as a time series with the same time index as
# the training data
df[lrinit.ypred] = model.predict(df.loc[:,x_col])
print(df[[ycol,lrinit.ylag1,lrinit.ypred]])
# print(df.iloc[:,[ci]])