
import matplotlib.pyplot as plt

# Data
activities = ['Fruits', 'Vegetables', 'Grains', 'Protein', 'Dairy', 'Snacks', 'Beverages']
percentages = [20, 15, 25, 10, 10, 10, 10]
colors = ['#FF6347', '#4682B4', '#8A2BE2', '#FFD700', '#32CD32', '#FF69B4', '#FF4500']

# Pie chart
plt.figure(figsize=(12, 8))
plt.pie(percentages, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
plt.title('Distribution of Food Intake by Category', y=1.05)

# Display the chart
plt.show()