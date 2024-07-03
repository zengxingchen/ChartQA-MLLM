
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given table data
data = [
    {'Crop': 'Tomatoes', 'Variety': 'Cherry', 'Month Harvested': 'August', 'Yield (kg)': 65, 'Garden Area (m^2)': 20},
    {'Crop': 'Zucchini', 'Variety': 'Green', 'Month Harvested': 'July', 'Yield (kg)': 80, 'Garden Area (m^2)': 15},
    {'Crop': 'Carrots', 'Variety': 'Nantes', 'Month Harvested': 'September', 'Yield (kg)': 30, 'Garden Area (m^2)': 10},
    {'Crop': 'Lettuce', 'Variety': 'Romaine', 'Month Harvested': 'June', 'Yield (kg)': 25, 'Garden Area (m^2)': 8},
    {'Crop': 'Peppers', 'Variety': 'Bell', 'Month Harvested': 'July', 'Yield (kg)': 40, 'Garden Area (m^2)': 12}
]

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Create a categorical palette to identify the crops
palette = sns.color_palette("hsv", len(df['Crop'].unique()))

# Map the crop names to the palette colors
color_map = {crop: color for crop, color in zip(df['Crop'].unique(), palette)}

# Create a bubble chart
plt.figure(figsize=(10, 6))
bubble = sns.scatterplot(
    data=df,
    x="Month Harvested",
    y="Garden Area (m^2)",
    size="Yield (kg)",
    hue="Crop",
    palette=color_map,
    alpha=0.6,
    sizes=(100, 1000),  # Range of circle sizes
    legend="full"
)

# Adjust the y-axis label
plt.ylabel('Garden Area (m^2)')

# Add a title
plt.title('Bubble Chart of Crops Yield and Garden Area')

# Position the legend outside of the plot/figure
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Show the plot
plt.show()