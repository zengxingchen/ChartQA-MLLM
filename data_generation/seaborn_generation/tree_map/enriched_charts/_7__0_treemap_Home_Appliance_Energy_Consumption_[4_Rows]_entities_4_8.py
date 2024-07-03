
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for creating the treemap
data = {
    'Category': ['Vegetables', 'Fruits', 'Dairy Products', 'Bakery Items', 'Meat', 
                 'Seafood', 'Beverages', 'Snacks', 'Frozen Foods', 'Grains and Cereals',
                 'Spices and Herbs', 'Condiments', 'Confectionery', 'Canned Goods', 'Nuts and Seeds'],
    'Quantity': [2000, 1500, 1200, 1000, 800, 
                 500, 1800, 1400, 700, 900, 
                 400, 600, 1300, 1100, 450]
}

# Convert the data dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Define size of the figure
plt.figure(figsize=(14,10))

# Define custom colors using specific color codes
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854',
          '#ffd92f', '#e5c494', '#b3b3b3', '#1b9e77', '#d95f02',
          '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d']

# Create the treemap
squarify.plot(sizes=df['Quantity'], label=df['Category'], color=colors, alpha=0.8)

# Set the title of the treemap
plt.title('Supermarket Food Item Distribution', fontsize=18)

# Remove the axis lines
plt.axis('off')

# Display the treemap
plt.show()