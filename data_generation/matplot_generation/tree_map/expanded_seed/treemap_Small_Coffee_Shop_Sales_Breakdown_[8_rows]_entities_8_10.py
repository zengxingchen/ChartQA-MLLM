
import matplotlib.pyplot as plt
import squarify

# Data given
data = [
    {'Item Category': 'Beverages', 'Item': 'Coffee', 'Monthly Sales ($)': 3500, 'Percentage of Total Sales': '40%'},
    {'Item Category': 'Beverages', 'Item': 'Tea', 'Monthly Sales ($)': 1050, 'Percentage of Total Sales': '12%'},
    {'Item Category': 'Food', 'Item': 'Pastries', 'Monthly Sales ($)': 2100, 'Percentage of Total Sales': '24%'},
    {'Item Category': 'Food', 'Item': 'Sandwiches', 'Monthly Sales ($)': 1400, 'Percentage of Total Sales': '16%'},
    {'Item Category': 'Beverages', 'Item': 'Smoothies', 'Monthly Sales ($)': 700, 'Percentage of Total Sales': '8%'},
    {'Item Category': 'Merchandise', 'Item': 'Mugs', 'Monthly Sales ($)': 420, 'Percentage of Total Sales': '4%'},
    {'Item Category': 'Merchandise', 'Item': 'T-shirts', 'Monthly Sales ($)': 280, 'Percentage of Total Sales': '3%'},
    {'Item Category': 'Food', 'Item': 'Cookies', 'Monthly Sales ($)': 140, 'Percentage of Total Sales': '2%'}
]

# Process data
categories = [entry['Item Category'] for entry in data]
items = [entry['Item'] for entry in data]
sales = [entry['Monthly Sales ($)'] for entry in data]
labels = ["{}\n{}\n${}\n{}".format(cat, item, sale, perc) for cat, item, sale, perc in zip(categories, items, sales, [entry['Percentage of Total Sales'] for entry in data])]

# Colors for each item category
colors = {
    'Beverages': 'lightblue',
    'Food': 'lightgreen',
    'Merchandise': 'lightcoral'
}

# Assign color to each item based on its category
item_colors = [colors[category] for category in categories]

# Create a figure to display the treemap
plt.figure(figsize=(12, 8))

# Using squarify to plot the treemap
squarify.plot(sizes=sales, label=labels, color=item_colors, alpha=0.8)

plt.title("Monthly Sales Treemap")
plt.axis('off') # Hides the axes
plt.show()