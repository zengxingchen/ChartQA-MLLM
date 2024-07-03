
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame from the provided data
data = [
    {'Startup Name': 'SensorFleet', 'Sector': 'Cybersecurity', 'Year Founded': 2016, 'Revenue Growth (Past Year %)': 250, 'Employee Growth (Past Year %)': 200, 'Current Employee Count': 35},
    {'Startup Name': 'CloudBench', 'Sector': 'Cloud Computing', 'Year Founded': 2019, 'Revenue Growth (Past Year %)': 500, 'Employee Growth (Past Year %)': 150, 'Current Employee Count': 25},
    {'Startup Name': 'GenoMe', 'Sector': 'Biotechnology', 'Year Founded': 2018, 'Revenue Growth (Past Year %)': 150, 'Employee Growth (Past Year %)': 100, 'Current Employee Count': 40},
    # ... (include all other data points)
    {'Startup Name': 'SolarSprint', 'Sector': 'Renewable Energy', 'Year Founded': 2015, 'Revenue Growth (Past Year %)': 180, 'Employee Growth (Past Year %)': 70, 'Current Employee Count': 50}
]

df = pd.DataFrame(data)

# Create a color palette for the Sectors
palette = sns.color_palette("hsv", len(df['Sector'].unique()))
color_map = {sector: color for sector, color in zip(df['Sector'].unique(), palette)}

# Create the bubble chart
plt.figure(figsize=(12, 8))
bubble_plot = sns.scatterplot(
    data=df,
    x='Year Founded',
    y='Revenue Growth (Past Year %)',
    size='Employee Growth (Past Year %)',
    sizes=(50, 1000),  # Control the range of bubble sizes
    hue='Sector',
    palette=color_map,
    alpha=0.7,
    legend=False
)

# Add labels to each bubble
for index, row in df.iterrows():
    plt.text(row['Year Founded'], row['Revenue Growth (Past Year %)'], row['Startup Name'], horizontalalignment='center', size='small', color='black', weight='semibold')

# Customize the axes and title
plt.title('Startup Growth Analysis')
plt.xlabel('Year Founded')
plt.ylabel('Revenue Growth (Past Year %)')

# Show sector colors in a legend
sector_patches = [plt.Line2D([0], [0], marker='o', color='gray', label=sector,
                              markerfacecolor=color, markersize=10)
                  for sector, color in color_map.items()]
plt.legend(handles=sector_patches, title='Sectors', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

# Show the plot
plt.show()