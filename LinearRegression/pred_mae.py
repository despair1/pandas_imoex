from itertools import combinations
from all_col_combo import all_col_combo
from load_csv_bonds import load_bonds
import scr_init
from rename_columns import rename_col
import lrinit
from predict import predict
from sklearn.metrics import mean_absolute_error
import pandas as pd

# df = load_bonds(start_day=scr_init.start_hist)
# rename_col(df)
# df = df.dropna()
# ycol = df.columns.to_series().str.contains(lrinit.testing).idxmax()
# df[lrinit.ylag1] = df[ycol].shift(-1)

def pred_mae(df: pd.DataFrame, x_col_nums,
             mae_len = lrinit.mae_Len) -> pd.DataFrame:

    df.columns = df.columns.str.slice(0, 5)
    # print("LLLLLLLLLLLLL", len(df))
    prev = df.index[-2]
    # print("PRRRRRRRR", prev, x_col)
    x_col = df.columns[0:x_col_nums]
    df1 = predict(df, x_col, prev, lrinit.ylag1, lrinit.ypred)
    # print(df1[[lrinit.ylag1,lrinit.ypred]])
    pr = df1[lrinit.ypred].iat[-1]
    df1 = df1[:prev]
    ml = df.index[- mae_len]
    mae1 = mean_absolute_error(df1.loc[ml:,[lrinit.ylag1]],df1.loc[ml:,[lrinit.ypred]])

    return pr,mae1

# print(sorted_df)


