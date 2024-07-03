
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Role': ['Athlete', 'Coach', 'Physiotherapist', 'Nutritionist', 'Sports Analyst'],
    'Training': [25, 20, 10, 15, 20],
    'Competition': [35, 25, 20, 10, 15],
    'Recovery': [15, 10, 40, 25, 30],
    'Nutrition': [15, 30, 20, 40, 25],
    'Other': [10, 15, 10, 10, 10]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Calculate the percentage
df.set_index('Role', inplace=True)
df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

# Start a figure with seaborn style
plt.figure(figsize=(12, 8))
sns.set_theme(style="whitegrid")

# Create a color map
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

# Starting position
bar_start = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0], index=df.index)

# Plot each category stack
for col, color in zip(df.columns, colors):
    sns.barplot(
        y=df_percentage[col],
        x=df_percentage.index,
        color=color,
        label=col,
        bottom=bar_start,
        width=0.75
    )
    bar_start += df_percentage[col]

# Customizations
plt.ylabel('Percentage')
plt.xlabel('Role')
plt.title('Distribution of Time Spent on Sports Activities by Professionals')
plt.xticks(rotation=45)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert y-axis labels to percentage
plt.gca().yaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()