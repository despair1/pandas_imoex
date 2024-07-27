from load_bonds import load_bonds
from rename_columns import rename_col
import pandas as pd
import matplotlib.pyplot as plt



df = load_bonds()
rename_col(df)
df.plot()
# df[-50:].plot()
print(df)
plt.show()