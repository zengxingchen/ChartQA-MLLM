
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given data in a list of dictionaries
data = [
    {'Week': 'Week 1', 'Average Noise Level (dB)': 55, 'Bird Sightings': 42},
    {'Week': 'Week 2', 'Average Noise Level (dB)': 50, 'Bird Sightings': 48},
    {'Week': 'Week 3', 'Average Noise Level (dB)': 60, 'Bird Sightings': 37},
    {'Week': 'Week 4', 'Average Noise Level (dB)': 52, 'Bird Sightings': 50},
    {'Week': 'Week 5', 'Average Noise Level (dB)': 58, 'Bird Sightings': 45},
    {'Week': 'Week 6', 'Average Noise Level (dB)': 53, 'Bird Sightings': 47},
    {'Week': 'Week 7', 'Average Noise Level (dB)': 59, 'Bird Sightings': 43},
    {'Week': 'Week 8', 'Average Noise Level (dB)': 49, 'Bird Sightings': 52},
    {'Week': 'Week 9', 'Average Noise Level (dB)': 61, 'Bird Sightings': 39},
    {'Week': 'Week 10', 'Average Noise Level (dB)': 57, 'Bird Sightings': 46},
    {'Week': 'Week 11', 'Average Noise Level (dB)': 54, 'Bird Sightings': 49},
    {'Week': 'Week 12', 'Average Noise Level (dB)': 56, 'Bird Sightings': 41}
]

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Create a scatterplot
plt.figure(figsize=(10, 6))  # Set the size of the figure
scatter_plot = sns.scatterplot(
    data=df,
    x='Average Noise Level (dB)',  # X-axis represents average noise level
    y='Bird Sightings',           # Y-axis represents bird sightings
    hue='Week',                   # Color points by week
    palette=sns.color_palette("hsv", len(df['Week'].unique())),  # Use a color palette that provides a unique color for each week
    s=100,                        # Set the size of the markers
    style='Week',                 # Different marker styles for each week
    markers=True,                 # Use markers
    alpha=0.7                     # Set transparency of markers
)

# Add titles and labels
plt.title('Scatterplot of Average Noise Level (dB) vs. Bird Sightings')
plt.xlabel('Average Noise Level (dB)')
plt.ylabel('Bird Sightings')

# Place the legend outside the plot
plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0)

# Show the plot
plt.tight_layout()  # Adjusts the plot to ensure everything fits without overlapping
plt.show()