
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for creating the treemap
data = {
    'Activity': [
        "Reforestation Project", "Coastal Cleanup", "Wildlife Conservation",
        "Renewable Energy Campaign", "Sustainable Agriculture Workshop",
        "Climate Change Awareness Rally", "Green Building Initiative",
        "Urban Gardening Program", "Plastic Ban Enforcement", "Carbon Footprint Reduction",
        "Eco-Friendly Transportation Promotion", "Water Conservation Project",
        "Energy Efficiency Drive", "Community Recycling Drive", "Tree Planting Event",
        "Ocean Conservation Effort", "Air Quality Improvement Plan", "Wildlife Habitat Restoration",
        "Solar Panel Installation Drive", "Electric Vehicle Subsidies"
    ],
    'Impact': [
        50000, 25000, 30000, 45000, 20000, 35000, 15000, 10000, 27000, 32000,
        21000, 29000, 23000, 19000, 40000, 34000, 37000, 22000, 41000, 24000
    ]
}

# Convert the data dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Define size of the figure
plt.figure(figsize=(16,12))

# Define custom colors using specific color codes
colors = [
    '#4c72b0', '#55a868', '#c44e52', '#8172b2', '#ccb974', '#64b5cd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ffbb78',
    '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7',
    '#dbdb8d', '#9edae5'
]

# Create the treemap
squarify.plot(sizes=df['Impact'], label=df['Activity'], color=colors, alpha=0.8)

# Set the title of the treemap
plt.title('Impact of Environmental Activities', fontsize=18, pad=20)

# Remove the axis lines
plt.axis('off')

# Display the treemap
plt.show()