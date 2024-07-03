
import matplotlib.pyplot as plt

# Data to plot
labels = 'Fruits', 'Vegetables', 'Grains', 'Proteins', 'Dairy', 'Fats and Oils', 'Sweets', 'Beverages'
sizes = [20, 25, 15, 18, 12, 7, 3, 5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#ff6666']

# Plot
plt.figure(figsize=[10, 6])  # Set the width and height of the chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Daily Food Intake by Category', y=1.08)  # Adjust title position to avoid overlap
plt.show()