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

def xcombo_mae(df: pd.DataFrame, mae_len = lrinit.mae_Len,
               col_num = 5, comb = 5) -> pd.DataFrame:
    mae = {
        "mae": [],
        "col": [],
        "pred": []
    }
    df.columns = df.columns.str.slice(0, 5)
    # print("LLLLLLLLLLLLL", len(df))
    prev = df.index[-2]
    for i in all_col_combo(col_num, comb):
        x_col = []
        for ii in i:
            x_col.append(df.columns[ii])
        # print("xxxxxxxxx", x_col)

        df1 = predict(df, x_col, prev, lrinit.ylag1, lrinit.ypred)
        # print(df1[[lrinit.ylag1,lrinit.ypred]])
        pr = df1[lrinit.ypred].iat[-1]
        df1 = df1[:prev]
        ml = df.index[- mae_len]
        mae1 = mean_absolute_error(df1.loc[ml:,[lrinit.ylag1]],df1.loc[ml:,[lrinit.ypred]])

        # print("mmmmmmmmm", mae1)
        mae["mae"].append(mae1)
        mae["col"].append(x_col)
        mae["pred"].append(pr)

    df4 = pd.DataFrame(mae)
    sorted_df = df4.sort_values(by='mae')
    # print(sorted_df["col"].iat[0]," {:.3f}".format(sorted_df["mae"].iat[0]))
    # df1 = predict(df, sorted_df["col"].iat[0], prev, lrinit.ylag1, lrinit.ypred, True)
    return sorted_df

# print(sorted_df)


