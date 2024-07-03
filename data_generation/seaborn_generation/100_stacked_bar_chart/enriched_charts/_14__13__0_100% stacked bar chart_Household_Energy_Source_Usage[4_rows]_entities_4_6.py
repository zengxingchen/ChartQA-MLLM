
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Data
data = {
    'Topic': ['Morning', 'Afternoon', 'Evening', 'Night'],
    'Classical': [25, 15, 10, 5],
    'Rock': [20, 25, 15, 10],
    'Jazz': [15, 20, 30, 25],
    'HipHop': [10, 15, 20, 35],
    'Country': [10, 10, 10, 10],
    'Pop': [20, 15, 15, 15]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Calculate the percentage
df.set_index('Topic', inplace=True)
df_percentage = df.divide(df.sum(axis=1), axis=0) * 100

# Start a figure with seaborn style
plt.figure(figsize=(8, 6))
sns.set_theme(style="whitegrid")

# Create a color map
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6"]

# Starting position
bar_start = pd.Series([0.0, 0.0, 0.0, 0.0], index=df.index)

for col, color in zip(df.columns, colors):
    # Plot each category stack
    sns.barplot(
        x=df_percentage.index,
        y=df_percentage[col],
        color=color,
        label=col,
        bottom=bar_start,
        ci=None,
        linewidth=0.5
    )
    # Add the values to the starting position
    bar_start += df_percentage[col]

# Customizations
plt.ylabel('Percentage')
plt.xlabel('Time of Day')
plt.title('Distribution of Music Preferences Throughout the Day')
plt.xticks(rotation=0)
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')

# Convert y-axis labels to percentage
plt.gca().yaxis.set_major_formatter(PercentFormatter())

# Show the plot
plt.tight_layout()
plt.show()