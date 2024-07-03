
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Country': [
        'China', 'United States', 'Germany', 'Japan', 'Netherlands',
        'South Korea', 'Hong Kong', 'France', 'Italy', 'United Kingdom',
        'Canada', 'Belgium', 'Singapore', 'Spain', 'Mexico',
        'India', 'Taiwan', 'Switzerland', 'Russia', 'Australia',
        'Brazil', 'Turkey', 'Sweden', 'Thailand'
    ],
    'Export Value': [
        2237, 1487, 1349, 634, 574, 
        555, 546, 536, 475, 469,
        447, 429, 394, 345, 340,
        323, 316, 311, 296, 280,
        265, 250, 240, 230
    ]
}
df = pd.DataFrame(data)

# Set the figure size and style
sns.set(style="whitegrid")
plt.figure(figsize=(14, 8))

# Create a vertical bar plot with custom color scheme and bar width
barplot = sns.barplot(
    x="Country",
    y="Export Value",
    data=df,
    palette=[
        '#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974',
        '#64b5cd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22',
        '#17becf', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
        '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#2ca02c',
        '#d62728', '#9467bd', '#8c564b', '#e377c2'
    ],
    ci=None
)

# Customize the appearance
barplot.set_title('Top Exporting Countries in 2021', fontsize=16)
barplot.bar_label(barplot.containers[0], fmt='%.0f', fontsize=10)
barplot.set(xlabel="Country", ylabel="Export Value (in billions USD)")

# Adjust the bandwidth
for bar in barplot.containers[0]:
    bar.set_width(0.6)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()