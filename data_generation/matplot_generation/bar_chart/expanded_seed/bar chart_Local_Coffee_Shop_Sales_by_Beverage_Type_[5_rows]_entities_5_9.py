
import matplotlib.pyplot as plt
import numpy as np

# Provided table data
data = [
    {'Beverage': 'Espresso', 'Monday': 95, 'Tuesday': 80, 'Wednesday': 105, 'Thursday': 120, 'Friday': 150},
    {'Beverage': 'Latte', 'Monday': 110, 'Tuesday': 130, 'Wednesday': 120, 'Thursday': 100, 'Friday': 180},
    {'Beverage': 'Cappuccino', 'Monday': 80, 'Tuesday': 76, 'Wednesday': 90, 'Thursday': 105, 'Friday': 115},
    {'Beverage': 'Americano', 'Monday': 50, 'Tuesday': 60, 'Wednesday': 55, 'Thursday': 70, 'Friday': 80},
    {'Beverage': 'Tea', 'Monday': 40, 'Tuesday': 38, 'Wednesday': 45, 'Thursday': 50, 'Friday': 60}
]

# Extract data for the plot
beverages = [d['Beverage'] for d in data]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
sales_data = {day: [d[day] for d in data] for day in days}

# Number of bars
n_bars = len(sales_data)
bar_width = 0.1
index = np.arange(len(beverages))

# Prepare the figure
fig, ax = plt.subplots(figsize=(10,6))

# Create bars for each day
for i, (day, sales) in enumerate(sales_data.items()):
    ax.bar(index + i * bar_width, sales, bar_width, label=day)

# Format the chart
ax.set_xlabel('Beverage', fontweight='bold')
ax.set_ylabel('Sales', fontweight='bold')
ax.set_title('Sales of Beverages During the Week')
ax.set_xticks(index + bar_width * (n_bars / 2))
ax.set_xticklabels(beverages)
ax.legend(title="Day")

# Display the plot
plt.show()