
import matplotlib.pyplot as plt

# Data
ages = [10, 20, 30, 40, 50, 60, 70, 80]
fruit_consumption = [2.5, 3.0, 3.2, 3.4, 3.1, 2.8, 2.5, 2.2]
fruit_consumers = [60, 75, 80, 85, 70, 60, 55, 50]
vegetable_consumption = [2.0, 2.5, 3.0, 3.2, 3.0, 2.8, 2.5, 2.2]
vegetable_consumers = [70, 85, 90, 95, 80, 70, 60, 55]
fast_food_consumption = [4.5, 5.0, 4.2, 3.8, 3.2, 2.5, 2.0, 1.5]
fast_food_consumers = [80, 95, 70, 60, 50, 40, 30, 20]

# Create a bubble chart
plt.figure(figsize=(12, 8))  # Adjust the width and height

plt.scatter(ages, fruit_consumption, s=[i * 3 for i in fruit_consumers], c='#FF6347', alpha=0.6, label='Fruit Consumption')
plt.scatter(ages, vegetable_consumption, s=[i * 3 for i in vegetable_consumers], c='#32CD32', alpha=0.6, label='Vegetable Consumption')
plt.scatter(ages, fast_food_consumption, s=[i * 3 for i in fast_food_consumers], c='#1E90FF', alpha=0.6, label='Fast Food Consumption')

# Customize the plot
plt.title('Average Food Consumption by Age Group', fontsize=18)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Average Consumption per Week', fontsize=14)
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()