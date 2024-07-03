
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Product': 'Americano', 'Category': 'Coffee', 'Average Sales Per Day (Units)': 95, 'Average Unit Price ($)': 3.0, 'Popularity Score (1-10)': 8},
    {'Product': 'Latte', 'Category': 'Coffee', 'Average Sales Per Day (Units)': 110, 'Average Unit Price ($)': 4.0, 'Popularity Score (1-10)': 9},
    {'Product': 'Croissant', 'Category': 'Pastry', 'Average Sales Per Day (Units)': 60, 'Average Unit Price ($)': 2.5, 'Popularity Score (1-10)': 7},
    {'Product': 'Iced Tea', 'Category': 'Beverages', 'Average Sales Per Day (Units)': 50, 'Average Unit Price ($)': 2.5, 'Popularity Score (1-10)': 6},
    {'Product': 'Bagel', 'Category': 'Pastry', 'Average Sales Per Day (Units)': 80, 'Average Unit Price ($)': 1.5, 'Popularity Score (1-10)': 7}
]

# Prepare the data for plotting
products = [item['Product'] for item in data]
categories = [item['Category'] for item in data]
sales = [item['Average Sales Per Day (Units)'] for item in data]
prices = [item['Average Unit Price ($)'] for item in data]
popularity = [item['Popularity Score (1-10)'] for item in data]
popularity_scaled = [p * 10 for p in popularity]  # Scale up the popularity for better visibility

# Assign colors based on categories
category_colors = {'Coffee': 'brown', 'Pastry': 'orange', 'Beverages': 'lightblue'}
colors = [category_colors[cat] for cat in categories]

# Create a bubble chart
plt.figure(figsize=(10, 6))
bubble = plt.scatter(sales, prices, s=popularity_scaled, c=colors, alpha=0.6) # alpha for bubble transparency

# Add labels and a legend
plt.xlabel('Average Sales Per Day (Units)')
plt.ylabel('Average Unit Price ($)')
plt.title('Product Sales Bubble Chart')
for i, product in enumerate(products):
    plt.text(sales[i], prices[i], product, ha='center', va='center', fontsize=8)

# Create a legend for categories
for category in category_colors:
    plt.scatter([], [], c=category_colors[category], alpha=0.6, label=category)
plt.legend(title="Category", loc='upper right')

# Show grid
plt.grid(True)

# Show the plot
plt.show()