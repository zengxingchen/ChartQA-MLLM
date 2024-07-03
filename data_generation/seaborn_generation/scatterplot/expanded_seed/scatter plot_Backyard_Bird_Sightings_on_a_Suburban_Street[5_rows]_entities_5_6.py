
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your data in a list of dictionaries
data = [
    {'Date': '2023-04-01', 'Species': 'Cardinal', 'Number of Sightings': 4},
    {'Date': '2023-04-02', 'Species': 'Blue Jay', 'Number of Sightings': 2},
    {'Date': '2023-04-03', 'Species': 'Robin', 'Number of Sightings': 7},
    {'Date': '2023-04-04', 'Species': 'Cardinal', 'Number of Sightings': 5},
    {'Date': '2023-04-05', 'Species': 'Hummingbird', 'Number of Sightings': 1}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create a scatter plot using seaborn
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(
    data=df,
    x='Date',
    y='Number of Sightings',
    hue='Species',           # Color encode the points by species
    style='Species',         # Use different markers for species
    s=100,                   # Set marker size
    palette='viridis',       # Use the 'viridis' color palette for variety
    alpha=0.7                # Set transparency to 70%
)

# Improve legibility of the plot
plt.xticks(rotation=45)      # Rotate x-axis labels for better visibility
scatter_plot.set_title('Number of Bird Sightings Over Time')  # Set title
scatter_plot.set_xlabel('Date')  # X-axis Label
scatter_plot.set_ylabel('Number of Sightings')  # Y-axis Label
scatter_plot.legend(title='Species')  # Add a legend with a title

# Show the plot
plt.show()