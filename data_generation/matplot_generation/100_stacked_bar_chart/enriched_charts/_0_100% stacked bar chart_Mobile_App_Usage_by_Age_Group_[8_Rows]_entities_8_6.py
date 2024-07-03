
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data representing the time spent on different activities in different departments
data = {
    'Department': ['Engineering', 'Design', 'Marketing', 'Sales', 'HR'],
    'Development': [40, 25, 20, 15, 10],
    'Research': [10, 15, 10, 5, 5],
    'Meetings': [20, 30, 35, 40, 30],
    'Training': [15, 20, 10, 10, 25],
    'Administration': [15, 10, 25, 30, 30]
}

df = pd.DataFrame(data)

# Calculate the percentage of time spent on each activity
df_percentage = df.drop('Department', axis=1).div(df.drop('Department', axis=1).sum(axis=1), axis=0) * 100

# List of colors for the bars
colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F']

# Plot stacked bar chart
fig, ax = plt.subplots(figsize=(10, 8))

bar_width = 0.6

departments = df['Department']
indices = np.arange(len(departments))

previous_values = np.zeros(len(df))
for col, color in zip(df_percentage.columns, colors):
    values = df_percentage[col]
    ax.barh(indices, values, color=color, edgecolor='white', height=bar_width, left=previous_values, label=col)
    previous_values += values

# Customize the plot
ax.set_xlabel('Percentage of Weekly Time Spent (%)', fontsize=12)
ax.set_title('Weekly Time Allocation by Department', fontsize=14)
ax.set_yticks(indices)
ax.set_yticklabels(departments)
ax.set_xlim(0, 100)
ax.legend(title='Activities', bbox_to_anchor=(1.05, 1), loc='upper left')

# Invert Y-axis
ax.invert_yaxis()

plt.tight_layout()
plt.show()