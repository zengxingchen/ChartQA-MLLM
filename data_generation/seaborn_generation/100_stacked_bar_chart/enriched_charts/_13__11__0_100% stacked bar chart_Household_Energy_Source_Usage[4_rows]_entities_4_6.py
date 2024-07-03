
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Activity': ['Adolescents', 'Adults', 'Seniors', 'Athletes', 'Students'],
    'Sleep': [30, 25, 35, 20, 25],
    'Work': [30, 35, 20, 40, 25],
    'Exercise': [20, 15, 10, 25, 20],
    'Leisure': [15, 20, 25, 10, 25],
    'Other': [5, 5, 10, 5, 5]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Calculate the percentage
df.set_index('Activity', inplace=True)
df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

# Start a figure with seaborn style
plt.figure(figsize=(12, 8))
sns.set_theme(style="whitegrid")

# Create a color map
colors = ["#3498db", "#e74c3c", "#2ecc71", "#f1c40f", "#9b59b6"]

# Starting position
bar_start = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0], index=df.index)

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
plt.xlabel('Activity')
plt.ylabel('Percentage')
plt.title('Distribution of Time Spent on Daily Activities')
plt.xticks(rotation=45)
plt.legend(title='Activity Type', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert y-axis labels to percentage
plt.gca().yaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()