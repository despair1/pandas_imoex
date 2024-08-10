import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from load_csv_bonds import load_bonds
from rename_columns import rename_col


df = load_bonds()
rename_col(df)
# df = df[-200:]
df = df.rename(columns=lambda x: x[:5])

# df.hist(histtype = "stepfilled", alpha=0.5)
sns.histplot(df)
plt.show()