
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import date2num
from matplotlib.cm import ScalarMappable

# Your data here
data = [
    {'Date': '2023-03-01', 'Species': 'Squirrels', 'Sightings': 25, 'Photographs Taken': 18, 'Average Observation Time (min)': 6},
    {'Date': '2023-03-02', 'Species': 'Birds - Common Sparrow', 'Sightings': 50, 'Photographs Taken': 35, 'Average Observation Time (min)': 3},
    # ... add all the other data points as well
    {'Date': '2023-03-15', 'Species': 'Squirrels', 'Sightings': 22, 'Photographs Taken': 20, 'Average Observation Time (min)': 6}
]

# Construct a dataframe
df = pd.DataFrame(data)

# Plotting
fig, ax = plt.subplots(figsize=(15, 8))

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = date2num(df['Date'])

# Create a scatter plot (bubble chart)
scatter = ax.scatter(
    df['Date'],
    df['Photographs Taken'],
    s=df['Sightings'] * 10,  # Multiply sightings by 10 for better visibility
    c=df['Average Observation Time (min)'],
    cmap='viridis',  # Colormap
    alpha=0.6,  # Transparency
    edgecolors='w',  # White edge color for each bubble
    linewidth=0.5
)

# Add a color bar
cbar = plt.colorbar(scatter)
cbar.set_label('Average Observation Time (min)', rotation=270, labelpad=15)

# Set the title and labels
ax.set_title('Wildlife Observations - Bubble Chart')
ax.set_xlabel('Date')
ax.set_ylabel('Photographs Taken')

# Format date on x-axis
plt.xticks(rotation=45)
ax.xaxis_date()  # interpret the x-axis values as dates
fig.autofmt_xdate()  # auto format the x-axis labels to fit into the plot

# Adding Species as annotation
for i, species in enumerate(df['Species']):
    ax.annotate(species, (df['Date'][i], df['Photographs Taken'][i]), fontsize=8, ha='center')

# Show the plot
plt.tight_layout()
plt.show()