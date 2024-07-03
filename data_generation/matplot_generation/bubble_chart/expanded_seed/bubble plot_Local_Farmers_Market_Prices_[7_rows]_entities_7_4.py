
import matplotlib.pyplot as plt

# Given data
data = [
    {'Product': 'Apples', 'Farmers Market': 'Sunnydale Market', 'Vendor ID': 23, 'Price per Unit ($)': 1.2, 'Bubble Size (Quantity Sold)': 150},
    {'Product': 'Oranges', 'Farmers Market': 'Freshfield Market', 'Vendor ID': 42, 'Price per Unit ($)': 0.85, 'Bubble Size (Quantity Sold)': 200},
    {'Product': 'Bananas', 'Farmers Market': 'Greentop Market', 'Vendor ID': 37, 'Price per Unit ($)': 0.6, 'Bubble Size (Quantity Sold)': 180},
    {'Product': 'Tomatoes', 'Farmers Market': 'Marketplace Central', 'Vendor ID': 19, 'Price per Unit ($)': 2.5, 'Bubble Size (Quantity Sold)': 90},
    {'Product': 'Potatoes', 'Farmers Market': 'Riverdale Market', 'Vendor ID': 8, 'Price per Unit ($)': 0.75, 'Bubble Size (Quantity Sold)': 300},
    {'Product': 'Carrots', 'Farmers Market': 'Hillside Market', 'Vendor ID': 27, 'Price per Unit ($)': 1.1, 'Bubble Size (Quantity Sold)': 160},
    {'Product': 'Strawberries', 'Farmers Market': 'Lakeside Market', 'Vendor ID': 33, 'Price per Unit ($)': 2.9, 'Bubble Size (Quantity Sold)': 120}
]

# Prepare data for plotting
products = [item['Product'] for item in data]
farmers_markets = [item['Farmers Market'] for item in data]
vendor_ids = [item['Vendor ID'] for item in data]
prices = [item['Price per Unit ($)'] for item in data]
quantities = [item['Bubble Size (Quantity Sold)'] for item in data]

# Create figure and axis
fig, ax = plt.subplots()

# Generate a color map based on Vendor ID
colors = plt.cm.jet(vendor_ids)

# Create the scatter plot (bubble chart)
scatter = ax.scatter(prices, products, s=quantities, c=colors, alpha=0.6, edgecolors="w", linewidth=1)

# Add annotation for the farmer's markets as diversified visual encodings
for i, txt in enumerate(farmers_markets):
    ax.annotate(txt, (prices[i], products[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Create a color bar for the color map
cbar = plt.colorbar(scatter)
cbar.set_label('Vendor ID')

# Set the title and labels
ax.set_title('Bubble Chart of Product Sales')
ax.set_xlabel('Price per Unit ($)')
ax.set_ylabel('Products')

# Show the plot
plt.show()