
import matplotlib.pyplot as plt

# Given data
chart_data = [
    {'Time': '06:00AM', 'Espresso': 5, 'Americano': 15, 'Latte': 20, 'Cappuccino': 10, 'Mocha': 5, 'Frappe': 10},
    {'Time': '07:00AM', 'Espresso': 10, 'Americano': 25, 'Latte': 40, 'Cappuccino': 15, 'Mocha': 10, 'Frappe': 15},
    {'Time': '08:00AM', 'Espresso': 20, 'Americano': 30, 'Latte': 50, 'Cappuccino': 25, 'Mocha': 20, 'Frappe': 25},
    {'Time': '09:00AM', 'Espresso': 15, 'Americano': 20, 'Latte': 35, 'Cappuccino': 10, 'Mocha': 15, 'Frappe': 20},
    {'Time': '10:00AM', 'Espresso': 10, 'Americano': 15, 'Latte': 25, 'Cappuccino': 5, 'Mocha': 10, 'Frappe': 10},
    {'Time': '11:00AM', 'Espresso': 5, 'Americano': 10, 'Latte': 20, 'Cappuccino': 5, 'Mocha': 5, 'Frappe': 5},
    {'Time': '12:00PM', 'Espresso': 2, 'Americano': 5, 'Latte': 15, 'Cappuccino': 10, 'Mocha': 10, 'Frappe': 10},
    {'Time': '01:00PM', 'Espresso': 1, 'Americano': 3, 'Latte': 10, 'Cappuccino': 5, 'Mocha': 5, 'Frappe': 8},
    {'Time': '02:00PM', 'Espresso': 2, 'Americano': 4, 'Latte': 8, 'Cappuccino': 6, 'Mocha': 6, 'Frappe': 7}
]

# Define coffee categories and colors
categories = ['Espresso', 'Americano', 'Latte', 'Cappuccino', 'Mocha', 'Frappe']
colors = ['#543E3E', '#8D6841', '#DABFAF', '#E9E2D0', '#705443', '#3891A6']

# Prepare the data for stacking
times = [data['Time'] for data in chart_data]
bottoms = [0] * len(chart_data)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot each category
for index, category in enumerate(categories):
    values = [data[category] for data in chart_data]
    percentages = [value / sum(values) * 100 for value in values]
    cumulative_bottoms = [bottoms[j] + (values[j] / sum(values) * 100 if j == 0 else percentages[j-1]) for j in range(len(values))]
    plt.bar(times, percentages, bottom=bottoms, color=colors[index], edgecolor='white', label=category)
    bottoms = cumulative_bottoms

# Customize the plot
plt.title('Sale percentages of various coffee types by hour')
plt.xlabel('Time of Day')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Coffee Types')
plt.tight_layout()

# Display stacked bar chart
plt.show()