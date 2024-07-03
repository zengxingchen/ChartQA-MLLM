
import matplotlib.pyplot as plt

# Data
food_categories = [
    'Fruits', 'Vegetables', 'Meat', 'Dairy', 
    'Grains', 'Sweets', 'Beverages'
]
percentages = [20.0, 25.0, 15.0, 10.0, 18.0, 7.0, 5.0]

# Colors
colors = [
    '#FF6384', '#36A2EB', '#FFCE56', '#FF9F40', 
    '#4BC0C0', '#9966FF', '#FFCD56'
]

# Plot
plt.figure(figsize=(12, 9))  # Width and height of the chart
plt.pie(percentages, labels=food_categories, colors=colors, startangle=140, autopct='%1.1f%%')

plt.title("Distribution of Food Categories in Daily Diet (2023)", pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()