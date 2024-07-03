
import matplotlib.pyplot as plt

# Data
categories = ['Cardio', 'Strength', 'Flexibility', 'Balance', 'Endurance', 'Recovery']
percentages = [35, 25, 15, 10, 8, 7]
colors = ['#ff6666', '#66b2ff', '#99ff99', '#ffcc66', '#ff99cc', '#c2f0c2']

# Pie chart
plt.figure(figsize=(12, 9))
plt.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')

# Title
plt.title('Weekly Fitness Activity Distribution', pad=30)

# Display the chart
plt.show()