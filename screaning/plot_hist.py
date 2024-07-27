import scr_init
from load_bonds import  load_bonds
from rename_columns import rename_col
import matplotlib.pyplot as plt

df = load_bonds(start_day=scr_init.start_hist)
rename_col(df)

df.plot()
df.hist()
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()