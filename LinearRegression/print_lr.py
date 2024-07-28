import scr_init
import lrinit
from load_bonds import  load_bonds
from rename_columns import rename_col


df = load_bonds(start_day=scr_init.start_hist)
rename_col(df)
ycol = df.columns.to_series().str.contains(lrinit.testing).idxmax()
# ci = df.columns.get_loc(ci)
df[lrinit.ylag1] = df[ycol].shift(-1)
print(df[[ycol,lrinit.ylag1]])
# print(df.iloc[:,[ci]])