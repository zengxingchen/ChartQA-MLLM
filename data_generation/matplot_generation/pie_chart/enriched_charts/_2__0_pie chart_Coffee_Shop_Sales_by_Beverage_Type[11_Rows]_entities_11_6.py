
import matplotlib.pyplot as plt

# Data
activities = ['Reading', 'Watching TV', 'Playing Sports', 'Traveling', 'Gardening', 'Cooking', 'Gaming']
percentages = [15, 25, 20, 10, 10, 10, 10]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFD700', '#DAF7A6', '#900C3F']

# Pie chart
plt.figure(figsize=(10, 7))
plt.pie(percentages, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
plt.title('Preferred Leisure Activities', y=1.08)

# Display the chart
plt.show()