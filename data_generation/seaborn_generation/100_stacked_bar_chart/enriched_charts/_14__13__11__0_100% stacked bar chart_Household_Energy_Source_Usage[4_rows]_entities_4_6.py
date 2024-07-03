
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Activity': ['Teenagers', 'Young Adults', 'Middle-aged Adults', 'Elderly', 'Professionals'],
    'Meditation': [20, 25, 15, 20, 15],
    'Reading': [25, 20, 30, 20, 20],
    'Exercise': [30, 25, 20, 15, 25],
    'Socializing': [15, 20, 25, 30, 30],
    'Other': [10, 10, 10, 15, 10]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Calculate the percentage
df.set_index('Activity', inplace=True)
df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

# Start a figure with seaborn style
plt.figure(figsize=(10, 14))
sns.set_theme(style="whitegrid")

# Create a color map
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

# Starting position
bar_start = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0], index=df.index)

for col, color in zip(df.columns, colors):
    # Plot each category stack
    sns.barplot(
        y=df_percentage.index,
        x=df_percentage[col],
        color=color,
        label=col,
        left=bar_start
    )
    # Add the values to the starting position
    bar_start += df_percentage[col]

# Customizations
plt.ylabel('Activity')
plt.xlabel('Percentage')
plt.title('Distribution of Time Spent on Mental Well-being Activities', pad=20)
plt.legend(title='Activity Type', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert x-axis labels to percentage
plt.gca().xaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()