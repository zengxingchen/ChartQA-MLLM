
import matplotlib.pyplot as plt

# Data
data = [
    {'Pet Type': 'Dogs', 'Number of Households': 2300},
    {'Pet Type': 'Cats', 'Number of Households': 1800},
    {'Pet Type': 'Fish', 'Number of Households': 600},
    {'Pet Type': 'Birds', 'Number of Households': 300},
    {'Pet Type': 'Reptiles', 'Number of Households': 200},
    {'Pet Type': 'Small Mammals', 'Number of Households': 150},
    {'Pet Type': 'Exotic', 'Number of Households': 50},
    {'Pet Type': 'No Pets', 'Number of Households': 1200}
]

# Prepare data for pie chart
pet_types = [d['Pet Type'] for d in data]
households = [d['Number of Households'] for d in data]

# Colors for each pet type
colors = plt.cm.tab20c.colors  # Using the 20-colors tableau color map (tab20c)

# Explode the first slice (Dogs) to highlight it
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)

# Create the pie chart
plt.figure(figsize=(10, 8))  # Set the figure size
plt.pie(households, labels=pet_types, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)

# 'Equal' aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Title
plt.title('Number of Households by Pet Type')

# Show the plot
plt.show()