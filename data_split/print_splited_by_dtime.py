import dsinit
import scr_init
from load_bond_imoex import get_candlestick_data
import pandas as pd
from splited_by_datetime import splited_by_datetime

def get_dict_tmpstmp_by_val(dict = dsinit.split_by_decreasing_values):
    for key, val in dict.items():
        df = get_candlestick_data(ticker=key,start_date=dsinit.start_day)
        # df1 = df[[dsinit.begin_col, dsinit.open_col]]
        df[scr_init.begin_col] = pd.to_datetime(df[scr_init.begin_col])
        df.set_index(scr_init.begin_col, inplace=True)
        indexes = []
        indexes.append(df.index[0])
        for i in val:
            for index, value in df[scr_init.open_col].items():
                if value < i:
                    indexes.append(index)
                    # print(index)
                    break
        indexes.append(df.index[-1])
        # print(indexes)
        # print(df.dtypes)
        if len(indexes)<2: continue
        pd.options.display.float_format = '{:.2f}'.format
        ds = splited_by_datetime(df,indexes)
        ds["decr"] = (ds[dsinit.e_col] - ds[dsinit.b_col]) / ds[dsinit.count_col] * 10
        print(ds)

get_dict_tmpstmp_by_val()