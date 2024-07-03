
import matplotlib.pyplot as plt

# Data to plot
labels = ['Vegetables', 'Fruits', 'Grains', 'Protein', 'Dairy', 'Fats']
sizes = [30, 20, 25, 15, 5, 5]
colors = ['#4CAF50', '#FFEB3B', '#FF9800', '#F44336', '#03A9F4', '#E91E63']

# Create pie chart
plt.figure(figsize=(12, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Distribution of Food Types in a Balanced Diet', y=1.05)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()