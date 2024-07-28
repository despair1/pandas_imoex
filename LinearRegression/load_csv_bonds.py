import scr_init
from typing import List
import pandas as pd
from load_bond_imoex import get_candlestick_data
import upinit
import os


def load_bonds(bonds_list = upinit.bonds_list, start_day=scr_init.start_day) -> List[pd.DataFrame]:
    dfl = {}
    # for bond_name in bonds_list:
    #     dfl[bond_name] = get_candlestick_data(bond_name,start_date=start_day)
    for i in bonds_list:
        for root, dirs, files in os.walk(upinit.bonds_dir):
            for file in files:
                if i in file:
                    print(os.path.join(root, file))
                    dfl[i] = pd.read_csv(os.path.join(root, file))
    # print(dfl)
    # return
    dfa = []
    for key,df in dfl.items():
        df1 = df[[scr_init.begin_col, scr_init.open_col]]
        df1.columns = [scr_init.begin_col,key]
        dfa.append(df1)
    df_open = None
    for i, v in enumerate(dfa):
        if not i:
            df_open = v
            continue
        df_open = df_open.merge(v, on=scr_init.begin_col, how='outer', sort=False)
    # return df_open
    df_open[scr_init.begin_col] = pd.to_datetime(df_open[scr_init.begin_col])
    df_open.set_index(scr_init.begin_col, inplace=True)
    # print(df_open)
    l = df_open.iloc[-1]/df_open.iloc[0]
    # print(l)
    sorted_columns = l.sort_values(ascending=False).index
    # print(sorted_columns)
    sorted_df = df_open[sorted_columns]
    # print(l, sorted_columns)
    return sorted_df

# df = load_bonds()
# print(df)