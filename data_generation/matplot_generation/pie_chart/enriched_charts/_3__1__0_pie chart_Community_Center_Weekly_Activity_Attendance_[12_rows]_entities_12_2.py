
import matplotlib.pyplot as plt

# Data setup
categories = ['Fruits', 'Vegetables', 'Proteins', 'Carbohydrates', 'Dairy', 'Fats', 'Sugars']
percentages = [25, 30, 20, 15, 5, 3, 2]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f']

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))  # width and height of the chart
ax.pie(percentages, labels=categories, autopct='%1.1f%%', colors=colors, startangle=140)
ax.set_title('Proportion of Different Types of Foods in a Balanced Diet', pad=20)

# Show plot
plt.show()