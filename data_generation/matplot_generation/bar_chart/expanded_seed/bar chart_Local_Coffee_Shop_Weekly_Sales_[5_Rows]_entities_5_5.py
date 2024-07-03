
import matplotlib.pyplot as plt
import numpy as np

# Provided data
data = [
    {'Day': 'Monday', 'Espresso': 95, 'Americano': 110, 'Cappuccino': 80, 'Latte': 130},
    {'Day': 'Tuesday', 'Espresso': 80, 'Americano': 120, 'Cappuccino': 70, 'Latte': 125},
    {'Day': 'Wednesday', 'Espresso': 75, 'Americano': 95, 'Cappuccino': 65, 'Latte': 100},
    {'Day': 'Thursday', 'Espresso': 90, 'Americano': 105, 'Cappuccino': 75, 'Latte': 150},
    {'Day': 'Friday', 'Espresso': 130, 'Americano': 150, 'Cappuccino': 100, 'Latte': 180}
]

# Getting list of days and types of coffee
days = [record['Day'] for record in data]
coffees = list(data[0].keys())[1:]  # Skip the 'Day' key

# Preparing data for the bar chart
values = {coffee: [record[coffee] for record in data] for coffee in coffees}

# Calculate the width of each bar
bar_width = 0.2
# Set positions of the bars on the x-axis
r = np.arange(len(days))
positions = [r + i * bar_width for i in range(len(coffees))]

# Setup the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Creating bars for each type of coffee
for idx, (coffee, pos) in enumerate(zip(coffees, positions)):
    ax.bar(pos, values[coffee], bar_width, label=coffee)

# General layout improvements
ax.set_xticks([r + bar_width for r in range(len(days))])
ax.set_xticklabels(days)
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Number of Cups Sold')
ax.set_title('Cups of Coffee Sold per Type per Day')
ax.legend()

# Show the plot
plt.show()