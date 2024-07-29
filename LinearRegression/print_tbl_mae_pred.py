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

pd.options.mode.copy_on_write = True
df = load_bonds(start_day=scr_init.start_hist)
rename_col(df)
df = df.dropna()
print(df.index[-20])
print(df.index[-15])
print(df.index[-10])
print(df.index[-5])

pd.options.display.float_format = '{:.3f}'.format
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
    for x in x_num:
        xx = df.index[-x]
        df2 = df.loc[xx:]
        for y in mae_len:
            df1 = xcombo_mae(df2,y)
            # print(x,y)
            # print(df1.head())
            df_mae[x].append(df1["mae"].iat[0])
            # df_mae[x].append(df1["pred"].iat[0])
            df_pred[x].append(df1["pred"].iat[0])
            df_mae1[(x,"mae")].append(df1["mae"].iat[0])
            df_mae1[(x,"pred")].append(df1["pred"].iat[0])

    df3 = pd.DataFrame(df_mae, index=mae_len)
    # df3.index.name = bond+"_mae"
    print(bond+"_mae")
    print(df3)
    df3 = pd.DataFrame(df_pred, index=mae_len)
    # df3.index.name = bond + "_pred"
    print(bond + "_pred")
    print(df3)
    # for x in x_num:
    #     xx = df.index[-x]
    #     df2 = df.loc[xx:]
    #     df1 = xcombo_mae(df2, 10)
    #     print(df1.head())