
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Role': ['Student', 'Teacher', 'Engineer', 'Artist', 'Doctor', 'Nurse'],
    'Exercise': [20, 10, 15, 5, 10, 15],
    'Meditation': [10, 10, 5, 15, 5, 10],
    'Work': [40, 30, 50, 25, 50, 45],
    'Leisure': [15, 20, 10, 20, 10, 10],
    'Family Time': [10, 20, 10, 15, 10, 10],
    'Socializing': [5, 10, 10, 20, 15, 10]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Calculate the percentage
df.set_index('Role', inplace=True)
df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

# Start a figure with seaborn style
plt.figure(figsize=(10, 14))
sns.set_theme(style="whitegrid")

# Create a color map
colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33A1", "#33FFF6"]

# Starting position
bar_start = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], index=df.index)

for col, color in zip(df.columns, colors):
    # Plot each category stack
    sns.barplot(
        x=df_percentage[col],
        y=df_percentage.index,
        color=color,
        label=col,
        left=bar_start,
        linewidth=0.8
    )
    # Add the values to the starting position
    bar_start += df_percentage[col]

# Customizations
plt.xlabel('Percentage', fontsize=14)
plt.ylabel('Role', fontsize=14)
plt.title('Distribution of Time Spent on Health Activities', fontsize=16, pad=20)
plt.xticks(rotation=0)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert x-axis labels to percentage
plt.gca().xaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()