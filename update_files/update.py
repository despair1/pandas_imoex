import upinit
import pandas as pd
import os
from load_bond_imoex import get_candlestick_data


def update():
    dict = {}
    for i in upinit.bonds_list:
        folder_path = upinit.bonds_dir
        # print(folder_path)
        df = get_candlestick_data(i,start_date=upinit.start_day)
        i = i + ".csv"
        f = os.path.join(folder_path, i)
        print(df)
        df.to_csv(f,index=False)

update()