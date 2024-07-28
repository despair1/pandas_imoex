from itertools import combinations
from all_col_combo import all_col_combo
from load_csv_bonds import load_bonds
import scr_init
from rename_columns import rename_col
import lrinit
from predict import predict
from sklearn.metrics import mean_absolute_error
import pandas as pd

df = load_bonds(start_day=scr_init.start_hist)
rename_col(df)
df = df.dropna()
ycol = df.columns.to_series().str.contains(lrinit.testing).idxmax()
df[lrinit.ylag1] = df[ycol].shift(-1)

mae = {
    "mae": [],
    "col": []
}
for i in all_col_combo():
    x_col = []
    for ii in i:
        x_col.append(df.columns[ii])
    print("xxxxxxxxx", x_col)
    prev = df.index[-2]
    df1 = predict(df, x_col, prev, lrinit.ylag1, lrinit.ypred)
    # print(df1[[lrinit.ylag1,lrinit.ypred]])
    df1 = df1[:prev]
    mae1 = mean_absolute_error(df1[lrinit.ylag1],df1[lrinit.ypred])
    print("mmmmmmmmm", mae1)
    mae["mae"].append(mae1)
    mae["col"].append(x_col)

df = pd.DataFrame(mae)
sorted_df = df.sort_values(by='mae')

print(sorted_df)


