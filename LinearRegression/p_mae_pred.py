
import pandas as pd

def p_mae_pred(bond, df_mae, df_pred, rep, mae_len):
    df3 = pd.DataFrame(df_mae, index=mae_len)
    # df3.index.name = bond+"_mae"
    nmin = " {:.3f}".format(df3.min().min())
    nmean = " {:.3f}".format(df3.mean().mean())
    nmax = " {:.3f}".format(df3.max().max())
    print(bond + "_mae", nmin, nmean, nmax)
    rep.append([bond + "_mae", nmin, nmean, nmax])
    # rep.append(["Count_cols", count_cols])
    print(df3)
    mae_m = nmean
    # print(df3.min().min(), df3.mean().mean(), df3.max().max())
    df3 = pd.DataFrame(df_pred, index=mae_len)
    # df3.index.name = bond + "_pred"
    nmin = " {:.3f}".format(df3.min().min())
    nmean = " {:.3f}".format(df3.mean().mean())
    nmax = " {:.3f}".format(df3.max().max())
    print(bond + "_pred", nmin, nmean, nmax)
    rep.append([bond + "_pred", nmin, nmean, nmax])
    print(df3)
    print("BBBB", bond, " dif min max pred - mean mae ", " {:.3f}".format(df3.max().max() -
                                                                          df3.min().min()), mae_m)
    rep.append(["BBBB", bond, " dif min max pred - mean mae ", " {:.3f}".format(df3.max().max() -
                                                                                df3.min().min()), mae_m])
    print()