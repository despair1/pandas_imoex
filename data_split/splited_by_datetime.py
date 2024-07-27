import pandas as pd
import dsinit



def splited_by_datetime(df: pd.DataFrame, dt) -> pd.DataFrame :
    st = dt[0]
    tmst = dt[1:]

    df_dict = { dsinit.date : [], dsinit.count_col : [],
                dsinit.low_col : [], dsinit.mean_col : [],
                dsinit.high_col : [],
                dsinit.b_col : [], dsinit.e_col: []}
    for i in tmst:
        # print(df[st:i].describe())
        df1 = df[st:i]
        df_dict[dsinit.date].append(df1.index[0])
        df_dict[dsinit.count_col].append(df1[dsinit.open_col].count())
        df_dict[dsinit.mean_col].append(df1[dsinit.open_col].mean())
        df_dict[dsinit.low_col].append(df1[dsinit.low_col].quantile(dsinit.qlow))
        df_dict[dsinit.high_col].append(df1[dsinit.high_col].quantile(dsinit.qhigh))
        df_dict[dsinit.b_col].append(df1[dsinit.open_col].iloc[0:dsinit.begin].mean())
        df_dict[dsinit.e_col].append(df1[dsinit.open_col].iloc[dsinit.end:].mean())
        st=i
        df1 = pd.DataFrame(df_dict)
    return df1