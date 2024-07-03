
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Role': ['Student', 'Teacher', 'Engineer', 'Artist', 'Doctor', 'Nurse'],
    'Local Tourism': [10, 15, 20, 5, 25, 20],
    'International Tourism': [20, 25, 30, 15, 10, 15],
    'Adventure Sports': [25, 20, 10, 30, 15, 15],
    'Relaxation': [15, 20, 10, 25, 20, 20],
    'Family Trip': [20, 10, 15, 10, 15, 10],
    'Friends Trip': [10, 10, 15, 15, 15, 20]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Calculate the percentage
df.set_index('Role', inplace=True)
df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

# Start a figure with seaborn style
plt.figure(figsize=(14, 10))
sns.set_theme(style="whitegrid")

# Create a color map
colors = ["#4B8BBE", "#306998", "#FFE873", "#FFD43B", "#646464", "#DE4B50"]

# Starting position
bar_start = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], index=df.index)

for col, color in zip(df.columns, colors):
    # Plot each category stack
    sns.barplot(
        x=bar_start,
        y=df_percentage.index,
        color=color,
        label=col,
        left=bar_start,
        linewidth=0.8,
        width=0.8
    )
    # Add the values to the starting position
    bar_start += df_percentage[col]

# Customizations
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('Role', fontsize=14)
plt.title('Distribution of Time Spent on Travel & Adventure Activities', fontsize=16, pad=20)
plt.xticks(rotation=0)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert x-axis labels to percentage
plt.gca().xaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()