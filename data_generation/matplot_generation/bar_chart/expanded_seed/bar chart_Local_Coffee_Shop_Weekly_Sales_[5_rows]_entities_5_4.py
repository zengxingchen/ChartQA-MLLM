
import matplotlib.pyplot as plt
import numpy as np

# Given data
data = [
    {'Day': 'Monday', 'Espresso': 45, 'Americano': 30, 'Cappuccino': 27, 'Latte': 33},
    {'Day': 'Tuesday', 'Espresso': 50, 'Americano': 25, 'Cappuccino': 31, 'Latte': 29},
    {'Day': 'Wednesday', 'Espresso': 40, 'Americano': 22, 'Cappuccino': 35, 'Latte': 38},
    {'Day': 'Thursday', 'Espresso': 60, 'Americano': 45, 'Cappuccino': 40, 'Latte': 42},
    {'Day': 'Friday', 'Espresso': 70, 'Americano': 50, 'Cappuccino': 45, 'Latte': 48}
]

# Extracting the values
days = [entry['Day'] for entry in data]
espresso = [entry['Espresso'] for entry in data]
americano = [entry['Americano'] for entry in data]
cappuccino = [entry['Cappuccino'] for entry in data]
latte = [entry['Latte'] for entry in data]

# Setting up the bar width and positions
bar_width = 0.2
index = np.arange(len(days))

# Plotting bars
fig, ax = plt.subplots()
bar1 = ax.bar(index, espresso, bar_width, label='Espresso', color='b')
bar2 = ax.bar(index + bar_width, americano, bar_width, label='Americano', color='r')
bar3 = ax.bar(index + 2 * bar_width, cappuccino, bar_width, label='Cappuccino', color='g')
bar4 = ax.bar(index + 3 * bar_width, latte, bar_width, label='Latte', color='y')

# Adding labels and title
ax.set_xlabel('Day', fontsize=15)
ax.set_ylabel('Sales', fontsize=15)
ax.set_title('Sales of Coffee Types Over Days of the Week', fontsize=15)

# Adding day labels to the x-axis
ax.set_xticks(index + bar_width + bar_width/2)
ax.set_xticklabels(days, rotation=45)

# Adding a legend
ax.legend()

# Displaying the plot
plt.tight_layout()
plt.show()