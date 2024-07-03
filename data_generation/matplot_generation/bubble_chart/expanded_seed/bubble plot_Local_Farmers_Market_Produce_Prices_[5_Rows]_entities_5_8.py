
import matplotlib.pyplot as plt

# Given data in a list of dictionaries
data = [
    {'Product': 'Apples', 'City': 'Smallville', 'Price Per Unit ($)': 0.3, 'Quantity Sold (Units)': 150, 'Average Weight per Unit (kg)': 0.2},
    {'Product': 'Oranges', 'City': 'Laketown', 'Price Per Unit ($)': 0.5, 'Quantity Sold (Units)': 200, 'Average Weight per Unit (kg)': 0.15},
    {'Product': 'Tomatoes', 'City': 'Greenfield', 'Price Per Unit ($)': 0.25, 'Quantity Sold (Units)': 300, 'Average Weight per Unit (kg)': 0.1},
    {'Product': 'Potatoes', 'City': 'Riverville', 'Price Per Unit ($)': 0.1, 'Quantity Sold (Units)': 400, 'Average Weight per Unit (kg)': 0.25},
    {'Product': 'Bananas', 'City': 'Eastwood', 'Price Per Unit ($)': 0.45, 'Quantity Sold (Units)': 120, 'Average Weight per Unit (kg)': 0.2}
]

# Extracting information for plotting
products = [entry['Product'] for entry in data]
prices = [entry['Price Per Unit ($)'] for entry in data]
quantities = [entry['Quantity Sold (Units)'] for entry in data]
weights = [entry['Average Weight per Unit (kg)'] for entry in data]
cities = [entry['City'] for entry in data]

# Assign a unique color for each city
city_color_map = {
    'Smallville': 'blue',
    'Laketown': 'orange',
    'Greenfield': 'green',
    'Riverville': 'red',
    'Eastwood': 'purple'
}
colors = [city_color_map[city] for city in cities]

# Create a bubble chart
plt.figure(figsize=(10, 6))
bubble_sizes = [quantity * 10 for quantity in quantities]  # Adjust sizes to be more visible in chart
for i in range(len(data)):
    plt.scatter(prices[i], weights[i], s=bubble_sizes[i], alpha=0.5, c=colors[i], label=products[i] + ' - ' + cities[i])

# Adding labels and title
plt.xlabel('Price Per Unit ($)')
plt.ylabel('Average Weight per Unit (kg)')
plt.title('Bubble Chart of Product Sales')

# Add grid for better readability
plt.grid(True)

# Creating a legend for our chart
legend_labels = [product + ' (' + city + ')' for product, city in zip(products, cities)]
plt.legend(legend_labels, loc='best', title="Products - Cities")

# Show plot
plt.show()