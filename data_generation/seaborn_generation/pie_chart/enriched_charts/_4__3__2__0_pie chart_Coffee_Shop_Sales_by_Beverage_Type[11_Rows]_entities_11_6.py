
import matplotlib.pyplot as plt

# Data
activities = ['Urban', 'Suburban', 'Rural', 'Industrial', 'Agricultural', 'Conservation', 'Other']
percentages = [30, 25, 15, 10, 10, 5, 5]
colors = ['#3498db', '#e74c3c', '#9b59b6', '#2ecc71', '#f1c40f', '#e67e22', '#1abc9c']

# Pie chart
plt.figure(figsize=(10, 7))
plt.pie(percentages, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
plt.title('Distribution of Land Use Types', y=1.08)

# Display the chart
plt.show()