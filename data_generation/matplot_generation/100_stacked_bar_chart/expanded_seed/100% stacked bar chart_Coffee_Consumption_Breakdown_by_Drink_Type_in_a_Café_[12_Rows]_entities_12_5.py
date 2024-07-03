
import matplotlib.pyplot as plt
import numpy as np

# Given data
data = [
    {'Month': 'January', 'Espresso': 15, 'Americano': 20, 'Cappuccino': 18, 'Latte': 17, 'Cold Brew': 5, 'Flat White': 7, 'Mocha': 9, 'Frappuccino': 2, 'Macchiato': 3, 'Filter': 2, 'Tea': 1, 'Hot Chocolate': 1},
    # ... (Include all other months here)
    {'Month': 'December', 'Espresso': 16, 'Americano': 22, 'Cappuccino': 19, 'Latte': 18, 'Cold Brew': 6, 'Flat White': 9, 'Mocha': 11, 'Frappuccino': 3, 'Macchiato': 2, 'Filter': 2, 'Tea': 1, 'Hot Chocolate': 2}
]

# Convert data into a format suitable for Matplotlib
months = [entry['Month'] for entry in data]
drinks = list(data[0].keys())[1:]  # Assuming all entries have the same keys
stacked_data = {drink: np.array([entry[drink] for entry in data]) for drink in drinks}

# Normalize the drink data to sum to 1 (100%)
totals = np.sum([stacked_data[drink] for drink in drinks], axis=0)
percentages = {drink: (stacked_data[drink] / totals) * 100 for drink in drinks}

# Plotting
fig, ax = plt.subplots()

# Initialize the bottom at zero for the first set of bars
bottom = np.zeros(len(months))

for drink in drinks:
    ax.bar(months, percentages[drink], bottom=bottom, label=drink)
    # Update the bottom position for the next stack
    bottom += percentages[drink]

# Customizations
ax.set_ylabel('Percentage')
ax.set_title('Coffee Sales by Type: 100% Stacked Bar Chart')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Drinks')

# Rotating the x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()