
import matplotlib.pyplot as plt

# Data
categories = ['Fruits', 'Vegetables', 'Grains', 'Protein Foods', 'Dairy', 'Fats and Oils', 'Sweets and Snacks']
percentages = [25.4, 20.1, 15.6, 14.3, 10.5, 7.2, 7.0]

# Colors
colors = ['#FFA07A', '#98FB98', '#8B4513', '#FFD700', '#87CEEB', '#FF6347', '#FF69B4']

# Pie chart
fig, ax = plt.subplots(figsize=(10, 7))  # Width, Height of the chart
ax.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Distribution of Food Categories in a Balanced Diet', pad=20)
plt.show()