
import matplotlib.pyplot as plt

# Data
fruits = ['Banana', 'Apple', 'Grapes', 'Orange', 'Pineapple', 'Strawberry', 'Blueberry', 'Watermelon', 'Cherry', 'Peach', 'Mango']
consumption = [150, 120, 100, 90, 80, 70, 60, 50, 40, 30, 20]
colors = ['#ffdd57', '#ff6347', '#8a2be2', '#ff4500', '#ffcc00', '#ff69b4', '#4169e1', '#32cd32', '#dc143c', '#ffa07a', '#ff8c00']

# Figure size
plt.figure(figsize=(12, 10))

# Vertical bar chart
plt.bar(fruits, consumption, color=colors, width=0.7)

# Labeling
plt.ylabel('Consumption (kg)')
plt.title('Fruit Consumption in 2024')
plt.gca().set_ylim([15, 160])  # Truncate y-axis

# Show and save plot
plt.tight_layout()
plt.show()