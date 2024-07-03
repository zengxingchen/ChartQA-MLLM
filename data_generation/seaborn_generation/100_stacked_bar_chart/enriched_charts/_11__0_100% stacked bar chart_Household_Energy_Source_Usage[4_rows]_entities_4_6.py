
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Role': ['Graphic Designer', 'Product Manager', 'Research Analyst', 'Marketing Specialist', 'Content Creator'],
    'Design': [20, 10, 15, 25, 30],
    'Development': [30, 20, 10, 20, 25],
    'Research': [15, 30, 40, 20, 15],
    'Marketing': [25, 30, 25, 25, 20],
    'Other': [10, 10, 10, 10, 10]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Calculate the percentage
df.set_index('Role', inplace=True)
df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

# Start a figure with seaborn style
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Create a color map
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#33FFF5"]

# Starting position
bar_start = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0], index=df.index)

for col, color in zip(df.columns, colors):
    # Plot each category stack
    sns.barplot(
        y=df_percentage[col],
        x=df_percentage.index,
        color=color,
        label=col,
        bottom=bar_start
    )
    # Add the values to the starting position
    bar_start += df_percentage[col]

# Customizations
plt.ylabel('Percentage')
plt.xlabel('Job Role')
plt.title('Distribution of Time Spent on Creative Activities')
plt.yticks(rotation=0)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert y-axis labels to percentage
plt.gca().yaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()