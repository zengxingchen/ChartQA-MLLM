
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'Electronics': [2000, 2100, 1900, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000],
    'Clothing': [1500, 1600, 1450, 1550, 1650, 1750, 1800, 1850, 1900, 1950, 2000, 2100],
    'HomeGoods': [800, 950, 700, 750, 850, 900, 950, 1000, 1100, 1150, 1200, 1300]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

# Getting cumulative values for stacking in the area plot
df_cum = df.cumsum(axis=1)

# Specific color codes for better visual appeal
colors = ['#FF5733', '#33FF57', '#3357FF']

# Increase the size of the plot
plt.figure(figsize=(14, 8))

# Stacking each column one by one
plt.fill_between(df.index, 0, df_cum['Electronics'], color=colors[0], alpha=0.5, label='Electronics')
plt.fill_between(df.index, df_cum['Electronics'], df_cum['Electronics'] + df_cum['Clothing'], color=colors[1], alpha=0.5, label='Clothing')
plt.fill_between(df.index, df_cum['Electronics'] + df_cum['Clothing'], df_cum['Electronics'] + df_cum['Clothing'] + df_cum['HomeGoods'], color=colors[2], alpha=0.5, label='HomeGoods')

# Add labels to the plot
for category in ['Electronics', 'Clothing', 'HomeGoods']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category, verticalalignment='center')

# Set the title and other chart settings
plt.title('Monthly Sales by Product Category')
plt.xlabel('Month')
plt.ylabel('Sales (In Thousands)')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()

plt.show()