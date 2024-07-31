from load_csv_bonds import load_bonds
from rename_columns import rename_col
import pandas as pd
import matplotlib.pyplot as plt



df = load_bonds()
rename_col(df)
df.dropna()
start_date = df.index.min()
end_date = df.index.max()
complete_date_range = pd.date_range(start=start_date, end=end_date, freq='D')
df = df.reindex(complete_date_range, method="ffill")
# df.plot()
# df[-50:].plot()
# print(df)
from statsmodels.tsa.deterministic import DeterministicProcess

dp = DeterministicProcess(
    index=df.index,  # dates from the training data
    constant=True,       # dummy feature for the bias (y_intercept)
    order=1,             # the time dummy (trend)
    drop=True,           # drop terms if necessary to avoid collinearity
)
# `in_sample` creates features for the dates given in the `index` argument
X = dp.in_sample()

print(X.head())
print(df.columns)
# plt.show()
from sklearn.linear_model import LinearRegression

y = df[df.columns[0]]  # the target

# The intercept is the same as the `const` feature from
# DeterministicProcess. LinearRegression behaves badly with duplicated
# features, so we need to be sure to exclude it here.
model = LinearRegression(fit_intercept=False)
model.fit(X, y)

y_pred = pd.Series(model.predict(X), index=X.index)

print(y_pred.head())

ax = df.plot(y=df.columns[0],  title="Tunnel Traffic - Linear Trend")
_ = y_pred.plot(ax=ax, linewidth=3, label="Trend")

# plt.show()
X = dp.out_of_sample(steps=30)
print(X.tail())

y_fore = pd.Series(model.predict(X), index=X.index)

ax = y_fore.plot(ax=ax, linewidth=3, label="Trend Forecast", color="C3")

plt.show()

print(y_fore.tail())