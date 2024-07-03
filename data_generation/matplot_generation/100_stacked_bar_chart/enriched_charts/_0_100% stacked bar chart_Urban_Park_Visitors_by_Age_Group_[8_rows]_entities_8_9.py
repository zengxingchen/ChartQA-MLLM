
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a dataframe from the table data
data = {
    'Year': ['2018', '2019', '2020', '2021'],
    'Google Chrome': [60, 62, 65, 67],
    'Firefox': [20, 18, 15, 13],
    'Edge': [5, 6, 7, 8],
    'Safari': [10, 9, 8, 7],
    'Other': [5, 5, 5, 5]
}

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Define the colors for the different browsers
colors = ['#4285F4', '#FF7139', '#00A4EF', '#BBC1C6', '#34A853']

# Data for stacking
columns = df.columns
n_rows = len(df)

# Initialize the figure and axes object
fig, ax = plt.subplots(figsize=(10, 6))  # Reasonable change in width and height of the chart

# Plotting
for i, column in enumerate(columns):
    values = df[column].values
    bottom_values = df[columns[:i]].sum(axis=1).values if i > 0 else np.zeros(n_rows)
    ax.barh(df.index, values, color=colors[i], edgecolor='white', height=0.8, left=bottom_values)

# Add percentages on top of the bars
for i in range(n_rows):
    for j, column in enumerate(columns):
        value = df[column].values[i]
        bottom_value = df[columns[:j]].sum(axis=1).values[i]
        # Only displaying if the value is not zero
        if value != 0:
            ax.text(bottom_value + value/2, i, f'{value}%', va='center', ha='center', color='black')

# Customize the y-axis
ax.set_yticks(np.arange(n_rows))
ax.set_yticklabels(df.index)

# Customize the x-axis
ax.set_xticks(np.linspace(0, 100, 11))
ax.set_xticklabels([f'{i}%' for i in range(0, 101, 10)])

# Set the title and labels
ax.set_title('Web Browser Usage Share (2018-2021)', fontsize=18)
ax.set_xlabel('Percentage Share', fontsize=14)
ax.set_ylabel('Year', fontsize=14)

# Add a legend
ax.legend(columns, loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=len(columns))

plt.tight_layout()
plt.show()