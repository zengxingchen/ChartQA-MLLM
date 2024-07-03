
import matplotlib.pyplot as plt
import numpy as np

# Data from the table
data = [
    {'Item': 'Espresso', 'Monday': 60, 'Tuesday': 55, 'Wednesday': 70, 'Thursday': 65, 'Friday': 80},
    {'Item': 'Cappuccino', 'Monday': 50, 'Tuesday': 45, 'Wednesday': 55, 'Thursday': 63, 'Friday': 75},
    {'Item': 'Latte', 'Monday': 80, 'Tuesday': 70, 'Wednesday': 85, 'Thursday': 90, 'Friday': 100},
    {'Item': 'Muffin', 'Monday': 40, 'Tuesday': 35, 'Wednesday': 42, 'Thursday': 50, 'Friday': 60},
    {'Item': 'Croissant', 'Monday': 30, 'Tuesday': 20, 'Wednesday': 25, 'Thursday': 30, 'Friday': 45}
]

# Initialize the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Setup bar width and positions
number_of_items = len(data)
number_of_days = len(data[0]) - 1  # Subtract 'Item' from the count
bar_width = 0.15
indices = np.arange(number_of_days)

# Colors for the bars
colors = ['red', 'green', 'blue', 'orange', 'purple']

# Plotting the bar chart
for i, item_data in enumerate(data):
    sales = [item_data[day] for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']]
    plt.bar(indices + i * bar_width, sales, color=colors[i], width=bar_width, label=item_data['Item'])

# Adding labels and title
plt.xlabel('Days')
plt.ylabel('Sales')
plt.title('Weekly Sales of Different Items')

# Set the position and labels for x-ticks
ax.set_xticks(indices + bar_width * (number_of_items - 1) / 2)  # Centering the x-ticks
ax.set_xticklabels(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

# Adding a legend
plt.legend()

# Display the plotted chart
plt.tight_layout()  # Adjust the padding between and around subplots
plt.show()