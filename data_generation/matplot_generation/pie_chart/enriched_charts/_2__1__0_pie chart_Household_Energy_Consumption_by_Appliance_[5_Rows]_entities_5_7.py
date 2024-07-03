
import matplotlib.pyplot as plt

# Data
categories = [
    'Fruits', 'Vegetables', 'Grains', 'Proteins', 'Dairy', 
    'Sweets', 'Fats'
]
percentages = [25.0, 20.0, 18.0, 15.0, 12.0, 7.0, 3.0]

# Colors
colors = [
    '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', 
    '#FF9F40', '#FF6384'
]

# Plot
plt.figure(figsize=(10, 7))  # Width and height of the chart
plt.pie(percentages, labels=categories, colors=colors, startangle=90, autopct='%1.1f%%')

plt.title("Preferred Food Categories in 2023", pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()