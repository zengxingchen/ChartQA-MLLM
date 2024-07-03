
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Country': [
        'China', 'United States', 'Germany', 'Japan', 'Netherlands',
        'South Korea', 'Hong Kong', 'France', 'Italy', 'United Kingdom',
        'Canada', 'Belgium', 'Singapore', 'Spain', 'Mexico',
        'India', 'Taiwan', 'Switzerland', 'Russia', 'Australia'
    ],
    'Export Value': [
        2237, 1487, 1349, 634, 574, 
        555, 546, 536, 475, 469,
        447, 429, 394, 345, 340,
        323, 316, 311, 296, 280
    ]
}
df = pd.DataFrame(data)

# Set the figure size and style
sns.set(style="whitegrid")
plt.figure(figsize=(12, 10))

# Create a horizontal bar plot with custom color scheme and bar width
barplot = sns.barplot(
    x="Export Value",
    y="Country",
    data=df,
    palette=[f'#{"%06x" % (i * 123567)}' for i in range(len(df))],
    orient='h'
)

# Customize the appearance
barplot.set_title('Top Exporting Countries in 2021')
barplot.bar_label(barplot.containers[0], fmt='%.0f')
barplot.set(ylabel="Country", xlabel="Export Value (in billions USD)")

# Adjust the bandwidth
for bar in barplot.containers[0]:
    bar.set_height(0.8)

# Show the plot
plt.tight_layout()
plt.show()