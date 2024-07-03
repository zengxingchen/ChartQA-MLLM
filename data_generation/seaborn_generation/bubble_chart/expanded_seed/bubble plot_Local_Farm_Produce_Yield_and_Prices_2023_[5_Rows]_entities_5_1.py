
import seaborn as sns
import matplotlib.pyplot as plt

# Provided chart data
data = [
    {'Crop': 'Apples', 'Harvested Volume (Metric Tons)': 2450, 'Average Price per Kilogram': 1.5, 'Surface Area Cultivated (Hectares)': 172},
    {'Crop': 'Oranges', 'Harvested Volume (Metric Tons)': 3200, 'Average Price per Kilogram': 1.2, 'Surface Area Cultivated (Hectares)': 198},
    {'Crop': 'Potatoes', 'Harvested Volume (Metric Tons)': 8700, 'Average Price per Kilogram': 0.3, 'Surface Area Cultivated (Hectares)': 540},
    {'Crop': 'Tomatoes', 'Harvested Volume (Metric Tons)': 4600, 'Average Price per Kilogram': 0.8, 'Surface Area Cultivated (Hectares)': 116},
    {'Crop': 'Zucchinis', 'Harvested Volume (Metric Tons)': 2200, 'Average Price per Kilogram': 1.1, 'Surface Area Cultivated (Hectares)': 58}
]

# Convert the data to a DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Set the aesthetic features of the plot
sns.set_theme(style="whitegrid")

# Create the bubble chart
plt.figure(figsize=(10, 6))
bubble_plot = sns.scatterplot(data=df,
                              x="Surface Area Cultivated (Hectares)",
                              y="Harvested Volume (Metric Tons)",
                              size="Average Price per Kilogram",
                              sizes=(100, 1000),  # Control the range of bubble sizes
                              hue="Crop",  # Color the bubbles by crop type,
                              palette="deep",  # Use a deep color palette for differentiation
                              alpha=0.6,  # Set transparency
                              legend="full")

# Customize the axes and legend
bubble_plot.set_title('Bubble Chart of Crops by Harvested Volume, Price and Cultivated Area')
bubble_plot.set_xlabel('Surface Area Cultivated (Hectares)')
bubble_plot.set_ylabel('Harvested Volume (Metric Tons)')
plt.legend(title='Crop Type', loc='upper left', bbox_to_anchor=(1, 1))  # Place legend outside the plot

# Show the plot
plt.tight_layout()
plt.show()