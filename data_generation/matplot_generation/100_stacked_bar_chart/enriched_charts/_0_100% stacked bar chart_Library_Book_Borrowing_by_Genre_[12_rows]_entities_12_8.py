
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = {
    'Category': ['Group A', 'Group B', 'Group C', 'Group D'],
    'Apples': [10, 15, 22, 18],
    'Bananas': [20, 25, 28, 24],
    'Oranges': [30, 35, 33, 22],
    'Cherries': [40, 25, 17, 36],
}

# Create DataFrame
df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

# Calculate the percentage of each component and create cumulated data for stack plotting
df_percent = df.div(df.sum(axis=1), axis=0) * 100
cumulated_percent = df_percent.cumsum(axis=1)
cumulated_percent.insert(0, 'start', 0)

# Plot
categories = df.index
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
bar_width = 0.6

fig, ax = plt.subplots(figsize=(12, 7))

for i, col in enumerate(df.columns):
    vals = df_percent[col]
    starts = cumulated_percent.iloc[:, i]
    ax.barh(categories, vals, left=starts, height=bar_width, color=colors[i], edgecolor='white')

# Customize the chart
ax.set_xlabel('Percentage')
ax.set_title('Distribution of Fruits by Group')
plt.xticks(np.arange(0, 101, 10))
ax.legend(df.columns, loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()