import pandas as pd
import numpy as np

df = pd.read_csv('data/dummy_data/book_sales.csv', index_col="Date", parse_dates=['Date']).drop(columns='Paperback')

df['Time'] = np.arange(len(df.index))

# target = weight * time + bias

import matplotlib.pyplot as plt
import seaborn as sns

# aqui construimos el grafico
fig, ax = plt.subplots()
ax.plot('Time', 'Hardcover', data=df, color='0.75')
ax = sns.regplot(x='Time', y='Hardcover', data=df, ci=None, scatter_kws=dict(color='0.25'))
ax.set_title('Time Plot of Hardcover Sales')

# aqui desplegamos el grafico
plt.show()