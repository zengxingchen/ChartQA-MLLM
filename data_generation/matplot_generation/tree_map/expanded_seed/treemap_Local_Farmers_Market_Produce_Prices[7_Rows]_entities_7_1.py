
import matplotlib.pyplot as plt
import squarify

# Our given dataset
data = [
    {'Produce Type': 'Fruits', 'Vendor': 'Apple Orchard', 'Price_per_lb': '$1.5'},
    {'Produce Type': 'Fruits', 'Vendor': 'Citrus Farm', 'Price_per_lb': '$2.0'},
    {'Produce Type': 'Vegetables', 'Vendor': 'Green Gardens', 'Price_per_lb': '$1.2'},
    {'Produce Type': 'Vegetables', 'Vendor': 'Organic Roots', 'Price_per_lb': '$1.8'},
    {'Produce Type': 'Herbs', 'Vendor': 'Fresh Herbs Co', 'Price_per_lb': '$15.0'},
    {'Produce Type': 'Dairy', 'Vendor': 'Happy Cows Dairy', 'Price_per_lb': '$3.0'},
    {'Produce Type': 'Bakery', 'Vendor': 'Stone Oven Bakery', 'Price_per_lb': '$5.0'}
]

# Extracting sizes and labels for the treemap
sizes = [float(item['Price_per_lb'].replace('$', '')) for item in data]
labels = [f"{item['Vendor']} ({item['Produce Type']}, {item['Price_per_lb']})" for item in data]

# Determine colors randomly
import random
colors = [plt.cm.Spectral(random.random()) for i in range(len(data))]

# Create the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Adding title and removing the axes
plt.title('Produce Price per lb Treemap')
plt.axis('off')

# Show the plot
plt.show()