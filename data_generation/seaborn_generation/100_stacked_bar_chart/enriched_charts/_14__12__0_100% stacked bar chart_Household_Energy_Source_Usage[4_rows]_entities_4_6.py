
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Industry': ['Tech', 'Healthcare', 'Finance', 'Education', 'Manufacturing', 'Retail'],
    'Research': [30, 20, 15, 25, 20, 10],
    'Development': [25, 15, 10, 20, 10, 15],
    'Marketing': [10, 10, 5, 15, 15, 20],
    'Sales': [15, 20, 30, 10, 20, 25],
    'HR': [10, 20, 20, 15, 20, 15],
    'Finance': [10, 15, 20, 15, 15, 15]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Calculate the percentage
df.set_index('Industry', inplace=True)
df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

# Start a figure with seaborn style
plt.figure(figsize=(12, 8))
sns.set_theme(style="whitegrid")

# Create a color map
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#33FFF6", "#F3FF33"]

# Starting position
bar_start = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], index=df.index)

for col, color in zip(df.columns, colors):
    # Plot each category stack
    sns.barplot(
        y=df_percentage[col],
        x=df_percentage.index,
        color=color,
        label=col,
        bottom=bar_start,
        linewidth=0.8,
        width=0.7
    )
    # Add the values to the starting position
    bar_start += df_percentage[col]

# Customizations
plt.ylabel('Percentage', fontsize=14)
plt.xlabel('Industry', fontsize=14)
plt.title('Distribution of Resources in Different Industries', fontsize=16, pad=20)
plt.yticks(rotation=0)
plt.legend(title='Department', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert y-axis labels to percentage
plt.gca().yaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()