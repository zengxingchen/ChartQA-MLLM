
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Field': ['Clothing', 'Footwear', 'Accessories', 'Cosmetics', 'Skincare', 'Haircare'],
    'Local Products': [30, 20, 25, 35, 40, 25],
    'International Brands': [25, 30, 20, 20, 25, 30],
    'Online Shopping': [20, 30, 35, 25, 20, 30],
    'In-Store Shopping': [25, 20, 20, 20, 15, 15]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Calculate the percentage
df.set_index('Field', inplace=True)
df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

# Start a figure with seaborn style
plt.figure(figsize=(10, 12))
sns.set_theme(style="whitegrid")

# Create a color map
colors = ["#2E8B57", "#6A5ACD", "#FFD700", "#FF6347"]

# Starting position
bar_start = pd.Series([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], index=df.index)

for col, color in zip(df.columns, colors):
    # Plot each category stack
    sns.barplot(
        y=bar_start,
        x=df_percentage.index,
        color=color,
        label=col,
        bottom=bar_start,
        linewidth=0.8,
        width=0.6
    )
    # Add the values to the starting position
    bar_start += df_percentage[col]

# Customizations
plt.ylabel('Percentage', fontsize=14)
plt.xlabel('Field', fontsize=14)
plt.title('Consumer Preferences in Fashion & Beauty', fontsize=16, pad=20)
plt.yticks(rotation=0)
plt.legend(title='Shopping Mode', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert y-axis labels to percentage
plt.gca().yaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()