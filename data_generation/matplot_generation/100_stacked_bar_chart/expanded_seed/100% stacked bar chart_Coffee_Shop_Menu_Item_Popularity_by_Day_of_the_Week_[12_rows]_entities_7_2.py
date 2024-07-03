
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Day': 'Monday', 'Espresso': 15, 'Latte': 20, 'Cappuccino': 10, 'Americano': 25, 'Mocha': 15, 'Iced Coffee': 10, 'Tea': 5},
    {'Day': 'Tuesday', 'Espresso': 10, 'Latte': 25, 'Cappuccino': 15, 'Americano': 20, 'Mocha': 10, 'Iced Coffee': 10, 'Tea': 10},
    {'Day': 'Wednesday', 'Espresso': 20, 'Latte': 15, 'Cappuccino': 20, 'Americano': 15, 'Mocha': 10, 'Iced Coffee': 15, 'Tea': 5},
    {'Day': 'Thursday', 'Espresso': 15, 'Latte': 20, 'Cappuccino': 25, 'Americano': 10, 'Mocha': 15, 'Iced Coffee': 10, 'Tea': 5},
    {'Day': 'Friday', 'Espresso': 10, 'Latte': 30, 'Cappuccino': 10, 'Americano': 20, 'Mocha': 15, 'Iced Coffee': 10, 'Tea': 5},
    {'Day': 'Saturday', 'Espresso': 20, 'Latte': 20, 'Cappuccino': 15, 'Americano': 15, 'Mocha': 10, 'Iced Coffee': 15, 'Tea': 5},
    {'Day': 'Sunday', 'Espresso': 15, 'Latte': 15, 'Cappuccino': 20, 'Americano': 5, 'Mocha': 20, 'Iced Coffee': 20, 'Tea': 5}
]

# Extracting categories
categories = data[0].keys() - {'Day'}
days = [day_data['Day'] for day_data in data]

# Calculating percentages
percent_data = {category: [] for category in categories}
for day_data in data:
    total = sum([day_data[drink] for drink in categories])
    for category in categories:
        percent_data[category].append((day_data[category] / total) * 100)

# Plotting
fig, ax = plt.subplots()

# Bottoms for the stacked bars
stack_bottoms = [0] * len(days)

for category in categories:
    ax.bar(days, percent_data[category], label=category, bottom=stack_bottoms)
    # Update the bottoms for the next category
    stack_bottoms = [old_bottom + new_bar for old_bottom, new_bar in zip(stack_bottoms, percent_data[category])]

ax.set_ylabel('Percentage')
ax.set_title('100% Stacked Bar Chart of Daily Drink Sales')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Display the plotted chart
plt.show()