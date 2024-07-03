
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
data = {
    'Country': ['Canada', 'Germany', 'UK', 'Japan', 'USA'],
    'Education': [15, 20, 10, 25, 30],
    'Employment': [50, 40, 60, 45, 40],
    'Healthcare': [20, 25, 20, 20, 15],
    'Leisure': [15, 15, 10, 10, 15]
}

df = pd.DataFrame(data)
df.set_index('Country', inplace=True)

# Calculate the percentage
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Bar Width
barWidth = 0.5

fig, ax = plt.subplots(figsize=(12, 8))

bars = np.add(df_percentage['Education'], df_percentage['Employment']).tolist()

# Create horizontal bars
ax.barh(df.index, df_percentage['Education'], color=colors[0], edgecolor='grey', height=barWidth, label='Education')
ax.barh(df.index, df_percentage['Employment'], left=df_percentage['Education'], color=colors[1], edgecolor='grey', height=barWidth, label='Employment')
ax.barh(df.index, df_percentage['Healthcare'], left=bars, color=colors[2], edgecolor='grey', height=barWidth, label='Healthcare')
ax.barh(df.index, df_percentage['Leisure'], left=np.add(bars, df_percentage['Healthcare']).tolist(), color=colors[3], edgecolor='grey', height=barWidth, label='Leisure')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Percentage')
ax.set_title('Percentage Distribution of Budget by Sector and Country')
ax.set_xlim(0, 100)
ax.set_xticks(np.arange(0, 101, 10))

# Add a legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)

# Display the values on the bars
for index, value in enumerate(df_percentage.index):
    for col in df_percentage.columns:
        # Get the value and the sum of previous elements
        bar_value = df_percentage.at[value, col]
        sum_previous = df_percentage.loc[value, :col].sum() - bar_value
        ax.text(sum_previous + bar_value / 2, index, f'{bar_value:.1f}%', va='center', ha='center')

plt.show()