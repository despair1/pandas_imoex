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
from pred_mae import pred_mae

pd.options.mode.copy_on_write = True
df = load_bonds(start_day=scr_init.start_hist)
rename_col(df)
df = df.dropna()
print(df.index[-20])
print(df.index[-15])
print(df.index[-10])
print(df.index[-5])
print("LastDay in csv  ", df.index[-1] )
df_save = df

pd.options.display.float_format = '{:.3f}'.format
rep = []
short_names = {}
for key in lrinit.selected_tables.keys():
    for bond in df.columns:
        if key in bond:
            short_names[key] = bond
print(short_names)
for key in lrinit.selected_tables.keys():
    bond = short_names[key]
    df = df_save

    df_short = pd.DataFrame()

    for i in lrinit.selected_tables[key]:
        for k in lrinit.selected_tables[key]:
            for bond in df.columns:
                if k in bond:
                    short_names[k] = bond
        df_short[short_names[i]] = df[short_names[i]]
    # print(df_short)
    df_short[lrinit.ylag1] = df[bond].shift(-1)
    df = df_short
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
    for x in x_num:
        xx = df.index[-x]
        df2 = df.loc[xx:]
        for y in mae_len:
            # print("EEEEEEEEE", df.columns)
            x_col = []
            for i in lrinit.selected_tables[key]:
                x_col.append(short_names[i])
            # print("XKKKKKKKK", x_col, df2.columns)



            pr,mae = pred_mae(df2,len(lrinit.selected_tables[key]), y)
            # print(x,y)
            # print(df1.head())
            df_mae[x].append(mae)
            # df_mae[x].append(df1["pred"].iat[0])
            df_pred[x].append(pr)


    df3 = pd.DataFrame(df_mae, index=mae_len)
    # df3.index.name = bond+"_mae"
    nmin = " {:.3f}".format(df3.min().min())
    nmean = " {:.3f}".format(df3.mean().mean())
    nmax = " {:.3f}".format(df3.max().max())
    print(bond+"_mae", nmin, nmean, nmax)
    rep.append([bond+"_mae", nmin, nmean, nmax])
    print(df3)
    mae_m = nmean
    # print(df3.min().min(), df3.mean().mean(), df3.max().max())
    df3 = pd.DataFrame(df_pred, index=mae_len)
    # df3.index.name = bond + "_pred"
    nmin = " {:.3f}".format(df3.min().min())
    nmean = " {:.3f}".format(df3.mean().mean())
    nmax = " {:.3f}".format(df3.max().max())
    print(bond + "_pred", nmin, nmean, nmax)
    rep.append([bond + "_pred", nmin, nmean, nmax])
    print(df3)
    print("BBBB", bond," dif min max pred - mean mae ", " {:.3f}".format(df3.max().max()-
                                         df3.min().min()), mae_m )
    rep.append(["BBBB", bond," dif min max pred - mean mae ", " {:.3f}".format(df3.max().max()-
                                                                               df3.min().min()), mae_m])
    print()
    # print( "{:.3f}".format(df3.min().min()), df3.mean().mean(), df3.max().max())
    # for x in x_num:
    #     xx = df.index[-x]
    #     df2 = df.loc[xx:]
    #     df1 = xcombo_mae(df2, 10)
    #     print(df1.head())
for x in rep:
    print(x)