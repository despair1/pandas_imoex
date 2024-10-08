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
import upinit
from p_mae_pred import p_mae_pred

pd.options.mode.copy_on_write = True
df = load_bonds(start_day=scr_init.start_hist)
rename_col(df)
df = df.dropna()
print(df.index[-20])
print(df.index[-15])
print(df.index[-10])
print(df.index[-5])
print("LastDay in csv  ", df.index[-1] )

pd.options.display.float_format = '{:.3f}'.format
rep = []
count_cols_dict = {}
count_cols_dict5 = {}
for bond in df.columns:
    # print(df.columns)
    # ycol = df.columns.to_series().str.contains(bond)
    # print("BBBBBBBBBBB", bond)
    df[lrinit.ylag1] = df[bond].shift(-1)


    x_num = (250,200,150,100,50)
    mae_len = (50,30,20,15,10,5)
    df_mae1 = {}
    for x in x_num:
        df_mae1[(x,"mae")]= []
        df_mae1[(x, "pred")] = []
    df_pred = {}
    for x in x_num:
        df_pred[x] = []
    # print(df_mae1)
    df_mae = { 250: [],
               200: [],
               150: [],
               100: [],
               50: []}
    # print(df.columns, len(df.columns))
    col_names = df.columns.str.slice(0, 5)
    count_cols = {}
    for x in col_names:
        count_cols[x] = 0
    count_cols5 = {}
    for x in col_names:
        count_cols5[x] = 0
    for x in x_num:
        xx = df.index[-x]
        df2 = df.loc[xx:]
        for y in mae_len:
            df1 = xcombo_mae(df2,y,len(df.columns)-1)
            for key in count_cols.keys():
                if key in df1["col"].iat[0]:
                    count_cols[key] += 1
            for key in count_cols5.keys():
                for row in range(len(df.columns) - 1):
                    # print(row)
                    if key in df1["col"].iat[row]:
                        count_cols5[key] += 1
            # print(x,y)
            # print(df1.head())
            df_mae[x].append(df1["mae"].iat[0])
            # df_mae[x].append(df1["pred"].iat[0])
            df_pred[x].append(df1["pred"].iat[0])
            df_mae1[(x,"mae")].append(df1["mae"].iat[0])
            df_mae1[(x,"pred")].append(df1["pred"].iat[0])

    # print("Count_cols", count_cols)
    count_cols_dict[bond] = count_cols
    count_cols_dict5[bond] = count_cols5

    p_mae_pred(bond,df_mae,df_pred,rep, mae_len)


for x in rep:
    print(x)
print()
for key, col in count_cols_dict.items():
    sorted_dict = dict(sorted(col.items(),
                              key=lambda item: item[1], reverse=True))
    print(key,sorted_dict)
    count_cols_dict[key]=sorted_dict
print()
for key, col in count_cols_dict5.items():
    sorted_dict = dict(sorted(col.items(),
                              key=lambda item: item[1], reverse=True))
    print(key,sorted_dict)


from bool_table_sorted_count_cols import get_bool_count_table

print(count_cols_dict)
b1,b2 = get_bool_count_table(count_cols_dict)
df3 = pd.DataFrame(df_mae, index=mae_len)
df4 = pd.DataFrame(df_pred, index=mae_len)

# print(df3[b1])
# print(b2)
p_mae_pred(bond,df_mae,df_pred,rep, mae_len)
p_mae_pred(bond,df3[b1],df4[b1],rep, mae_len)