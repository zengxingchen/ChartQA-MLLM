
import matplotlib.pyplot as plt

# Data
food = ['Breakfast', 'Lunch', 'Dinner', 'Snack1', 'Snack2', 'Dessert', 'Beverage']
calories = [450, 650, 700, 200, 150, 300, 100]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A1FF33', '#33A1FF', '#FF5733']

# Create a vertical bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(food, calories, color=colors, edgecolor='black', width=0.5)

# Customizing the plot
plt.ylabel('Calories')
plt.title('Daily Caloric Intake from Different Foods')
plt.ylim(50, max(calories) + 100)
plt.tight_layout()

# Show grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()