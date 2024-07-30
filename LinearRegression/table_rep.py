



def table_rep(df, bond, desc=""):
    clist = list(zip(df,bond))
    for df3,bon in clist:
        nmin = " {:.3f}".format(df3.min().min())
        nmean = " {:.3f}".format(df3.mean().mean())
        nmax = " {:.3f}".format(df3.max().max())
        print(bon, nmin, nmean, nmax)
        # print(df3)
