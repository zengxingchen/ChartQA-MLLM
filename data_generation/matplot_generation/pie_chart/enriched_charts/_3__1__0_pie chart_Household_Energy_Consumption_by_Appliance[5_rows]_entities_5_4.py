
import matplotlib.pyplot as plt

# Data to plot
labels = ['Fruits', 'Vegetables', 'Grains', 'Proteins', 'Dairy', 'Sweets']
sizes = [25.0, 20.0, 18.0, 15.0, 12.0, 10.0]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create pie chart
plt.figure(figsize=(10, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Food Categories in a Balanced Diet', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()