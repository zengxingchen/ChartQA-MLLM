
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Activity': ['Morning', 'Afternoon', 'Evening', 'Night'],
    'Exercise': [20, 10, 15, 5],
    'Work': [30, 40, 25, 10],
    'Leisure': [10, 20, 30, 5],
    'Household': [5, 10, 10, 5],
    'Socializing': [15, 10, 10, 5],
    'Sleep': [20, 10, 10, 70]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Calculate the percentage
df.set_index('Activity', inplace=True)
df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

# Start a figure with seaborn style
plt.figure(figsize=(10, 10))
sns.set_theme(style="whitegrid")

# Create a color map
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

# Starting position
bar_start = pd.Series([0.0, 0.0, 0.0, 0.0], index=df.index)

for col, color in zip(df.columns, colors):
    # Plot each category stack
    sns.barplot(
        x=df_percentage.index,
        y=df_percentage[col],
        color=color,
        label=col,
        bottom=bar_start
    )
    # Add the values to the starting position
    bar_start += df_percentage[col]

# Customizations
plt.ylabel('Percentage')
plt.xlabel('Time of Day')
plt.title('Distribution of Daily Activities')
plt.xticks(rotation=0)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert y-axis labels to percentage
plt.gca().yaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()