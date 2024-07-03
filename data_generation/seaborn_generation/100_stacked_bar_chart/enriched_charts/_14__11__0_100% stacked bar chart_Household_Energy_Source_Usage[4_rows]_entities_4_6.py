
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Role': ['Fruit', 'Vegetables', 'Grains', 'Protein', 'Dairy'],
    'Calories': [10, 20, 30, 40, 10],
    'Fat': [5, 10, 20, 30, 25],
    'Carbs': [30, 40, 20, 5, 25],
    'Protein': [10, 20, 20, 20, 25],
    'Other': [45, 10, 10, 5, 15]
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
colors = ["#FF6347", "#4682B4", "#32CD32", "#FFD700", "#8A2BE2"]

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
plt.xlabel('Percentage')
plt.ylabel('Food Category')
plt.title('Nutritional Composition of Different Food Categories')
plt.xticks(rotation=0)
plt.legend(title='Nutrient', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert x-axis labels to percentage
plt.gca().xaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()