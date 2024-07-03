
import matplotlib.pyplot as plt

# Given char table data
data = [
    {'Product': 'Apples', 'Category': 'Fruit', 'Week 1 Price ($)': 0.89, 'Week 2 Price ($)': 0.92, 'Week 3 Price ($)': 0.94, 'Week 4 Price ($)': 0.97, 'Average Demand': 'High', 'Region': 'Northwest'},
    {'Product': 'Oranges', 'Category': 'Fruit', 'Week 1 Price ($)': 0.7, 'Week 2 Price ($)': 0.75, 'Week 3 Price ($)': 0.8, 'Week 4 Price ($)': 0.83, 'Average Demand': 'Medium', 'Region': 'Southeast'},
    {'Product': 'Potatoes', 'Category': 'Vegetable', 'Week 1 Price ($)': 0.55, 'Week 2 Price ($)': 0.53, 'Week 3 Price ($)': 0.51, 'Week 4 Price ($)': 0.54, 'Average Demand': 'High', 'Region': 'Northeast'},
    {'Product': 'Carrots', 'Category': 'Vegetable', 'Week 1 Price ($)': 0.62, 'Week 2 Price ($)': 0.65, 'Week 3 Price ($)': 0.64, 'Week 4 Price ($)': 0.68, 'Average Demand': 'Medium', 'Region': 'Southwest'},
    {'Product': 'Honey', 'Category': 'Condiment', 'Week 1 Price ($)': 3.4, 'Week 2 Price ($)': 3.5, 'Week 3 Price ($)': 3.6, 'Week 4 Price ($)': 3.65, 'Average Demand': 'Low', 'Region': 'South'},
    {'Product': 'Kale', 'Category': 'Vegetable', 'Week 1 Price ($)': 0.99, 'Week 2 Price ($)': 0.97, 'Week 3 Price ($)': 0.95, 'Week 4 Price ($)': 0.98, 'Average Demand': 'Medium', 'Region': 'Northeast'},
    {'Product': 'Almonds', 'Category': 'Nut', 'Week 1 Price ($)': 4.5, 'Week 2 Price ($)': 4.55, 'Week 3 Price ($)': 4.6, 'Week 4 Price ($)': 4.7, 'Average Demand': 'Low', 'Region': 'West'},
    {'Product': 'Eggs', 'Category': 'Dairy', 'Week 1 Price ($)': 2.0, 'Week 2 Price ($)': 2.05, 'Week 3 Price ($)': 2.1, 'Week 4 Price ($)': 2.15, 'Average Demand': 'High', 'Region': 'Southeast'}
]

# Set the demands and regions to be represented in the bubble chart
demands = {'Low': 1, 'Medium': 2, 'High': 3}
regions = {'Northwest': 'blue', 'Southeast': 'red', 'Northeast': 'green', 'Southwest': 'orange', 'South': 'purple', 'West': 'brown'}

# Initialize lists for each piece of data
products, avg_prices, avg_demands, price_changes, region_colors = [], [], [], [], []

# Process the data
for item in data:
    products.append(item['Product'])
    
    # Calculate the average price for each product over the 4 weeks
    avg_price = sum([item[f'Week {i} Price ($)'] for i in range(1, 5)]) / 4
    avg_prices.append(avg_price)
    
    # Map the average demand to an integer for plotting
    avg_demand = demands[item['Average Demand']]
    avg_demands.append(avg_demand)
    
    # Calculate the price change as the difference of the last and first week's prices
    price_change = item['Week 4 Price ($)'] - item['Week 1 Price ($)']
    price_changes.append(price_change)
    
    # Map the region to a color
    region_color = regions[item['Region']]
    region_colors.append(region_color)

# Create a bubble chart
plt.figure(figsize=(10, 6))

# The bubble sizes will be proportional to the price change
# We amplify the size by an arbitrary factor to make it more visually impactful
bubble_sizes = [change * 200 for change in price_changes]

# Plot the bubble chart
for i in range(len(products)):
    plt.scatter(avg_prices[i], avg_demands[i], s=bubble_sizes[i], color=region_colors[i], alpha=0.6, label=products[i])

# Create a legend and title
plt.legend()
plt.title('Average Weekly Price vs Average Demand by Region and Price Change')
plt.xlabel('Average Weekly Price ($)')
plt.ylabel('Average Demand (1=Low, 2=Medium, 3=High)')

# Customizing the grid
plt.grid(True, linestyle='--', color='lightgrey', alpha=0.7)

# Add product names with regions as annotations
for i, product in enumerate(products):
    plt.annotate(f'{product} ({data[i]["Region"]})', 
                 (avg_prices[i], avg_demands[i]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center')

# Show the plot
plt.show()