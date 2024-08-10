from load_csv_bonds import load_bonds
from rename_columns import rename_col
import pandas as pd
import lrinit
from xcombo_mae import xcombo_mae

dict1 = {"26222RMFS8_7.1%__2410": {'26222': 20, '26234': 19, '26243': 16, '26219': 15, '26212': 14, 'ylag1': 0},
"26234RMFS3_4.5%__2507": {'26234': 29, '26222': 24, '26219': 16, '26243': 15, '26212': 7, 'ylag1': 0},
"26219RMFS4_7.75%_2609": {'26243': 28, '26219': 27, '26222': 15, '26212': 9, '26234': 8, 'ylag1': 0},
"26212RMFS9_7.05%_2801": {'26212': 30, '26234': 27, '26219': 20, '26222': 10, '26243': 7, 'ylag1': 0},
"26243RMFS4_9.5%__3805": {'26212': 26, '26243': 20, '26219': 14, '26234': 13, '26222': 11, 'ylag1': 0}}

df = load_bonds()
rename_col(df)
df = df.dropna()
pd.options.display.float_format = '{:.3f}'.format
pd.options.mode.copy_on_write = True
def get_bool_count_table(dict1=dict1):
    for bond in dict1.keys():
        df[lrinit.ylag1] = df[bond].shift(-1)
        x_num = (250, 200, 150, 100, 50)
        mae_len = (50, 30, 20, 15, 10, 5)
        df_bool = {}
        for x in x_num:
            df_bool[x] = []
        df_bool2 = {}
        for x in x_num:
            df_bool2[x] = []
        col_names = df.columns.str.slice(0, 5)
        for x in x_num:
            xx = df.index[-x]
            df2 = df.loc[xx:]
            for y in mae_len:
                df1 = xcombo_mae(df2, y, len(df.columns) - 1)
                first_key = next(iter(dict1[bond]))
                key_iterator = iter(dict1[bond].keys())

                # Access the first and second keys
                first_key = next(key_iterator)
                second_key = next(key_iterator)

                # Print the first key
                # print(first_key)
                # print(first_key in df1["col"].iat[0])
                df_bool[x].append(first_key in df1["col"].iat[0])
                df_bool2[x].append((first_key in df1["col"].iat[0]) and
                                   (second_key in df1["col"].iat[0]))
        df_boolr = pd.DataFrame(df_bool, index=mae_len)
        print("BBBBBBBBB", bond)
        print(df_boolr)
        df_boolr2 = pd.DataFrame(df_bool2, index=mae_len)
        print(df_boolr2)
        return df_boolr, df_boolr2

get_bool_count_table()