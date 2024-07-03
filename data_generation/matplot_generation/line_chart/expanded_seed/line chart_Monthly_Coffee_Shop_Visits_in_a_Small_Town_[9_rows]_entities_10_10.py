
import matplotlib.pyplot as plt

# Data from the provided chart table
data = [
    {'Month': 'January', 'Espresso Express': 123, 'Cafe Mocha': 140, 'Java Central': 110, 'Brewed Awakenings': 95, 'The Grind House': 108},
    {'Month': 'February', 'Espresso Express': 134, 'Cafe Mocha': 150, 'Java Central': 95, 'Brewed Awakenings': 105, 'The Grind House': 120},
    {'Month': 'March', 'Espresso Express': 145, 'Cafe Mocha': 160, 'Java Central': 120, 'Brewed Awakenings': 115, 'The Grind House': 135},
    {'Month': 'April', 'Espresso Express': 155, 'Cafe Mocha': 170, 'Java Central': 130, 'Brewed Awakenings': 125, 'The Grind House': 140},
    {'Month': 'May', 'Espresso Express': 160, 'Cafe Mocha': 180, 'Java Central': 140, 'Brewed Awakenings': 130, 'The Grind House': 150},
    {'Month': 'June', 'Espresso Express': 170, 'Cafe Mocha': 190, 'Java Central': 150, 'Brewed Awakenings': 140, 'The Grind House': 160},
    {'Month': 'July', 'Espresso Express': 180, 'Cafe Mocha': 200, 'Java Central': 155, 'Brewed Awakenings': 145, 'The Grind House': 165},
    {'Month': 'August', 'Espresso Express': 190, 'Cafe Mocha': 210, 'Java Central': 160, 'Brewed Awakenings': 150, 'The Grind House': 170},
    {'Month': 'September', 'Espresso Express': 175, 'Cafe Mocha': 195, 'Java Central': 145, 'Brewed Awakenings': 135, 'The Grind House': 160},
    {'Month': 'October', 'Espresso Express': 165, 'Cafe Mocha': 180, 'Java Central': 135, 'Brewed Awakenings': 125, 'The Grind House': 155}
]

# Extracting month names for the x-axis
months = [entry['Month'] for entry in data]

# Plotting each coffee shop's sales trend
plt.figure(figsize=(12, 8))
coffee_shops = list(data[0].keys())[1:]  # Get coffee shop names skipping the 'Month' key

# Line style settings and markers for each coffee shop
line_styles = ['-', '--', '-.', ':']
markers = ['o', '^', 's', 'D', 'x']
colors = ['b', 'g', 'r', 'c', 'm']

for i, shop in enumerate(coffee_shops):
    sales = [entry[shop] for entry in data]
    plt.plot(months, sales, label=shop, linestyle=line_styles[i % len(line_styles)], marker=markers[i % len(markers)], color=colors[i % len(colors)])

# Adding titles and labels
plt.title('Monthly Sales Trends of Various Coffee Shops')
plt.xlabel('Month')
plt.ylabel('Sales (in units)')

# Adding grid for readability
plt.grid(True)

# Adding a legend to identify the lines
plt.legend(title='Coffee Shops')

# Show the plot
plt.show()