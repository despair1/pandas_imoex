from  load_csv_walk import load_csv_walk
from group_by_day import group_by_day
from merge_open import merge_open
import matplotlib.pyplot as plt
from sort_col_by_risen import sort_col_by_risen
from  rename_col import rename_col


def day_mean_all():
    dfs = load_csv_walk()
    dfs = group_by_day(dfs)
    df = merge_open(dfs)
    df = sort_col_by_risen(df)
    rename_col(df)
    return df