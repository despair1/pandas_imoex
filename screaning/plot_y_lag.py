import matplotlib.pyplot as plt
import scr_init
import seaborn as sns
from load_bonds import load_bonds
import matplotlib.pyplot as plt
from rename_columns import rename_col


df = load_bonds(bonds_list=scr_init.ylag_list, start_day=scr_init.start_hist)
rename_col(df)
for i in range(df.shape[1]):
    df["y"] = df.iloc[:,i].shift(-1)
    fig, ax = plt.subplots()
    ax.plot(df[df.columns[i]], df["y"])
    sns.regplot(x=df[df.columns[i]], y=df["y"])
    s = df.iloc[0,i]
    e = df.iloc[-1,i]
    sf = f"{s:.2f}"
    ef = f"{e:.2f}"
    p = (e/s-1)*100
    pf = f"{p:.2f}"
    plt.title(f"Start {sf} End {ef} : {pf}%")
    plt.show()