
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = {
    'Category': ['Paris', 'London', 'New York', 'Tokyo', 'Berlin', 'Sydney', 'Toronto', 'Moscow', 'Dubai', 'Mumbai'],
    'Apples': [12, 15, 18, 10, 16, 14, 11, 13, 15, 17],
    'Bananas': [18, 20, 22, 30, 24, 26, 27, 19, 25, 21],
    'Oranges': [25, 30, 27, 35, 28, 29, 30, 33, 32, 31],
    'Cherries': [35, 35, 33, 25, 32, 31, 32, 35, 28, 31],
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
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']
bar_width = 0.6

fig, ax = plt.subplots(figsize=(10, 12))

for i, col in enumerate(df.columns):
    vals = df_percent[col]
    starts = cumulated_percent.iloc[:, i]
    ax.bar(categories, vals, bottom=starts, width=bar_width, color=colors[i], edgecolor='white')

# Customize the chart
ax.set_ylabel('Percentage')
ax.set_title('Fruit Distribution by City')
plt.yticks(np.arange(0, 101, 10))
ax.legend(df.columns, loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()