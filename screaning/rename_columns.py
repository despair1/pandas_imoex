import scr_init
import pandas as pd


def rename_col(df: pd.DataFrame):
    for i in scr_init.names2blank:
        df.columns = df.columns.str.replace(i,"")
    for substr, suffix in scr_init.col_suffix:
        df.rename(columns=lambda x: x + suffix if substr in x else x, inplace=True)