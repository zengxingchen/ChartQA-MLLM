
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Beverage Type': 'Espresso', 'Units Sold': 1500, 'Revenue (USD)': 4500, 'Month': 'January'},
    {'Beverage Type': 'Latte', 'Units Sold': 2000, 'Revenue (USD)': 6000, 'Month': 'January'},
    {'Beverage Type': 'Cappuccino', 'Units Sold': 1800, 'Revenue (USD)': 5400, 'Month': 'January'},
    {'Beverage Type': 'Iced Coffee', 'Units Sold': 2200, 'Revenue (USD)': 4400, 'Month': 'January'},
    {'Beverage Type': 'Mocha', 'Units Sold': 1200, 'Revenue (USD)': 4800, 'Month': 'January'},
    {'Beverage Type': 'Tea', 'Units Sold': 800, 'Revenue (USD)': 2400, 'Month': 'January'},
    {'Beverage Type': 'Hot Chocolate', 'Units Sold': 600, 'Revenue (USD)': 1800, 'Month': 'January'},
    {'Beverage Type': 'Cold Brew', 'Units Sold': 300, 'Revenue (USD)': 900, 'Month': 'January'}
]

# Extracting values for plotting
beverage_types = [item['Beverage Type'] for item in data]
units_sold = [item['Units Sold'] for item in data]
revenue = [item['Revenue (USD)'] for item in data]

# Bubble size can be adjusted for better aesthetics
# Here, we're multiplying units sold by a constant to scale it up for visualization
bubble_sizes = [u * 5 for u in units_sold]

# Generating the plot
plt.figure(figsize=(10, 6))
bubble_chart = plt.scatter(units_sold, revenue, s=bubble_sizes, alpha=0.5)

# Adding title and labels
plt.title('Beverage Sales Data (January)')
plt.xlabel('Units Sold')
plt.ylabel('Revenue (USD)')

# Adding individual labels for each bubble
for i in range(len(data)):
    plt.text(units_sold[i], revenue[i], beverage_types[i], ha='center', va='center')

# Show the plot
plt.show()