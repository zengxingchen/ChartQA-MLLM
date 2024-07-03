
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Role': ['Software Developer', 'Project Manager', 'Quality Assurance', 'Design Engineer'],
    'Email': [10, 25, 15, 5],
    'Meetings': [15, 35, 25, 20],
    'Development': [50, 10, 30, 45],
    'Support': [5, 5, 15, 5],
    'Training': [10, 10, 10, 15],
    'Other': [10, 15, 5, 10]
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
colors = ["#FF9999", "#66B2FF", "#99FF99", "#FFCC99", "#FFD700", "#B22222"]

# Starting position
bar_start = pd.Series([0.0, 0.0, 0.0, 0.0], index=df.index)

for col, color in zip(df.columns, colors):
    # Plot each category stack
    sns.barplot(
        x=df_percentage[col],
        y=df_percentage.index,
        color=color,
        label=col,
        left=bar_start
    )
    # Add the values to the starting position
    bar_start += df_percentage[col]

# Customizations
plt.xlabel('Percentage')
plt.ylabel('Job Role')
plt.title('Distribution of Time Spent on Job Activities')
plt.xticks(rotation=0)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert x-axis labels to percentage
plt.gca().xaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()