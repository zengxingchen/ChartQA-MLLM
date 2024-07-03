
import matplotlib.pyplot as plt

# Table data
category = ['Fruits', 'Vegetables', 'Grains', 'Proteins', 'Dairy', 'Sweets']
percentage = [30.0, 20.0, 15.0, 15.0, 10.0, 10.0]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FF6347']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))  # Change width and height of the chart
ax.pie(percentage, labels=category, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Daily Recommended Food Intake by Category', pad=30)
plt.show()