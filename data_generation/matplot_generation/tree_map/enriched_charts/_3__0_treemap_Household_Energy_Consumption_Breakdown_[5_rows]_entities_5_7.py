
import matplotlib.pyplot as plt
import squarify

# Data points
regions = [
    'Amazon Rainforest', 'Congo Rainforest', 'Southeast Asian Rainforest', 
    'Temperate Deciduous Forest', 'Boreal Forest', 'Mediterranean Forest', 
    'Temperate Coniferous Forest', 'Mangrove Forest', 'Savanna Woodland', 
    'Tropical Dry Forest', 'Cloud Forest', 'Tropical Montane Forest', 
    'Flooded Grasslands', 'Montane Grasslands', 'Polar Desert'
]
number_of_trees = [
    50000, 30000, 20000, 15000, 35000, 10000, 12000, 8000, 
    18000, 14000, 6000, 11000, 7000, 9000, 500
]
carbon_sequestration = [
    600000, 400000, 250000, 200000, 450000, 150000, 160000, 100000, 
    220000, 180000, 75000, 135000, 90000, 120000, 3000
]

# Color scheme using specific color codes
colors = [
    '#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF6666',
    '#99CC99', '#FFB366', '#66CCCC', '#B2FF66', '#6699FF',
    '#FF9966', '#FF99CC', '#66FFB2', '#FF6699', '#99B2FF'
]

# Create a figure with altered width and height
fig, ax = plt.subplots(figsize=(14, 10))

# Creating a treemap
squarify.plot(sizes=number_of_trees, label=regions, color=colors, alpha=0.8, value=carbon_sequestration, edgecolor='white', linewidth=2)

# Chart title and subtitle
plt.title('Forest Carbon Sequestration by Region', fontsize=18, color='darkblue')
plt.suptitle('Global Environmental Impact of Forests', fontsize=22)

# Remove the axes
plt.axis('off')

# Show plot
plt.show()