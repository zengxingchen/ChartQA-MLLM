
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Provided data as a list of dictionaries
data = [
    {'Age Group': '10-18', 'Average Screen Time (Hours/Day)': 4.5, 'Number of Apps Installed': 72, 'Average Monthly Data Usage (GB)': 3.5, 'Population Segment Size (Millions)': 30},
    # ... (include other records here) ...
    {'Age Group': '35-44', 'Average Screen Time (Hours/Day)': 3.2, 'Number of Apps Installed': 52, 'Average Monthly Data Usage (GB)': 3.1, 'Population Segment Size (Millions)': 33}
]

# Convert list of dictionaries into DataFrame
df = pd.DataFrame(data)

# Initialize a figure
plt.figure(figsize=(14, 8))

# Create a bubble chart
bubble_chart = sns.scatterplot(
    data=df,
    x='Age Group',
    y='Average Screen Time (Hours/Day)',
    size='Population Segment Size (Millions)',
    hue='Average Monthly Data Usage (GB)',
    sizes=(200, 1000),  # Controls the range of sizes for the bubbles
    alpha=0.6,          # Opacity level of the bubbles
    palette='cool',     # Color palette
    legend='full'       # Show legend
)

# Add axis labels and a title
plt.xlabel('Age Group', fontsize=14)
plt.ylabel('Average Screen Time (Hours/Day)', fontsize=14)
plt.title('Bubble Chart of Screen Time by Age Group', fontsize=16)

# Adjust legend for bubble sizes
h, l = bubble_chart.get_legend_handles_labels()
bubble_chart.legend(h[1:], l[1:], title='Average Monthly Data Usage (GB)', loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.tight_layout()
plt.show()