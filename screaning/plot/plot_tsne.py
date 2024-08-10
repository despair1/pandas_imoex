from load_csv_bonds import load_bonds
from rename_columns import rename_col
import pandas as pd
import matplotlib.pyplot as plt



df = load_bonds()
rename_col(df)
# df.plot()
# df[-50:].plot()
# print(df)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Example data: 100 samples with 50 features each
df.dropna()
X = df.dropna()

# Perform t-SNE
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, n_iter=1000)
X_embedded = tsne.fit_transform(X)

# Plot the result
plt.scatter(X_embedded[:, 0], X_embedded[:, 1])
plt.title('t-SNE Visualization')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()