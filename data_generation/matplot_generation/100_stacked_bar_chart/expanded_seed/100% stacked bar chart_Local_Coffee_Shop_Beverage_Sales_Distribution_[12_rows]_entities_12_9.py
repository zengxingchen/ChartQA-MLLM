
import matplotlib.pyplot as plt
import numpy as np

# Given table data
data = [
    {'Month': 'January', 'Espresso': '20%', 'Americano': '25%', 'Latte': '30%', 'Cappuccino': '10%', 'Mocha': '10%', 'Tea': '5%'},
    {'Month': 'February', 'Espresso': '19%', 'Americano': '22%', 'Latte': '32%', 'Cappuccino': '11%', 'Mocha': '11%', 'Tea': '5%'},
    # ... (include all other months here)
    {'Month': 'December', 'Espresso': '23%', 'Americano': '24%', 'Latte': '22%', 'Cappuccino': '15%', 'Mocha': '11%', 'Tea': '5%'}
]

# Extract the months
months = [x['Month'] for x in data]

# Convert percentage strings to floats and calculate cumulative values for stacking
percentages = {k: np.array([float(x[k].rstrip('%')) for x in data]) for k in data[0] if k != 'Month'}
cumulative = np.array([0] * len(data))  # initialize with zeros

# Plot each stack in the bar chart
for beverage, values in percentages.items():
    plt.bar(months, values, bottom=cumulative, label=beverage)
    cumulative += values

# Formatting the chart
plt.xlabel('Month')
plt.ylabel('Percentage (%)')
plt.title('Monthly Beverage Sales Distribution')
plt.xticks(rotation=45)  # Rotate month labels for better visibility
plt.yticks(np.arange(0, 101, 10))  # Set y-axis ticks to show percentage
plt.legend(loc='upper left', bbox_to_anchor=(1,1))  # Move the legend out of the chart

# Display the stacked bar chart
plt.tight_layout()  # Adjust layout to fit everything nicely
plt.show()