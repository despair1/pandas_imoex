import pandas as pd
from typing import List
from sklearn.linear_model import LinearRegression


def predict(df : pd.DataFrame, x_col_names: List, last_y_index,
            y_col_name: str, pred_col_name ):
    X = df.loc[:last_y_index, x_col_names]
    y = df.loc[:last_y_index, y_col_name]  # target
    model = LinearRegression()
    model.fit(X, y)
    df[pred_col_name] = model.predict(df.loc[:, x_col_names])

    return df