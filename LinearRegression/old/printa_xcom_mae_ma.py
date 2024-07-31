from itertools import combinations
from all_col_combo import all_col_combo
from load_csv_bonds import load_bonds
import scr_init
from rename_columns import rename_col
import lrinit
from predict import predict
from sklearn.metrics import mean_absolute_error
import pandas as pd
from xcombo_mae import xcombo_mae

pd.options.mode.copy_on_write = True
df = load_bonds(start_day=scr_init.start_hist)
rename_col(df)
df = df.dropna()
ycol = df.columns.to_series().str.contains(lrinit.bond_for_mae_list).idxmax()
print("YYYYYYYYYY", ycol, ycol)
print(len(df.columns))
len1= len(df.columns)
ma = "ma"+ycol[2:5]
m1 = "m1"+ycol[2:5]
df[ma] = df[ycol].shift(1)
df[m1] = df[ycol].shift(2)
df = df.dropna()
# df[ma] = df[ma]/1.5+df[ycol]
# df[m1] = df[m1]/1.5+df[ma]

df[lrinit.ylag1] = df[ycol].shift(-1)

print("bond for mae  ", lrinit.bond_for_mae_list)
x_num = (250,200,150,100,50)
mae_len = (50,30,20,15,10)
df_mae = { 250: [],
           200: [],
           150: [],
           100: [],
           50: []}
df_mae_ma = {}
for x in x_num:
    df_mae_ma[x] = []
for x in x_num:
    xx = df.index[-x]
    df2 = df.loc[xx:]
    for y in mae_len:
        df1 = xcombo_mae(df2,y, len1)
        df_ma = xcombo_mae(df2, y, len1+2)
        print("start day mae wind", -x,y, ycol)
        print()
        # print(df_ma.head())
        df_mae[x].append(df1["mae"].iat[0])
        df_mae_ma[x].append(df_ma["mae"].iat[0])

from table_rep import table_rep

print(lrinit.bond_for_mae_list)
df3 = pd.DataFrame(df_mae, index=mae_len)
print(df3)
df3_ma = pd.DataFrame(df_mae_ma, index=mae_len)
print(df3_ma)
table_rep((df3,df3_ma),("std","std_with_lag2"))
# mae_last_days = 10
# print("mae last days ", mae_last_days)
# for x in x_num:
#     xx = df.index[-x]
#     print("start_training_day", xx)
#     df2 = df.loc[xx:]
#     df1 = xcombo_mae(df2, mae_last_days)
#     print(df1.head())

print("YYYYYYYYYY", ycol, ycol[2:5])