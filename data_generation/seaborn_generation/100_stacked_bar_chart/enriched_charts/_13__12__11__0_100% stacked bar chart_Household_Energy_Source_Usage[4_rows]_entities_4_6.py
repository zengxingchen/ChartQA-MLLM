
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Role': ['Leader', 'Innovator', 'Manager', 'Visionary', 'Collaborator'],
    'Preparation': [30, 20, 25, 15, 10],
    'Performance': [25, 30, 20, 10, 15],
    'Strategy': [20, 25, 15, 30, 10],
    'Inspiration': [10, 15, 25, 30, 20],
    'Teamwork': [15, 10, 15, 15, 45]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Calculate the percentage
df.set_index('Role', inplace=True)
df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

# Start a figure with seaborn style
plt.figure(figsize=(10, 12))
sns.set_theme(style="whitegrid")

# Create a color map
colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]

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
        width=0.85
    )
    bar_start += df_percentage[col]

# Customizations
plt.xlabel('Percentage')
plt.ylabel('Role')
plt.title('Distribution of Time Spent on Leadership Activities by Professionals', pad=20)
plt.xticks(rotation=0)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert x-axis labels to percentage
plt.gca().xaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()